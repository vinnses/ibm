<script lang="ts">
  let { data }: { data: any } = $props();
  let query = $state('');
  let onlyMissing = $state(false);
  const normalize = (value: string) => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  function visible(component: any) {
    if (onlyMissing && component.fichaState !== 'not_located') return false;
    const search = normalize(query.trim());
    return !search || normalize(`${component.code} ${component.name} ${component.counterpart?.code ?? ''} ${component.counterpart?.name ?? ''}`).includes(search);
  }
</script>

<svelte:head>
  <title>Grade curricular {data.year} · Informática Biomédica UFPR</title>
  <meta name="description" content={`Consulte a grade curricular de ${data.year} de Informática Biomédica da UFPR, suas disciplinas, fichas e documentos formais.`} />
  <meta property="og:title" content={`Grade curricular ${data.year} · Informática Biomédica UFPR`} />
  <meta property="og:description" content={`Disciplinas, fichas e documentos formais da grade curricular de ${data.year} de Informática Biomédica da UFPR.`} />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Dados, Documentos e Análises sobre IBM/UFPR" />
  <meta property="og:locale" content="pt_BR" />
  <meta name="twitter:card" content="summary" />
</svelte:head>

<main class="grade">
  <div class="heading">
    <div><p class="eyebrow">Bacharelado em Informática Biomédica · UFPR</p><h1>Grade curricular <span>{data.year}</span></h1><p class="intro">Disciplinas por período, fichas disponíveis e pistas de correspondência entre as duas grades.</p></div>
    <nav class="year-tabs" aria-label="Escolher currículo"><a class:active={data.year === 2011} aria-current={data.year === 2011 ? 'page' : undefined} href="/curriculos/curriculum-2011">2011</a><a class:active={data.year === 2023} aria-current={data.year === 2023 ? 'page' : undefined} href="/curriculos/curriculum-2023">2023</a></nav>
  </div>

  <div class="overview" aria-label="Resumo da grade"><div><strong>8</strong><span>períodos</span></div><div><strong>{data.summary.coded}</strong><span>componentes com código</span></div><div><strong>{data.summary.missing}</strong><span>Fichas 1 não localizadas</span></div></div>

  <div class="explain"><span class="state-dot missing"></span><span>Ficha 1 não localizada na busca pública</span><span class="state-dot neutral"></span><span>Ficha 1 não se aplica</span></div>

  <section class="controls" aria-label="Filtrar disciplinas">
    <label><span>Buscar disciplina ou código</span><input type="search" placeholder="Ex.: Bioinformática ou CI1169" bind:value={query} /></label>
    <label class="checkbox"><input type="checkbox" bind:checked={onlyMissing} /><span>Mostrar apenas Fichas 1 não localizadas</span></label>
  </section>

  <div class="semesters">
    {#each data.periods as period}
      {@const items = period.components.filter(visible)}
      {#if items.length}
        <details class="semester" open={query.trim().length > 0 || onlyMissing || period.number < 3}>
          <summary><span>{period.number}º período</span><span class="period-meta">{period.components.length} componente{period.components.length === 1 ? '' : 's'} <span class="chevron" aria-hidden="true">⌄</span></span></summary>
          <div class="cards">
            {#each items as component (component.id)}
              <article class="course" id={component.code}>
                <div class="course-top"><span class="code">{component.code}</span><span class="hours">{component.hours ?? '—'} h</span></div>
                <h3><a href={`/disciplinas/${component.id}`}>{component.name}</a></h3>
                <p class="course-kind">{component.nature === 'elective_space' ? 'Espaço optativo' : component.nature.includes('TCC') || component.code === 'CI262' ? 'Trabalho de conclusão de curso' : component.nature.includes('estágio') ? 'Estágio obrigatório' : 'Disciplina obrigatória'}</p>
                <div class="course-bottom">
                  {#if component.fichaState === 'not_located'}
                    <span class="ficha-state"><span class="state-dot missing"></span>Ficha 1 não localizada</span>
                  {:else if component.fichaState === 'not_applicable'}
                    <span class="ficha-state"><span class="state-dot neutral"></span>Ficha 1 não se aplica</span>
                  {/if}
                  {#if component.fichas.length}<a class="ficha-link" href={component.fichas[0].url} target="_blank" rel="noopener">Abrir Ficha 1 ↗</a>{/if}
                </div>
                {#if component.counterpart}
                  <details class="compare"><summary>Comparar com a grade {component.counterpart.year}</summary><div class="peer"><span class="peer-type">{component.counterpart.relation} · não comprova equivalência formal</span><a href={`/disciplinas/${component.counterpart.id}`}>{component.counterpart.code} · {component.counterpart.name}</a><small>{component.counterpart.hours ?? '—'} h · {component.counterpart.year}</small>{#if !component.counterpart.ficha}<small>Ficha 1 não localizada ou não aplicável</small>{/if}{#if component.counterpart.ficha}<a class="peer-ficha" href={component.counterpart.ficha.url} target="_blank" rel="noopener">Abrir Ficha 1 da outra grade ↗</a>{/if}</div></details>
                {/if}
              </article>
            {/each}
          </div>
        </details>
      {/if}
    {/each}
  </div>

  {#if !data.periods.some((period: any) => period.components.some(visible))}<p class="empty">Nenhuma disciplina corresponde à busca. <button onclick={() => { query = ''; onlyMissing = false; }}>Limpar filtros</button></p>{/if}

  <section class="sources"><div><h2>Documentos da grade</h2><p>Estes documentos definem a estrutura formal. A aplicação de uma Ficha 1 à grade indicada pode ainda exigir confirmação.</p></div><ul>{#each data.formalDocuments as document}<li><a href={document.url} target="_blank" rel="noopener">{document.title} ↗</a></li>{/each}</ul></section>
  <p class="last-note">“Não localizada” descreve o resultado da busca pública, não a inexistência da Ficha. As relações entre grades são pistas de navegação, não atos de equivalência.</p>
</main>

<style>
  .heading{display:flex;align-items:end;justify-content:space-between;gap:2rem;margin:.2rem 0 1.6rem}.eyebrow{margin:0 0 .45rem;color:var(--green);font-size:.75rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase}h1{margin:0;font-size:clamp(2.1rem,5vw,3.7rem);letter-spacing:-.055em}h1 span{color:var(--green)}.intro{max-width:650px;margin:.8rem 0 0;color:var(--muted);font-size:1rem}.year-tabs{display:flex;gap:.35rem;padding:.35rem;border:1px solid var(--line);border-radius:13px;background:var(--surface)}.year-tabs a{min-width:75px;padding:.55rem .9rem;border-radius:9px;text-align:center;font-weight:750;text-decoration:none}.year-tabs a.active{background:var(--green-dark);color:#fff}
  .overview{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;overflow:hidden;border:1px solid var(--line);border-radius:16px;background:var(--line)}.overview div{display:flex;align-items:baseline;gap:.6rem;min-height:82px;padding:1.25rem;background:var(--surface)}.overview strong{font-size:1.8rem;line-height:1;color:var(--green-dark)}.overview span{font-size:.82rem;color:var(--muted)}
  .explain{display:flex;align-items:center;gap:.45rem .65rem;flex-wrap:wrap;margin:1.1rem 0 1.4rem;color:var(--muted);font-size:.75rem}.explain span:not(.state-dot){margin-right:1rem}.state-dot{display:inline-block;flex:none;width:9px;height:9px;border-radius:50%}.state-dot.missing{background:#d6a354}.state-dot.neutral{background:#a6b6b0}
  .controls{display:flex;align-items:end;gap:1.5rem;margin-bottom:1.2rem;padding:1rem 1.2rem;border:1px solid var(--line);border-radius:14px;background:var(--surface)}.controls label:first-child{display:grid;gap:.4rem;flex:1;font-size:.78rem;font-weight:700}.controls input[type=search]{width:100%;min-height:43px;padding:.6rem .8rem;border:1px solid #b8cbc3;border-radius:9px;background:#fff;color:var(--ink);font:inherit;font-weight:400}.controls .checkbox{display:flex;align-items:center;gap:.5rem;max-width:280px;padding-bottom:.55rem;font-size:.79rem;cursor:pointer}.controls input[type=checkbox]{width:17px;height:17px;accent-color:var(--green)}
  .semesters{display:grid;gap:1rem}.semester{border:1px solid var(--line);border-radius:14px;background:var(--surface);overflow:hidden}.semester>summary{display:flex;justify-content:space-between;align-items:center;gap:1rem;padding:1rem 1.25rem;cursor:pointer;list-style:none;font-size:1.13rem;font-weight:800}.semester>summary::-webkit-details-marker,.compare>summary::-webkit-details-marker{display:none}.semester[open]>summary{border-bottom:1px solid var(--line)}.period-meta{color:var(--muted);font-size:.78rem;font-weight:500}.chevron{display:inline-block;margin-left:1rem;font-size:1.2rem;transition:transform .2s}.semester[open] .chevron{transform:rotate(180deg)}.cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.8rem;padding:1rem}.course{min-width:0;display:flex;flex-direction:column;padding:1rem;border:1px solid var(--line);border-radius:12px;background:#fff;box-shadow:0 2px 8px #17312d08}.course-top,.course-bottom{display:flex;align-items:center;justify-content:space-between;gap:.5rem}.code{color:var(--green-dark);font-size:.77rem;font-weight:800;letter-spacing:.06em}.hours{color:var(--muted);font-size:.75rem}.course h3{min-height:2.65em;margin:.5rem 0 .25rem;font-size:1rem}.course h3 a{color:var(--ink);text-decoration:none}.course h3 a:hover{text-decoration:underline}.course-kind{margin:.1rem 0 1.1rem;color:var(--muted);font-size:.75rem}.course-bottom{margin-top:auto;align-items:baseline;flex-wrap:wrap}.ficha-state{display:inline-flex;align-items:center;gap:.4rem;color:var(--muted);font-size:.72rem}.ficha-link{font-size:.76rem;font-weight:750;white-space:nowrap}.compare{margin-top:.85rem;padding-top:.75rem;border-top:1px solid var(--line)}.compare>summary{color:var(--green-dark);font-size:.73rem;font-weight:700;cursor:pointer;list-style:none}.compare>summary::before{content:'↗';margin-right:.35rem}.peer{display:grid;gap:.2rem;margin-top:.65rem;padding:.7rem;border-radius:8px;background:var(--soft);font-size:.78rem}.peer-type,.peer small{color:var(--muted);font-size:.68rem}.peer a{font-weight:700}.empty{padding:1.5rem;border:1px dashed var(--line);border-radius:12px}.empty button{border:0;background:transparent;color:var(--green-dark);font:inherit;font-weight:700;text-decoration:underline;cursor:pointer}
  .sources{display:grid;grid-template-columns:1.5fr 1fr;gap:2rem;margin-top:2.2rem;padding:1.5rem;border:1px solid var(--line);border-radius:14px;background:var(--soft)}.sources h2{margin:0 0 .4rem;font-size:1.1rem}.sources p{margin:0;color:var(--muted);font-size:.83rem}.sources ul{margin:0;padding-left:1.2rem;font-size:.83rem}.sources li+li{margin-top:.4rem}.last-note{max-width:850px;margin:1rem 0 0;color:var(--muted);font-size:.75rem}
  @media(max-width:1000px){.cards{grid-template-columns:repeat(2,minmax(0,1fr))}.overview div{display:grid;gap:.3rem}}
  @media(max-width:680px){.heading{align-items:start;flex-direction:column;gap:1rem}.year-tabs{width:100%}.year-tabs a{flex:1}.overview{grid-template-columns:1fr}.overview div{min-height:65px}.controls{align-items:stretch;flex-direction:column;gap:.7rem}.controls .checkbox{padding:0}.cards{grid-template-columns:1fr}.course h3{min-height:0}.sources{grid-template-columns:1fr;gap:1rem}}
</style>
