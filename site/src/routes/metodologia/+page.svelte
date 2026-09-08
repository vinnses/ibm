<script lang="ts">let { data } = $props();</script>

<svelte:head><title>Método e evidência · IBM</title></svelte:head>
<main>
  <p class="eyebrow">Como ler sem extrapolar</p>
  <h1>Método e evidência</h1>
  <p class="lede">O projeto separa documento, extração e análise. Uma proposta de continuidade não é uma equivalência formal; uma fonte localizada não é automaticamente aplicável a um currículo.</p>
  <section class="method-grid">
    <article><span>01</span><h2>Documento</h2><p>{data.document_count} registros preservados no modelo público, com URL, caminho, hash e estado documental.</p></article>
    <article><span>02</span><h2>Extração</h2><p>{data.evidence_count} registros de evidência ligam página, seção ou trecho às entidades que sustentam.</p></article>
    <article><span>03</span><h2>Análise</h2><p>Domínios, tópicos, ocorrências e linhagens mantêm estado de revisão e força de evidência próprios.</p></article>
  </section>
  <section>
    <h2>Três códigos, três perguntas</h2>
    <dl>
      <dt>Tipo de mudança</dt><dd>O que a hipótese descreve: mantido, movido, fragmentado, fundido, novo ou indeterminado.</dd>
      <dt>Força da evidência</dt><dd>Quanto o registro sustenta: documentado, fortemente sustentado, provável, hipótese ou indeterminado.</dd>
      <dt>Estado de revisão</dt><dd>Onde está no processo: proposto, revisado, contestado ou indeterminado.</dd>
    </dl>
  </section>
  <section class="warning"><h2>Ausência não é remoção</h2><p>“Documento não localizado” registra o limite de uma busca pública. “Aplicabilidade indeterminada” registra uma versão existente que não pode ser atribuída silenciosamente à unidade histórica.</p></section>
  <section><h2>Amostras de evidência</h2><ul>{#each data.sample_evidence as item}<li><a href={`/evidencias/${item.id}`}>Ver evidência {item.id}</a>{#if item.excerpt}<p>{item.excerpt}</p>{/if}</li>{/each}</ul></section>
  <p><a class="action" href="/mapa-curricular">Aplicar esse método no mapa</a></p>
</main>

<style>
  h1 { max-width: 12ch; font-size: clamp(3rem, 8vw, 6rem); text-transform: uppercase; }
  .method-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 3rem 0; }
  .method-grid article { padding: 1rem; border-top: 4px solid var(--ink); background: var(--surface); }
  .method-grid span { color: var(--red); font: 900 .8rem var(--mono); }
  .method-grid h2 { margin: .5rem 0; font: 900 2rem var(--display); text-transform: uppercase; }
  section:not(.method-grid) { max-width: 58rem; margin-top: 3rem; }
  .warning { padding: 1.2rem; border: 2px dashed var(--red); background: var(--red-soft); }
  li + li { margin-top: .8rem; }
  li p { margin: .2rem 0; color: var(--ink-soft); }
  .action { display: inline-block; padding: .7rem 1rem; border: 2px solid var(--ink); background: var(--red); color: white; font-weight: 900; text-decoration: none; }
  @media (max-width: 700px) { .method-grid { grid-template-columns: 1fr; } }
</style>
