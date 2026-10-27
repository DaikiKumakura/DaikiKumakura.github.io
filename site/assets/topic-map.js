/* Topic navigation is primary; the optional network is drawn once. */
(() => {
  const source=document.getElementById('topic-map-data');
  if(!source)return;
  const network=JSON.parse(source.textContent);
  const filters=[...document.querySelectorAll('[data-cluster-filter]')];
  const records=[...document.querySelectorAll('[data-article-cluster]')];
  filters.forEach(link=>link.addEventListener('click',event=>{
    if(event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;
    event.preventDefault();
    const selected=link.dataset.clusterFilter;
    filters.forEach(item=>item.setAttribute('aria-current',String(item===link)));
    let count=0;
    records.forEach(record=>{record.hidden=selected!=='all'&&record.dataset.articleCluster!==selected;if(!record.hidden)count++;});
    const group=network.clusters.find(group=>String(group.id)===selected);
    document.querySelector('[data-topic-status]').textContent=group?`${count} articles · ${group.label}`:`Showing all ${count} articles`;
  }));
  const svg=document.querySelector('[data-topic-map] svg');
  if(!svg)return;
  const ns='http://www.w3.org/2000/svg';
  const el=(tag,attrs)=>{const n=document.createElementNS(ns,tag);Object.entries(attrs||{}).forEach(([k,v])=>n.setAttribute(k,v));return n;};
  const index=new Map(network.nodes.map(node=>[node.id,node]));
  const edges=el('g',{class:'topic-edges'});svg.append(edges);
  network.edges.forEach(edge=>{
    const a=index.get(edge.source),b=index.get(edge.target);
    edges.append(el('line',{x1:a.x,y1:a.y,x2:b.x,y2:b.y,'stroke-width':.6+edge.weight*3,'stroke-opacity':.12+edge.weight*.6}));
  });
  network.nodes.forEach(node=>{
    const label=`Cluster ${node.cluster}: ${node.title}`;
    const link=el('a',{href:node.href,class:'map-node map-article',tabindex:'0','aria-label':label,transform:`translate(${node.x} ${node.y})`});
    link.style.setProperty('--node-color',`hsl(${(node.cluster-1)*360/Math.max(1,network.clusters.length)} 55% 73%)`);
    const title=el('title');title.textContent=label;
    link.append(el('circle',{r:18,class:'map-halo'}),el('circle',{r:6,class:'map-dot'}),title);
    const select=()=>{document.querySelector('[data-map-selection]').textContent=label;};
    link.addEventListener('mouseenter',select);link.addEventListener('focus',select);svg.append(link);
  });
})();
