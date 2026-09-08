<script lang="ts">
  import CoverageBadge from '$lib/components/CoverageBadge.svelte';
  import EvidenceList from '$lib/components/EvidenceList.svelte';
  import StatusBadge from '$lib/components/StatusBadge.svelte';
  let { data } = $props();
</script>

<svelte:head><title>{data.component.code} · IBM</title></svelte:head>
<main>
  <p class="breadcrumb"><a href={`/curriculos/${data.curriculum?.id}`}>← {data.curriculum?.label}</a></p>
  <header class="record-header">
    <p class="eyebrow">Componente curricular · camada factual</p>
    <h1>{data.component.code || 'Espaço optativo'} <span>{data.component.name}</span></h1>
    <CoverageBadge {...data.coverage} /> <StatusBadge value={data.component.evidence_state} />
    <p>{data.coverage.detail}</p>
    <a class="map-action" href={`/mapa-curricular?disciplina=${data.component.id}`}>Localizar no mapa 2011→2023</a>
  </header>
  <section class="facts">
    <dl>
      <dt>Período recomendado</dt><dd>{data.component.recommended_period ?? 'Não informado'}</dd>
      <dt>Carga horária</dt><dd>{data.component.workload_hours ?? 'Não informada'} h</dd>
      <dt>Natureza</dt><dd>{data.component.nature}</dd>
      <dt>Limitação documental</dt><dd>{data.component.notes || 'Nenhuma nota adicional registrada.'}</dd>
    </dl>
  </section>
  <div class="two-column">
    <section><h2>Conteúdos propostos</h2>{#if data.occurrences.length}<ul class="occurrences">{#each data.occurrences as occurrence}<li><div><a href={`/conteudos/${occurrence.topic?.id}`}>{occurrence.topic?.label}</a> <StatusBadge value={occurrence.review_state} /> <StatusBadge value={occurrence.evidence_strength} /></div><blockquote>{occurrence.evidence_text}</blockquote><p class="meta">{occurrence.locator}</p><EvidenceList items={occurrence.evidence} compact /></li>{/each}</ul>{:else}<p class="gap">Nenhuma ocorrência analítica foi proposta no corpus utilizável. Isso não prova ausência de conteúdo.</p>{/if}</section>
    <section><h2>Possíveis destinos ou origens</h2>{#if data.relatedComponents.length}<div class="related">{#each data.relatedComponents as item}<article><h3><a href={`/disciplinas/${item.id}`}>{item.code} · {item.name}</a></h3><p>{item.curriculum?.label} · {item.workload_hours ?? '—'} h</p><CoverageBadge {...item.coverage} /></article>{/each}</div>{:else}<p class="gap">Nenhuma contraparte está ligada por candidato de linhagem. Ausência de candidato não significa remoção.</p>{/if}</section>
  </div>
  <section><h2>Candidatos de continuidade</h2>{#if data.relations.length}<div class="relations">{#each data.relations as relation}<article><strong>{relation.change_type}</strong> <StatusBadge value={relation.review_state} /> <StatusBadge value={relation.evidence_strength} /><p>{relation.notes}</p><EvidenceList items={relation.evidence} compact /></article>{/each}</div>{:else}<p class="gap">Nenhum candidato registrado.</p>{/if}</section>
  <section><h2>Pré-requisitos e condições</h2>{#if data.dependencies.length}<ul>{#each data.dependencies as dependency}<li>{dependency.requirement_text} <StatusBadge value={dependency.documentary_state} /></li>{/each}</ul>{:else}<p class="gap">Nenhuma dependência registrada.</p>{/if}</section>
  <section><h2>Ver evidências</h2><EvidenceList items={data.evidence} /></section>
</main>

<style>
  .breadcrumb { margin-top: 0; }
  .record-header { padding: clamp(1.2rem, 4vw, 2.5rem); border: 2px solid var(--ink); background: var(--surface); box-shadow: 6px 6px 0 var(--red); }
  .record-header h1 { max-width: 20ch; font-size: clamp(2.5rem, 7vw, 5.5rem); }
  .record-header h1 span { display: block; margin-top: .4rem; font: 800 clamp(1.2rem, 3vw, 2rem)/1.1 var(--sans); letter-spacing: 0; }
  .map-action { display: inline-block; margin-top: .6rem; font-weight: 900; }
  .facts { max-width: 56rem; margin: 2.5rem 0; padding: 1rem; border-left: .35rem solid var(--ink); background: var(--surface); }
  .two-column { display: grid; grid-template-columns: 1.25fr .75fr; gap: 2rem; }
  section h2 { font: 900 1.45rem var(--display); text-transform: uppercase; }
  .occurrences { padding-left: 1.2rem; }
  .occurrences li + li { margin-top: 1.2rem; }
  blockquote { margin: .5rem 0; padding-left: .75rem; border-left: 3px solid var(--highlight-strong); }
  .related, .relations { display: grid; gap: .7rem; }
  .related article, .relations article { padding: .8rem; border: 1px solid var(--line); background: var(--surface); }
  .related h3 { margin: 0; font-size: .95rem; }
  .related p { margin: .35rem 0; color: var(--ink-soft); font-size: .85rem; }
  .gap { padding: .8rem; border: 1px dashed var(--line); background: var(--surface); color: var(--ink-soft); }
  @media (max-width: 760px) { .two-column { grid-template-columns: 1fr; } .record-header { box-shadow: 4px 4px 0 var(--red); } }
</style>
