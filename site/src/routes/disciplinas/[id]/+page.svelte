<script lang="ts">
  import { byId, model } from '$lib/data';
  import EvidenceList from '$lib/components/EvidenceList.svelte';
  import StatusBadge from '$lib/components/StatusBadge.svelte';
  let { data } = $props();
</script>

<svelte:head><title>{data.component.code} · IBM</title></svelte:head>
<main>
  <p><a href={`/curriculos/${data.curriculum?.id}`}>← {data.curriculum?.label}</a></p>
  <h1>{data.component.code || 'Espaço optativo'} · {data.component.name}</h1>
  <StatusBadge value={data.component.evidence_state} />
  <dl>
    <dt>Período recomendado</dt><dd>{data.component.recommended_period ?? 'Não informado'}</dd>
    <dt>Carga horária</dt><dd>{data.component.workload_hours ?? 'Não informada'} h</dd>
    <dt>Natureza</dt><dd>{data.component.nature}</dd>
  </dl>
  {#if data.component.notes}<p class="meta">{data.component.notes}</p>{/if}
  <h2>Tópicos associados</h2>
  {#if data.occurrences.length}
    <ul>{#each data.occurrences as occurrence}{@const topic = byId(model.analytical.content_topics, occurrence.topic_id)}<li><a href={`/conteudos/${topic?.id}`}>{topic?.label}</a> <StatusBadge value={occurrence.review_state} /></li>{/each}</ul>
  {:else}<p class="meta">Nenhuma ocorrência analítica foi classificada no W032.</p>{/if}
  <h2>Dependências</h2>
  {#if data.dependencies.length}<ul>{#each data.dependencies as dependency}<li>{dependency.requirement_text}</li>{/each}</ul>{:else}<p class="meta">Nenhuma dependência registrada.</p>{/if}
  <h2>Evidências</h2>
  <EvidenceList ids={data.component.evidence_ids} />
</main>
