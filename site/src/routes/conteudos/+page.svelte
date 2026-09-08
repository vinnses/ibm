<script lang="ts">
  import FixtureNotice from '$lib/components/FixtureNotice.svelte';
  import StatusBadge from '$lib/components/StatusBadge.svelte';
  let { data } = $props();

</script>

<svelte:head><title>Conteúdos · IBM</title></svelte:head>
<main>
  <h1>Conteúdos</h1>
  <p class="lede">Primeira taxonomia analítica do W033, separada dos registros factuais e publicada como proposta para revisão.</p>
  <p><a class="map-link" href="/mapa-curricular">Explorar conteúdos no mapa 2011→2023</a></p>
  {#if data.has_fixture}<FixtureNotice />{/if}
  <form method="GET" class="filters">
    <label>Currículo
      <select name="curriculo" value={data.curriculum ?? ''}>
        <option value="">2011 e 2023</option>
        <option value="curriculum-2011">2011</option>
        <option value="curriculum-2023">2023</option>
      </select>
    </label>
    <label>Domínio
      <select name="dominio" value={data.domain ?? ''}>
        <option value="">Todos</option>
        {#each data.domains as domain}<option value={domain.id}>{domain.label}</option>{/each}
      </select>
    </label>
    <button type="submit">Aplicar</button>
  </form>
  <nav class="domains" aria-label="Domínios de conteúdo">
    {#each data.domains as domain}<a href={`/conteudos?dominio=${domain.id}`}>{domain.label}</a>{/each}
  </nav>
  <div class="grid">
    {#each data.topics as topic}
      <article class="card">
        <h2><a href={`/conteudos/${topic.id}`}>{topic.label}</a></h2>
        <p>{topic.domain_label}</p>
        <p class="meta">{topic.occurrence_count} ocorrência(s)</p>
        <StatusBadge value={topic.review_state} />
      </article>
    {/each}
  </div>
  <h2>Candidatos de continuidade</h2>
  <p class="lede">Relações propostas para revisão. Tipo de mudança e força da evidência são campos independentes.</p>
  <div class="grid">
    {#each data.relations as relation}
      <article class="card">
        <h3>{relation.change_type}</h3>
        <StatusBadge value={relation.review_state} /> <StatusBadge value={relation.evidence_strength} />
        <p>{relation.notes}</p>
        {#if relation.topic_id}<a href={`/conteudos/${relation.topic_id}`}>Inspecionar ocorrências e evidências</a>{/if}
      </article>
    {/each}
  </div>
</main>

<style>
  .map-link { display: inline-block; padding: .55rem .75rem; border: 1px solid var(--ink); background: var(--red); color: white; font-weight: 900; text-decoration: none; }
  .filters { display: flex; flex-wrap: wrap; align-items: end; gap: 1rem; margin: 1.5rem 0; padding: 1rem; background: white; border: 1px solid #cbd4cc; }
  label { display: grid; gap: .25rem; font-weight: 700; }
  select, button { min-height: 2.4rem; padding: .35rem .55rem; font: inherit; }
  .domains { display: flex; flex-wrap: wrap; gap: .5rem 1rem; }
</style>
