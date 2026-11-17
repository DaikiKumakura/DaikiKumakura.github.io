// Keep tables semantic and expose horizontal scrolling in the keyboard order.
(() => {
  const japanese = document.documentElement.lang === 'ja';
  const update = (region) => {
    if (region.scrollWidth > region.clientWidth + 1) {
      region.tabIndex = 0;
    } else {
      region.removeAttribute('tabindex');
    }
  };
  const observer = new ResizeObserver((entries) => {
    for (const entry of entries) {
      if (!entry.target.isConnected) {
        observer.unobserve(entry.target);
        continue;
      }
      update(entry.target.closest('.table-scroll') || entry.target);
    }
  });
  const processed = new WeakSet();
  const prepare = (element) => {
    if (processed.has(element)) return;
    processed.add(element);
    let region = element;
    if (element.tagName === 'TABLE') {
      region = document.createElement('div');
      region.className = 'table-scroll';
      region.setAttribute('role', 'group');
      region.setAttribute('aria-label', element.caption?.textContent.trim() || (japanese ? '表' : 'Table'));
      element.before(region);
      region.append(element);
    }
    observer.observe(region);
    if (region !== element) observer.observe(element);
    update(region);
  };
  const main = document.getElementById('main');
  main.querySelectorAll('table, pre').forEach(prepare);
  new MutationObserver((records) => {
    for (const record of records) {
      for (const node of record.addedNodes) {
        if (!(node instanceof Element)) continue;
        if (node.matches('table, pre')) prepare(node);
        node.querySelectorAll('table, pre').forEach(prepare);
      }
    }
  }).observe(main, {childList: true, subtree: true});
})();
