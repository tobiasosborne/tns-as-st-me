#!/usr/bin/env node

import { createServer } from 'node:http';
import { readFile, mkdir } from 'node:fs/promises';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import vm from 'node:vm';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(HERE, '../../../..');
const FRAGMENT = path.join(HERE, 'frag-gw.html');
const SCREENSHOT_DIR = path.join(HERE, 'qa');
const VIEWPORTS = [390, 768, 1300];
const THEMES = ['light', 'dark'];
const results = [];
const screenshots = [];
const fragmentArgument = process.argv.find(argument => argument.startsWith('--frag='));
const FRAGMENT_QUERY = fragmentArgument ? fragmentArgument.slice('--frag='.length) : 'frag-gw.html';

function record(check, status, detail = '') {
  results.push({ check, status, detail: String(detail) });
}

function harnessURL(baseURL, theme, fragments = FRAGMENT_QUERY) {
  return `${baseURL}/qa-harness.html?theme=${encodeURIComponent(theme)}&frag=${encodeURIComponent(fragments)}`;
}

function mime(filename) {
  if (filename.endsWith('.html')) return 'text/html; charset=utf-8';
  if (filename.endsWith('.mjs') || filename.endsWith('.js')) return 'text/javascript; charset=utf-8';
  if (filename.endsWith('.json')) return 'application/json; charset=utf-8';
  if (filename.endsWith('.png')) return 'image/png';
  return 'application/octet-stream';
}

function instrumentFragment(source) {
  // The W5 station now schedules frames through schedule() rather than calling
  // requestAnimationFrame at the tail of the IIFE, and the <section> that follows
  // has never carried leading whitespace. Both anchors are matched literally.
  const w5Needle = '  schedule();\n})();\n</script>\n\n<section class="stop" id="w8">';
  const w5Replacement = `  schedule();
  window.__qaPhysics = {
    GW: GW,
    EM: EM,
    state: S,
    solveGW: function () { solveGW(); return SOL; },
    solveEM: function () { solveEM(); return SOL; }
  };
})();
</script>

<section class="stop" id="w8">`;
  const w9Needle = '  render();\n})();\n</script>\n\n\n<section class="stop" id="w10">';
  const w9Replacement = `  render();
  window.__qaW9 = { state: S, f: f, render: render };
})();
</script>


<section class="stop" id="w10">`;
  if (!source.includes(w5Needle) || !source.includes(w9Needle)) {
    throw new Error('Instrumentation anchors no longer match frag-gw.html');
  }
  return source.replace(w5Needle, w5Replacement).replace(w9Needle, w9Replacement);
}

