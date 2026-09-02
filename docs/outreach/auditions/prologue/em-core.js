/*
 * EMCore -- reference electrodynamics for the infrared-triangle prologue.
 * Gaussian natural units, c = hbar = 1.  Fields are per unit source charge;
 * an elementary charge has e^2 = alpha.  ES2017, no DOM and no dependencies.
 */
(function (root, factory) {
  'use strict';
  var EMCore = factory();
  if (typeof module === 'object' && module.exports) module.exports = EMCore;
  if (root) {
    root.PROLOGUE = root.PROLOGUE || {};
    root.PROLOGUE.em = EMCore;
  }
}(typeof window !== 'undefined' ? window : null, function () {
  'use strict';

  var RETARDED_TOLERANCE = 1e-13;
  var ALPHA = 1 / 137.035999084;
  var PI = Math.PI;

  function assertVector3(v, name) {
    if (!Array.isArray(v) || v.length !== 3 || !v.every(Number.isFinite)) {
      throw new TypeError(name + ' must be a finite three-vector');
    }
  }

  function add(a, b) { return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]; }
  function sub(a, b) { return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]; }
  function scale(a, s) { return [a[0] * s, a[1] * s, a[2] * s]; }
  function dot(a, b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }
  function cross(a, b) {
    return [a[1] * b[2] - a[2] * b[1],
      a[2] * b[0] - a[0] * b[2],
      a[0] * b[1] - a[1] * b[0]];
  }
  function norm2(a) { return dot(a, a); }
  function norm(a) { return Math.sqrt(norm2(a)); }
  function unit(a, name) {
    var m = norm(a);
    if (!(m > 0)) throw new RangeError((name || 'vector') + ' must be nonzero');
    return scale(a, 1 / m);
  }
  function clamp(x, lo, hi) { return Math.max(lo, Math.min(hi, x)); }
  function transverseDoubleCross(n, a) { return cross(n, cross(n, a)); }

  /* 1. Trajectory model -------------------------------------------------- */
  function makeKick(options) {
    options = options || {};
    var betaI = (options.betaI || [0, 0, 0]).slice();
    var betaF = (options.betaF || [0, 0, 0]).slice();
    var profile = options.profile || 'raised-cosine';
    var tau = options.tau == null ? 1 : Number(options.tau);
    assertVector3(betaI, 'betaI');
    assertVector3(betaF, 'betaF');
    if (norm2(betaI) >= 1 || norm2(betaF) >= 1) {
      throw new RangeError('endpoint speeds must be strictly smaller than c');
    }
    if (['raised-cosine', 'tanh', 'instant'].indexOf(profile) < 0) {
      throw new RangeError("profile must be 'raised-cosine', 'tanh', or 'instant'");
    }
    if (profile === 'instant') tau = 0;
    if (profile !== 'instant' && !(tau > 0)) {
      throw new RangeError('a smooth kick requires tau > 0');
    }
    var delta = sub(betaF, betaI);

    function blend(t) {
      if (profile === 'instant') return t < 0 ? 0 : 1;
      if (profile === 'raised-cosine') {
        var s = t / tau + 0.5;
        if (s <= 0) return 0;
        if (s >= 1) return 1;
        return 0.5 * (1 - Math.cos(PI * s));
      }
      var a = tau / 2;
      return 0.5 * (1 + Math.tanh(t / a));
    }

    function blendDerivative(t) {
      if (profile === 'instant') return 0;
      if (profile === 'raised-cosine') {
        var s = t / tau + 0.5;
        return s <= 0 || s >= 1 ? 0 : PI * Math.sin(PI * s) / (2 * tau);
      }
      var a = tau / 2;
      var c = Math.cosh(t / a);
      if (!Number.isFinite(c)) return 0;
      return 0.5 / (a * c * c);
    }

    // J(t) is an antiderivative of blend(t), normalized by J(0)=0.
    function blendIntegral(t) {
      if (profile === 'instant') return t < 0 ? 0 : t;
      if (profile === 'raised-cosine') {
        var s = t / tau + 0.5;
        function primitive(y) {
          return tau * (0.5 * y - Math.sin(PI * y) / (2 * PI));
        }
        var pHalf = primitive(0.5);
        if (s <= 0) return -pHalf;
        if (s >= 1) return primitive(1) - pHalf + (s - 1) * tau;
        return primitive(s) - pHalf;
      }
      var a = tau / 2;
      var z = t / a;
      // Stable log(cosh(z)); the subtraction at z=0 vanishes.
      var az = Math.abs(z);
      var logCosh = az + Math.log1p(Math.exp(-2 * az)) - Math.log(2);
      return 0.5 * (t + a * logCosh);
    }

    function position(t) {
      if (!Number.isFinite(t)) throw new TypeError('t must be finite');
      return add(scale(betaI, t), scale(delta, blendIntegral(t)));
    }
    function velocity(t) {
      if (!Number.isFinite(t)) throw new TypeError('t must be finite');
      return add(betaI, scale(delta, blend(t)));
    }
    function acceleration(t) {
      if (!Number.isFinite(t)) throw new TypeError('t must be finite');
      return scale(delta, blendDerivative(t));
    }

    var bounds = profile === 'raised-cosine' ? [-tau / 2, tau / 2]
      : profile === 'tanh' ? [-10 * tau, 10 * tau] : [0, 0];
    return Object.freeze({
      betaI: Object.freeze(betaI), betaF: Object.freeze(betaF),
      tau: tau, profile: profile, bounds: Object.freeze(bounds),
      position: position, velocity: velocity, acceleration: acceleration
    });
  }

  /* 2. Exact Lienard-Wiechert field ------------------------------------- */
  function retardedTime(kick, x, t) {
    assertVector3(x, 'x');
    if (!Number.isFinite(t)) throw new TypeError('t must be finite');
    function residual(s) {
      return t - s - norm(sub(x, kick.position(s)));
    }
    var hi = t;
    var fHi = residual(hi);
    if (Math.abs(fHi) <= RETARDED_TOLERANCE) return hi;
    var span = Math.max(1, norm(sub(x, kick.position(t))));
    var lo = t - span;
    var fLo = residual(lo);
    for (var grow = 0; fLo < 0 && grow < 200; grow += 1) {
      span *= 2;
      lo = t - span;
      fLo = residual(lo);
    }
    if (!(fLo >= 0 && fHi <= 0)) throw new Error('failed to bracket retarded time');

    var s = hi;
    for (var iter = 0; iter < 100; iter += 1) {
      var rVec = sub(x, kick.position(s));
      var distance = norm(rVec);
      var f = t - s - distance;
      if (Math.abs(f) <= RETARDED_TOLERANCE) return s;
      if (f > 0) { lo = s; fLo = f; } else { hi = s; fHi = f; }
      var direction = distance > 0 ? scale(rVec, 1 / distance) : [0, 0, 0];
      var derivative = -1 + dot(direction, kick.velocity(s));
      var candidate = s - f / derivative;
      if (!(candidate > lo && candidate < hi) || !Number.isFinite(candidate)) {
        candidate = (lo * (-fHi) + hi * fLo) / (fLo - fHi);
      }
      if (!(candidate > lo && candidate < hi) || !Number.isFinite(candidate)) {
        candidate = 0.5 * (lo + hi);
      }
      s = candidate;
    }
    s = 0.5 * (lo + hi);
    if (Math.abs(residual(s)) > 5 * RETARDED_TOLERANCE) {
      throw new Error('retarded-time solve did not reach tolerance');
    }
    return s;
  }

  function lwPieces(kick, x, t, tRet) {
    var rVec = sub(x, kick.position(tRet));
    var R = norm(rVec);
    if (!(R > 0)) throw new RangeError('field is singular on the charge');
    var n = scale(rVec, 1 / R);
    var beta = kick.velocity(tRet);
    var accel = kick.acceleration(tRet);
    var kappa = 1 - dot(n, beta);
    var velocityPart = scale(sub(n, beta),
      (1 - norm2(beta)) / (kappa * kappa * kappa * R * R));
    var radiationPart = scale(cross(n, cross(sub(n, beta), accel)),
      1 / (kappa * kappa * kappa * R));
    var E = add(velocityPart, radiationPart);
    return {E: E, B: cross(n, E), tRet: tRet, n: n, R: R,
      velocityPart: velocityPart, radiationPart: radiationPart};
  }

  function uniformRetardedTime(beta, x, t) {
    var a = 1 - norm2(beta);
    var b = 2 * (dot(x, beta) - t);
    var c = t * t - norm2(x);
    var disc = Math.max(0, b * b - 4 * a * c);
    return (-b - Math.sqrt(disc)) / (2 * a);
  }

  function uniformField(beta, x, t) {
    var tRet = uniformRetardedTime(beta, x, t);
    var fake = {
      position: function (s) { return scale(beta, s); },
      velocity: function () { return beta; },
      acceleration: function () { return [0, 0, 0]; }
    };
    return lwPieces(fake, x, t, tRet);
  }

  function shellMemoryCoefficient(betaI, betaF, nhat) {
    var n = unit(nhat, 'nhat');
    var hi = scale(betaI, 1 / (1 - dot(n, betaI)));
    var hf = scale(betaF, 1 / (1 - dot(n, betaF)));
    return transverseDoubleCross(n, sub(hf, hi));
  }

  function instantField(kick, x, t) {
    var radius = norm(x);
    var onShell = t >= 0 && Math.abs(radius - t) <= RETARDED_TOLERANCE;
    var useNew = t > radius;
    var result = uniformField(useNew ? kick.betaF : kick.betaI, x, t);
    if (onShell && radius > 0) {
      var radialDirection = scale(x, 1 / radius);
      var coefficient = scale(shellMemoryCoefficient(
        kick.betaI, kick.betaF, radialDirection), 1 / radius);
      result.shell = Object.freeze({
        distribution: 'delta(t-|x|)',
        transverseCoefficient: Object.freeze(coefficient),
        note: 'radiationPart contains only the regular part; multiply this coefficient by delta(t-|x|)'
      });
    } else {
      result.shell = null;
    }
    return result;
  }

  function fieldAt(kick, x, t) {
    if (!kick || typeof kick.position !== 'function') throw new TypeError('invalid kick');
    assertVector3(x, 'x');
    if (kick.profile === 'instant') return instantField(kick, x, t);
    var tRet = retardedTime(kick, x, t);
    return lwPieces(kick, x, t, tRet);
  }

  /* 3. Field lines ------------------------------------------------------ */
  function fieldDirection(kick, t, point, sign) {
    var E = fieldAt(kick, point, t).E;
    var magnitude = norm(E);
    if (!(magnitude > 0) || !Number.isFinite(magnitude)) return null;
    return scale(E, sign / magnitude);
  }

  function rk4FieldStep(kick, t, point, h, sign) {
    var k1 = fieldDirection(kick, t, point, sign);
    if (!k1) return null;
    var k2 = fieldDirection(kick, t, add(point, scale(k1, h / 2)), sign);
    if (!k2) return null;
    var k3 = fieldDirection(kick, t, add(point, scale(k2, h / 2)), sign);
    if (!k3) return null;
    var k4 = fieldDirection(kick, t, add(point, scale(k3, h)), sign);
    if (!k4) return null;
    return add(point, scale(add(add(k1, scale(k2, 2)), add(scale(k3, 2), k4)), h / 6));
  }

  function fieldLine(kick, t, seedPoint, options) {
    options = options || {};
    assertVector3(seedPoint, 'seedPoint');
    if (kick.profile === 'instant') {
      throw new RangeError('fieldLine requires a smooth kick; use purcellLines for instant');
    }
    var step = options.step == null ? 0.05 : Number(options.step);
    var maxSteps = options.maxSteps == null ? 800 : Math.floor(options.maxSteps);
    if (!(step > 0) || !(maxSteps > 0)) throw new RangeError('step and maxSteps must be positive');

    function trace(sign) {
      var points = [seedPoint.slice()];
      for (var i = 0; i < maxSteps; i += 1) {
        var next;
        try { next = rk4FieldStep(kick, t, points[points.length - 1], step, sign); }
        catch (error) { break; }
        if (!next || !next.every(Number.isFinite)) break;
        points.push(next);
        if (norm(sub(next, kick.position(t))) < step * 0.6) break;
      }
      return points;
    }
    var backward = trace(-1).reverse();
    var forward = trace(1);
    return backward.slice(0, -1).concat(forward);
  }

  function aberrateDirection(restDirection, beta) {
    var ell = unit(restDirection, 'restDirection');
    var b2 = norm2(beta);
    if (b2 === 0) return ell;
    var gamma = 1 / Math.sqrt(1 - b2);
    var betaDotEll = dot(beta, ell);
    var spatial = add(ell, scale(beta,
      gamma + (gamma - 1) * betaDotEll / b2));
    return scale(spatial, 1 / (gamma * (1 + betaDotEll)));
  }

  function slerpUnit(a, b, fraction) {
    var cosine = clamp(dot(a, b), -1, 1);
    var angle = Math.acos(cosine);
    if (angle < 1e-12) return unit(add(scale(a, 1 - fraction), scale(b, fraction)));
    var sine = Math.sin(angle);
    return add(scale(a, Math.sin((1 - fraction) * angle) / sine),
      scale(b, Math.sin(fraction * angle) / sine));
  }

  function fibonacciDirections(count) {
    var directions = [];
    var goldenAngle = PI * (3 - Math.sqrt(5));
    for (var i = 0; i < count; i += 1) {
      var z = 1 - 2 * (i + 0.5) / count;
      var radial = Math.sqrt(Math.max(0, 1 - z * z));
      var phi = i * goldenAngle;
      directions.push([radial * Math.cos(phi), radial * Math.sin(phi), z]);
    }
    return directions;
  }

  function purcellLines(betaI, betaF, t, options) {
    options = options || {};
    assertVector3(betaI, 'betaI');
    assertVector3(betaF, 'betaF');
    if (norm2(betaI) >= 1 || norm2(betaF) >= 1) throw new RangeError('speeds must be subluminal');
    if (!(t > 0)) throw new RangeError('Purcell construction requires t > 0');
    var nLines = options.nLines == null ? 24 : Math.floor(options.nLines);
    if (!(nLines >= 2)) throw new RangeError('nLines must be at least 2');
    var labels = fibonacciDirections(nLines);
    return labels.map(function (label, index) {
      var outerDirection = aberrateDirection(label, betaI);
      var innerDirection = aberrateDirection(label, betaF);
      var oldPosition = scale(betaI, t);
      var newPosition = scale(betaF, t);
      var outerShell = scale(outerDirection, t);
      var innerShell = scale(innerDirection, t);
      var outerRay = unit(sub(outerShell, oldPosition));
      var connector = [];
      var connectorSteps = 12;
      for (var j = 0; j <= connectorSteps; j += 1) {
        connector.push(scale(slerpUnit(innerDirection, outerDirection,
          j / connectorSteps), t));
      }
      return Object.freeze({
        index: index, label: Object.freeze(label), flux: 4 * PI / nLines,
        innerDirection: Object.freeze(innerDirection),
        outerDirection: Object.freeze(outerDirection),
        inner: Object.freeze([Object.freeze(newPosition), Object.freeze(innerShell)]),
        shell: Object.freeze(connector.map(Object.freeze)),
        outer: Object.freeze([Object.freeze(outerShell),
          Object.freeze(add(outerShell, scale(outerRay, t)))])
      });
    });
  }

  /* 4. Frequency domain ------------------------------------------------- */
  var GL8_X = [
    -0.9602898564975363, -0.7966664774136267,
    -0.5255324099163290, -0.1834346424956498,
    0.1834346424956498, 0.5255324099163290,
    0.7966664774136267, 0.9602898564975363
  ];
  var GL8_W = [
    0.1012285362903763, 0.2223810344533745,
    0.3137066458778873, 0.3626837833783620,
    0.3626837833783620, 0.3137066458778873,
    0.2223810344533745, 0.1012285362903763
  ];

  function gaussLegendre8Vector(fn, a, b, panels, dimension) {
    var result = new Array(dimension).fill(0);
    var width = (b - a) / panels;
    for (var panel = 0; panel < panels; panel += 1) {
      var left = a + panel * width;
      var mid = left + width / 2;
      var half = width / 2;
      for (var j = 0; j < 8; j += 1) {
        var value = fn(mid + half * GL8_X[j]);
        var weight = half * GL8_W[j];
        for (var k = 0; k < dimension; k += 1) result[k] += weight * value[k];
      }
    }
    return result;
  }

  function radiationAmplitudeVector(kick, nhat, omega, options) {
    var n = unit(nhat, 'nhat');
    if (!(omega >= 0) || !Number.isFinite(omega)) throw new RangeError('omega must be finite and nonnegative');
    var dc = shellMemoryCoefficient(kick.betaI, kick.betaF, n);
    if (kick.profile === 'instant' || omega === 0) {
      return dc.map(function (x) { return Object.freeze({re: x, im: 0}); });
    }
    options = options || {};
    var oscillations = omega * Math.max(kick.tau, 1e-15);
    var panels = options.n == null ? Math.max(24, Math.ceil(24 + 2 * oscillations))
      : Math.max(1, Math.floor(options.n));
    var bounds = kick.bounds;
    var raw = gaussLegendre8Vector(function (s) {
      var beta = kick.velocity(s);
      var accel = kick.acceleration(s);
      var kappa = 1 - dot(n, beta);
      var g = scale(cross(n, cross(sub(n, beta), accel)), 1 / (kappa * kappa));
      var phase = omega * (s - dot(n, kick.position(s)));
      var c = Math.cos(phase);
      var si = Math.sin(phase);
      return [g[0] * c, g[1] * c, g[2] * c,
        g[0] * si, g[1] * si, g[2] * si];
    }, bounds[0], bounds[1], panels, 6);
    return [0, 1, 2].map(function (j) {
      return Object.freeze({re: raw[j], im: raw[j + 3]});
    });
  }

  function radiationSpectrum(kick, nhat, omegas, options) {
    if (!Array.isArray(omegas)) throw new TypeError('omegas must be an array');
    return omegas.map(function (omega) {
      var amplitude = radiationAmplitudeVector(kick, nhat, Number(omega), options);
      var absoluteSquared = amplitude.reduce(function (sum, z) {
        return sum + z.re * z.re + z.im * z.im;
      }, 0);
      // Gaussian units: q=e, e^2=alpha, positive-frequency convention.
      return ALPHA * absoluteSquared / (4 * PI * PI);
    });
  }

  function checkedPolarization(nhat, eps) {
    assertVector3(eps, 'eps');
    var n = unit(nhat, 'nhat');
    var eNorm = norm(eps);
    if (!(eNorm > 0)) throw new RangeError('eps must be nonzero');
    var e = eps.slice();
    if (Math.abs(dot(n, e)) > 1e-10 * eNorm) throw new RangeError('eps must be transverse to nhat');
    return {n: n, eps: e};
  }

  function softAmplitude(kick, nhat, eps) {
    var basis = checkedPolarization(nhat, eps);
    var n = basis.n;
    var hi = scale(kick.betaI, 1 / (1 - dot(n, kick.betaI)));
    var hf = scale(kick.betaF, 1 / (1 - dot(n, kick.betaF)));
    // Coefficient of 1/omega in the current/potential amplitude.  The
    // electric radiation convention carries the opposite transverse sign.
    return dot(sub(hf, hi), basis.eps);
  }

  function softFactorWeinberg(particles, nhat, eps) {
    if (!Array.isArray(particles)) throw new TypeError('particles must be an array');
    var basis = checkedPolarization(nhat, eps);
    return particles.reduce(function (sum, particle) {
      validateParticle(particle);
      var denominator = 1 - dot(basis.n, particle.beta);
      if (denominator <= 1e-15) throw new RangeError('soft factor is singular at a null collinear pole');
      return sum + particle.eta * particle.Q * dot(particle.beta, basis.eps) / denominator;
    }, 0);
  }

  function photonNumber(kick, nhat, omegaMin, omegaMax, options) {
    if (!(omegaMin > 0) || !(omegaMax > omegaMin)) {
      throw new RangeError('require 0 < omegaMin < omegaMax');
    }
    var n = unit(nhat, 'nhat');
    if (kick.profile === 'instant') {
      var g = shellMemoryCoefficient(kick.betaI, kick.betaF, n);
      return ALPHA * norm2(g) * Math.log(omegaMax / omegaMin) / (4 * PI * PI);
    }
    options = options || {};
    var panels = options.n == null ? 48 : Math.max(1, Math.floor(options.n));
    var lo = Math.log(omegaMin);
    var hi = Math.log(omegaMax);
    // d omega / omega = d(log omega), so this directly integrates dI/domega.
    return gaussLegendre8Vector(function (logOmega) {
      var omega = Math.exp(logOmega);
      return [radiationSpectrum(kick, n, [omega], options)[0]];
    }, lo, hi, panels, 1)[0];
  }

  /* 5. Celestial sphere ------------------------------------------------- */
  function validateParticle(particle) {
    assertVector3(particle.beta, 'particle.beta');
    if (norm2(particle.beta) > 1 + 1e-14) throw new RangeError('particle speed cannot exceed c');
    if (particle.eta !== 1 && particle.eta !== -1) throw new RangeError('particle.eta must be +1 or -1');
    if (!Number.isFinite(particle.Q)) throw new TypeError('particle.Q must be finite');
  }

  function chargeConservation(particles, tolerance) {
    if (!Array.isArray(particles)) throw new TypeError('particles must be an array');
    tolerance = tolerance == null ? 1e-12 : Math.abs(tolerance);
    var sum = particles.reduce(function (total, particle) {
      validateParticle(particle);
      return total + particle.eta * particle.Q;
    }, 0);
    return Object.freeze({sum: sum, conserved: Math.abs(sum) <= tolerance,
      tolerance: tolerance});
  }

  function spherePattern(particles, nhat) {
    if (!Array.isArray(particles)) throw new TypeError('particles must be an array');
    var n = unit(nhat, 'nhat');
    var current = particles.reduce(function (sum, particle) {
      validateParticle(particle);
      var denominator = 1 - dot(n, particle.beta);
      if (denominator <= 1e-15) throw new RangeError('sphere pattern is singular at a null collinear pole');
      return add(sum, scale(particle.beta, particle.eta * particle.Q / denominator));
    }, [0, 0, 0]);
    return norm2(transverseDoubleCross(n, current));
  }

  /* 6. Memory: radiation-order identity and separate Coulomb drift ------ */
  function memoryKickClosedForm(kick, x) {
    assertVector3(x, 'x');
    var radius = norm(x);
    if (!(radius > 0)) throw new RangeError('x must be away from the source');
    return scale(shellMemoryCoefficient(kick.betaI, kick.betaF,
      scale(x, 1 / radius)), 1 / radius);
  }

  function memoryKickQuadrature(kick, x, options) {
    options = options || {};
    assertVector3(x, 'x');
    var radius = norm(x);
    if (!(radius > 0)) throw new RangeError('x must be away from the source');
    var n = scale(x, 1 / radius);
    if (kick.profile === 'instant') return memoryKickClosedForm(kick, x);
    var rule = options.rule || 'gauss-legendre';
    if (rule !== 'gauss-legendre') throw new RangeError("rule must be 'gauss-legendre'");
    var panels = options.n == null ? 16 : Math.max(1, Math.floor(options.n));
    var integral;
    if (kick.profile === 'tanh') {
      // y=blend(s) maps the infinite tanh tail exactly to [0,1], and
      // acceleration(s) ds = (betaF-betaI) dy.
      var deltaBeta = sub(kick.betaF, kick.betaI);
      integral = gaussLegendre8Vector(function (y) {
        var beta = add(kick.betaI, scale(deltaBeta, y));
        var kappa = 1 - dot(n, beta);
        return scale(cross(n, cross(sub(n, beta), deltaBeta)), 1 / (kappa * kappa));
      }, 0, 1, panels, 3);
    } else {
      integral = gaussLegendre8Vector(function (s) {
      var beta = kick.velocity(s);
      var accel = kick.acceleration(s);
      var kappa = 1 - dot(n, beta);
      return scale(cross(n, cross(sub(n, beta), accel)), 1 / (kappa * kappa));
      }, kick.bounds[0], kick.bounds[1], panels, 3);
    }
    return scale(integral, 1 / radius);
  }

  function uniformCoulombAntiderivative(beta, x, t) {
    var speed = norm(beta);
    if (speed < 1e-14) return scale(x, t / Math.pow(norm(x), 3));
    var bhat = scale(beta, 1 / speed);
    var xParallel = dot(x, bhat);
    var xPerp = sub(x, scale(bhat, xParallel));
    var xPerp2 = norm2(xPerp);
    var y = xParallel - speed * t;
    var d = Math.sqrt(y * y + (1 - speed * speed) * xPerp2);
    if (!(d > 0)) throw new RangeError('Coulomb drift is singular where the charge meets x');
    var primitive = scale(bhat, (1 - speed * speed) / (speed * d));
    if (xPerp2 > 1e-28) {
      primitive = add(primitive, scale(xPerp, -y / (speed * xPerp2 * d)));
    }
    return primitive;
  }

  function uniformCoulombIntegral(beta, x, t0, t1) {
    return sub(uniformCoulombAntiderivative(beta, x, t1),
      uniformCoulombAntiderivative(beta, x, t0));
  }

  function coulombDrift(kick, x, t0, t1) {
    assertVector3(x, 'x');
    if (!Number.isFinite(t0) || !Number.isFinite(t1) || t1 < t0) {
      throw new RangeError('require finite t0 <= t1');
    }
    if (norm2(sub(kick.betaI, kick.betaF)) < 1e-30) {
      return uniformCoulombIntegral(kick.betaI, x, t0, t1);
    }
    if (kick.profile !== 'instant') {
      throw new RangeError('closed-form Coulomb drift is defined for the instantaneous Purcell kick');
    }
    var arrival = norm(x);
    var result = [0, 0, 0];
    if (t0 < Math.min(t1, arrival)) {
      result = add(result, uniformCoulombIntegral(kick.betaI, x,
        t0, Math.min(t1, arrival)));
    }
    if (t1 > Math.max(t0, arrival)) {
      result = add(result, uniformCoulombIntegral(kick.betaF, x,
        Math.max(t0, arrival), t1));
    }
    return result;
  }

  /* 7. Conservation per angle ------------------------------------------ */
  function coulombProfile(beta, nhat, radius) {
    assertVector3(beta, 'beta');
    if (norm2(beta) >= 1) throw new RangeError('speed must be subluminal');
    var n = unit(nhat, 'nhat');
    radius = radius == null ? 1 : Number(radius);
    if (!(radius > 0)) throw new RangeError('r must be positive');
    var kappa = 1 - dot(n, beta);
    return (1 - norm2(beta)) / (kappa * kappa * radius * radius);
  }

  function sphericalFrame(direction) {
    var n = unit(direction, 'nhat');
    var zAxis = Math.abs(n[2]) < 0.8 ? [0, 0, 1] : [1, 0, 0];
    var trial = Math.abs(zAxis[1]) < 0.8 ? [0, 1, 0] : [0, 0, 1];
    var xAxis = unit(cross(trial, zAxis));
    var yAxis = cross(zAxis, xAxis);
    var theta = Math.acos(clamp(dot(n, zAxis), -1, 1));
    var phi = Math.atan2(dot(n, yAxis), dot(n, xAxis));
    function at(th, ph) {
      var st = Math.sin(th), ct = Math.cos(th);
      var cp = Math.cos(ph), sp = Math.sin(ph);
      return {
        n: add(add(scale(xAxis, st * cp), scale(yAxis, st * sp)), scale(zAxis, ct)),
        eTheta: add(add(scale(xAxis, ct * cp), scale(yAxis, ct * sp)), scale(zAxis, -st)),
        ePhi: add(scale(xAxis, -sp), scale(yAxis, cp))
      };
    }
    return {theta: theta, phi: phi, at: at};
  }

  function derivative5(fn, x, h) {
    return (fn(x - 2 * h) - 8 * fn(x - h) + 8 * fn(x + h) - fn(x + 2 * h)) /
      (12 * h);
  }

  function sphereDivergence(vectorField, nhat, h) {
    if (typeof vectorField !== 'function') throw new TypeError('vectorField must be a function');
    h = h == null ? 1e-4 : Number(h);
    if (!(h > 0 && h < 0.05)) throw new RangeError('h must lie between 0 and 0.05');
    var frame = sphericalFrame(nhat);
    var theta = frame.theta;
    var phi = frame.phi;
    function sinATheta(th) {
      var basis = frame.at(th, phi);
      return Math.sin(th) * dot(vectorField(basis.n), basis.eTheta);
    }
    function aPhi(ph) {
      var basis = frame.at(theta, ph);
      return dot(vectorField(basis.n), basis.ePhi);
    }
    return (derivative5(sinATheta, theta, h) + derivative5(aPhi, phi, h)) /
      Math.sin(theta);
  }

  function dcRadiationField(kick, nhat) {
    return shellMemoryCoefficient(kick.betaI, kick.betaF, nhat);
  }

  function angularLedger(kick, nhat) {
    var n = unit(nhat, 'nhat');
    var before = coulombProfile(kick.betaI, n, 1);
    var after = coulombProfile(kick.betaF, n, 1);
    // In spherical coordinates div_S grad_S log(1-n.beta)
    // = (1-beta^2)/(1-n.beta)^2 - 1.  The constants cancel in the kick.
    var divergenceBefore = before - 1;
    var divergenceAfter = after - 1;
    return Object.freeze({before: before, after: after,
      difference: after - before,
      dcRadiationTerm: divergenceAfter - divergenceBefore});
  }

  /* 8. Antipodal geometry ---------------------------------------------- */
  function penroseCoords(t, radius) {
    if (!Number.isFinite(t) || !Number.isFinite(radius) || radius < 0) {
      throw new RangeError('penroseCoords requires finite t and r >= 0');
    }
    var u = t - radius;
    var v = t + radius;
    var U = Math.atan(u);
    var V = Math.atan(v);
    return Object.freeze({u: u, v: v, U: U, V: V,
      T: U + V, R: V - U});
  }

  function freeParticleEndpoints(x0, velocity) {
    assertVector3(x0, 'x0');
    assertVector3(velocity, 'v');
    if (norm2(velocity) >= 1) throw new RangeError('speed must be subluminal');
    var future = unit(velocity, 'v');
    var past = scale(future, -1);
    return Object.freeze({past: Object.freeze(past), future: Object.freeze(future),
      antipodalResidual: norm(add(past, future))});
  }

  return {
    constants: Object.freeze({alpha: ALPHA, c: 1, hbar: 1,
      retardedTolerance: RETARDED_TOLERANCE, units: 'Gaussian'}),
    makeKick: makeKick,
    fieldAt: fieldAt,
    fieldLine: fieldLine,
    purcellLines: purcellLines,
    radiationSpectrum: radiationSpectrum,
    softAmplitude: softAmplitude,
    softFactorWeinberg: softFactorWeinberg,
    photonNumber: photonNumber,
    spherePattern: spherePattern,
    chargeConservation: chargeConservation,
    memoryKickQuadrature: memoryKickQuadrature,
    memoryKickClosedForm: memoryKickClosedForm,
    coulombDrift: coulombDrift,
    coulombProfile: coulombProfile,
    angularLedger: angularLedger,
    sphereDivergence: sphereDivergence,
    dcRadiationField: dcRadiationField,
    penroseCoords: penroseCoords,
    freeParticleEndpoints: freeParticleEndpoints
  };
}));
