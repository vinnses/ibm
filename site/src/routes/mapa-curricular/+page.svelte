<script lang="ts">
  import CoverageBadge from '$lib/components/CoverageBadge.svelte';
  import EvidenceList from '$lib/components/EvidenceList.svelte';
  import StatusBadge from '$lib/components/StatusBadge.svelte';
  import VisualLegend from '$lib/components/VisualLegend.svelte';

  let { data } = $props();
  // svelte-ignore state_referenced_locally
  let selectedComponentId = $state(data.initial_component && data.components.some((item: any) => item.id === data.initial_component) ? data.initial_component : '');
  // svelte-ignore state_referenced_locally
  let selectedTopicId = $state(data.initial_topic && data.topics.some((item: any) => item.id === data.initial_topic) ? data.initial_topic : '');
  let mobileCurriculum = $state<'curriculum-2011' | 'curriculum-2023'>('curriculum-2011');
  let period = $state('');
  let domain = $state('');
  let discipline = $state('');
  let reviewState = $state('');
  let evidenceStrength = $state('');
  let coverage = $state('');
  let sharedOnly = $state(false);
  let proposedOnly = $state(false);
  let indeterminateOnly = $state(false);
  let showMoreFilters = $state(false);

  let selectedComponent = $derived(data.components.find((item: any) => item.id === selectedComponentId));
  let selectedTopic = $derived(data.topics.find((item: any) => item.id === selectedTopicId));
  let selectedTopicOccurrences = $derived(data.occurrences.filter((item: any) => item.topic_id === selectedTopicId));
  let selectedRelations = $derived(data.relations.filter((relation: any) =>
    (selectedComponentId && [...relation.source_component_ids, ...relation.target_component_ids].includes(selectedComponentId)) ||
    (selectedTopicId && relation.topic_ids.includes(selectedTopicId))
  ));
  let relatedComponentIds = $derived(new Set(selectedRelations.flatMap((relation: any) => [...relation.source_component_ids, ...relation.target_component_ids])));
  let activeTopicIds = $derived(new Set(selectedTopicId ? [selectedTopicId] : (selectedComponent?.topic_ids ?? [])));
  let oppositeComponents = $derived(selectedComponent ? data.components.filter((item: any) =>
    item.curriculum_id !== selectedComponent.curriculum_id &&
    (item.topic_ids.some((id: string) => selectedComponent.topic_ids.includes(id)) || relatedComponentIds.has(item.id))
  ) : []);
  let crossCurriculumTopicIds = $derived(new Set(data.topics.filter((topic: any) => {
    const curricula = new Set(data.occurrences.filter((item: any) => item.topic_id === topic.id).map((item: any) => data.components.find((component: any) => component.id === item.component_instance_id)?.curriculum_id));
    return curricula.has('curriculum-2011') && curricula.has('curriculum-2023');
  }).map((topic: any) => topic.id)));

  function visible(component: any) {
    if (period && String(component.recommended_period ?? '') !== period) return false;
    if (domain && !component.domain_ids.includes(domain)) return false;
    if (discipline && component.id !== discipline) return false;
    if (reviewState && !component.review_states.includes(reviewState)) return false;
    if (evidenceStrength && !component.evidence_strengths.includes(evidenceStrength)) return false;
    if (coverage && component.coverage.state !== coverage) return false;
    if (sharedOnly && !component.topic_ids.some((id: string) => crossCurriculumTopicIds.has(id))) return false;
    if (proposedOnly && !component.review_states.includes('proposed')) return false;
    if (indeterminateOnly && !component.evidence_strengths.includes('indeterminate') && component.coverage.state !== 'indeterminate' && component.coverage.state !== 'applicability_indeterminate') return false;
    return true;
  }

  function selectComponent(id: string) {
    selectedComponentId = id;
    selectedTopicId = '';
  }

  function selectTopic(id: string) {
    selectedTopicId = id;
    selectedComponentId = '';
  }

  function resetFilters() {
    period = ''; domain = ''; discipline = ''; reviewState = ''; evidenceStrength = ''; coverage = '';
    sharedOnly = false; proposedOnly = false; indeterminateOnly = false;
  }
