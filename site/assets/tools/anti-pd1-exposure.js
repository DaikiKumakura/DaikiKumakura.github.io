/* Explorer for the fixed vs weight-based dosing analysis of anti-PD-1 antibodies.
   It only looks up numbers computed by the article's analysis (see data file); it recalculates no PK. */
(function () {
  'use strict';
  var root = document.getElementById('exposure-tool');
  if (!root) return;
  var lang = root.getAttribute('data-lang') === 'ja' ? 'ja' : 'en';
  var T = {
    en: {
      drug: 'Drug', weight: 'Body weight (kg)', scenario: 'Scenario', maxBelow: 'Allowed share below the lower limit (%)', maxAbove: 'Allowed share above the upper limit (%)',
      regimen: 'Regimen', below: 'Below lower limit', above: 'Above upper limit', first: 'Below lower limit, first interval', cmin: 'Median trough (mg/L)', cavg: 'Median average (mg/L)', cmax: 'Median peak (mg/L)', verdict: 'Stays in range?',
      yes: 'Yes', no: 'No', inBand: function (w, band, n) { return w + ' kg falls in the ' + band + ' kg band (' + n + ' of 20,000 simulated adults per regimen).'; },
      pct: function (p) { return p; }, loading: 'Loading data…', failed: 'The data could not be loaded.',
      limits: function (f, c) { return 'Lower limit: steady-state trough of ' + f + ' mg/L (5th percentile of the reference weight-based regimen). Upper limit: steady-state peak of ' + c + ' mg/L (median at 10 mg/kg every 2 weeks).'; },
      chartTitle: 'Share below the lower limit by weight band', chartAlt: 'Bar chart of the share of simulated patients below the lower limit, by weight band and regimen.',
      extremes: 'Fixed-weight virtual patients (main analysis)', ext40: '40 kg', ext160: '160 kg',
      percentile: function (w, p, name) {
        var q = [['1%', 1], ['5%', 5], ['50%', 50], ['95%', 95], ['99%', 99]], i;
        if (w < p['1%']) return 'Lighter than the 1st percentile of ' + name + '.';
        for (i = 0; i < q.length - 1; i++) if (w < p[q[i + 1][0]]) return 'Between the ' + q[i][1] + 'th and ' + q[i + 1][1] + 'th percentiles of ' + name + '.';
        return 'Heavier than the 99th percentile of ' + name + '.';
      },
      pop: 'NHANES adults', asianPop: 'NHANES non-Hispanic Asian adults',
      scen: { main: 'Main analysis', pembro_footnote: 'Table footnote values (CL 0.202, exponent 0.578)', exponent_low: 'Weight exponent at lower end of 95% CI', exponent_high: 'Weight exponent at upper end of 95% CI', asian_weights: 'Asian weight distribution', ignore_sex: 'Sex ignored', pembro_low_albumin: 'Low albumin (30 g/L)', nivo_constant_cl: 'Time-varying clearance ignored' },
      drugs: { pembrolizumab: 'Pembrolizumab', nivolumab: 'Nivolumab' }
    },
    ja: {
      drug: '薬剤', weight: '体重（kg）', scenario: '条件', maxBelow: '下限を下回ってよい割合（%）', maxAbove: '上限を超えてよい割合（%）',
      regimen: '投与方式', below: '下限を下回る割合', above: '上限を超える割合', first: '下限を下回る割合（初回の投与間隔）', cmin: 'トラフ中央値（mg/L）', cavg: '平均濃度中央値（mg/L）', cmax: '最高濃度中央値（mg/L）', verdict: '範囲を保てるか',
      yes: '保てる', no: '外れる', inBand: function (w, band, n) { return w + ' kg は ' + band + ' kg の帯です（各方式で仮想成人20,000人のうち ' + n + '人）。'; },
      loading: 'データを読み込んでいます…', failed: 'データを読み込めませんでした。',
      limits: function (f, c) { return '下限：定常状態のトラフ ' + f + ' mg/L（体重換算の基準方式の5パーセンタイル）。上限：定常状態の最高濃度 ' + c + ' mg/L（10 mg/kg 2週ごとの中央値）。'; },
      chartTitle: '体重帯別に下限を下回る割合', chartAlt: '体重帯と投与方式ごとの、下限を下回る仮想患者の割合の棒グラフ。',
      extremes: '体重を固定した仮想患者（主解析）', ext40: '40 kg', ext160: '160 kg',
      percentile: function (w, p, name) {
        var q = [['1%', 1], ['5%', 5], ['50%', 50], ['95%', 95], ['99%', 99]], i;
        if (w < p['1%']) return name + 'の1パーセンタイルより軽い体重です。';
        for (i = 0; i < q.length - 1; i++) if (w < p[q[i + 1][0]]) return name + 'の' + q[i][1] + '〜' + q[i + 1][1] + 'パーセンタイルの間です。';
        return name + 'の99パーセンタイルより重い体重です。';
      },
      pop: 'NHANES成人', asianPop: 'NHANES非ヒスパニック系アジア人成人',
      scen: { main: '主解析', pembro_footnote: '表の脚注の値（CL 0.202、指数0.578）', exponent_low: '体重の指数を95%CIの下端', exponent_high: '体重の指数を95%CIの上端', asian_weights: 'アジア人の体重分布', ignore_sex: '性を無視', pembro_low_albumin: '低アルブミン（30 g/L）', nivo_constant_cl: '時間変化するCLを無視' },
      drugs: { pembrolizumab: 'Pembrolizumab', nivolumab: 'Nivolumab' }
    }
  }[lang];
  var COLORS = ['#0072B2', '#D55E00', '#009E73', '#CC79A7', '#E69F00', '#56B4E9'];
  var data = null, state = { drug: 'pembrolizumab', weight: 80, scenario: 'main', maxBelow: 10, maxAbove: 5 };

  function el(tag, attrs, children) {
    var node = document.createElement(tag), key;
    for (key in attrs || {}) { if (key === 'text') node.textContent = attrs[key]; else node.setAttribute(key, attrs[key]); }
    (children || []).forEach(function (child) { node.appendChild(child); });
    return node;
  }
  function field(id, label, control) { return el('div', { 'class': 'tool-field' }, [el('label', { 'for': id, text: label }), control]); }
  function bandIndex(w) { var i = 0; while (i + 1 < data.lower.length && w >= data.lower[i + 1]) i++; return i; }
  function pct(x) { return (x * 100).toFixed(1); }

  var controls = el('div', { 'class': 'tool-controls' });
  var out = el('div', { 'aria-live': 'polite' });
  root.innerHTML = '';
  root.appendChild(el('p', { 'class': 'meta', text: T.loading }));

  function select(id, options, value) {
    var s = el('select', { id: id });
    options.forEach(function (o) { var opt = el('option', { value: o[0], text: o[1] }); if (o[0] === value) opt.selected = true; s.appendChild(opt); });
    return s;
  }
  function number(id, value, min, max, step) { return el('input', { id: id, type: 'number', value: value, min: min, max: max, step: step, inputmode: 'decimal' }); }

  function buildControls() {
    controls.innerHTML = '';
    var drugSel = select('tool-drug', Object.keys(data.drugs).map(function (d) { return [d, T.drugs[d]]; }), state.drug);
    var scenSel = select('tool-scenario', Object.keys(data.drugs[state.drug].scenarios).map(function (s) { return [s, T.scen[s] || s]; }), state.scenario);
    var weight = number('tool-weight', state.weight, 30, 200, 1);
    var below = number('tool-below', state.maxBelow, 0, 100, 1);
    var above = number('tool-above', state.maxAbove, 0, 100, 1);
    drugSel.addEventListener('change', function () { state.drug = drugSel.value; state.scenario = 'main'; buildControls(); render(); });
    scenSel.addEventListener('change', function () { state.scenario = scenSel.value; render(); });
    weight.addEventListener('input', function () { var v = parseFloat(weight.value); if (v >= 30 && v <= 200) { state.weight = v; render(); } });
    below.addEventListener('input', function () { var v = parseFloat(below.value); if (v >= 0 && v <= 100) { state.maxBelow = v; render(); } });
    above.addEventListener('input', function () { var v = parseFloat(above.value); if (v >= 0 && v <= 100) { state.maxAbove = v; render(); } });
    [field('tool-drug', T.drug, drugSel), field('tool-weight', T.weight, weight), field('tool-scenario', T.scenario, scenSel), field('tool-below', T.maxBelow, below), field('tool-above', T.maxAbove, above)].forEach(function (f) { controls.appendChild(f); });
  }

  function chart(drug, scenarioTable, regimens, selected) {
    var W = 640, H = 260, L = 44, B = 40, top = 24, ns = 'http://www.w3.org/2000/svg';
    var max = 0.1;
    data.bands.forEach(function (b) { regimens.forEach(function (r) { max = Math.max(max, scenarioTable[b][r].below); }); });
    max = Math.ceil(max * 20) / 20;
    var svg = document.createElementNS(ns, 'svg');
    svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H); svg.setAttribute('role', 'img'); svg.setAttribute('aria-label', T.chartAlt); svg.setAttribute('class', 'tool-chart');
    function add(tag, attrs, text) { var n = document.createElementNS(ns, tag), k; for (k in attrs) n.setAttribute(k, attrs[k]); if (text !== undefined) n.textContent = text; svg.appendChild(n); return n; }
    var gw = (W - L - 8) / data.bands.length, bw = Math.min(14, (gw - 8) / regimens.length);
    function y(v) { return H - B - (H - B - top) * v / max; }
    var t, ticks = 4;
    for (t = 0; t <= ticks; t++) { var v = max * t / ticks; add('line', { x1: L, x2: W - 8, y1: y(v), y2: y(v), stroke: '#ddd' }); add('text', { x: L - 6, y: y(v) + 4, 'text-anchor': 'end', 'font-size': 11, fill: '#555' }, Math.round(v * 100) + '%'); }
    add('rect', { x: L + gw * selected, y: top, width: gw, height: H - B - top, fill: '#25577b', opacity: 0.08 });
    data.bands.forEach(function (b, i) {
      regimens.forEach(function (r, j) {
        var h = (H - B - top) * scenarioTable[b][r].below / max;
        add('rect', { x: L + gw * i + (gw - bw * regimens.length) / 2 + bw * j, y: H - B - h, width: bw - 1, height: h, fill: COLORS[j % COLORS.length] });
      });
      add('text', { x: L + gw * (i + 0.5), y: H - B + 16, 'text-anchor': 'middle', 'font-size': 11, fill: '#333' }, b.replace('>=', '≥'));
    });
    add('line', { x1: L, x2: W - 8, y1: y(state.maxBelow / 100), y2: y(state.maxBelow / 100), stroke: '#b00020', 'stroke-dasharray': '4 3' });
    add('text', { x: W - 10, y: y(state.maxBelow / 100) - 4, 'text-anchor': 'end', 'font-size': 11, fill: '#b00020' }, state.maxBelow + '%');
    add('text', { x: L + (W - L) / 2, y: H - 6, 'text-anchor': 'middle', 'font-size': 11, fill: '#555' }, 'kg');
    return svg;
  }

  function render() {
    var drug = data.drugs[state.drug], table = drug.scenarios[state.scenario], thr = drug.thresholds[state.scenario];
    var i = bandIndex(state.weight), band = data.bands[i], regimens = drug.regimens.slice().sort(function (a, b) { return (a.indexOf('mg/kg') > -1 ? 0 : 1) - (b.indexOf('mg/kg') > -1 ? 0 : 1) || a.localeCompare(b); });
    out.innerHTML = '';
    var first = table[band][regimens[0]];
    var popName = state.scenario === 'asian_weights' ? T.asianPop : T.pop;
    var popKey = state.scenario === 'asian_weights' ? 'NHANES non-Hispanic Asian' : 'NHANES adults';
    out.appendChild(el('p', { text: T.inBand(state.weight, band.replace('>=', '≥'), first.n) + ' ' + T.percentile(state.weight, data.population[popKey], popName) }));
    var head = el('tr', {}, [T.regimen, T.below, T.above, T.first, T.cmin, T.cavg, T.cmax, T.verdict].map(function (h) { return el('th', { scope: 'col', text: h }); }));
    var body = regimens.map(function (r) {
      var c = table[band][r], ok = c.below * 100 <= state.maxBelow && c.above * 100 <= state.maxAbove;
      return el('tr', {}, [el('th', { scope: 'row', text: r }), el('td', { text: pct(c.below) + '%' }), el('td', { text: pct(c.above) + '%' }), el('td', { text: pct(c.first) + '%' }),
        el('td', { text: c.cmin.toFixed(1) }), el('td', { text: c.cavg.toFixed(1) }), el('td', { text: c.cmax.toFixed(1) }), el('td', { text: ok ? T.yes : T.no, 'class': ok ? 'tool-ok' : 'tool-out' })]);
    });
    out.appendChild(el('table', { 'class': 'tool-table' }, [el('thead', {}, [head]), el('tbody', {}, body)]));
    out.appendChild(el('p', { 'class': 'meta', text: T.limits(thr.floor.toFixed(1), thr.ceiling.toFixed(0)) }));
    out.appendChild(el('h3', { text: T.chartTitle }));
    out.appendChild(chart(state.drug, table, regimens, i));
    out.appendChild(el('p', { 'class': 'tool-legend meta' }, regimens.map(function (r, j) { return el('span', {}, [el('span', { 'class': 'tool-swatch', style: 'background:' + COLORS[j % COLORS.length] }), document.createTextNode(r + ' ')]); })));
    if (state.scenario === 'main') {
      out.appendChild(el('h3', { text: T.extremes }));
      var rows = drug.extremes.slice().sort(function (a, b) { return a.wt - b.wt || a.regimen.localeCompare(b.regimen); }).map(function (e) {
        return el('tr', {}, [el('th', { scope: 'row', text: e.wt + ' kg · ' + e.regimen }), el('td', { text: pct(e.below) + '%' }), el('td', { text: pct(e.above) + '%' }), el('td', { text: pct(e.first) + '%' })]);
      });
      out.appendChild(el('table', { 'class': 'tool-table' }, [el('thead', {}, [el('tr', {}, [T.regimen, T.below, T.above, T.first].map(function (h) { return el('th', { scope: 'col', text: h }); }))]), el('tbody', {}, rows)]));
    }
  }

  fetch(root.getAttribute('data-src')).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }).then(function (json) {
    data = json; root.innerHTML = ''; buildControls(); root.appendChild(controls); root.appendChild(out); render();
  }).catch(function () { root.innerHTML = ''; root.appendChild(el('p', { 'class': 'notice', text: T.failed })); });
}());
