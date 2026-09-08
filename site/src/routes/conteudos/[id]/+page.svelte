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
  {#if data.occurrences.length}
    <div class="grid">
      {#each data.occurrences as occurrence}
        <article class="card">
          <h3><a href={`/disciplinas/${occurrence.component?.id}`}>{occurrence.component?.code} · {occurrence.component?.name}</a></h3>
          <p class="meta">{occurrence.curriculum?.label}</p>
          <StatusBadge value={occurrence.review_state} /> <StatusBadge value={occurrence.evidence_strength} />
          <blockquote>{occurrence.evidence_text}</blockquote>
          <p class="meta">{occurrence.locator}</p>
          <p>{occurrence.notes}</p>
          <EvidenceList items={occurrence.evidence} />
        </article>
      {/each}
    </div>
  {:else}<p class="meta">Nenhuma ocorrência classificada.</p>{/if}
  <h2>Relações de evolução</h2>
  {#if data.relations.length}
    <ul class="relations">
      {#each data.relations as relation}
        <li><strong>{relation.change_type}</strong> · <StatusBadge value={relation.review_state} /> <StatusBadge value={relation.evidence_strength} /><p>{relation.notes}</p><p class="meta">Método: {relation.candidate_method}. {relation.analysis_provenance}</p><EvidenceList items={relation.evidence} /></li>
      {/each}
    </ul>
  {:else}<p class="meta">Nenhuma relação inferida.</p>{/if}
  <h2>Evidências</h2><EvidenceList items={data.evidence} />
</main>

<style>
  blockquote { margin: 1rem 0; padding-left: 1rem; border-left: .2rem solid #8ca696; }
  .relations { padding-left: 1.2rem; }
  .relations li + li { margin-top: 1rem; }
</style>
