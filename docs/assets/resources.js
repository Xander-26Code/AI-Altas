/* Progressive enhancement: the complete Markdown catalog remains without JS. */
async function initializeCatalog() {
  const root = document.getElementById('resource-explorer');
  if (!root || root.dataset.ready) return;
  try {
    const response = await fetch(root.dataset.catalogUrl);
    if (!response.ok) throw new Error('catalog unavailable');
    const { topics, resources } = await response.json();
    const titleMap = Object.fromEntries(topics.map(t => [t.slug, t.title]));
    const create = (tag, text, className) => {
      const node = document.createElement(tag);
      if (text) node.textContent = text;
      if (className) node.className = className;
      return node;
    };
    const controls = create('div', '', 'catalog-controls');
    const queryLabel = create('label', '搜索名称、主题或推荐理由');
    const query = create('input');
    query.type = 'search'; query.placeholder = '例如：数学、RAG、CUDA、中文';
    queryLabel.append(query); controls.append(queryLabel);
    const filters = {};
    for (const [field, label, values] of [
      ['topic','专题',topics.map(t => [t.slug,t.title])],
      ['language','语言',['中文','中英','英文'].map(x => [x,x])],
      ['level','难度',['入门','进阶','研究'].map(x => [x,x])],
      ['compute','计算条件',['无','CPU','可选GPU','GPU'].map(x => [x,x])],
      ['access','费用',['免费','部分免费','付费'].map(x => [x,x])]
    ]) {
      const wrapper = create('label', label);
      const select = create('select');
      const all = create('option','全部'); all.value = ''; select.append(all);
      for (const [value,text] of values) {
        const option = create('option',text); option.value = value; select.append(option);
      }
      filters[field] = select; wrapper.append(select); controls.append(wrapper);
    }
    const reset = create('button','清除筛选','md-button');
    reset.type = 'button'; controls.append(reset);
    const status = create('p','', 'catalog-status'); status.setAttribute('aria-live','polite');
    const list = create('div','', 'resource-cards');
    root.append(controls,status,list);
    const update = () => {
      const term = query.value.trim().toLocaleLowerCase();
      const chosen = resources.filter(r => {
        const text = [r.title,r.why,r.language,...r.topics.map(t => titleMap[t])].join(' ').toLocaleLowerCase();
        return (!term || text.includes(term)) && Object.entries(filters).every(([field,input]) =>
          !input.value || (field === 'topic' ? r.topics.includes(input.value) : r[field] === input.value));
      });
      status.textContent = `显示 ${chosen.length} / ${resources.length} 个资源。计算条件对应入门活动，大规模实验另计。`;
      list.replaceChildren();
      if (!chosen.length) list.append(create('p','没有匹配的资源，请减少筛选条件。'));
      for (const r of chosen) {
        const card = create('article','', 'resource-card');
        const heading = create('h3'); const link = create('a',r.title); link.href = r.url;
        link.rel = 'noopener noreferrer'; heading.append(link); card.append(heading);
        card.append(create('p',`${r.language} · ${r.level} · ${r.access} · ${r.compute}`, 'resource-meta'));
        card.append(create('p',r.why));
        const nav = create('p','', 'resource-topics');
        r.topics.forEach((t,i) => {
          if (i) nav.append(document.createTextNode(' / '));
          const a = create('a',titleMap[t]); a.href = `topics/${t}.html`; nav.append(a);
        });
        card.append(nav);
        card.append(create('small',`内容核实：${r.checked_on} · ${r.verification === 'content-reviewed' ? '查看过页面' : '官方索引核实'}`));
        list.append(card);
      }
    };
    query.addEventListener('input',update);
    Object.values(filters).forEach(el => el.addEventListener('change',update));
    reset.addEventListener('click',() => { query.value=''; Object.values(filters).forEach(el => el.value=''); update(); query.focus(); });
    root.dataset.ready = 'true'; root.hidden = false;
    document.getElementById('resource-fallback').hidden = true;
    update();
  } catch (_) { /* Markdown fallback stays visible. */ }
}
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded',initializeCatalog);
else initializeCatalog();
