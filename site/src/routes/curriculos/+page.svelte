<script lang="ts">
  import StatusBadge from '$lib/components/StatusBadge.svelte';
  let { data } = $props();
</script>

<svelte:head><title>Currículos · IBM</title></svelte:head>
<main>
  <h1>Currículos</h1>
  <p class="lede">Versões formais mantidas como unidades históricas distintas.</p>
  <div class="grid">
    {#each data.curricula as curriculum}
      <article class="card">
        <h2><a href={`/curriculos/${curriculum.id}`}>{curriculum.label}</a></h2>
        <p>{curriculum.validity}</p>
        <StatusBadge value={curriculum.documentary_state} />
      </article>
    {/each}
  </div>
</main>
