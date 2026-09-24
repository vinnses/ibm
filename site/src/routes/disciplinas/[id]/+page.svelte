<script lang="ts">let { data } = $props();</script>
<svelte:head>
  <title>{data.component.code} {data.component.name} · Grade {data.year} · Informática Biomédica UFPR</title>
  <meta name="description" content={`${data.component.name} (${data.component.code}) na grade ${data.year} de Informática Biomédica da UFPR. Consulte período, Ficha 1 disponível e documentos relacionados.`} />
  <meta property="og:title" content={`${data.component.code} ${data.component.name} · Grade ${data.year} · Informática Biomédica UFPR`} />
  <meta property="og:description" content={`Consulte período, Ficha 1 disponível e documentos de ${data.component.name} (${data.component.code}) na grade ${data.year}.`} />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Dados, Documentos e Análises sobre IBM/UFPR" />
  <meta property="og:locale" content="pt_BR" />
</svelte:head>
<main class="detail">
  <a class="back" href={`/curriculos/curriculum-${data.year}`}>← Voltar à grade {data.year}</a>
  <header><p class="eyebrow">Grade {data.year} · {data.component.period}º período</p><h1><span>{data.component.code}</span>{data.component.name}</h1><p class="summary">{data.component.hours ?? '—'} horas · {data.component.nature === 'elective_space' ? 'Espaço optativo' : data.component.nature.includes('TCC') || data.component.code === 'CI262' ? 'Trabalho de conclusão de curso' : data.component.nature.includes('estágio') ? 'Estágio obrigatório' : 'Disciplina obrigatória'}</p></header>
  <div class="columns">
    <section class="panel"><h2>Ficha 1</h2>
      {#if data.component.fichas.length}
        <ul class="fichas">{#each data.component.fichas as ficha}<li><a href={ficha.url} target="_blank" rel="noopener">Abrir {ficha.title} ↗</a><small>{ficha.note}</small></li>{/each}</ul>
      {:else if data.component.fichaState === 'not_located'}
        <p class="notice">Ficha 1 não localizada na busca pública. Isso não prova que o documento não exista.</p>
      {:else}
        <p class="notice">Este componente não entra na busca de Fichas 1; consulte os documentos formais e regulamentos pertinentes.</p>
      {/if}
    </section>
    <section class="panel"><h2>Na outra grade</h2>
      {#if data.component.counterpart}
        <p>Foi localizada uma disciplina com {data.component.counterpart.relation === 'Mesmo código' ? 'o mesmo código' : 'nome semelhante'}:</p>
        <a class="peer" href={`/disciplinas/${data.component.counterpart.id}`}><strong>{data.component.counterpart.code} · {data.component.counterpart.name}</strong><span>Grade {data.component.counterpart.year} · {data.component.counterpart.hours ?? '—'} h →</span></a>
        <p class="notice">Essa ligação facilita a consulta; não estabelece equivalência formal nem identidade de conteúdo.</p>
      {:else}<p class="notice">Nenhuma correspondência simples foi indicada. Isso não significa que a disciplina não tenha relação com conteúdos da outra grade.</p>{/if}
    </section>
  </div>
  {#if data.component.prerequisites.length}<section class="panel below"><h2>Pré-requisitos registrados</h2><ul>{#each data.component.prerequisites as requirement}<li>{requirement}</li>{/each}</ul></section>{/if}
  <section class="sources"><h2>Documentos formais da grade {data.year}</h2><ul>{#each data.formalDocuments as document}<li><a href={document.url} target="_blank" rel="noopener">{document.title} ↗</a></li>{/each}</ul></section>
</main>
<style>
  .detail{max-width:1050px}.back{font-size:.86rem;font-weight:700}header{margin:1.6rem 0 2rem}.eyebrow{margin:0 0 .4rem;color:var(--green);font-size:.77rem;font-weight:800;text-transform:uppercase;letter-spacing:.08em}h1{display:grid;gap:.3rem;max-width:850px;margin:0;font-size:clamp(2rem,5vw,3.5rem);letter-spacing:-.04em}h1 span{color:var(--green);font-size:.85rem;letter-spacing:.08em}.summary{color:var(--muted)}.columns{display:grid;grid-template-columns:1fr 1fr;gap:1rem}.panel{padding:1.4rem;border:1px solid var(--line);border-radius:14px;background:var(--surface)}h2{margin:0 0 .7rem;font-size:1.2rem}.panel p{font-size:.88rem}.notice{color:var(--muted)}.fichas{padding-left:1.2rem}.fichas li+li{margin-top:.9rem}.fichas a{font-weight:750}.fichas small{display:block;margin-top:.25rem;color:var(--muted);font-size:.75rem}.peer{display:grid;gap:.25rem;padding:1rem;border-radius:10px;background:var(--soft);text-decoration:none}.peer span{color:var(--muted);font-size:.78rem}.below{margin-top:1rem}.below ul{margin-bottom:0}.sources{margin-top:2.5rem;padding-top:1rem;border-top:1px solid var(--line);font-size:.84rem}.sources li+li{margin-top:.4rem}@media(max-width:700px){.columns{grid-template-columns:1fr}}
</style>
