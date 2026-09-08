<script lang="ts">
  import StatusBadge from '$lib/components/StatusBadge.svelte';
  let { data } = $props();
</script>

<svelte:head><title>Evidência · IBM</title></svelte:head>
<main>
  <p class="eyebrow">Registro de proveniência</p>
  <h1>Evidência</h1>
  <p class="lede">Este registro liga um trecho ou localizador documental às entidades que o utilizam. Ele não amplia a aplicabilidade da fonte.</p>
  <div class="evidence-sheet">
    <StatusBadge value={data.evidence.documentary_state} />
    <dl>
      <dt>Título documental</dt><dd><a href={`/documentos/${data.document?.id}`}>{data.document?.title}</a></dd>
      <dt>Tipo</dt><dd>{data.document?.document_type}</dd>
      <dt>Instituição</dt><dd>{data.document?.institution}</dd>
      <dt>Data</dt><dd>{data.document?.document_date}</dd>
      <dt>Página</dt><dd>{data.evidence.page ?? 'Não especificada'}</dd>
      <dt>Seção</dt><dd>{data.evidence.section ?? 'Não especificada'}</dd>
      <dt>Célula/intervalo</dt><dd>{data.evidence.cell_range ?? 'Não aplicável'}</dd>
      <dt>Trecho utilizado</dt><dd class="excerpt">{data.evidence.normalized_excerpt ?? 'Não transcrito neste registro'}</dd>
      <dt>Aplicabilidade</dt><dd>{data.evidence.applicability_note}</dd>
      <dt>Estado documental</dt><dd><StatusBadge value={data.document?.documentary_state ?? 'indeterminate'} /></dd>
      <dt>SHA-256</dt><dd><code>{data.document?.sha256}</code></dd>
      <dt>URL original</dt><dd><a href={data.document?.original_url} rel="noreferrer">Abrir origem institucional</a></dd>
    </dl>
    <p class="actions"><a href={data.document_anchor} target="_blank">Abrir documento preservado{data.evidence.page ? ` próximo à página ${data.evidence.page}` : ''}</a> <a href={`/documentos/${data.document?.id}`}>Ver registro do documento</a></p>
  </div>
  {#if data.evidence.notes}<p class="note">Nota: {data.evidence.notes}</p>{/if}
  <p>{data.links.length} vínculo(s) de proveniência usam esta evidência.</p>
</main>

<style>
  h1 { font-size: clamp(3rem, 8vw, 6rem); text-transform: uppercase; }
  .evidence-sheet { max-width: 64rem; margin-top: 2rem; padding: clamp(1rem, 4vw, 2.5rem); border: 1px solid var(--ink); background: var(--surface); box-shadow: 7px 7px 0 var(--ink); }
  .evidence-sheet dl { margin-top: 1.5rem; }
  .excerpt { padding: .7rem; border-left: 3px solid var(--highlight-strong); background: var(--paper); font-family: var(--serif); }
  .actions { display: flex; flex-wrap: wrap; gap: .6rem 1rem; margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid var(--line); font-weight: 800; }
  .note { max-width: 60rem; color: var(--ink-soft); }
  @media (max-width: 650px) { .evidence-sheet { box-shadow: 4px 4px 0 var(--ink); } }
</style>
