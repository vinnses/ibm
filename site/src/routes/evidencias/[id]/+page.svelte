<script lang="ts">
  import StatusBadge from '$lib/components/StatusBadge.svelte';
  let { data } = $props();
</script>

<svelte:head><title>Evidência · IBM</title></svelte:head>
<main>
  <h1>Evidência</h1>
  <StatusBadge value={data.evidence.documentary_state} />
  <dl>
    <dt>Documento</dt><dd><a href={`/documentos/${data.document?.id}`}>{data.document?.title}</a></dd>
    <dt>Página</dt><dd>{data.evidence.page ?? 'Não especificada'}</dd>
    <dt>Seção</dt><dd>{data.evidence.section ?? 'Não especificada'}</dd>
    <dt>Célula/intervalo</dt><dd>{data.evidence.cell_range ?? 'Não aplicável'}</dd>
    <dt>Trecho normalizado</dt><dd>{data.evidence.normalized_excerpt ?? 'Não transcrito neste registro'}</dd>
    <dt>Aplicabilidade</dt><dd>{data.evidence.applicability_note}</dd>
  </dl>
  <p class="meta">{data.evidence.notes}</p>
  <p>{data.links.length} vínculo(s) de proveniência usam esta evidência.</p>
</main>
