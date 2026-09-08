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
  <p><a class="map-action" href={`/mapa-curricular?conteudo=${data.topic.id}`}>Seguir este conteúdo no mapa 2011→2023</a></p>
  <dl><dt>Domínio</dt><dd>{data.domain?.label}</dd><dt>Aliases</dt><dd>{data.topic.aliases.join(', ') || 'Nenhum registrado'}</dd><dt>Proveniência da identificação</dt><dd>{data.topic.identification_provenance}</dd></dl>
  <h2>Ocorrências em disciplinas</h2>
  {#if data.occurrences.length}
    <div class="comparison">
      {#each ['curriculum-2011', 'curriculum-2023'] as curriculumId}
        <section><h3>{curriculumId === 'curriculum-2011' ? '2011' : '2023'}</h3>
          {#each data.occurrences.filter((item: any) => item.component?.curriculum_id === curriculumId) as occurrence}
            <article class="card">
              <h4><a href={`/disciplinas/${occurrence.component?.id}`}>{occurrence.component?.code} · {occurrence.component?.name}</a></h4>
              <StatusBadge value={occurrence.review_state} /> <StatusBadge value={occurrence.evidence_strength} />
              <blockquote>{occurrence.evidence_text}</blockquote><p class="meta">{occurrence.locator}</p><p>{occurrence.notes}</p><p><strong>Aplicabilidade:</strong> {occurrence.evidence[0]?.applicability ?? 'Não especificada'}</p><EvidenceList items={occurrence.evidence} />
            </article>
          {/each}
          {#if !data.occurrences.some((item: any) => item.component?.curriculum_id === curriculumId)}<p class="missing">Nenhuma ocorrência localizada neste corpus. Isso não prova ausência histórica.</p>{/if}
        </section>
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
  .map-action { display: inline-block; padding: .55rem .75rem; border: 1px solid var(--ink); background: var(--red); color: white; font-weight: 900; text-decoration: none; }
  .comparison { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem; }
  .comparison > section > h3 { padding-bottom: .3rem; border-bottom: 2px solid var(--ink); font: 900 2rem var(--display); }
  .comparison .card + .card { margin-top: .8rem; }
  .comparison h4 { margin: 0 0 .5rem; }
  blockquote { margin: 1rem 0; padding-left: 1rem; border-left: .2rem solid #8ca696; }
  .relations { padding-left: 1.2rem; }
  .relations li + li { margin-top: 1rem; }
  .missing { padding: .8rem; border: 1px dashed var(--line); color: var(--ink-soft); background: var(--surface); }
  @media (max-width: 700px) { .comparison { grid-template-columns: 1fr; } }
</style>
