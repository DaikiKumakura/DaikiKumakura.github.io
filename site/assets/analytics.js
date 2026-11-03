/* Basic consent mode: the Google library is not loaded before permission. */
(() => {
  'use strict';
  const id = document.currentScript?.dataset.measurementId;
  if (!/^G-[A-Z0-9]+$/.test(id || '') || location.hostname !== 'daikikumakura.github.io' || location.protocol !== 'https:') return;
  const key = 'dk-analytics-consent-v1';
  const notice = document.getElementById('analytics-notice');
  if (!notice) return;
  let loaded = false;
  function remember(value) { try { localStorage.setItem(key, value); } catch (_) { /* Session-only choice if storage is unavailable. */ } }
  function choice() { try { return localStorage.getItem(key); } catch (_) { return null; } }
  function cleanUrl(value) {
    try { const url = new URL(value); return /^https?:$/.test(url.protocol) ? url.origin + url.pathname : ''; } catch (_) { return ''; }
  }
  function enable() {
    if (loaded) return;
    loaded = true;
    window['ga-disable-' + id] = false;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('consent', 'default', {analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied'});
    window.gtag('consent', 'update', {analytics_storage: 'granted'});
    window.gtag('js', new Date());
    window.gtag('config', id, {
      allow_google_signals: false,
      allow_ad_personalization_signals: false,
      cookie_expires: 60 * 60 * 24 * 90,
      page_location: location.origin + location.pathname,
      page_referrer: cleanUrl(document.referrer)
    });
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + id;
    document.head.appendChild(script);
  }
  function removeCookies() {
    for (const name of ['_ga', '_ga_' + id.slice(2).replaceAll('-', '_')]) {
      for (const domain of ['', ';domain=' + location.hostname, ';domain=.' + location.hostname]) {
        document.cookie = name + '=;Max-Age=0;path=/' + domain + ';SameSite=Lax;Secure';
      }
    }
  }
  document.getElementById('analytics-allow').addEventListener('click', () => {
    remember('granted'); notice.hidden = true; enable();
  });
  document.getElementById('analytics-decline').addEventListener('click', () => {
    remember('denied'); notice.hidden = true;
    window['ga-disable-' + id] = true;
    removeCookies();
    if (loaded) location.reload();
  });
  document.getElementById('analytics-settings').addEventListener('click', () => {
    notice.hidden = false; notice.scrollIntoView({block: 'center'});
    document.getElementById('analytics-decline').focus();
  });
  const saved = choice();
  if (saved === 'granted') enable();
  else if (saved !== 'denied') notice.hidden = false;
})();
