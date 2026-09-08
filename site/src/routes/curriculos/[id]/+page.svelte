<script lang="ts">
  import EvidenceList from '$lib/components/EvidenceList.svelte';
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
  <h2>Evidências formais</h2>
  <EvidenceList ids={data.curriculum.evidence_ids} />
  <h2>Disciplinas e componentes</h2>
  <div class="grid">
    {#each data.components as component}
      <article class="card">
        <h3><a href={`/disciplinas/${component.id}`}>{component.code || 'Espaço optativo'} · {component.name}</a></h3>
        <p class="meta">Período {component.recommended_period ?? 'não informado'} · {component.workload_hours ?? '—'} h</p>
        <StatusBadge value={component.evidence_state} />
      </article>
    {/each}
  </div>
</main>
