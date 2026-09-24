<script lang="ts">let { children } = $props();</script>

<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="/" aria-label="Informática Biomédica — início"><span class="brand-icon">IB</span><span class="brand-copy">Informática Biomédica<small>Acervo curricular · UFPR</small></span></a>
    <nav aria-label="Navegação principal"><a href="/">Grades</a><a href="/documentos">Documentos</a><a href="/analises/">Análises</a><a href="/metodologia">Metodologia</a></nav>
  </div>
</header>
<div id="conteudo">{@render children()}</div>
<footer class="site-footer"><div><strong>Informática Biomédica · UFPR</strong><p>Consulta documental independente. Cada dado deve ser lido com sua fonte, versão e limite.</p></div><a href="/metodologia">Como ler as fontes ↗</a></footer>

<style>
  :global(:root){--bg:#f6f6f2;--surface:#fff;--ink:#1a302d;--muted:#586a66;--line:#d9e1dc;--green:#176f5e;--green-dark:#105746;--soft:#edf4f0;--amber:#986522;--amber-soft:#fff7e8;--focus:#1769d2;font-family:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:var(--ink);background:var(--bg)}
  :global(*){box-sizing:border-box}
  :global(body){margin:0;line-height:1.5}
  :global(a){color:var(--green-dark);text-underline-offset:.18em}
  :global(a:focus-visible),:global(button:focus-visible),:global(input:focus-visible),:global(select:focus-visible),:global(summary:focus-visible){outline:3px solid var(--focus);outline-offset:3px}
  :global(main){width:min(1200px,calc(100% - 2rem));margin:0 auto;padding:2rem 0 5rem}
  :global(h1),:global(h2),:global(h3){line-height:1.2;text-wrap:balance}
  :global(h1),:global(h2){font-family:Georgia,"Times New Roman",serif;font-weight:600;letter-spacing:-.025em}
  .skip{position:absolute;z-index:20;top:-5rem;left:1rem;padding:.6rem 1rem;background:var(--ink);color:#fff}.skip:focus{top:1rem}
  .site-header{border-bottom:1px solid var(--line);background:var(--surface)}.header-inner{width:min(1200px,calc(100% - 2rem));min-height:76px;margin:auto;display:flex;align-items:center;justify-content:space-between;gap:2rem}.brand{display:flex;align-items:center;gap:.75rem;color:var(--ink);text-decoration:none}.brand-icon{display:grid;place-items:center;width:42px;height:42px;border:1px solid var(--green-dark);border-radius:4px;color:var(--green-dark);font-family:Georgia,"Times New Roman",serif;font-size:1.35rem;font-weight:700;letter-spacing:-.06em}.brand-copy{font-weight:730;line-height:1.15}.brand-copy small{display:block;margin-top:.25rem;color:var(--muted);font-size:.72rem;font-weight:500;letter-spacing:.02em}nav{display:flex;gap:1.4rem;flex-wrap:wrap}nav a{font-size:.86rem;font-weight:650;text-decoration:none}nav a:hover{text-decoration:underline}
  .site-footer{display:flex;align-items:start;justify-content:space-between;gap:2rem;padding:2rem max(1rem,calc((100% - 1200px)/2));border-top:1px solid var(--line);background:var(--surface);font-size:.84rem}.site-footer p{margin:.35rem 0 0;color:var(--muted)}.site-footer a{white-space:nowrap}
  @media(max-width:700px){.header-inner{align-items:start;flex-direction:column;gap:.7rem;padding:1rem 0}nav{width:100%;gap:.8rem 1.2rem}.site-footer{flex-direction:column}}
</style>