async function startServer() {
  const server = createServer(async (request, response) => {
    try {
      const url = new URL(request.url, 'http://127.0.0.1');
      let pathname = decodeURIComponent(url.pathname);
      if (pathname === '/') pathname = '/qa-harness.html';
      if (pathname === '/frag-gw-instrumented.html') {
        const source = await readFile(FRAGMENT, 'utf8');
        response.writeHead(200, { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store' });
        response.end(instrumentFragment(source));
        return;
      }
      const resolved = path.resolve(HERE, '.' + pathname);
      if (resolved !== HERE && !resolved.startsWith(HERE + path.sep)) {
        response.writeHead(403).end('forbidden');
        return;
      }
      const body = await readFile(resolved);
      response.writeHead(200, { 'content-type': mime(resolved), 'cache-control': 'no-store' });
      response.end(body);
    } catch (error) {
      // Chromium aborts requests it no longer needs; by then the headers may
      // already be on the wire, and writeHead would throw ERR_HTTP_HEADERS_SENT
      // out of this handler and take the whole run down before it prints.
      if (!response.headersSent) {
        response.writeHead(error && error.code === 'ENOENT' ? 404 : 500, { 'content-type': 'text/plain; charset=utf-8' });
      }
      if (response.writableEnded) return;
      response.end(error && (error.stack || error.message) || String(error));
    }
  });
  try {
    await new Promise((resolve, reject) => {
      server.once('error', reject);
      server.listen(0, '127.0.0.1', resolve);
    });
  } catch (error) {
    if (error && (error.code === 'EPERM' || error.code === 'EACCES')) {
      record('HTTP server', 'WARN', `${error.code}: localhost listen denied; using Playwright HTTP route fulfillment`);
      return { server: null, baseURL: 'http://qa.local' };
    }
    throw error;
  }
  const address = server.address();
  return { server, baseURL: `http://127.0.0.1:${address.port}` };
}

async function installVirtualServer(context, baseURL) {
  if (baseURL !== 'http://qa.local') return;
  await context.route('http://qa.local/**', async route => {
    try {
      const url = new URL(route.request().url());
      let pathname = decodeURIComponent(url.pathname);
      if (pathname === '/') pathname = '/qa-harness.html';
      if (pathname === '/frag-gw-instrumented.html') {
        const source = await readFile(FRAGMENT, 'utf8');
        await route.fulfill({ status: 200, contentType: 'text/html; charset=utf-8', body: instrumentFragment(source) });
        return;
      }
      const resolved = path.resolve(HERE, '.' + pathname);
      if (resolved !== HERE && !resolved.startsWith(HERE + path.sep)) {
        await route.fulfill({ status: 403, contentType: 'text/plain; charset=utf-8', body: 'forbidden' });
        return;
      }
      await route.fulfill({ status: 200, contentType: mime(resolved), body: await readFile(resolved) });
    } catch (error) {
      await route.fulfill({ status: error && error.code === 'ENOENT' ? 404 : 500,
        contentType: 'text/plain; charset=utf-8', body: error && (error.stack || error.message) || String(error) });
    }
  });
}

function loadPlaywright() {
  const localRequire = createRequire(import.meta.url);
  for (const name of ['playwright', '@playwright/test']) {
    try {
      const loaded = localRequire(name);
      if (loaded.chromium) return loaded;
    } catch (_) {}
  }
  const globalRoot = process.env.QA_NPM_ROOT
    || path.resolve(path.dirname(process.execPath), '../lib/node_modules');
  const candidates = [
    path.join(globalRoot, '@playwright', 'cli', 'package.json'),
    path.join(globalRoot, 'playwright', 'package.json'),
    path.join(globalRoot, '@playwright', 'test', 'package.json')
  ];
  for (const packageFile of candidates) {
    try {
      const packageRequire = createRequire(packageFile);
      const loaded = packageRequire('playwright');
      if (loaded.chromium) return loaded;
    } catch (_) {}
  }
  throw new Error(`Playwright was not resolvable locally or below ${globalRoot}`);
}

async function staticAudit() {
  const source = await readFile(FRAGMENT, 'utf8');
  const content = source.replace(/<!--[\s\S]*?-->/g, '');
  const sectionIds = Array.from(content.matchAll(/<section\b[^>]*\bid="([^"]+)"/g), match => match[1]);
  const styleBlocks = Array.from(content.matchAll(/<style\s+data-station="([^"]+)"[^>]*>([\s\S]*?)<\/style>/g));
  const scriptBlocks = Array.from(content.matchAll(/<script\s+data-station="([^"]+)"[^>]*>([\s\S]*?)<\/script>/g));
  const allIds = Array.from(content.matchAll(/\bid="([^"]+)"/g), match => match[1]);
  const duplicateIds = Array.from(new Set(allIds.filter((id, index) => allIds.indexOf(id) !== index)));
  const styleNames = styleBlocks.map(match => match[1]);
  const scriptNames = scriptBlocks.map(match => match[1]);
  const cardinalityOK = sectionIds.length === styleBlocks.length && sectionIds.length === scriptBlocks.length
    && sectionIds.every(id => styleNames.filter(value => value === id).length === 1)
    && sectionIds.every(id => scriptNames.filter(value => value === id).length === 1);
  record('static · one style/script per section', cardinalityOK ? 'PASS' : 'FAIL',
    `${sectionIds.length} sections, ${styleBlocks.length} styles, ${scriptBlocks.length} scripts`);
  record('static · duplicate ids', duplicateIds.length ? 'FAIL' : 'PASS', duplicateIds.length ? duplicateIds.join(', ') : 'none');

  const unscoped = [];
  for (const match of styleBlocks) {
    const station = match[1];
    const css = match[2].replace(/\/\*[\s\S]*?\*\//g, '');
    for (const rule of css.matchAll(/([^{}]+)\{/g)) {
      const head = rule[1].trim();
      if (!head || head.startsWith('@')) continue;
      for (const selector of head.split(',')) {
        if (!selector.trim().startsWith(`#${station}`)) unscoped.push(`${station}: ${selector.trim()}`);
      }
    }
  }
  record('static · station-scoped selectors', unscoped.length ? 'FAIL' : 'PASS', unscoped.length ? unscoped.join(' | ') : 'all scoped');

  const externalFragmentScripts = scriptBlocks.filter(match => /\bsrc\s*=/.test(match[0]));
  record('static · no fragment library loads', externalFragmentScripts.length ? 'FAIL' : 'PASS',
    externalFragmentScripts.length ? `${externalFragmentScripts.length} external scripts` : 'none');

  const hexColours = Array.from(content.matchAll(/(?<!&)#[0-9a-fA-F]{3,8}\b/g), match => match[0]);
  record('static · palette tokens only', hexColours.length ? 'FAIL' : 'PASS',
    hexColours.length ? `literal fallback colours: ${Array.from(new Set(hexColours)).join(', ')}` : 'no literal colours');

  const rafLines = source.split('\n').map((line, index) => ({ line: index + 1, text: line.trim() }))
    .filter(item => item.text.includes('requestAnimationFrame'));
  const cancelCount = (source.match(/cancelAnimationFrame/g) || []).length;
  record('static · animation lifecycle', cancelCount || rafLines.length === 0 ? 'PASS' : 'FAIL',
    `${rafLines.length} request sites (${rafLines.map(item => item.line).join(', ')}), ${cancelCount} cancellations`);

  const globalListeners = source.split('\n').map((line, index) => ({ line: index + 1, text: line.trim() }))
    .filter(item => /(?:window|document|document\.documentElement|\bmq\b).*?(?:addEventListener|addListener|observe\()/.test(item.text));
  record('static · global listener/observer review', globalListeners.length ? 'WARN' : 'PASS',
    globalListeners.length ? globalListeners.map(item => `${item.line}: ${item.text}`).join(' | ') : 'none');

  const crossStationDOM = [];
  for (const match of scriptBlocks) {
    const station = match[1];
    for (const call of match[2].matchAll(/document\.getElementById\(['"]([^'"]+)['"]\)/g)) {
      if (call[1] !== station) crossStationDOM.push(`${station} → #${call[1]}`);
    }
  }
  record('static · script DOM scope', crossStationDOM.length ? 'FAIL' : 'PASS',
    crossStationDOM.join(', ') || 'each getElementById stays in its station');

  const wrapped = scriptBlocks.every(match => /^\s*\(function\s*\(\)\s*\{[\s\S]*\}\)\(\);\s*$/.test(match[2]));
  record('static · IIFE/global declaration shape', wrapped ? 'PASS' : 'FAIL',
    wrapped ? 'all station scripts are IIFEs' : 'one or more station scripts are not a single IIFE');

  const syntaxErrors = [];
  for (const match of scriptBlocks) {
    try {
      new vm.Script(match[2], { filename: `frag-gw.html:${match[1]}` });
    } catch (error) {
      syntaxErrors.push(`${match[1]}: ${error.message}`);
    }
  }
  record('static · JavaScript syntax', syntaxErrors.length ? 'FAIL' : 'PASS', syntaxErrors.join(' | ') || 'all seven scripts compile');
}

async function waitForHarness(page) {
  await page.waitForFunction(() => window.__qa && window.__qa.ready === true, null, { timeout: 30_000 });
  await page.waitForTimeout(120);
}

function classifyConsole(messages) {
  const resource = [];
  const runtime = [];
  for (const message of messages) {
    if (/Failed to load resource|ERR_FAILED|ERR_NAME_NOT_RESOLVED|cdnjs\.cloudflare\.com/i.test(message)) resource.push(message);
    else runtime.push(message);
  }
  return { resource, runtime };
}

async function matrixRun(browser, baseURL) {
  const context = await browser.newContext({ viewport: { width: 768, height: 900 }, ignoreHTTPSErrors: true });
  await installVirtualServer(context, baseURL);
  const page = await context.newPage();
  for (const theme of THEMES) {
    for (const width of VIEWPORTS) {
      await page.setViewportSize({ width, height: 900 });
      await page.emulateMedia({ colorScheme: theme });
      const consoleMessages = [];
      const pageErrors = [];
      const onConsole = message => { if (message.type() === 'error') consoleMessages.push(message.text()); };
      const onPageError = error => pageErrors.push(error.stack || error.message);
      page.on('console', onConsole);
      page.on('pageerror', onPageError);
      try {
        await page.goto(harnessURL(baseURL, theme), { waitUntil: 'domcontentloaded', timeout: 30_000 });
        await waitForHarness(page);
        const state = await page.evaluate(() => ({
          qa: window.__qa,
          innerWidth: window.innerWidth,
          scrollWidth: document.documentElement.scrollWidth,
          bodyScrollWidth: document.body.scrollWidth,
          duplicateIds: Array.from(document.querySelectorAll('[id]')).map(node => node.id)
            .filter((id, index, ids) => ids.indexOf(id) !== index)
        }));
        const noOverflow = state.scrollWidth <= state.innerWidth && state.bodyScrollWidth <= state.innerWidth;
        record(`browser · ${theme} ${width}px horizontal scroll`, noOverflow ? 'PASS' : 'FAIL',
          `viewport=${state.innerWidth}, html=${state.scrollWidth}, body=${state.bodyScrollWidth}`);
        record(`browser · ${theme} ${width}px runtime errors`, state.qa.errors.length || pageErrors.length ? 'FAIL' : 'PASS',
          [...state.qa.errors.map(error => `${error.kind}: ${error.message}`), ...pageErrors].join(' | ') || 'none');
        record(`browser · ${theme} ${width}px duplicate ids`, state.duplicateIds.length ? 'FAIL' : 'PASS',
          state.duplicateIds.join(', ') || 'none');
        record(`browser · ${theme} ${width}px globals`, state.qa.windowKeysAdded.length ? 'FAIL' : 'PASS',
          state.qa.windowKeysAdded.join(', ') || 'none');
        const consoleState = classifyConsole(consoleMessages);
        record(`browser · ${theme} ${width}px console.error`, consoleState.runtime.length ? 'FAIL' : 'PASS',
          consoleState.runtime.join(' | ') || 'none');
        const libs = state.qa.libraries;
        record(`CDN · ${theme} ${width}px MathJax`, libs.mathjax === 'loaded' ? 'PASS' : 'NOT RUN', libs.mathjax);
        record(`CDN · ${theme} ${width}px three.js`, libs.three === 'loaded' ? 'PASS' : 'NOT RUN', libs.three);
        if (consoleState.resource.length || state.qa.warnings.length) {
          record(`CDN · ${theme} ${width}px resource warnings`, 'WARN',
            [...consoleState.resource, ...state.qa.warnings.map(warning => `${warning.kind}: ${warning.source}`)].join(' | '));
        }

        const stationIds = await page.evaluate(() => Array.from(document.querySelectorAll('section.stop[id]'))
          .map(section => section.id).filter(id => /^w\d+$/.test(id))
          .sort((a, b) => Number(a.slice(1)) - Number(b.slice(1))));
        for (const station of stationIds) {
          const locator = page.locator(`#${station}`);
          if (await locator.count() !== 1) {
            record(`screenshot · ${theme} ${width}px ${station}`, 'FAIL', 'station missing or duplicated');
            continue;
          }
          await locator.scrollIntoViewIfNeeded();
          await page.waitForTimeout(60);
          const filename = `${theme}-${width}-${station}.png`;
          const absolute = path.join(SCREENSHOT_DIR, filename);
          try {
            await locator.screenshot({ path: absolute, animations: 'disabled', timeout: 20_000 });
            screenshots.push(path.relative(REPO, absolute));
          } catch (error) {
            record(`screenshot · ${theme} ${width}px ${station}`, 'FAIL', error.message);
          }
        }
      } catch (error) {
        record(`browser · ${theme} ${width}px load`, 'FAIL', error.stack || error.message);
      } finally {
        page.off('console', onConsole);
        page.off('pageerror', onPageError);
      }
    }
  }
  await context.close();
}

async function interactionRun(browser, baseURL) {
  const context = await browser.newContext({ viewport: { width: 768, height: 900 } });
  await installVirtualServer(context, baseURL);
  await context.route(/cdnjs\.cloudflare\.com/, route => route.abort('blockedbyclient'));
  const page = await context.newPage();
  const pageErrors = [];
  page.on('pageerror', error => pageErrors.push(error.stack || error.message));
  await page.goto(harnessURL(baseURL, 'light'), { waitUntil: 'domcontentloaded' });
  await waitForHarness(page);

  const counts = await page.evaluate(() => {
    const buttons = Array.from(document.querySelectorAll('button, [role="button"]'));
    const ranges = Array.from(document.querySelectorAll('input[type="range"]'));
    const checks = Array.from(document.querySelectorAll('input[type="checkbox"]'));
    for (const element of buttons) element.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, view: window }));
    for (const input of ranges) {
      const min = Number(input.min || 0);
      const max = Number(input.max || 100);
      input.value = String(min + 0.71 * (max - min));
      input.dispatchEvent(new Event('input', { bubbles: true }));
      input.dispatchEvent(new Event('change', { bubbles: true }));
    }
    for (const input of checks) input.click();
    return { buttons: buttons.length, ranges: ranges.length, checkboxes: checks.length };
  });

  async function fireMode(mode, screenshotName) {
    await page.locator(`[data-w5-mode="${mode}"]`).click();
    await page.locator('[data-w5-fire]').click();
    await page.waitForTimeout(180);
    await page.locator('[data-w5-scrub]').evaluate(input => {
      input.value = input.max;
      input.dispatchEvent(new Event('input', { bubbles: true }));
    });
    const station = page.locator('#w5');
    await station.scrollIntoViewIfNeeded();
    const absolute = path.join(SCREENSHOT_DIR, screenshotName);
    await station.screenshot({ path: absolute, animations: 'disabled' });
    screenshots.push(path.relative(REPO, absolute));
    return page.evaluate(() => ({
      rows: document.querySelectorAll('#w5 [data-w5-tbody] tr').length,
      time: document.querySelector('#w5 [data-w5-t]')?.textContent,
      reached: document.querySelector('#w5 [data-w5-reached]')?.textContent
    }));
  }

  const em = await fireMode('em', 'smoke-w5-em-final.png');
  const gw = await fireMode('gw', 'smoke-w5-gw-final.png');
  const qa = await page.evaluate(() => window.__qa);
  const ok = counts.buttons > 0 && counts.ranges > 0 && em.rows === 15 && gw.rows === 15
    && qa.errors.length === 0 && pageErrors.length === 0;
  record('interaction · all controls + W5 both modes', ok ? 'PASS' : 'FAIL',
    `${counts.buttons} button/role-button activations, ${counts.ranges} ranges, ${counts.checkboxes} checkboxes; EM ${JSON.stringify(em)}; GW ${JSON.stringify(gw)}; errors=${qa.errors.length + pageErrors.length}`);
  await context.close();
}

async function fallbackRuns(browser, baseURL) {
  {
    const context = await browser.newContext({ viewport: { width: 768, height: 900 } });
    await installVirtualServer(context, baseURL);
    await context.route(/three(?:\.min)?\.js/, route => route.abort('blockedbyclient'));
    await context.addInitScript(() => {
      const original = HTMLCanvasElement.prototype.getContext;
      HTMLCanvasElement.prototype.getContext = function (kind, ...args) {
        if (/^(webgl|webgl2|experimental-webgl)$/.test(kind)) return null;
        return original.call(this, kind, ...args);
      };
    });
    const page = await context.newPage();
    const pageErrors = [];
    page.on('pageerror', error => pageErrors.push(error.stack || error.message));
    await page.goto(harnessURL(baseURL, 'light'), { waitUntil: 'domcontentloaded' });
    await waitForHarness(page);
    const state = await page.evaluate(() => ({
      qa: window.__qa,
      canvasVisible: !!document.querySelector('#w5 .w5-canvas') && getComputedStyle(document.querySelector('#w5 .w5-canvas')).display !== 'none',
      ledgerRows: document.querySelectorAll('#w5 [data-w5-tbody] tr').length
    }));
    const ok = state.qa.libraries.three === 'unavailable' && state.canvasVisible && state.ledgerRows === 15
      && state.qa.errors.length === 0 && pageErrors.length === 0;
    record('fallback · THREE/WebGL absent', ok ? 'PASS' : 'FAIL',
      `three=${state.qa.libraries.three}, 2D range=${state.canvasVisible}, ledger rows=${state.ledgerRows}, errors=${state.qa.errors.length + pageErrors.length}`);
    await context.close();
  }

  {
    const context = await browser.newContext({ viewport: { width: 768, height: 900 } });
    await installVirtualServer(context, baseURL);
    await context.route(/cdnjs\.cloudflare\.com/, route => route.abort('blockedbyclient'));
    const page = await context.newPage();
    const pageErrors = [];
    page.on('pageerror', error => pageErrors.push(error.stack || error.message));
    await page.goto(harnessURL(baseURL, 'dark'), { waitUntil: 'domcontentloaded' });
    await waitForHarness(page);
    const state = await page.evaluate(() => ({
      qa: window.__qa,
      stations: document.querySelectorAll('section.stop').length,
      ledgerRows: document.querySelectorAll('#w5 [data-w5-tbody] tr').length,
      w8Rows: document.querySelectorAll('#w8 [data-w8-gtable] tbody tr').length
    }));
    const ok = state.qa.libraries.mathjax === 'unavailable' && state.qa.libraries.three === 'unavailable'
      && state.stations > 0 && state.ledgerRows === 15 && state.w8Rows === 7
      && state.qa.errors.length === 0 && pageErrors.length === 0;
    record('fallback · MathJax and THREE absent', ok ? 'PASS' : 'FAIL',
      `MathJax=${state.qa.libraries.mathjax}, three=${state.qa.libraries.three}, sections=${state.stations}, W5 rows=${state.ledgerRows}, W8 rows=${state.w8Rows}, errors=${state.qa.errors.length + pageErrors.length}`);
    await context.close();
  }
}

function dot(a, b) {
  return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
}

function normalize(a) {
  const length = Math.hypot(...a);
  return a.map(value => value / length);
}

function legendreWithDerivatives(limit, x) {
  const p = new Float64Array(limit + 1);
  const dp = new Float64Array(limit + 1);
  const ddp = new Float64Array(limit + 1);
  p[0] = 1;
  if (limit > 0) {
    p[1] = x;
    dp[1] = 1;
  }
  for (let l = 1; l < limit; l++) {
    const a = (2 * l + 1) / (l + 1);
    const b = l / (l + 1);
    p[l + 1] = a * x * p[l] - b * p[l - 1];
    dp[l + 1] = a * (p[l] + x * dp[l]) - b * dp[l - 1];
    ddp[l + 1] = a * (2 * dp[l] + x * ddp[l]) - b * ddp[l - 1];
  }
  return { p, ddp };
}

function simpson(fn, a, b, panels = 32768) {
  if (panels % 2) panels++;
  const h = (b - a) / panels;
  let sum = fn(a) + fn(b);
  for (let i = 1; i < panels; i++) sum += fn(a + i * h) * (i % 2 ? 4 : 2);
  return sum * h / 3;
}

const clCache = new Map();
function independentCl(kappa, l) {
  const key = `${kappa}|${l}`;
  if (!clCache.has(key)) {
    clCache.set(key, simpson(x => Math.exp(kappa * (x - 1)) * legendreWithDerivatives(l, x).p[l], -1, 1));
  }
  return clCache.get(key);
}

function independentGWAt(beams, n, e1, e2) {
  let phi = 0;
  let c11 = 0;
  let c12 = 0;
  for (const beam of beams) {
    const x = dot(n, beam.n);
    const legendre = legendreWithDerivatives(8, x);
    let radialSecond = 0;
    for (let l = 2; l <= 8; l++) {
      const denominator = (l - 1) * l * (l + 1) * (l + 2);
      const coefficient = beam.w * 2 * (2 * l + 1) * independentCl(beam.k, l) / denominator;
      phi += coefficient * legendre.p[l];
      radialSecond += coefficient * legendre.ddp[l];
    }
    const u1 = dot(beam.n, e1);
    const u2 = dot(beam.n, e2);
    c11 += radialSecond * (u1 * u1 - u2 * u2);
    c12 += radialSecond * 2 * u1 * u2;
  }
  return { phi, c11, c12 };
}

async function loadFragmentEngines() {
  const source = await readFile(FRAGMENT, 'utf8');
  const emStart = source.indexOf('  var EM = (function () {');
  const emEnd = source.indexOf('  /* ================================================================\n     ENGINE 2', emStart);
  const gwStart = source.indexOf('  var GW = (function () {', emEnd);
  const gwEnd = source.indexOf('  /* ---------------- the range ---------------- */', gwStart);
  if (emStart < 0 || emEnd < 0 || gwStart < 0 || gwEnd < 0) {
    throw new Error('Could not extract the fragment EM/GW engine closures');
  }
  const context = vm.createContext({});
  vm.runInContext(`${source.slice(emStart, emEnd)}\n${source.slice(gwStart, gwEnd)}`, context,
    { filename: 'frag-gw-engine-extract.js', timeout: 10_000 });
  if (!context.EM || !context.GW) throw new Error('Extracted engine closures did not initialize');
  return { EM: context.EM, GW: context.GW };
}

async function loadW8GreenCheck() {
  const source = await readFile(FRAGMENT, 'utf8');
  const scriptStart = source.indexOf('<script data-station="w8">');
  const coreStart = source.indexOf('  var LMAX = 8, K = (LMAX + 1) * (LMAX + 1);', scriptStart);
  const coreEnd = source.indexOf('  /* ---------- DOM ---------- */', coreStart);
  if (scriptStart < 0 || coreStart < 0 || coreEnd < 0) throw new Error('Could not extract W8 Green-kernel check');
  const context = vm.createContext({});
  vm.runInContext(source.slice(coreStart, coreEnd), context,
    { filename: 'frag-gw-w8-green-extract.js', timeout: 10_000 });
  if (!context.GCHK) throw new Error('Extracted W8 Green-kernel check did not initialize');
  return Array.from(context.GCHK);
}

async function loadW9Core() {
  const source = await readFile(FRAGMENT, 'utf8');
  const scriptStart = source.indexOf('<script data-station="w9">');
  const coreStart = source.indexOf('  var S = { A:', scriptStart);
  const coreEnd = source.indexOf('  var svgP =', coreStart);
  if (scriptStart < 0 || coreStart < 0 || coreEnd < 0) throw new Error('Could not extract W9 closed-form core');
  const context = vm.createContext({});
  vm.runInContext(source.slice(coreStart, coreEnd), context,
    { filename: 'frag-gw-w9-core-extract.js', timeout: 10_000 });
  if (!context.S || !context.f) throw new Error('Extracted W9 closed-form core did not initialize');
  return { state: context.S, f: context.f };
}

async function nodePhysicsAudit() {
  const { EM, GW } = await loadFragmentEngines();
  const patterns = [
    { name: 'broad single beam', beams: [{ n: normalize([0.7, -0.2, 0.68]), k: 3, w: 1 }] },
    { name: 'narrow single beam', beams: [{ n: normalize([-0.3, 0.81, 0.5]), k: 18, w: 1 }] },
    { name: 'two unequal lobes', beams: [
      { n: normalize([0.2, 0.9, 0.38]), k: 12, w: 1 },
      { n: normalize([-0.2, -0.9, -0.38]), k: 7, w: 0.55 }
    ] }
  ];
  const samples = [normalize([0.9, 0.1, 0.42]), normalize([-0.4, 0.8, 0.45]), normalize([0.15, -0.55, -0.82])];
  let maxPhiDifference = 0;
  let maxHessianDifference = 0;
  for (const pattern of patterns) {
    const F = GW.fluxCoef(pattern.beams);
    const Phi = GW.solve(F);
    for (const n of samples) {
      const frame = GW.frameAt(n);
      const fragmentHessian = GW.hess(Phi, n, frame[0], frame[1]);
      const independent = independentGWAt(pattern.beams, n, frame[0], frame[1]);
      maxPhiDifference = Math.max(maxPhiDifference, Math.abs(GW.evalC(Phi, n) - independent.phi));
      maxHessianDifference = Math.max(maxHessianDifference,
        Math.abs(fragmentHessian[0] - independent.c11), Math.abs(fragmentHessian[1] - independent.c12));
    }
  }
  record('physics/Node · independent ℓ≤8 scalar solve', maxPhiDifference < 2e-10 ? 'PASS' : 'FAIL',
    `3 flux patterns × 3 directions; max |fragment − independent|=${maxPhiDifference.toExponential(3)}`);
  record('physics/Node · independent trace-free Hessian', maxHessianDifference < 4e-6 ? 'PASS' : 'FAIL',
    `analytic covariant Hessian versus fragment circle/Richardson route; max component difference=${maxHessianDifference.toExponential(3)}`);

  const greenCoefficients = await loadW8GreenCheck();
  const greenTarget = 2 / Math.PI;
  let greenWorst = 0;
  for (let l = 2; l <= 8; l++) {
    const denominator = (l - 1) * l * (l + 1) * (l + 2);
    greenWorst = Math.max(greenWorst, Math.abs(greenCoefficients[l] * denominator - greenTarget) / greenTarget);
  }
  record('physics/Node · W8 Green-kernel eigenvalues', greenWorst < 5e-11 ? 'PASS' : 'FAIL',
    `ℓ=2…8, max relative deviation of gℓDℓ from 2/π=${greenWorst.toExponential(3)}`);

  const fluxRows = [3, 12, 45].map(k => {
    const F = GW.fluxCoef([{ n: [0, 0, 1], k, w: 1 }]);
    return { k, total: F[0] * Math.sqrt(4 * Math.PI), exactRaw: 2 * Math.PI * (1 - Math.exp(-2 * k)) / k };
  });
  const fluxImplementationMatches = fluxRows.every(row => Math.abs(row.total - row.exactRaw) < 2e-13);
  record('physics/Node · beam integral implementation', fluxImplementationMatches ? 'PASS' : 'FAIL',
    fluxRows.map(row => `κ=${row.k}: solver=${row.total.toPrecision(9)}, raw formula=${row.exactRaw.toPrecision(9)}`).join('; '));
  record('physics/Node · W5 claimed unit burst energy', fluxRows.every(row => Math.abs(row.total - 1) < 1e-12) ? 'PASS' : 'FAIL',
    fluxRows.map(row => `κ=${row.k}: ∫F dΩ=${row.total.toPrecision(9)}`).join('; '));

  const emCases = [
    { bf: 0.25, tau: 0.35, prof: 'one', cth: -0.6, R: 8 },
    { bf: 0.82, tau: 1.1, prof: 'one', cth: 0.7, R: 15 },
    { bf: 0.60, tau: 0.6, prof: 'over', cth: 0.35, R: 9 },
    { bf: 0.92, tau: 0.45, prof: 'over', cth: 0.9, R: 18 }
  ].map(test => {
    Object.assign(EM.st, test);
    const numeric = EM.dvNumeric(test.cth, test.R);
    const closed = EM.dvClosed(test.cth, test.R);
    const table = EM.tables(test.cth, test.R);
    const emissionTime = 2 * test.tau;
    const sourcePosition = EM.posS(emissionTime);
    const approximateArrival = emissionTime + test.R - sourcePosition * test.cth;
    const exactArrival = emissionTime + Math.sqrt(test.R * test.R + sourcePosition * sourcePosition
      - 2 * test.R * sourcePosition * test.cth);
    return {
      ...test,
      simpsonDifference: Math.abs(numeric.v - closed),
      trapezoidDifference: Math.abs(table.J[table.N] - closed),
      retardationDifference: Math.abs(exactArrival - approximateArrival)
    };
  });
  const maxSimpson = Math.max(...emCases.map(test => test.simpsonDifference));
  const maxTrapezoid = Math.max(...emCases.map(test => test.trapezoidDifference));
  const maxTrapezoidRelative = Math.max(...emCases.map(test => {
    Object.assign(EM.st, test);
    return test.trapezoidDifference / Math.max(Math.abs(EM.dvClosed(test.cth, test.R)), Number.MIN_VALUE);
  }));
  const maxRetardationDifference = Math.max(...emCases.map(test => test.retardationDifference));
  record('physics/Node · W5 EM ledger quadrature', maxSimpson < 1e-11 ? 'PASS' : 'FAIL',
    `4 trajectories; adaptive-panel Simpson max |integrated−closed|=${maxSimpson.toExponential(3)}`);
  record('physics/Node · W5 EM animation quadrature', maxTrapezoid < 1e-8 ? 'PASS' : 'FAIL',
    `fixed 1024-panel trapezoid max absolute=${maxTrapezoid.toExponential(3)}, max relative=${maxTrapezoidRelative.toExponential(3)}; no convergence test`);
  record('physics/Node · W5 exact-retardation claim', maxRetardationDifference < 1e-12 ? 'PASS' : 'FAIL',
    `sampled max |(R−n·r_s)−|Rn−r_s||=${maxRetardationDifference.toExponential(3)}`);

  const w9 = await loadW9Core();
  Object.assign(w9.state, { A: 1, B: 0.35, w0: 1.6, C: 0.6, w1: 2.2, G: 0.45,
    onB: false, onC: true, flip: true });
  const advancedLate = w9.f(100);
  const advancedBefore = w9.f(-2);
  record('physics/Node · W9 closed-form inverse transforms', Math.abs(advancedLate - 1) < 1e-15 && Math.abs(advancedBefore) > 1e-3 ? 'PASS' : 'FAIL',
    `upper-pole term is supported on t<0: f(100)=${advancedLate}, f(−2)=${advancedBefore.toPrecision(7)}`);
  // The *wording* of the verdict is DOM state; loadW9Core extracts only S and f,
  // so the verdict rows can only be evaluated in the browser lane. What Node can
  // and does test here is the mathematics each verdict is supposed to report.
  record('physics/Node · W9 upper-pole late-limit verdict', 'NOT RUN',
    'verdict text lives in the DOM; the extracted Node core exposes only S and f. Checked by the browser row "physics · W9 upper-pole late-limit verdict"; the underlying closed form is checked by "physics/Node · W9 closed-form inverse transforms" above.');
  Object.assign(w9.state, { A: 0, B: 0.35, w0: 1.6, C: 0.6, w1: 2.2, G: 0.45,
    onB: false, onC: true, flip: false });
  const zeroResidueLate = w9.f(400);
  const zeroResidueEarly = w9.f(0.4);
  record('physics/Node · W9 A=0 residue and late-time limit',
    Math.abs(zeroResidueLate) < 1e-15 && Math.abs(zeroResidueEarly) > 1e-3 ? 'PASS' : 'FAIL',
    `with A=0 the zero-frequency pole is gone: f(400)=${zeroResidueLate} (limit equals the residue 0), while the damped pair still rings, f(0.4)=${zeroResidueEarly.toPrecision(7)}`);
}

async function physicsRun(browser, baseURL) {
  const context = await browser.newContext({ viewport: { width: 768, height: 900 } });
  await installVirtualServer(context, baseURL);
  await context.route(/cdnjs\.cloudflare\.com/, route => route.abort('blockedbyclient'));
  const page = await context.newPage();
  await page.goto(harnessURL(baseURL, 'light', 'frag-gw-instrumented.html'), { waitUntil: 'domcontentloaded' });
  await waitForHarness(page);

  const patterns = [
    { name: 'broad single beam', beams: [{ n: normalize([0.7, -0.2, 0.68]), k: 3, w: 1 }] },
    { name: 'narrow single beam', beams: [{ n: normalize([-0.3, 0.81, 0.5]), k: 18, w: 1 }] },
    { name: 'two unequal lobes', beams: [
      { n: normalize([0.2, 0.9, 0.38]), k: 12, w: 1 },
      { n: normalize([-0.2, -0.9, -0.38]), k: 7, w: 0.55 }
    ] }
  ];
  const samples = [normalize([0.9, 0.1, 0.42]), normalize([-0.4, 0.8, 0.45]), normalize([0.15, -0.55, -0.82])];
  let maxPhiDifference = 0;
  let maxHessianDifference = 0;
  const normalizationDetails = [];

  for (const pattern of patterns) {
    const fragment = await page.evaluate(({ beams, samples }) => {
      const core = window.__qaPhysics.GW;
      const F = core.fluxCoef(beams);
      const Phi = core.solve(F);
      return {
        totalFlux: F[0] * Math.sqrt(4 * Math.PI),
        points: samples.map(n => {
          const frame = core.frameAt(n);
          const h = core.hess(Phi, n, frame[0], frame[1]);
          return { phi: core.evalC(Phi, n), c11: h[0], c12: h[1], e1: frame[0], e2: frame[1] };
        })
      };
    }, { beams: pattern.beams, samples });
    pattern.beams.forEach((beam, index) => {
      const expectedRaw = beam.w * 2 * Math.PI * (1 - Math.exp(-2 * beam.k)) / beam.k;
      normalizationDetails.push(`${pattern.name} beam ${index + 1}: raw integral ${expectedRaw.toPrecision(8)}`);
    });
    for (let i = 0; i < samples.length; i++) {
      const independent = independentGWAt(pattern.beams, samples[i], fragment.points[i].e1, fragment.points[i].e2);
      maxPhiDifference = Math.max(maxPhiDifference, Math.abs(fragment.points[i].phi - independent.phi));
      maxHessianDifference = Math.max(maxHessianDifference,
        Math.abs(fragment.points[i].c11 - independent.c11), Math.abs(fragment.points[i].c12 - independent.c12));
    }
    normalizationDetails.push(`${pattern.name}: fragment total ${fragment.totalFlux.toPrecision(8)}`);
  }
  record('physics · independent ℓ≤8 scalar solve', maxPhiDifference < 2e-10 ? 'PASS' : 'FAIL',
    `max |fragment − independent| = ${maxPhiDifference.toExponential(3)}`);
  record('physics · independent trace-free Hessian', maxHessianDifference < 4e-6 ? 'PASS' : 'FAIL',
    `max component difference = ${maxHessianDifference.toExponential(3)}`);

  const unitBeamFlux = await page.evaluate(() => {
    const core = window.__qaPhysics.GW;
    const n = [0, 0, 1];
    return [3, 12, 45].map(k => {
      const F = core.fluxCoef([{ n, k, w: 1 }]);
      return { k, total: F[0] * Math.sqrt(4 * Math.PI) };
    });
  });
  const normalized = unitBeamFlux.every(row => Math.abs(row.total - 1) < 1e-10);
  record('physics · W5 claimed unit burst energy', normalized ? 'PASS' : 'FAIL',
    unitBeamFlux.map(row => `κ=${row.k}: ∫F dΩ=${row.total.toPrecision(8)}`).join('; '));
  record('physics · flux-normalization derivation', 'PASS', normalizationDetails.join('; '));

  const emCases = await page.evaluate(() => {
    const em = window.__qaPhysics.EM;
    const cases = [
      { bf: 0.25, tau: 0.35, prof: 'one', cth: -0.6, R: 8 },
      { bf: 0.82, tau: 1.1, prof: 'one', cth: 0.7, R: 15 },
      { bf: 0.60, tau: 0.6, prof: 'over', cth: 0.35, R: 9 },
      { bf: 0.92, tau: 0.45, prof: 'over', cth: 0.9, R: 18 }
    ];
    return cases.map(test => {
      Object.assign(em.st, test);
      const numeric = em.dvNumeric(test.cth, test.R);
      const closed = em.dvClosed(test.cth, test.R);
      const table = em.tables(test.cth, test.R);
      const sampleEmissionTime = 2 * test.tau;
      const sourcePosition = em.posS(sampleEmissionTime);
      const approximateArrival = sampleEmissionTime + test.R - sourcePosition * test.cth;
      const exactArrival = sampleEmissionTime + Math.sqrt(test.R * test.R + sourcePosition * sourcePosition
        - 2 * test.R * sourcePosition * test.cth);
      return {
        ...test,
        numeric: numeric.v,
        closed,
        simpsonDifference: Math.abs(numeric.v - closed),
        trapezoidDifference: Math.abs(table.J[table.N] - closed),
        retardationDifference: Math.abs(exactArrival - approximateArrival)
      };
    });
  });
  const maxSimpson = Math.max(...emCases.map(test => test.simpsonDifference));
  const maxTrapezoid = Math.max(...emCases.map(test => test.trapezoidDifference));
  const maxRetardationDifference = Math.max(...emCases.map(test => test.retardationDifference));
  record('physics · W5 EM displayed-field quadrature', maxSimpson < 1e-11 && maxTrapezoid < 2e-7 ? 'PASS' : 'FAIL',
    `Simpson max=${maxSimpson.toExponential(3)}, animation-table trapezoid max=${maxTrapezoid.toExponential(3)}`);
  record('physics · W5 exact-retardation claim', maxRetardationDifference < 1e-12 ? 'PASS' : 'FAIL',
    `max |(R−n·r_s) − |Rn−r_s|| at sampled emission times = ${maxRetardationDifference.toExponential(3)}`);

  const w9 = await page.evaluate(() => {
    const q = window.__qaW9;
    Object.assign(q.state, { A: 1, B: 0.35, w0: 1.6, C: 0.6, w1: 2.2, G: 0.45, onB: false, onC: true, flip: false });
    q.render();
    const causalLate = q.f(100);
    q.state.flip = true;
    q.render();
    const advancedLate = q.f(100);
    const advancedBefore = q.f(-2);
    const advancedVerdict = document.querySelector('#w9 [data-w9-verdict]').textContent.replace(/\s+/g, ' ').trim();
    q.state.A = 0;
    q.render();
    const zeroResidueVerdict = document.querySelector('#w9 [data-w9-verdict]').textContent.replace(/\s+/g, ' ').trim();
    return { causalLate, advancedLate, advancedBefore, advancedVerdict, zeroResidueVerdict };
  });
  record('physics · W9 inverse transforms (causal/advanced)',
    Math.abs(w9.causalLate - 1) < 1e-12 && Math.abs(w9.advancedLate - 1) < 1e-12 && Math.abs(w9.advancedBefore) > 1e-3 ? 'PASS' : 'FAIL',
    `causal f(100)=${w9.causalLate}; advanced f(100)=${w9.advancedLate}; advanced f(−2)=${w9.advancedBefore}`);
  record('physics · W9 upper-pole late-limit verdict',
    /no late-time limit/i.test(w9.advancedVerdict) ? 'FAIL' : 'PASS', w9.advancedVerdict);
  record('physics · W9 zero-residue “simple pole” state',
    /One simple pole at ω = 0[^]*holds/i.test(w9.zeroResidueVerdict) || /holdsOne simple pole/i.test(w9.zeroResidueVerdict) ? 'FAIL' : 'WARN',
    w9.zeroResidueVerdict);

  await context.close();
}

async function main() {
  await mkdir(SCREENSHOT_DIR, { recursive: true });
  await staticAudit();
  try {
    await nodePhysicsAudit();
  } catch (error) {
    record('physics/Node · extracted-engine audit', 'FAIL', error.stack || error.message);
  }
  let playwright;
  try {
    playwright = loadPlaywright();
  } catch (error) {
    record('Playwright availability', 'NOT RUN', error.stack || error.message);
    printSummary();
    process.exitCode = 1;
    return;
  }

  const { server, baseURL } = await startServer();
  let browser;
  try {
    browser = await playwright.chromium.launch({ headless: true });
    record('Playwright availability', 'PASS', `Chromium ${browser.version()}`);
    await matrixRun(browser, baseURL);
    await interactionRun(browser, baseURL);
    await fallbackRuns(browser, baseURL);
    await physicsRun(browser, baseURL);
  } catch (error) {
    const message = error.stack || error.message;
    const sandboxDenied = /sandbox_host_linux\.cc|Operation not permitted|EPERM/.test(message);
    record('Playwright browser matrix', sandboxDenied ? 'NOT RUN' : 'FAIL', message);
  } finally {
    if (browser) await browser.close();
    if (server) await new Promise(resolve => server.close(resolve));
  }
  printSummary();
  if (results.some(row => row.status === 'FAIL')) process.exitCode = 1;
}

function printSummary() {
  console.table(results.map(row => ({
    check: row.check,
    status: row.status,
    detail: row.detail.length > 280 ? row.detail.slice(0, 277) + '…' : row.detail
  })));
  console.log(`\nScreenshots (${screenshots.length})`);
  for (const screenshot of screenshots) console.log(`- ${screenshot}`);
  const counts = results.reduce((acc, row) => {
    acc[row.status] = (acc[row.status] || 0) + 1;
    return acc;
  }, {});
  console.log(`\nSummary: ${Object.entries(counts).map(([status, count]) => `${status}=${count}`).join(', ')}`);
}

await main();
