<script lang="ts">
  let { children } = $props();
</script>

<a class="skip-link" href="#conteudo-principal">Pular para o conteúdo</a>
<header class="site-header">
  <a class="brand" href="/" aria-label="Início — Informática Biomédica em revisão">
    <span class="brand-mark" aria-hidden="true">IBM</span>
    <span><strong>currículo em exame</strong><small>arquivo · análise · intervenção</small></span>
  </a>
  <nav aria-label="Navegação principal">
    <a href="/mapa-curricular">Mapa 2011→2023</a>
    <a href="/curriculos">Currículos</a>
    <a href="/conteudos">Conteúdos</a>
    <a href="/metodologia">Método</a>
  </nav>
</header>

<div id="conteudo-principal">{@render children()}</div>

<footer>
  <p class="footer-principle">O site protesta; os dados depõem.</p>
  <p>Revisão curricular documentada · estados analíticos permanecem explícitos · W034</p>
</footer>

<style>
  :global(:root) {
    --paper: #f3efe5; --surface: #fffdf7; --ink: #181716; --ink-soft: #5c5750;
    --line: #918b80; --line-soft: #d8d1c4; --red: #c5242b; --red-dark: #86171d;
    --red-soft: #f9e5e3; --amber: #a66b00; --amber-soft: #fff2ce; --green: #3d7251;
    --green-dark: #214b32; --green-soft: #e5f0e8; --highlight: #ffe66a80;
    --highlight-strong: #d8b900; --link: #7c1820;
    --display: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
    --sans: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --serif: Georgia, 'Times New Roman', serif; --mono: 'SFMono-Regular', Consolas, 'Liberation Mono', monospace;
    --focus: 3px solid #1262d2;
  }
  :global(*) { box-sizing: border-box; }
  :global(html) { scroll-behavior: smooth; }
  :global(body) { margin: 0; color: var(--ink); background: var(--paper); font-family: var(--sans); line-height: 1.55; }
  :global(body::before) { position: fixed; z-index: -1; inset: 0; content: ''; pointer-events: none; opacity: .25; background-image: repeating-linear-gradient(0deg, transparent 0 31px, #7c746613 31px 32px); }
  :global(a) { color: var(--link); text-underline-offset: .17em; text-decoration-thickness: .08em; }
  :global(a:hover) { text-decoration-thickness: .14em; }
  :global(a:focus-visible), :global(button:focus-visible), :global(select:focus-visible), :global(input:focus-visible), :global(summary:focus-visible) { outline: var(--focus); outline-offset: 3px; }
  :global(main) { width: min(76rem, calc(100% - 2rem)); margin: 0 auto; padding: clamp(2rem, 5vw, 4rem) 0 5rem; }
  :global(h1), :global(h2), :global(h3) { text-wrap: balance; }
  :global(h1) { margin: 0 0 .75rem; font-family: var(--display); line-height: .98; letter-spacing: -.025em; }
  :global(h2) { margin-top: 2rem; line-height: 1.15; }
  :global(.lede) { max-width: 52rem; color: var(--ink-soft); font-family: var(--serif); font-size: 1.08rem; }
  :global(.grid) { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(17rem, 100%), 1fr)); gap: 1rem; margin-top: 1.5rem; }
  :global(.card) { padding: 1rem; border: 1px solid var(--line); background: var(--surface); }
  :global(.card h2), :global(.card h3) { margin: 0 0 .4rem; }
  :global(.meta) { margin: .25rem 0; color: var(--ink-soft); }
  :global(dl) { display: grid; grid-template-columns: minmax(8rem, 12rem) 1fr; gap: .55rem 1rem; }
  :global(dt) { font-weight: 800; }
  :global(dd) { margin: 0; overflow-wrap: anywhere; }
  :global(code) { font-family: var(--mono); font-size: .88em; overflow-wrap: anywhere; }
  :global(.eyebrow) { color: var(--red-dark); font-size: .76rem; font-weight: 900; letter-spacing: .12em; text-transform: uppercase; }
  .skip-link { position: fixed; z-index: 100; top: .5rem; left: .5rem; padding: .7rem 1rem; background: var(--ink); color: white; transform: translateY(-160%); }
  .skip-link:focus { transform: translateY(0); }
  .site-header { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 1rem 2rem; padding: .85rem max(1rem, calc((100% - 76rem) / 2)); border-bottom: 2px solid var(--ink); background: var(--surface); }
  .brand { display: flex; align-items: center; gap: .65rem; color: var(--ink); text-decoration: none; }
  .brand-mark { display: grid; place-items: center; width: 3.1rem; aspect-ratio: 1; border: 2px solid var(--red); color: var(--red); font-family: var(--display); font-size: 1.25rem; transform: rotate(-2deg); }
  .brand strong, .brand small { display: block; }
  .brand strong { font: 900 .86rem/1 var(--sans); text-transform: uppercase; letter-spacing: .07em; }
  .brand small { margin-top: .25rem; color: var(--ink-soft); font-size: .64rem; letter-spacing: .04em; }
  nav { display: flex; flex-wrap: wrap; gap: .35rem 1rem; }
  nav a { color: var(--ink); font-size: .79rem; font-weight: 800; }
  nav a:first-child { color: var(--red-dark); }
  footer { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 1rem; padding: 1.5rem max(1rem, calc((100% - 76rem) / 2)); border-top: 2px solid var(--ink); background: var(--surface); color: var(--ink-soft); font-size: .78rem; }
  footer p { margin: 0; }
  .footer-principle { color: var(--red-dark); font-family: var(--serif); font-weight: 700; font-style: italic; }
  @media (max-width: 680px) {
    .site-header { align-items: flex-start; }
    nav { width: 100%; display: grid; grid-template-columns: repeat(2, 1fr); border-top: 1px solid var(--line-soft); padding-top: .65rem; }
    nav a { min-height: 2.2rem; display: flex; align-items: center; }
    :global(dl) { grid-template-columns: 1fr; gap: .1rem; }
    :global(dd) { margin-bottom: .75rem; }
  }
  @media (prefers-reduced-motion: reduce) { :global(html) { scroll-behavior: auto; } }
</style>
