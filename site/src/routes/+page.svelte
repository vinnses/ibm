<script lang="ts">let { data } = $props();</script>

<svelte:head>
  <title>Currículo em exame · Informática Biomédica UFPR</title>
  <meta name="description" content="Investigação histórica e documental dos currículos 2011 e 2023 da Informática Biomédica da UFPR." />
</svelte:head>

<main class="home">
  <section class="hero" aria-labelledby="project-title">
    <p class="eyebrow">Arquivo aberto · hipótese à vista</p>
    <h1 id="project-title">O currículo<br /><span>em exame</span></h1>
    <p class="hero-note">O site protesta;<br />os dados depõem.</p>
    <div class="hero-copy">
      <p>Entre 2011 e 2023, o curso de Informática Biomédica foi reorganizado. Esta interface permite seguir disciplinas, conteúdos e documentos sem transformar semelhança em fato.</p>
      <a class="primary-action" href="/mapa-curricular">Explorar 2011 → 2023 <span aria-hidden="true">↗</span></a>
    </div>
    <div class="annotation" aria-hidden="true">comparar nomes não basta</div>
  </section>

  <section class="premise" aria-labelledby="premise-title">
    <div><p class="section-number">01</p><h2 id="premise-title">Investigar antes de concluir</h2></div>
    <p>O mapa começa pelo conteúdo documentado. Cada hipótese de continuidade mantém visíveis seu estado de revisão, sua força de evidência e os limites de aplicabilidade da fonte.</p>
  </section>

  <section class="map-callout" aria-labelledby="map-title">
    <div class="map-poster"><p>2011</p><span aria-hidden="true">→</span><p>2023</p><div class="marked">conteúdo</div></div>
    <div>
      <p class="eyebrow">Visualização principal</p><h2 id="map-title">Onde isso aparece depois?</h2>
      <p>Selecione uma disciplina. Destaque tópicos relacionados, possíveis destinos ou origens, carga horária, pré-requisitos e o documento que sustenta cada ocorrência.</p>
      <ul><li>{data.summary.components} componentes curriculares</li><li>{data.summary.topics} tópicos analíticos propostos</li><li>{data.summary.relations} candidatos de linhagem</li></ul>
      <a class="secondary-action" href="/mapa-curricular">Abrir mapa histórico</a>
    </div>
  </section>

  <section class="gap-callout" aria-labelledby="gaps-title">
    <p class="stamp">Atenção documental</p>
    <div><h2 id="gaps-title">A lacuna também precisa aparecer.</h2><p>{data.summary.gaps} componentes estão marcados com documento de conteúdo não localizado. Outros {data.summary.applicability_indeterminate} têm Ficha preservada cuja aplicabilidade ao currículo permanece indeterminada. Área vazia nunca substitui essa explicação.</p></div>
    <a href="/mapa-curricular">Filtrar lacunas</a>
  </section>

  <section class="entry-grid" aria-label="Entradas para a investigação">
    <a href="/curriculos"><span>02</span><h2>Estruturas formais</h2><p>Veja períodos, cargas e dependências de cada unidade histórica.</p></a>
    <a href="/conteudos"><span>03</span><h2>Conteúdos</h2><p>Siga tópicos sem depender do nome da disciplina.</p></a>
    <a href="/metodologia"><span>04</span><h2>Método e evidência</h2><p>Entenda estados, fontes, preservação e limites.</p></a>
  </section>

  <section class="boundary"><strong>Este estágio não analisa a proposta de 2026.</strong> A interface é uma entrada para a investigação histórica 2011–2023, não um manifesto final.</section>
</main>

