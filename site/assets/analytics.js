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
    try { trackEngagement(); } catch (_) { /* engagement events are optional */ }
  }
  function articleSlug() {
    const match = location.pathname.match(/\/writing\/([^/]+?)(?:-en|-ja)?\.html$/);
    return match ? match[1] : '';
  }
  // Engagement events after consent: a "read" is 30 s of visible time plus 75% scroll depth (fired once per page view);
  // link clicks are labelled by page section. Only pathnames are sent, never query strings or fragments.
  function trackEngagement() {
    if (typeof document.addEventListener !== 'function' || typeof window.addEventListener !== 'function') return;
    const slug = articleSlug();
    const language = (document.documentElement && document.documentElement.lang) || '';
    const send = (name, params) => window.gtag('event', name, Object.assign({article_slug: slug, content_language: language}, params));
    if (slug) {
      let visibleSeconds = 0, deepest = 0, sent = false;
      const check = () => {
        if (sent || visibleSeconds < 30 || deepest < 0.75) return;
        sent = true;
        send('article_read', {read_seconds: visibleSeconds});
      };
      window.addEventListener('scroll', () => {
        const root = document.documentElement;
        const total = root.scrollHeight - root.clientHeight;
        if (total > 0) deepest = Math.max(deepest, (window.scrollY || root.scrollTop || 0) / total);
        check();
      }, {passive: true});
      const timer = setInterval(() => {
        if (document.visibilityState === 'visible') visibleSeconds += 1;
        check();
        if (sent) clearInterval(timer);
      }, 1000);
    }
    document.addEventListener('click', event => {
      const link = event.target && event.target.closest ? event.target.closest('a[href]') : null;
      if (!link) return;
      let name = '';
      if (link.closest('.related')) name = 'related_click';
      else if (link.closest('.terms')) name = 'glossary_click';
      else if (link.closest('.languages')) name = 'language_switch';
      else if (link.closest('.cite')) name = 'cite_click';
      if (!name) return;
      let target = '';
      try { target = new URL(link.href, location.href).pathname; } catch (_) { /* ignore malformed links */ }
      send(name, {link_path: target});
    }, true);
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