</script>

<svelte:head>
  <title>Mapa curricular 2011→2023 · IBM</title>
  <meta name="description" content="Explore conteúdos, disciplinas, lacunas e evidências dos currículos 2011 e 2023." />
</svelte:head>

<main class="map-page">
  <header class="map-intro">
    <p class="kicker">Investigue a mudança</p>
    <h1>Mapa curricular <span>2011 → 2023</span></h1>
    <p class="lede">Selecione uma disciplina para ver o que foi documentado e onde seus conteúdos aparecem no outro currículo. As conexões são candidatas propostas — não equivalências estabelecidas.</p>
    <div class="summary" aria-label="Resumo do acervo analítico">
      <span><strong>{data.summary.components}</strong> componentes</span>
      <span><strong>{data.summary.topics}</strong> tópicos propostos</span>
      <span><strong>{data.summary.relations}</strong> linhagens candidatas</span>
      <span><strong>{data.summary.gaps}</strong> lacunas explícitas</span>
    </div>
  </header>

  <VisualLegend />

  <section class="filter-panel" aria-labelledby="filter-title">
    <div class="filter-heading"><h2 id="filter-title">Recortar o mapa</h2><button class="text-button" type="button" onclick={() => showMoreFilters = !showMoreFilters}>{showMoreFilters ? 'Menos filtros' : 'Mais filtros'}</button></div>
    <div class="filters primary-filters">
      <label>Período<select bind:value={period}><option value="">Todos</option>{#each [1,2,3,4,5,6,7,8] as value}<option value={String(value)}>{value}º</option>{/each}</select></label>
      <label>Domínio<select bind:value={domain}><option value="">Todos</option>{#each data.domains as item}<option value={item.id}>{item.label}</option>{/each}</select></label>
      <label>Disciplina<select bind:value={discipline}><option value="">Todas</option>{#each data.components as item}<option value={item.id}>{item.code} · {item.name}</option>{/each}</select></label>
      <label>Disponibilidade documental<select bind:value={coverage}><option value="">Todas</option><option value="not_located">Documento não localizado</option><option value="applicability_indeterminate">Aplicabilidade indeterminada</option><option value="contradictory">Fonte contraditória</option><option value="sufficient">Cobertura suficiente</option><option value="indeterminate">Indeterminada</option></select></label>
    </div>
    {#if showMoreFilters}
      <div class="filters secondary-filters">
        <label>Estado de revisão<select bind:value={reviewState}><option value="">Todos</option><option value="proposed">Proposto</option><option value="reviewed">Revisado</option><option value="contested">Contestado</option><option value="indeterminate">Indeterminado</option></select></label>
        <label>Força da evidência<select bind:value={evidenceStrength}><option value="">Todas</option><option value="documented">Documentada</option><option value="strongly_supported">Fortemente sustentada</option><option value="probable">Provável</option><option value="hypothesis">Hipótese</option><option value="indeterminate">Indeterminada</option></select></label>
        <label class="check"><input type="checkbox" bind:checked={sharedOnly} /> Tópicos nos dois currículos</label>
        <label class="check"><input type="checkbox" bind:checked={proposedOnly} /> Somente relações/tópicos propostos</label>
        <label class="check"><input type="checkbox" bind:checked={indeterminateOnly} /> Somente casos indeterminados</label>
      </div>
    {/if}
    <button class="reset" type="button" onclick={resetFilters}>Limpar filtros</button>
  </section>

  <div class="mobile-switch" role="group" aria-label="Currículo visível em tela pequena">
    <button class:active={mobileCurriculum === 'curriculum-2011'} onclick={() => mobileCurriculum = 'curriculum-2011'}>2011</button>
    <button class:active={mobileCurriculum === 'curriculum-2023'} onclick={() => mobileCurriculum = 'curriculum-2023'}>2023</button>
  </div>

  <section class="timeline" aria-label="Componentes curriculares por período">
    {#each data.curricula as curriculum}
      <div class="curriculum-column" data-active={mobileCurriculum === curriculum.id}>
        <div class="year-heading"><span>{curriculum.year}</span><small>{curriculum.label}</small></div>
        {#each [1,2,3,4,5,6,7,8] as periodNumber}
          {@const periodComponents = data.components.filter((item: any) => item.curriculum_id === curriculum.id && item.recommended_period === periodNumber && visible(item))}
          {#if periodComponents.length}
            <section class="period" aria-labelledby={`${curriculum.id}-p${periodNumber}`}>
              <h2 id={`${curriculum.id}-p${periodNumber}`}>{periodNumber}º período <span>{periodComponents.length}</span></h2>
              <div class="component-list">
                {#each periodComponents as component}
                  <button
                    type="button"
                    class:selected={selectedComponentId === component.id}
                    class:related={relatedComponentIds.has(component.id) && selectedComponentId !== component.id}
                    class:topic-match={activeTopicIds.size > 0 && component.topic_ids.some((id: string) => activeTopicIds.has(id))}
                    class="component-card"
                    onclick={() => selectComponent(component.id)}
                    aria-pressed={selectedComponentId === component.id}
                  >
                    <span class="component-title"><strong>{component.code}</strong> {component.name}</span>
                    <span class="component-meta">{component.workload_hours ?? '—'} h · {component.topic_ids.length} tópico(s)</span>
                    <CoverageBadge {...component.coverage} />
                  </button>
                {/each}
              </div>
            </section>
          {/if}
        {/each}
      </div>
    {/each}
  </section>

  {#if selectedComponent}
    <aside class="inspection" aria-live="polite" aria-labelledby="inspection-title">
      <div class="inspection-bar"><p class="stamp">Disciplina selecionada</p><button class="close" type="button" aria-label="Fechar inspeção" onclick={() => selectedComponentId = ''}>×</button></div>
      <h2 id="inspection-title">{selectedComponent.code} · {selectedComponent.name}</h2>
      <p class="meta">{selectedComponent.curriculum_id === 'curriculum-2011' ? '2011' : '2023'} · {selectedComponent.recommended_period}º período · {selectedComponent.workload_hours ?? '—'} h</p>
      <CoverageBadge {...selectedComponent.coverage} />
      <p class="coverage-detail">{selectedComponent.coverage.detail}</p>
      <a class="detail-link" href={`/disciplinas/${selectedComponent.id}`}>Abrir ficha analítica completa</a>

      <div class="inspection-grid">
        <section>
          <h3>Conteúdos documentados</h3>
          {#if selectedComponent.topics.length}
            <ul class="topic-list">{#each selectedComponent.topics as topic}<li><button type="button" onclick={() => selectTopic(topic.id)}>{topic.label}</button> <StatusBadge value={topic.review_state} /></li>{/each}</ul>
          {:else}<p class="empty-state">Nenhum tópico foi extraído do corpus utilizável. Isso não significa ausência de conteúdo.</p>{/if}
        </section>
        <section>
          <h3>Possíveis destinos/origens</h3>
          {#if oppositeComponents.length}
            {#each oppositeComponents as counterpart}
              {@const shared = counterpart.topics.filter((topic: any) => selectedComponent.topic_ids.includes(topic.id))}
              <article class="comparison-card">
                <h4><button type="button" onclick={() => selectComponent(counterpart.id)}>{counterpart.code} · {counterpart.name}</button></h4>
                <p>{counterpart.workload_hours ?? '—'} h · {counterpart.recommended_period}º período</p>
                <p><strong>Compartilhados:</strong> {shared.length ? shared.map((item: any) => item.label).join(', ') : 'nenhum rótulo idêntico; vínculo por candidato de linhagem'}</p>
                <p><strong>Exclusivos nesta comparação:</strong> {counterpart.topics.filter((topic: any) => !selectedComponent.topic_ids.includes(topic.id)).map((item: any) => item.label).join(', ') || 'nenhum no corpus'}</p>
              </article>
            {/each}
          {:else}<p class="empty-state">Nenhuma contraparte foi proposta ou localizada no corpus disponível.</p>{/if}
        </section>
      </div>

      <section>
        <h3>Candidatos de continuidade</h3>
        {#if selectedRelations.length}
          <div class="relation-list">{#each selectedRelations as relation}<article data-change={relation.change_type}><div><strong>{relation.change_type}</strong> <StatusBadge value={relation.review_state} /> <StatusBadge value={relation.evidence_strength} /></div><p>{relation.notes}</p><EvidenceList items={relation.evidence} compact /></article>{/each}</div>
        {:else}<p class="empty-state">Nenhuma relação candidata registrada. Ausência de relação não prova remoção.</p>{/if}
      </section>

      <section><h3>Pré-requisitos e condições</h3>{#if selectedComponent.dependencies.length}<ul>{#each selectedComponent.dependencies as dependency}<li>{dependency.requirement_text} <StatusBadge value={dependency.documentary_state} /></li>{/each}</ul>{:else}<p class="empty-state">Nenhuma dependência registrada para este componente.</p>{/if}</section>
      <section><h3>Ver evidências</h3><EvidenceList items={selectedComponent.evidence} /></section>
    </aside>
  {:else if selectedTopic}
    <aside class="inspection" aria-live="polite" aria-labelledby="topic-title">
      <div class="inspection-bar"><p class="stamp">Conteúdo em trânsito</p><button class="close" type="button" aria-label="Fechar inspeção" onclick={() => selectedTopicId = ''}>×</button></div>
      <h2 id="topic-title">{selectedTopic.label}</h2>
      <p><strong>Domínio:</strong> {data.domains.find((item: any) => item.id === selectedTopic.domain_id)?.label}</p>
      <p><strong>Aliases:</strong> {selectedTopic.aliases.join(', ') || 'nenhum registrado'}</p>
      <StatusBadge value={selectedTopic.review_state} />
      <p>{selectedTopic.description}</p>
      <div class="comparison-columns">
        {#each data.curricula as curriculum}
          <section><h3>{curriculum.year}</h3>{#each selectedTopicOccurrences.filter((item: any) => data.components.find((component: any) => component.id === item.component_instance_id)?.curriculum_id === curriculum.id) as occurrence}{@const component = data.components.find((item: any) => item.id === occurrence.component_instance_id)}{#if component}<article class="comparison-card"><h4><button type="button" onclick={() => selectComponent(component.id)}>{component.code} · {component.name}</button></h4><StatusBadge value={occurrence.review_state} /> <StatusBadge value={occurrence.evidence_strength} /><blockquote>{occurrence.evidence_text}</blockquote><p class="meta">{occurrence.locator}</p><p><strong>Aplicabilidade:</strong> {occurrence.evidence[0]?.applicability || 'não especificada'}</p><EvidenceList items={occurrence.evidence} /></article>{/if}{/each}{#if !selectedTopicOccurrences.some((item: any) => data.components.find((component: any) => component.id === item.component_instance_id)?.curriculum_id === curriculum.id)}<p class="empty-state">Nenhuma ocorrência localizada neste corpus.</p>{/if}</section>
        {/each}
      </div>
      <section><h3>Candidatos de continuidade</h3>{#if selectedRelations.length}{#each selectedRelations as relation}<article class="relation-card"><strong>{relation.change_type}</strong> <StatusBadge value={relation.review_state} /> <StatusBadge value={relation.evidence_strength} /><p>{relation.notes}</p><EvidenceList items={relation.evidence} compact /></article>{/each}{:else}<p class="empty-state">Nenhum candidato associado.</p>{/if}</section>
      <a class="detail-link" href={`/conteudos/${selectedTopic.id}`}>Abrir registro completo do conteúdo</a>
    </aside>
  {:else}
    <section class="selection-prompt"><span aria-hidden="true">↳</span><div><h2>Comece por uma disciplina</h2><p>O mapa destacará tópicos e possíveis destinos ou origens. Em telas pequenas, alterne entre os anos sem reduzir os cartões.</p></div></section>
  {/if}
</main>

<style>
  .map-page { width: min(96rem, calc(100% - 2rem)); }
  .map-intro { display: grid; grid-template-columns: minmax(0, 2fr) minmax(17rem, 1fr); gap: .5rem 2rem; margin-bottom: 1.5rem; padding: clamp(1.25rem, 4vw, 3rem); border: 2px solid var(--ink); background: var(--paper); box-shadow: 8px 8px 0 var(--red); }
  .kicker { grid-column: 1 / -1; margin: 0; color: var(--red); font-weight: 900; letter-spacing: .12em; text-transform: uppercase; }
  h1 { max-width: 15ch; font-family: var(--display); font-size: clamp(2.4rem, 7vw, 5.8rem); letter-spacing: -.04em; text-transform: uppercase; }
  h1 span { color: var(--red); white-space: nowrap; }
  .map-intro .lede { align-self: end; font-size: 1.05rem; }
  .summary { grid-column: 1 / -1; display: flex; flex-wrap: wrap; gap: .5rem; margin-top: 1rem; }
  .summary span { padding: .35rem .6rem; border: 1px solid var(--ink); background: var(--surface); font-size: .8rem; }
  .filter-panel { position: sticky; z-index: 5; top: 0; margin: 1rem 0; padding: .75rem 1rem; border: 1px solid var(--line); background: color-mix(in srgb, var(--surface) 94%, transparent); backdrop-filter: blur(8px); }
  .filter-heading { display: flex; justify-content: space-between; align-items: center; gap: 1rem; }
  .filter-heading h2 { margin: 0; font: 900 .9rem/1 var(--sans); letter-spacing: .08em; text-transform: uppercase; }
  .filters { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: .75rem; margin-top: .75rem; }
  .secondary-filters { grid-template-columns: repeat(5, minmax(0, 1fr)); padding-top: .75rem; border-top: 1px dashed var(--line); }
  label { display: grid; gap: .2rem; color: var(--ink-soft); font-size: .72rem; font-weight: 800; }
  select { width: 100%; min-height: 2.5rem; border: 1px solid var(--line); background: var(--paper); font: inherit; color: var(--ink); }
  .check { display: flex; align-items: center; gap: .45rem; }
  .check input { width: 1.1rem; height: 1.1rem; accent-color: var(--red); }
  .text-button, .reset { padding: .25rem; border: 0; background: transparent; color: var(--red-dark); font: 800 .8rem var(--sans); text-decoration: underline; cursor: pointer; }
  .reset { margin-top: .5rem; }
  .mobile-switch { display: none; }
  .timeline { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(1rem, 4vw, 3rem); align-items: start; }
  .curriculum-column { min-width: 0; }
  .year-heading { position: sticky; z-index: 4; top: 8.5rem; display: flex; align-items: baseline; gap: 1rem; padding: .5rem .75rem; border: 2px solid var(--ink); background: var(--ink); color: var(--paper); }
  .year-heading span { font: 900 clamp(2rem, 5vw, 4rem)/.9 var(--display); }
  .year-heading small { font-weight: 700; }
  .period { margin: 1rem 0 1.5rem; }
  .period h2 { display: flex; justify-content: space-between; margin: 0 0 .45rem; padding-bottom: .35rem; border-bottom: 1px solid var(--ink); font: 900 .86rem/1 var(--sans); letter-spacing: .05em; text-transform: uppercase; }
  .period h2 span { color: var(--ink-soft); }
  .component-list { display: grid; gap: .45rem; }
  .component-card { display: grid; gap: .32rem; width: 100%; padding: .75rem; border: 1px solid var(--line); border-left: .35rem solid var(--line); background: var(--surface); color: var(--ink); text-align: left; cursor: pointer; transition: border-color .15s, transform .15s, background .15s; }
  .component-card:hover { border-color: var(--ink); transform: translateX(2px); }
  .component-card:focus-visible { outline: var(--focus); outline-offset: 2px; }
  .component-card.selected { border-color: var(--red); border-left-color: var(--red); background: var(--red-soft); }
  .component-card.related { border-left-color: var(--red); border-left-style: double; }
  .component-card.topic-match { box-shadow: inset 0 -.38rem 0 var(--highlight); }
  .component-title { line-height: 1.25; }
  .component-title strong { display: inline-block; margin-right: .25rem; font-family: var(--mono); color: var(--red-dark); }
  .component-meta { color: var(--ink-soft); font-size: .76rem; }
  .inspection { margin-top: 2rem; padding: clamp(1rem, 3vw, 2rem); border: 2px solid var(--ink); background: var(--surface); box-shadow: 7px 7px 0 var(--ink); }
  .inspection-bar { display: flex; justify-content: space-between; align-items: start; }
  .stamp { display: inline-block; margin: 0; padding: .25rem .45rem; border: 2px solid var(--red); color: var(--red); font: 900 .74rem var(--sans); letter-spacing: .08em; text-transform: uppercase; transform: rotate(-1deg); }
  .close { min-width: 2.5rem; min-height: 2.5rem; border: 1px solid var(--ink); background: var(--paper); font-size: 1.5rem; cursor: pointer; }
  .inspection > h2 { margin: .8rem 0 .3rem; font: 900 clamp(1.6rem, 4vw, 2.7rem)/1 var(--display); }
  .coverage-detail { max-width: 56rem; color: var(--ink-soft); }
  .detail-link { display: inline-block; margin: .5rem 0 1rem; font-weight: 850; }
  .inspection-grid, .comparison-columns { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem; }
  .inspection h3 { margin: 1.5rem 0 .6rem; border-bottom: 1px solid var(--line); padding-bottom: .3rem; font: 900 .86rem var(--sans); letter-spacing: .06em; text-transform: uppercase; }
  .topic-list { padding-left: 1.2rem; }
  .topic-list li + li { margin-top: .4rem; }
  .topic-list button, .comparison-card button { padding: 0; border: 0; background: transparent; color: var(--link); font: inherit; font-weight: 750; text-align: left; text-decoration: underline; cursor: pointer; }
  .comparison-card, .relation-list article, .relation-card { margin-bottom: .7rem; padding: .75rem; border: 1px solid var(--line); background: var(--paper); }
  .comparison-card h4 { margin: 0 0 .3rem; }
  .comparison-card p { margin: .35rem 0; font-size: .86rem; }
  .relation-list article { border-left: .35rem dashed var(--line); }
  .relation-list article[data-change='maintained'] { border-left-style: solid; }
  .relation-list article[data-change='fragmented'], .relation-list article[data-change='merged'] { border-left-style: double; border-left-color: var(--red); }
  .empty-state { padding: .7rem; border: 1px dashed var(--line); color: var(--ink-soft); background: var(--paper); }
  blockquote { margin: .75rem 0; padding-left: .75rem; border-left: 3px solid var(--highlight-strong); }
  .selection-prompt { display: flex; gap: 1rem; margin: 2rem auto 0; max-width: 48rem; padding: 1.2rem; border-top: 2px solid var(--red); background: var(--surface); }
  .selection-prompt > span { color: var(--red); font-size: 2rem; }
  .selection-prompt h2, .selection-prompt p { margin: 0; }
  @media (max-width: 900px) {
    .map-intro { grid-template-columns: 1fr; }
    .summary { grid-column: auto; }
    .filters, .secondary-filters { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .year-heading { top: 11rem; }
  }
  @media (max-width: 700px) {
    .map-page { width: min(100% - 1rem, 42rem); padding-top: 1rem; }
    .map-intro { box-shadow: 4px 4px 0 var(--red); }
    .map-intro h1 { font-size: clamp(2.25rem, 14vw, 4rem); }
    .filter-panel { position: static; }
    .filters, .secondary-filters { grid-template-columns: 1fr; }
    .mobile-switch { position: sticky; z-index: 6; top: 0; display: grid; grid-template-columns: 1fr 1fr; margin: 1rem 0; padding: .25rem; background: var(--ink); }
    .mobile-switch button { min-height: 2.75rem; border: 0; background: transparent; color: var(--paper); font-weight: 900; }
    .mobile-switch button.active { background: var(--red); }
    .timeline { grid-template-columns: 1fr; }
    .curriculum-column[data-active='false'] { display: none; }
    .year-heading { position: static; }
    .inspection { box-shadow: 4px 4px 0 var(--ink); }
    .inspection-grid, .comparison-columns { grid-template-columns: 1fr; }
  }
</style>
