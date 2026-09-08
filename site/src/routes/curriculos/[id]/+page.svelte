<script lang="ts">
  import EvidenceList from '$lib/components/EvidenceList.svelte';
  import CoverageBadge from '$lib/components/CoverageBadge.svelte';
  import StatusBadge from '$lib/components/StatusBadge.svelte';
  let { data } = $props();
</script>

<svelte:head><title>{data.curriculum.label} · IBM</title></svelte:head>
<main>
  <p><a href="/curriculos">← Currículos</a></p>
  <h1>{data.curriculum.label}</h1>
  <StatusBadge value={data.curriculum.documentary_state} />
  <p>{data.curriculum.validity}</p>
  <p class="meta">{data.curriculum.notes}</p>
  <p><a class="map-link" href="/mapa-curricular">Comparar no mapa 2011→2023</a></p>
  <h2>Evidências formais</h2>
  <EvidenceList items={data.evidence} />
  <h2>Disciplinas e componentes</h2>
  <div class="grid">
    {#each data.components as component}
      <article class="card">
        <h3><a href={`/disciplinas/${component.id}`}>{component.code || 'Espaço optativo'} · {component.name}</a></h3>
        <p class="meta">Período {component.recommended_period ?? 'não informado'} · {component.workload_hours ?? '—'} h</p>
        <StatusBadge value={component.evidence_state} /> <CoverageBadge {...component.coverage} />
      </article>
    {/each}
  </div>
</main>

<style>.map-link { display: inline-block; padding: .5rem .7rem; border: 1px solid var(--ink); background: var(--red); color: white; font-weight: 900; text-decoration: none; }</style>
