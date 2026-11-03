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
