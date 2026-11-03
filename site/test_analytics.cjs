const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const code = fs.readFileSync(__dirname + '/assets/analytics.js', 'utf8');
function page(saved = null, hostname = 'daikikumakura.github.io', blockedStorage = false) {
  const tags = [], cookies = [], elements = {};
  const state = {value: saved, reloads: 0};
  for (const name of ['analytics-notice', 'analytics-allow', 'analytics-decline', 'analytics-settings']) {
    elements[name] = {hidden: true, addEventListener: (_, fn) => elements[name].click = fn, scrollIntoView() {}, focus() {}};
  }
  const document = {currentScript: {dataset: {measurementId: 'G-JCF6NTYHW3'}},
    getElementById: id => elements[id], createElement: () => ({}),
    head: {appendChild: tag => tags.push(tag)}, referrer: 'https://www.google.com/search?q=private-query'};
  Object.defineProperty(document, 'cookie', {set: value => cookies.push(value)});
  const context = {document, window: {}, URL, Date,
    location: {hostname, protocol: 'https:', origin: 'https://' + hostname, pathname: '/writing/example.html', reload: () => state.reloads++},
    localStorage: {getItem() {if (blockedStorage) throw Error(); return state.value;}, setItem(_, value) {if (blockedStorage) throw Error(); state.value = value;}}};
  vm.runInNewContext(code, context);
  return {context, elements, tags, cookies, state};
}
const fresh = page();
assert.equal(fresh.tags.length, 0);
assert.equal(fresh.elements['analytics-notice'].hidden, false);
fresh.elements['analytics-decline'].click();
assert.equal(fresh.state.value, 'denied');
assert.equal(fresh.tags.length, 0);
assert.equal(fresh.state.reloads, 0);
assert.equal(page('denied').tags.length, 0);
const accepted = page('granted');
assert.equal(accepted.tags.length, 1);
assert.match(accepted.tags[0].src, /G-JCF6NTYHW3$/);
const configs = accepted.context.window.dataLayer.filter(item => item[0] === 'config');
assert.equal(configs.length, 1);
assert.equal(configs[0][2].allow_google_signals, false);
assert.equal(configs[0][2].allow_ad_personalization_signals, false);
assert.equal(configs[0][2].page_location, 'https://daikikumakura.github.io/writing/example.html');
assert.equal(configs[0][2].page_referrer, 'https://www.google.com/search');
accepted.elements['analytics-allow'].click();
assert.equal(accepted.tags.length, 1);
accepted.elements['analytics-decline'].click();
assert.equal(accepted.context.window['ga-disable-G-JCF6NTYHW3'], true);
assert.equal(accepted.state.value, 'denied');
assert.equal(accepted.state.reloads, 1);
assert.equal(accepted.cookies.length, 6);
assert.equal(page('granted', 'localhost').tags.length, 0);
const storageBlocked = page(null, 'daikikumakura.github.io', true);
assert.equal(storageBlocked.tags.length, 0);
storageBlocked.elements['analytics-allow'].click();
assert.equal(storageBlocked.tags.length, 1);
console.log('Analytics consent, denial, revocation, storage failure, sanitized page data and no duplicate loading: PASS');

function engagementPage() {
  const listeners = {doc: {}, win: {}}, elements = {}, intervals = [];
  for (const name of ['analytics-notice', 'analytics-allow', 'analytics-decline', 'analytics-settings']) {
    elements[name] = {hidden: true, addEventListener() {}, scrollIntoView() {}, focus() {}};
  }
  const root = {scrollHeight: 2000, clientHeight: 1000, scrollTop: 0, lang: 'en'};
  const document = {currentScript: {dataset: {measurementId: 'G-JCF6NTYHW3'}}, getElementById: id => elements[id], createElement: () => ({}),
    head: {appendChild() {}}, referrer: '', documentElement: root, visibilityState: 'visible', addEventListener: (type, fn) => listeners.doc[type] = fn};
  Object.defineProperty(document, 'cookie', {set() {}});
  const window = {scrollY: 0, addEventListener: (type, fn) => listeners.win[type] = fn};
  const context = {document, window, URL, Date, setInterval: fn => { intervals.push(fn); return intervals.length; }, clearInterval() {},
    location: {hostname: 'daikikumakura.github.io', protocol: 'https:', origin: 'https://daikikumakura.github.io', pathname: '/writing/example-en.html', href: 'https://daikikumakura.github.io/writing/example-en.html', reload() {}},
    localStorage: {getItem: () => 'granted', setItem() {}}};
  vm.runInNewContext(code, context);
  const events = () => window.dataLayer.filter(item => item[0] === 'event').map(item => [item[1], item[2]]);
  return {listeners, intervals, window, events};
}
const engaged = engagementPage();
assert.equal(engaged.events().length, 0);
engaged.window.scrollY = 800;
engaged.listeners.win.scroll();
for (let i = 0; i < 29; i++) engaged.intervals[0]();
assert.equal(engaged.events().length, 0);
engaged.intervals[0]();
engaged.intervals[0]();
const reads = engaged.events().filter(([name]) => name === 'article_read');
assert.equal(reads.length, 1);
assert.equal(reads[0][1].article_slug, 'example');
assert.equal(reads[0][1].content_language, 'en');
const link = {href: '/writing/other.html?secret=1#frag', closest: selector => selector === '.related' ? {} : null};
engaged.listeners.doc.click({target: {closest: () => link}});
const clicks = engaged.events().filter(([name]) => name === 'related_click');
assert.equal(clicks.length, 1);
assert.equal(clicks[0][1].link_path, '/writing/other.html');
console.log('Reading and navigation events after consent, once per page view, pathnames only: PASS');
