<script lang="ts">
  let { data } = $props();
  let query = $state('');
  let kind = $state('Todos');
  const categories = ['Todos', 'Resolução', 'Projeto pedagógico', 'Ficha 1', 'Ficha 2', 'Outro documento'];
  const normalize = (value: string) => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  let filtered = $derived(data.documents.filter((document) =>
    (kind === 'Todos' || document.type === kind) &&
    (!query.trim() || normalize(`${document.title} ${document.type} ${document.institution}`).includes(normalize(query.trim())))
  ));
</script>

<svelte:head>
  <title>Documentos · Informática Biomédica UFPR</title>
  <meta name="description" content="Consulte os documentos públicos preservados sobre as grades de Informática Biomédica da UFPR." />
</svelte:head>

<main class="archive">
  <header class="page-heading">
    <p class="eyebrow">Acervo público</p>
    <h1>Documentos</h1>
    <p>Resoluções, projetos pedagógicos e fichas já disponíveis para consulta. Cada registro leva ao arquivo preservado.</p>
  </header>

  <section class="controls" aria-label="Filtrar documentos">
    <label>Buscar por título ou instituição<input type="search" placeholder="Ex.: Programação 1" bind:value={query} /></label>
    <label>Tipo de documento<select bind:value={kind}>{#each categories as category}<option value={category}>{category}</option>{/each}</select></label>
  </section>

  <p class="result-count">{filtered.length} documento{filtered.length === 1 ? '' : 's'}</p>
  {#if filtered.length}
    <ul class="document-list">
      {#each filtered as document (document.id)}
        <li><a href={`/documentos/${document.id}`}><span class="type">{document.type}</span><strong>{document.title}</strong><span class="meta">{document.institution}{document.date ? ` · ${document.date}` : ''}</span></a></li>
      {/each}
    </ul>
  {:else}
    <p class="empty">Nenhum documento corresponde a esses filtros.</p>
  {/if}
  <p class="limit">Este acervo reúne somente os arquivos atualmente publicados. A ausência de um documento aqui não significa que ele não exista.</p>
</main>

<style>
  .archive{max-width:1050px}.page-heading{max-width:760px;margin-bottom:2rem}.eyebrow{margin:0 0 .45rem;color:var(--green);font-size:.75rem;font-weight:800;letter-spacing:.11em;text-transform:uppercase}h1{margin:0;font-size:clamp(2.3rem,5vw,3.8rem);letter-spacing:-.045em}.page-heading p:last-child{max-width:690px;color:var(--muted)}
  .controls{display:grid;grid-template-columns:minmax(0,2fr) minmax(180px,1fr);gap:1rem;padding:1.1rem;border:1px solid var(--line);border-radius:12px;background:var(--surface)}.controls label{display:grid;gap:.4rem;font-size:.8rem;font-weight:700}.controls input,.controls select{width:100%;min-height:43px;padding:.55rem .7rem;border:1px solid #aec2bc;border-radius:8px;background:#fff;color:var(--ink);font:inherit;font-weight:400}
  .result-count{margin:1.45rem 0 .65rem;color:var(--muted);font-size:.8rem}.document-list{display:grid;gap:.65rem;margin:0;padding:0;list-style:none}.document-list a{display:grid;grid-template-columns:145px minmax(0,1fr) auto;align-items:baseline;gap:1rem;padding:1rem 1.1rem;border:1px solid var(--line);border-radius:10px;background:var(--surface);color:var(--ink);text-decoration:none}.document-list a:hover{border-color:var(--green);background:var(--soft)}.document-list strong{font-size:.95rem;font-weight:700}.type,.meta{color:var(--muted);font-size:.76rem}.type{color:var(--green-dark);font-weight:750}.meta{text-align:right}.empty{padding:1.5rem;border:1px dashed var(--line);border-radius:10px}.limit{max-width:720px;margin-top:1.4rem;color:var(--muted);font-size:.8rem}
  @media(max-width:760px){.document-list a{grid-template-columns:1fr;gap:.25rem}.meta{text-align:left}}@media(max-width:600px){.controls{grid-template-columns:1fr}}
</style>
