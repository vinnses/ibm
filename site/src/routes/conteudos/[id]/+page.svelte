<script lang="ts">
  import EvidenceList from '$lib/components/EvidenceList.svelte';
  import FixtureNotice from '$lib/components/FixtureNotice.svelte';
  import StatusBadge from '$lib/components/StatusBadge.svelte';
  let { data } = $props();
</script>

<svelte:head><title>{data.topic.label} · IBM</title></svelte:head>
<main>
  <p><a href="/conteudos">← Conteúdos</a></p>
  <h1>{data.topic.label}</h1>
  {#if data.topic.is_fixture}<FixtureNotice />{/if}
  <StatusBadge value={data.topic.review_state} />
  <p>{data.topic.description}</p>
  <dl><dt>Domínio</dt><dd>{data.domain?.label}</dd><dt>Proveniência da identificação</dt><dd>{data.topic.identification_provenance}</dd></dl>
  <h2>Ocorrências em disciplinas</h2>
  <p class="meta">{data.occurrences.length ? `${data.occurrences.length} ocorrência(s).` : 'Nenhuma ocorrência classificada.'}</p>
  <h2>Relações de evolução</h2>
  <p class="meta">{data.relations.length ? `${data.relations.length} relação(ões).` : 'Nenhuma relação inferida.'}</p>
  <h2>Evidências</h2><EvidenceList ids={data.topic.evidence_ids} />
</main>
