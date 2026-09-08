<script lang="ts">
  import { byId, model } from '$lib/data';
  import FixtureNotice from '$lib/components/FixtureNotice.svelte';
  import StatusBadge from '$lib/components/StatusBadge.svelte';
</script>

<svelte:head><title>Conteúdos · IBM</title></svelte:head>
<main>
  <h1>Conteúdos</h1>
  <p class="lede">Camada analítica separada dos registros factuais. O W032 não produz taxonomia substantiva nem linhagem curricular.</p>
  <FixtureNotice />
  <div class="grid">
    {#each model.analytical.content_topics as topic}
      {@const domain = byId(model.analytical.content_domains, topic.domain_id)}
      <article class="card">
        <h2><a href={`/conteudos/${topic.id}`}>{topic.label}</a></h2>
        <p>{domain?.label}</p>
        <StatusBadge value={topic.review_state} />
      </article>
    {/each}
  </div>
</main>