<style>
  .home { width: min(76rem, calc(100% - 2rem)); }
  .hero { position: relative; display: grid; grid-template-columns: 1.4fr .8fr; gap: 1rem 3rem; min-height: 34rem; padding: clamp(1.5rem, 5vw, 4rem); border: 2px solid var(--ink); background: var(--surface); overflow: hidden; }
  .hero::before { position: absolute; inset: 0; content: ''; pointer-events: none; background: linear-gradient(112deg, transparent 0 64%, var(--red) 64% 66%, transparent 66%); opacity: .85; }
  .hero .eyebrow { grid-column: 1 / -1; align-self: start; margin: 0; }
  .hero h1 { position: relative; align-self: center; margin: 0; font-size: clamp(4.3rem, 12vw, 9.2rem); text-transform: uppercase; }
  .hero h1 span { display: inline-block; color: var(--red); transform: translateX(clamp(0rem, 5vw, 4rem)); }
  .hero-note { position: relative; align-self: center; margin: 0; color: var(--ink); font: italic 700 clamp(1.25rem, 3vw, 2rem)/1.2 var(--serif); transform: rotate(-2deg); }
  .hero-copy { position: relative; max-width: 38rem; align-self: end; padding-top: 1rem; border-top: 1px solid var(--ink); font-family: var(--serif); font-size: 1.05rem; }
  .primary-action, .secondary-action { display: inline-flex; gap: 1rem; align-items: center; margin-top: .6rem; padding: .75rem 1rem; border: 2px solid var(--ink); background: var(--red); color: white; font-family: var(--sans); font-weight: 900; text-decoration: none; box-shadow: 4px 4px 0 var(--ink); }
  .annotation { position: absolute; right: 3%; bottom: 5%; color: var(--red); font: 900 .72rem var(--mono); text-transform: uppercase; transform: rotate(-4deg); }
  .premise { display: grid; grid-template-columns: 1fr 1.4fr; gap: 2rem; align-items: end; padding: 5rem 0 3rem; border-bottom: 1px solid var(--ink); }
  .section-number { margin: 0; color: var(--red); font: 900 .8rem var(--mono); }
  .premise h2, .map-callout h2, .gap-callout h2, .entry-grid h2 { margin: .25rem 0; font: 900 clamp(2rem, 5vw, 4rem)/.95 var(--display); text-transform: uppercase; }
  .premise > p { margin: 0; max-width: 40rem; font-family: var(--serif); font-size: 1.2rem; }
  .map-callout { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(2rem, 6vw, 5rem); align-items: center; padding: 4rem 0; }
  .map-poster { position: relative; display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; min-height: 24rem; padding: 2rem; border: 2px solid var(--ink); background: var(--ink); color: var(--paper); box-shadow: 10px 10px 0 var(--red); }
  .map-poster p { margin: 0; font: 900 clamp(3rem, 8vw, 6rem) var(--display); }
  .map-poster p:last-of-type { color: var(--red); }
  .map-poster span { font-size: 2rem; }
  .marked { position: absolute; bottom: 2rem; left: 20%; padding: .2rem .6rem; background: #ffdf2d; color: var(--ink); font: 900 1rem var(--mono); transform: rotate(-3deg); }
  .map-callout ul { padding-left: 1.2rem; }
  .secondary-action { background: var(--surface); color: var(--ink); box-shadow: 4px 4px 0 var(--red); }
  .gap-callout { display: grid; grid-template-columns: auto 1fr auto; gap: 1.5rem; align-items: center; padding: 2rem; border: 2px dashed var(--red); background: var(--red-soft); }
  .gap-callout .stamp { padding: .35rem; border: 2px solid var(--red); color: var(--red); font: 900 .75rem var(--sans); text-transform: uppercase; transform: rotate(-2deg); }
  .gap-callout h2 { font-size: clamp(1.7rem, 4vw, 3rem); }
  .entry-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; padding: 4rem 0; }
  .entry-grid > a { min-height: 16rem; padding: 1.2rem; border: 1px solid var(--ink); background: var(--surface); color: var(--ink); text-decoration: none; }
  .entry-grid > a:hover { box-shadow: inset 0 -.6rem 0 var(--highlight); }
  .entry-grid span { color: var(--red); font: 900 .75rem var(--mono); }
  .entry-grid h2 { font-size: clamp(1.6rem, 3vw, 2.5rem); }
  .entry-grid p { color: var(--ink-soft); }
  .boundary { padding: 1rem; border-left: .4rem solid var(--red); background: var(--surface); }
  @media (max-width: 760px) {
    .hero { grid-template-columns: 1fr; min-height: auto; }
    .hero h1 { font-size: clamp(3.6rem, 20vw, 6.5rem); }
    .hero h1 span { transform: none; }
    .hero::before, .annotation { display: none; }
    .premise, .map-callout, .gap-callout, .entry-grid { grid-template-columns: 1fr; }
    .premise { padding-top: 3rem; }
    .map-poster { min-height: 18rem; box-shadow: 5px 5px 0 var(--red); }
    .entry-grid > a { min-height: 11rem; }
  }
</style>
