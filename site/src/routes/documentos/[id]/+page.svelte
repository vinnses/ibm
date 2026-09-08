<script lang="ts">
  import StatusBadge from '$lib/components/StatusBadge.svelte';
  let { data } = $props();
</script>

<svelte:head><title>{data.document.title} · IBM</title></svelte:head>
<main>
  <h1>{data.document.title}</h1>
  <StatusBadge value={data.document.documentary_state} />
  <dl>
    <dt>Instituição</dt><dd>{data.document.institution}</dd>
    <dt>Tipo</dt><dd>{data.document.document_type}</dd>
    <dt>Data/versão</dt><dd>{data.document.document_date}</dd>
    <dt>Aplicabilidade</dt><dd><StatusBadge value={data.document.applicability_status} /> {data.document.applicability_note}</dd>
    <dt>Origem</dt><dd><a href={data.document.original_url} rel="noreferrer">URL original</a></dd>
    <dt>Caminho preservado</dt><dd><code>{data.document.repository_path}</code></dd>
    <dt>SHA-256</dt><dd><code>{data.document.sha256}</code></dd>
  </dl>
  <p><a href={data.document.public_path} target="_blank">Abrir cópia preservada</a></p>
  <h2>Evidências vinculadas</h2>
  <ul>{#each data.evidence as evidence}<li><a href={`/evidencias/${evidence.id}`}>{evidence.id}</a>{#if evidence.section} · {evidence.section}{/if}</li>{/each}</ul>
</main>
