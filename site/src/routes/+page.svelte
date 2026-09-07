<svelte:head>
  <title>Informática Biomédica — UFPR</title>
  <meta
    name="description"
    content="Infraestrutura inicial do site do projeto Informática Biomédica da UFPR."
  />
</svelte:head>

<main>
  <section aria-labelledby="project-title">
    <p>Infraestrutura inicial do projeto</p>
    <h1 id="project-title">Informática Biomédica — UFPR</h1>
    <p>Esta página comprova a execução da aplicação SvelteKit.</p>
  </section>
</main>

<style>
  :global(*) {
    box-sizing: border-box;
  }

  :global(body) {
    margin: 0;
    color: #17211b;
    background: #f4f6f2;
    font-family: system-ui, sans-serif;
  }

  main {
    min-height: 100vh;
    display: grid;
    place-items: center;
    padding: 2rem;
  }

  section {
    width: min(42rem, 100%);
    padding: clamp(2rem, 6vw, 4rem);
    border: 1px solid #cbd4cc;
    background: #ffffff;
  }

  h1 {
    margin: 0.5rem 0 1rem;
    font-size: clamp(2rem, 6vw, 3.75rem);
    line-height: 1.05;
  }

  p {
    margin: 0;
    line-height: 1.6;
  }

  section > p:first-child {
    color: #4b6254;
    font-size: 0.875rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }
</style>

