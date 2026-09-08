<script lang="ts">
  let { children } = $props();
</script>

<header>
  <a class="brand" href="/">IBM · revisão curricular</a>
  <nav aria-label="Navegação principal">
    <a href="/curriculos">Currículos</a>
    <a href="/conteudos">Conteúdos</a>
  </nav>
</header>

{@render children()}

<footer>Infraestrutura de inspeção documental — W032</footer>

<style>
  :global(*) { box-sizing: border-box; }
  :global(body) { margin: 0; color: #17211b; background: #f4f6f2; font-family: system-ui, sans-serif; line-height: 1.55; }
  :global(a) { color: #175a39; text-underline-offset: .15em; }
  :global(main) { width: min(72rem, calc(100% - 2rem)); margin: 0 auto; padding: 2.5rem 0 4rem; }
  :global(h1) { margin: 0 0 .75rem; line-height: 1.12; }
  :global(h2) { margin-top: 2rem; }
  :global(.lede) { max-width: 48rem; color: #445249; }
  :global(.grid) { display: grid; grid-template-columns: repeat(auto-fit, minmax(17rem, 1fr)); gap: 1rem; margin-top: 1.5rem; }
  :global(.card) { padding: 1rem; border: 1px solid #cbd4cc; background: white; }
  :global(.card h2), :global(.card h3) { margin: 0 0 .4rem; }
  :global(.meta) { margin: .25rem 0; color: #59645d; }
  :global(dl) { display: grid; grid-template-columns: minmax(8rem, 12rem) 1fr; gap: .55rem 1rem; }
  :global(dt) { font-weight: 700; }
  :global(dd) { margin: 0; overflow-wrap: anywhere; }
  header { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 1rem; padding: 1rem max(1rem, calc((100% - 72rem) / 2)); border-bottom: 1px solid #cbd4cc; background: white; }
  .brand { font-weight: 800; text-decoration: none; }
  nav { display: flex; gap: 1rem; }
  footer { padding: 1.2rem max(1rem, calc((100% - 72rem) / 2)); border-top: 1px solid #cbd4cc; color: #59645d; }
  @media (max-width: 520px) { :global(dl) { grid-template-columns: 1fr; gap: .1rem; } :global(dd) { margin-bottom: .75rem; } }
</style>
