<svelte:head>
  <title>Informática Biomédica — UFPR</title>
  <meta
    name="description"
    content="Infraestrutura de consulta e revisão curricular da Informática Biomédica da UFPR."
  />
</svelte:head>

<main>
  <section aria-labelledby="project-title" class="card">
    <p class="eyebrow">Infraestrutura de revisão</p>
    <h1 id="project-title">Informática Biomédica — UFPR</h1>
    <p class="lede">Consulte currículos e disciplinas como fatos documentais separados da camada analítica de conteúdos. Tópicos propostos permanecem visíveis com seu estado explícito.</p>
    <p><a href="/curriculos">Abrir currículos</a> · <a href="/conteudos">Abrir conteúdos</a></p>
  </section>
</main>

<style>
  section {
    max-width: 48rem;
    padding: clamp(1.5rem, 5vw, 3rem);
  }

  h1 {
    margin: 0.5rem 0 1rem;
    font-size: clamp(2rem, 6vw, 3.75rem);
    line-height: 1.05;
  }

  .eyebrow {
    color: #4b6254;
    font-size: 0.875rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }
</style>
