<script lang="ts">let { children } = $props();</script>

<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="/" aria-label="Informática Biomédica — início"><span class="brand-icon">ibm<span>.</span></span><span class="brand-copy">Informática Biomédica<small>Grades curriculares · UFPR</small></span></a>
    <nav aria-label="Navegação principal"><a href="/curriculos/curriculum-2011">Grade 2011</a><a href="/curriculos/curriculum-2023">Grade 2023</a><a href="/metodologia">Sobre as fontes</a></nav>
  </div>
</header>
<div id="conteudo">{@render children()}</div>
<footer class="site-footer"><div><strong>Informática Biomédica · UFPR</strong><p>Consulta documental independente. As grades e as Fichas 1 devem ser lidas com a versão e a fonte indicadas.</p></div><a href="/metodologia">Fontes e limites da consulta ↗</a></footer>

<style>
  :global(:root){--bg:#f7f9f7;--surface:#fff;--ink:#17312d;--muted:#58706a;--line:#dce6e1;--green:#117963;--green-dark:#075745;--soft:#eaf5f0;--amber:#986522;--amber-soft:#fff7e8;--focus:#1769d2;font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:var(--ink);background:var(--bg)}
  :global(*){box-sizing:border-box}
  :global(body){margin:0;line-height:1.5}
  :global(a){color:var(--green-dark);text-underline-offset:.18em}
  :global(a:focus-visible),:global(button:focus-visible),:global(input:focus-visible),:global(select:focus-visible),:global(summary:focus-visible){outline:3px solid var(--focus);outline-offset:3px}
  :global(main){width:min(1200px,calc(100% - 2rem));margin:0 auto;padding:2rem 0 5rem}
  :global(h1),:global(h2),:global(h3){line-height:1.2;text-wrap:balance}
  .skip{position:absolute;z-index:20;top:-5rem;left:1rem;padding:.6rem 1rem;background:var(--ink);color:#fff}.skip:focus{top:1rem}
  .site-header{border-bottom:1px solid var(--line);background:var(--surface)}.header-inner{width:min(1200px,calc(100% - 2rem));min-height:76px;margin:auto;display:flex;align-items:center;justify-content:space-between;gap:2rem}.brand{display:flex;align-items:center;gap:.75rem;color:var(--ink);text-decoration:none}.brand-icon{display:grid;place-items:center;width:44px;height:44px;border-radius:12px;background:var(--green-dark);color:#fff;font-size:1.45rem;font-weight:800;letter-spacing:-.09em}.brand-icon span{color:#8fe0bd}.brand-copy{font-weight:760;line-height:1.15}.brand-copy small{display:block;margin-top:.25rem;color:var(--muted);font-size:.72rem;font-weight:500;letter-spacing:.02em}nav{display:flex;gap:1.4rem;flex-wrap:wrap}nav a{font-size:.89rem;font-weight:650;text-decoration:none}nav a:hover{text-decoration:underline}
  .site-footer{display:flex;align-items:start;justify-content:space-between;gap:2rem;padding:2rem max(1rem,calc((100% - 1200px)/2));border-top:1px solid var(--line);background:var(--surface);font-size:.84rem}.site-footer p{margin:.35rem 0 0;color:var(--muted)}.site-footer a{white-space:nowrap}
  @media(max-width:700px){.header-inner{align-items:start;flex-direction:column;gap:.7rem;padding:1rem 0}nav{width:100%;gap:.8rem 1.2rem}.site-footer{flex-direction:column}}
</style>
