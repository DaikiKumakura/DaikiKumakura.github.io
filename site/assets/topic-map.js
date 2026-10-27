/* A small dependency-free network; the ordinary topic links remain available. */
(() => {
  const mount = document.querySelector('[data-topic-map]');
  const source = document.getElementById('topic-map-data');
  if (!mount || !source) return;
  const topics = JSON.parse(source.textContent);
  const svg = mount.querySelector('svg');
  const ns = 'http://www.w3.org/2000/svg';
  const el = (name, attrs = {}) => { const n = document.createElementNS(ns, name); Object.entries(attrs).forEach(([k,v]) => n.setAttribute(k, v)); return n; };
  const edges = el('g', {class:'topic-edges'}), nodesLayer = el('g');
  svg.append(edges, nodesLayer);
  const palette = ['#9cb8ff','#83d8cc','#e7bca8','#cbb6f5','#a5ca93','#f4d492'];
  const nodes = [], links = [], articleNodes = new Map();
  const center = {x:400,y:240};
  const viewport={x:0,y:0,w:800,h:480};
  const setView=()=>svg.setAttribute('viewBox',`${viewport.x} ${viewport.y} ${viewport.w} ${viewport.h}`);
  function zoom(factor){const width=Math.max(320,Math.min(1600,viewport.w*factor)),height=width*.6;viewport.x+=(viewport.w-width)/2;viewport.y+=(viewport.h-height)/2;viewport.w=width;viewport.h=height;setView();}
  mount.querySelectorAll('[data-map-zoom]').forEach(b=>b.addEventListener('click',()=>zoom(b.dataset.mapZoom==='in'?.8:1.25)));
  mount.querySelector('[data-map-reset]').addEventListener('click',()=>{Object.assign(viewport,{x:0,y:0,w:800,h:480});setView();nodes.forEach(n=>{n.x=n.initialX;n.y=n.initialY;n.homeX=n.x;n.homeY=n.y;n.vx=n.vy=0;});});
  svg.addEventListener('wheel',e=>{e.preventDefault();zoom(e.deltaY>0?1.08:1/1.08);},{passive:false});
  const short = label => label.length > 30 ? label.slice(0,28)+'…' : label;
  const makeNode = (data, x, y, group, main) => {
    const g=el('g', {class:main?'map-node map-topic':'map-node map-article',tabindex:'0',role:'link','aria-label':data.label});
    const halo=el('circle',{r:main?25:13,class:'map-halo'}), dot=el('circle',{r:main?8:4,class:'map-dot'});
    const title=el('title');title.textContent=data.label;
    const text=el('text',{x:x>500?-17:17,y:4,class:'map-label','text-anchor':x>500?'end':'start'});text.textContent=short(data.label);
    g.style.setProperty('--node-color',palette[group%palette.length]);g.append(halo,dot,text,title);nodesLayer.append(g);
    const node={...data,x,y,initialX:x,initialY:y,vx:0,vy:0,homeX:x,homeY:y,g,main,group};nodes.push(node);
    g.addEventListener('keydown', e => { if(e.key==='Enter'){location.href=data.href;} });
    g.addEventListener('click', () => {if(!node.dragged) location.href=data.href;});
    return node;
  };
  topics.forEach((topic,i) => {
    const angle=2*Math.PI*i/topics.length-Math.PI/2;
    const x=center.x+230*Math.cos(angle), y=center.y+150*Math.sin(angle);
    const anchor=makeNode({label:topic.label,href:topic.href},x,y,i,true);
    topic.articles.forEach((article,j) => {
      let n=articleNodes.get(article.href);
      if(!n){const a=angle+(j-(topic.articles.length-1)/2)*0.38;n=makeNode({label:article.title,href:article.href},x+70*Math.cos(a),y+56*Math.sin(a),i,false);articleNodes.set(article.href,n);}
      const line=el('line');edges.append(line);links.push({a:anchor,b:n,line});
    });
  });
  let pointer=null,pan=null;
  function position(e) {const p=svg.createSVGPoint();p.x=e.clientX;p.y=e.clientY;return p.matrixTransform(svg.getScreenCTM().inverse());}
  nodes.forEach(n=>n.g.addEventListener('pointerdown',e=>{pointer={n,id:e.pointerId,start:position(e)};n.dragged=false;n.g.setPointerCapture(e.pointerId);n.g.classList.add('dragging');e.preventDefault();}));
  svg.addEventListener('pointerdown',e=>{if(e.target!==svg)return;pan={x:e.clientX,y:e.clientY,vx:viewport.x,vy:viewport.y};svg.setPointerCapture(e.pointerId);});
  svg.addEventListener('pointermove',e=>{if(pan){const rect=svg.getBoundingClientRect();viewport.x=pan.vx-(e.clientX-pan.x)*viewport.w/rect.width;viewport.y=pan.vy-(e.clientY-pan.y)*viewport.h/rect.height;setView();return;}if(!pointer||pointer.id!==e.pointerId)return;const p=position(e),n=pointer.n;if(Math.hypot(p.x-pointer.start.x,p.y-pointer.start.y)>4)n.dragged=true;n.x=p.x;n.y=p.y;n.homeX=n.x;n.homeY=n.y;});
  svg.addEventListener('pointerup',e=>{pan=null;if(pointer&&pointer.id===e.pointerId){pointer.n.g.classList.remove('dragging');pointer=null;}});
  svg.addEventListener('pointercancel',()=>{pan=null;if(pointer)pointer.n.g.classList.remove('dragging');pointer=null;});
  const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function draw(){
    if(!reduced)links.forEach(({a,b})=>{const dx=b.x-a.x,dy=b.y-a.y,d=Math.max(1,Math.hypot(dx,dy)),force=(d-78)*.0008;if(!pointer||pointer.n!==a){a.vx+=dx/d*force;a.vy+=dy/d*force;}if(!pointer||pointer.n!==b){b.vx-=dx/d*force;b.vy-=dy/d*force;}});
    for(const n of nodes){
      if(!reduced && (!pointer||pointer.n!==n)){
        n.vx+=(n.homeX-n.x)*.003;n.vy+=(n.homeY-n.y)*.003;
        for(const o of nodes){if(o===n)continue;let dx=n.x-o.x,dy=n.y-o.y,d=Math.max(20,Math.hypot(dx,dy));if(d<48){n.vx+=dx/d*.08;n.vy+=dy/d*.08;}}
        n.vx*=.91;n.vy*=.91;n.x+=n.vx;n.y+=n.vy;
      }
      n.g.setAttribute('transform',`translate(${n.x} ${n.y})`);
    }
    links.forEach(({a,b,line})=>{line.setAttribute('x1',a.x);line.setAttribute('y1',a.y);line.setAttribute('x2',b.x);line.setAttribute('y2',b.y);});
    requestAnimationFrame(draw);
  }
  draw();
})();
