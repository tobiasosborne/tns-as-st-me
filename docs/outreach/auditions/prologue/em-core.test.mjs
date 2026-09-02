import assert from 'node:assert/strict';
import {createRequire} from 'node:module';

const require = createRequire(import.meta.url);
const EM = require('./em-core.js');

const PI = Math.PI;
const add = (a, b) => a.map((x, i) => x + b[i]);
const sub = (a, b) => a.map((x, i) => x - b[i]);
const scale = (a, s) => a.map(x => x * s);
const dot = (a, b) => a.reduce((s, x, i) => s + x * b[i], 0);
const cross = (a, b) => [a[1] * b[2] - a[2] * b[1],
  a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
const norm = a => Math.sqrt(dot(a, a));
const unit = a => scale(a, 1 / norm(a));
const vecResidual = (a, b) => norm(sub(a, b));
const relativeVecResidual = (a, b) => vecResidual(a, b) / Math.max(norm(a), norm(b), 1e-300);
const fmt = x => Number(x).toExponential(3);

let state = 0x5eed1234;
function random() {
  state |= 0;
  state = (state + 0x6D2B79F5) | 0;
  let t = Math.imul(state ^ (state >>> 15), 1 | state);
  t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
  return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
}
function randomVector(radius = 1) {
  const z = 2 * random() - 1;
  const phi = 2 * PI * random();
  const q = Math.sqrt(1 - z * z);
  return scale([q * Math.cos(phi), q * Math.sin(phi), z], radius);
}
function randomBeta(max = 0.72) {
  return randomVector(max * Math.cbrt(random()));
}

function test(name, fn) {
  try {
    fn();
    console.log(`ok - ${name}`);
  } catch (error) {
    console.error(`not ok - ${name}`);
    throw error;
  }
}

function uniformRetarded(beta, x, t) {
  const a = 1 - dot(beta, beta);
  const b = 2 * (dot(x, beta) - t);
  const c = t * t - dot(x, x);
  return (-b - Math.sqrt(b * b - 4 * a * c)) / (2 * a);
}

function tangentFromThreePointLine(points) {
  assert.equal(points.length, 3);
  return unit(sub(points[2], points[0]));
}

function polarizationBasis(n) {
  const trial = Math.abs(n[2]) < 0.8 ? [0, 0, 1] : [1, 0, 0];
  const e1 = unit(cross(n, trial));
  return [e1, cross(n, e1)];
}

test('1 trajectory: closed forms, origin, and C1 raised-cosine join (tol 2e-7)', () => {
  const kick = EM.makeKick({betaI: [0.12, -0.08, 0.03],
    betaF: [0.51, 0.09, -0.11], tau: 0.7, profile: 'raised-cosine'});
  assert.deepEqual(kick.position(0), [0, 0, 0]);
  let maxPositionDerivative = 0;
  let maxVelocityDerivative = 0;
  const h = 2e-6;
  for (const t of [-0.6, -0.21, 0, 0.17, 0.6]) {
    const dp = scale(sub(kick.position(t + h), kick.position(t - h)), 1 / (2 * h));
    const dv = scale(sub(kick.velocity(t + h), kick.velocity(t - h)), 1 / (2 * h));
    maxPositionDerivative = Math.max(maxPositionDerivative, vecResidual(dp, kick.velocity(t)));
    maxVelocityDerivative = Math.max(maxVelocityDerivative, vecResidual(dv, kick.acceleration(t)));
  }
  const edge = kick.tau / 2;
  const joinResidual = Math.max(norm(kick.acceleration(-edge)), norm(kick.acceleration(edge)),
    vecResidual(kick.velocity(-edge), kick.betaI), vecResidual(kick.velocity(edge), kick.betaF));
  assert.ok(maxPositionDerivative < 2e-9);
  assert.ok(maxVelocityDerivative < 2e-7);
  assert.ok(joinResidual < 2e-16);
  console.log(`  position derivative ${fmt(maxPositionDerivative)}, acceleration derivative ${fmt(maxVelocityDerivative)}, join ${fmt(joinResidual)}`);
});

test('1 trajectory: tanh and instant endpoint behavior (tol 1e-8)', () => {
  const tanh = EM.makeKick({betaI: [-0.2, 0, 0], betaF: [0.3, 0.2, 0],
    tau: 0.4, profile: 'tanh'});
  const instant = EM.makeKick({betaI: [-0.2, 0, 0], betaF: [0.3, 0.2, 0],
    tau: 99, profile: 'instant'});
  const residual = Math.max(vecResidual(tanh.velocity(-10 * tanh.tau), tanh.betaI),
    vecResidual(tanh.velocity(10 * tanh.tau), tanh.betaF));
  assert.ok(residual < 1e-8);
  assert.ok(vecResidual(instant.position(-2), scale(instant.betaI, -2)) === 0);
  assert.ok(vecResidual(instant.position(2), scale(instant.betaF, 2)) === 0);
  console.log(`  tanh endpoint residual ${fmt(residual)}, instant tau ${instant.tau}`);
});

test('2 retarded-time solver: uniform-motion closed form (tol 3e-13)', () => {
  let worst = 0;
  for (let i = 0; i < 40; i += 1) {
    const beta = randomBeta(0.8);
    const kick = EM.makeKick({betaI: beta, betaF: beta, tau: 0.31,
      profile: i % 2 ? 'raised-cosine' : 'tanh'});
    const x = randomVector(0.4 + 8 * random());
    const t = -2 + 7 * random();
    const actual = EM.fieldAt(kick, x, t).tRet;
    const expected = uniformRetarded(beta, x, t);
    worst = Math.max(worst, Math.abs(actual - expected));
  }
  assert.ok(worst < 3e-13, `worst retarded-time residual ${worst}`);
  console.log(`  max |t_ret(numeric)-t_ret(closed)| ${fmt(worst)}`);
});

test('2 Lienard-Wiechert decomposition and instantaneous Purcell shell (tol 2e-14)', () => {
  const smooth = EM.makeKick({betaI: [0.1, -0.05, 0], betaF: [0.5, 0.1, 0.08],
    tau: 0.6, profile: 'raised-cosine'});
  const f = EM.fieldAt(smooth, [2.2, -1.1, 0.7], 2.4);
  const decomposition = vecResidual(f.E, add(f.velocityPart, f.radiationPart));
  const magnetic = vecResidual(f.B, cross(f.n, f.E));
  assert.ok(decomposition < 2e-14 && magnetic < 2e-14);

  const instant = EM.makeKick({betaI: smooth.betaI, betaF: smooth.betaF,
    profile: 'instant'});
  const oldReference = EM.fieldAt(EM.makeKick({betaI: smooth.betaI, betaF: smooth.betaI,
    tau: 1, profile: 'raised-cosine'}), [4, 1, 0], 2);
  const newReference = EM.fieldAt(EM.makeKick({betaI: smooth.betaF, betaF: smooth.betaF,
    tau: 1, profile: 'raised-cosine'}), [0.5, 0.1, 0], 2);
  const old = EM.fieldAt(instant, [4, 1, 0], 2);
  const fresh = EM.fieldAt(instant, [0.5, 0.1, 0], 2);
  assert.ok(relativeVecResidual(old.E, oldReference.E) < 2e-14);
  assert.ok(relativeVecResidual(fresh.E, newReference.E) < 2e-14);
  const shell = EM.fieldAt(instant, [2, 0, 0], 2);
  assert.ok(shell.shell);
  const transverse = Math.abs(dot(shell.n, shell.shell.transverseCoefficient));
  assert.ok(transverse < 2e-14);
  console.log(`  E split ${fmt(decomposition)}, B=n×E ${fmt(magnetic)}, shell radial coefficient ${fmt(transverse)}`);
});

test('3 RK4 streamline: uniform-motion lines are straight (tol 3e-11)', () => {
  const beta = [0.31, -0.14, 0.08];
  const kick = EM.makeKick({betaI: beta, betaF: beta, tau: 0.4});
  const t = 1.3;
  const center = scale(beta, t);
  const seed = add(center, [0.7, 0.5, -0.2]);
  const line = EM.fieldLine(kick, t, seed, {step: 0.025, maxSteps: 50});
  const ray = unit(sub(seed, center));
  let worst = 0;
  for (const point of line) worst = Math.max(worst, norm(cross(sub(point, center), ray)));
  assert.ok(worst < 3e-11, `straight-line residual ${worst}`);
  console.log(`  max perpendicular departure ${fmt(worst)} over ${line.length} points`);
});

test('3 Purcell flux labels and smooth tau->0 tangents (flux tol 2e-14, tangent tol 8e-4)', () => {
  const betaI = [-0.28, 0.08, 0.03];
  const betaF = [0.43, -0.11, 0.09];
  const t = 2;
  const lines = EM.purcellLines(betaI, betaF, t, {nLines: 19});
  let fluxJacobianResidual = 0;
  for (const line of lines) {
    for (const [beta, direction] of [[betaI, line.outerDirection], [betaF, line.innerDirection]]) {
      const gamma2 = 1 / (1 - dot(beta, beta));
      const transformedDensity = gamma2 * Math.pow(1 + dot(beta, line.label), 2);
      fluxJacobianResidual = Math.max(fluxJacobianResidual,
        Math.abs(EM.coulombProfile(beta, direction, 1) - transformedDensity));
    }
  }
  assert.ok(fluxJacobianResidual < 2e-14);

  const chosen = lines[7];
  const innerDirection = unit(sub(chosen.inner[1], chosen.inner[0]));
  const outerDirection = unit(sub(chosen.outer[1], chosen.outer[0]));
  const innerSeed = add(chosen.inner[0], scale(sub(chosen.inner[1], chosen.inner[0]), 0.45));
  const outerSeed = add(chosen.outer[0], scale(sub(chosen.outer[1], chosen.outer[0]), 0.35));
  const rows = [];
  for (const tau of [0.2, 0.05, 0.0125, 0.003125]) {
    const kick = EM.makeKick({betaI, betaF, tau, profile: 'raised-cosine'});
    const innerTangent = tangentFromThreePointLine(EM.fieldLine(kick, t, innerSeed,
      {step: 1e-5, maxSteps: 1}));
    const outerTangent = tangentFromThreePointLine(EM.fieldLine(kick, t, outerSeed,
      {step: 1e-5, maxSteps: 1}));
    rows.push([tau, Math.max(norm(cross(innerTangent, innerDirection)),
      norm(cross(outerTangent, outerDirection)))]);
  }
  console.log('  tau        max tangent residual');
  rows.forEach(([n, residual]) => console.log(`  ${n.toFixed(6)}   ${fmt(residual)}`));
  assert.ok(rows.at(-1)[1] < 8e-4 && rows.at(-1)[1] < rows[0][1]);
  console.log(`  flux/Jacobian identity residual ${fmt(fluxJacobianResidual)}`);
});

test('4 instantaneous spectrum: omega-independent soft plateau (tol 2e-15)', () => {
  const kick = EM.makeKick({betaI: [0.08, -0.23, 0.04],
    betaF: [0.52, 0.07, -0.1], profile: 'instant'});
  const n = unit([0.3, -0.4, 0.8]);
  const values = EM.radiationSpectrum(kick, n, [1e-8, 0.2, 7, 1e6]);
  const spread = Math.max(...values) - Math.min(...values);
  const memory = EM.memoryKickClosedForm(kick, n);
  const expected = EM.constants.alpha * dot(memory, memory) / (4 * PI * PI);
  const residual = Math.max(spread, Math.abs(values[0] - expected));
  assert.ok(residual < 2e-15);
  console.log(`  plateau/formula absolute residual ${fmt(residual)}`);
});

test('4 radiation-spectrum GL8 convergence table (reference n=64, tol 2e-14)', () => {
  const kick = EM.makeKick({betaI: [-0.25, 0.1, 0], betaF: [0.58, -0.08, 0.13],
    tau: 0.35, profile: 'raised-cosine'});
  const n = unit([0.2, 0.7, -0.4]);
  const omega = 23;
  const reference = EM.radiationSpectrum(kick, n, [omega], {n: 64})[0];
  console.log('  panels     |spectrum-reference|');
  let finalResidual = Infinity;
  for (const panels of [1, 2, 4, 8, 16]) {
    const value = EM.radiationSpectrum(kick, n, [omega], {n: panels})[0];
    finalResidual = Math.abs(value - reference);
    console.log(`  ${String(panels).padStart(4)}       ${fmt(finalResidual)}`);
  }
  assert.ok(finalResidual < 2e-14);
});

test('4 classical soft coefficient equals the single-emitter Weinberg factor (tol 2e-15)', () => {
  const kick = EM.makeKick({betaI: [-0.18, 0.04, 0.12], betaF: [0.44, 0.2, -0.07],
    tau: 0.2});
  const n = unit([0.2, -0.5, 0.7]);
  const [eps] = polarizationBasis(n);
  const particles = [{Q: 1, beta: kick.betaI, eta: -1},
    {Q: 1, beta: kick.betaF, eta: 1}];
  const residual = Math.abs(EM.softAmplitude(kick, n, eps) -
    EM.softFactorWeinberg(particles, n, eps));
  assert.ok(residual < 2e-15);
  console.log(`  coefficient residual ${fmt(residual)}`);
});

test('4 photon number: exact logarithm (tol 2e-16) and log-GL8 convergence (tol 2e-13)', () => {
  const instant = EM.makeKick({betaI: [0, 0, 0], betaF: [0.61, 0.08, 0],
    profile: 'instant'});
  const n = unit([0.3, 0.1, 0.8]);
  const n1 = EM.photonNumber(instant, n, 1e-7, 2);
  const n2 = EM.photonNumber(instant, n, 1e-5, 2);
  const plateau = EM.radiationSpectrum(instant, n, [1])[0];
  const logResidual = Math.abs((n1 - n2) - plateau * Math.log(100));
  assert.ok(logResidual < 2e-16);

  const smooth = EM.makeKick({betaI: [-0.16, 0.04, 0], betaF: [0.49, 0.12, -0.09],
    tau: 0.3, profile: 'raised-cosine'});
  const reference = EM.photonNumber(smooth, n, 0.03, 12, {n: 40});
  console.log('  panels     |N-reference|');
  let finalResidual = Infinity;
  for (const panels of [2, 4, 8, 16, 24]) {
    const value = EM.photonNumber(smooth, n, 0.03, 12, {n: panels});
    finalResidual = Math.abs(value - reference);
    console.log(`  ${String(panels).padStart(4)}       ${fmt(finalResidual)}`);
  }
  assert.ok(finalResidual < 2e-13);
  console.log(`  instant logarithm residual ${fmt(logResidual)}`);
});

test('5 polarization sum on the celestial sphere and charge check (tol 3e-15)', () => {
  const particles = [
    {Q: 1, beta: [0.4, 0.1, 0], eta: 1},
    {Q: 1, beta: [-0.2, 0.3, 0.1], eta: -1},
    {Q: -0.5, beta: [0.1, -0.25, 0.2], eta: 1},
    {Q: -0.5, beta: [-0.1, 0.05, -0.3], eta: -1}
  ];
  const n = unit([0.31, -0.28, 0.83]);
  const [e1, e2] = polarizationBasis(n);
  const sum = Math.pow(EM.softFactorWeinberg(particles, n, e1), 2) +
    Math.pow(EM.softFactorWeinberg(particles, n, e2), 2);
  const residual = Math.abs(sum - EM.spherePattern(particles, n));
  assert.ok(residual < 3e-15);
  assert.equal(EM.chargeConservation(particles).conserved, true);
  const bad = particles.concat({Q: 0.2, beta: [0, 0, 0], eta: 1});
  assert.equal(EM.chargeConservation(bad).conserved, false);
  const nullLegs = [{Q: 1, beta: [1, 0, 0], eta: 1},
    {Q: 1, beta: [0, 1, 0], eta: -1}];
  assert.ok(Number.isFinite(EM.spherePattern(nullLegs, n)));
  console.log(`  polarization-sum residual ${fmt(residual)}, violating sum ${EM.chargeConservation(bad).sum}`);
});

test('6 two-route radiation memory for fixed-seed random kicks (relative tol 1e-10)', () => {
  let worst = 0;
  for (let i = 0; i < 30; i += 1) {
    const tau = 0.03 + 0.7 * random();
    const kick = EM.makeKick({betaI: randomBeta(), betaF: randomBeta(), tau,
      profile: i % 2 ? 'raised-cosine' : 'tanh'});
    const x = randomVector(tau * (1e3 + 5e3 * random()));
    const numerical = EM.memoryKickQuadrature(kick, x, {rule: 'gauss-legendre', n: 16});
    const closed = EM.memoryKickClosedForm(kick, x);
    worst = Math.max(worst, relativeVecResidual(numerical, closed));
  }
  assert.ok(worst < 1e-10, `worst memory residual ${worst}`);
  console.log(`  max random relative residual ${fmt(worst)}`);
});

test('6 memory GL8 convergence table (closed form reference, relative tol 2e-13)', () => {
  const kick = EM.makeKick({betaI: [-0.31, 0.08, 0.06], betaF: [0.62, -0.12, 0.11],
    tau: 0.4, profile: 'raised-cosine'});
  const x = scale(unit([0.2, 0.6, -0.7]), 400);
  const closed = EM.memoryKickClosedForm(kick, x);
  console.log('  panels     relative residual');
  let finalResidual = Infinity;
  for (const panels of [1, 2, 4, 8, 16]) {
    const numerical = EM.memoryKickQuadrature(kick, x, {rule: 'gauss-legendre', n: panels});
    finalResidual = relativeVecResidual(numerical, closed);
    console.log(`  ${String(panels).padStart(4)}       ${fmt(finalResidual)}`);
  }
  assert.ok(finalResidual < 2e-13);
});

const GLX = [-0.9602898564975363, -0.7966664774136267, -0.525532409916329,
  -0.1834346424956498, 0.1834346424956498, 0.525532409916329,
  0.7966664774136267, 0.9602898564975363];
const GLW = [0.1012285362903763, 0.2223810344533745, 0.3137066458778873,
  0.362683783378362, 0.362683783378362, 0.3137066458778873,
  0.2223810344533745, 0.1012285362903763];
function integrateVelocityPart(kick, x, a, b, panels) {
  const result = [0, 0, 0];
  const width = (b - a) / panels;
  for (let p = 0; p < panels; p += 1) {
    const mid = a + (p + 0.5) * width;
    for (let j = 0; j < 8; j += 1) {
      const value = EM.fieldAt(kick, x, mid + width * GLX[j] / 2).velocityPart;
      for (let k = 0; k < 3; k += 1) result[k] += width * GLW[j] * value[k] / 2;
    }
  }
  return result;
}

test('6 Coulomb drift closed form and independent GL8 convergence (relative tol 3e-13)', () => {
  const kick = EM.makeKick({betaI: [-0.24, 0.07, 0.02],
    betaF: [0.47, -0.09, 0.13], profile: 'instant'});
  const x = [4, 1.2, -0.7];
  const arrival = norm(x);
  const t0 = -1.3;
  const t1 = 8.2;
  const closed = EM.coulombDrift(kick, x, t0, t1);
  console.log('  panels     relative residual');
  let finalResidual = Infinity;
  for (const panels of [1, 2, 4, 8, 16]) {
    const numeric = add(integrateVelocityPart(kick, x, t0, arrival, panels),
      integrateVelocityPart(kick, x, arrival, t1, panels));
    finalResidual = relativeVecResidual(numeric, closed);
    console.log(`  ${String(panels).padStart(4)}       ${fmt(finalResidual)}`);
  }
  assert.ok(finalResidual < 3e-13);
});

test('7 boosted-Coulomb profile is the exact radial 1/r^2 coefficient (tol 3e-14)', () => {
  let worst = 0;
  for (let i = 0; i < 20; i += 1) {
    const beta = randomBeta(0.82);
    const n = randomVector(1);
    const r = 3 + 20 * random();
    const uniform = EM.makeKick({betaI: beta, betaF: beta, tau: 0.2});
    const field = EM.fieldAt(uniform, scale(n, r), r);
    const measured = dot(field.E, n);
    worst = Math.max(worst, Math.abs(measured - EM.coulombProfile(beta, n, r)));
  }
  assert.ok(worst < 3e-14);
  console.log(`  max radial-profile absolute residual ${fmt(worst)}`);
});

test('7 angular ledger: Coulomb change equals DC sphere divergence (analytic tol 2e-15, numeric tol 3e-9)', () => {
  let analyticWorst = 0;
  let numericWorst = 0;
  for (let i = 0; i < 30; i += 1) {
    const kick = EM.makeKick({betaI: randomBeta(0.75), betaF: randomBeta(0.75),
      profile: 'instant'});
    const n = randomVector(1);
    const ledger = EM.angularLedger(kick, n);
    analyticWorst = Math.max(analyticWorst, Math.abs(ledger.difference - ledger.dcRadiationTerm));
    const divergence = EM.sphereDivergence(direction => EM.dcRadiationField(kick, direction), n, 1e-4);
    numericWorst = Math.max(numericWorst, Math.abs(divergence - ledger.difference));
  }
  assert.ok(analyticWorst < 2e-15);
  assert.ok(numericWorst < 3e-9, `numerical divergence residual ${numericWorst}`);
  console.log(`  analytic residual ${fmt(analyticWorst)}, 5-point spherical residual ${fmt(numericWorst)}`);
});

test('8 Penrose tan-map and free-particle antipodes (tol 5e-15)', () => {
  const mapped = EM.penroseCoords(2.3, 4.7);
  const mapResidual = Math.max(Math.abs(Math.tan(mapped.U) - mapped.u),
    Math.abs(Math.tan(mapped.V) - mapped.v),
    Math.abs(mapped.T - mapped.U - mapped.V),
    Math.abs(mapped.R - mapped.V + mapped.U));
  let antipodalWorst = 0;
  for (let i = 0; i < 20; i += 1) {
    const endpoints = EM.freeParticleEndpoints(randomVector(3), randomBeta(0.9));
    antipodalWorst = Math.max(antipodalWorst, endpoints.antipodalResidual,
      norm(add(endpoints.past, endpoints.future)));
  }
  assert.ok(mapResidual < 5e-15 && antipodalWorst < 1e-15);
  console.log(`  compactification residual ${fmt(mapResidual)}, antipodal residual ${fmt(antipodalWorst)}`);
});

console.log('\nAll EMCore tests passed.');
