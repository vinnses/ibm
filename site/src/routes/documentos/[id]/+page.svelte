<script lang="ts">let { data } = $props();</script>
<svelte:head>
  <title>{data.document.title} · Informática Biomédica UFPR</title>
  <meta name="description" content={`Consulte ${data.document.title}, documento público preservado sobre o curso de Informática Biomédica da UFPR.`} />
  <meta property="og:title" content={`${data.document.title} · Informática Biomédica UFPR`} />
  <meta property="og:description" content={`Documento público preservado sobre Informática Biomédica da UFPR: ${data.document.title}.`} />
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="Informática Biomédica · UFPR" />
  <meta property="og:locale" content="pt_BR" />
</svelte:head>

<main class="document-detail">
  <a class="back" href="/documentos">← Todos os documentos</a>
  <header>
    <p class="eyebrow">{data.document.type}</p>
    <h1>{data.document.title}</h1>
    <p class="meta">{data.document.institution}{data.document.date ? ` · ${data.document.date}` : ''}</p>
  </header>
  <div class="document-action"><div><h2>Arquivo preservado</h2><p>Consulte o documento original em PDF.</p></div><a href={data.document.fileUrl} target="_blank" rel="noopener">Abrir documento ↗</a></div>
  {#if !data.document.applicabilityConfirmed}<p class="caution">A relação desta versão com uma grade específica ainda pode exigir confirmação documental.</p>{/if}
</main>

<style>
  .document-detail{max-width:900px}.back{font-size:.85rem;font-weight:700}header{margin:2rem 0}.eyebrow{margin:0 0 .5rem;color:var(--green);font-size:.76rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase}h1{max-width:770px;margin:0;font-size:clamp(2.1rem,5vw,3.6rem);letter-spacing:-.04em}.meta{color:var(--muted)}.document-action{display:flex;align-items:center;justify-content:space-between;gap:1.5rem;padding:1.5rem;border:1px solid var(--line);border-radius:12px;background:var(--surface)}h2{margin:0;font-size:1.1rem}.document-action p{margin:.25rem 0 0;color:var(--muted);font-size:.84rem}.document-action a{flex:none;padding:.7rem 1rem;border-radius:8px;background:var(--green-dark);color:#fff;font-size:.84rem;font-weight:750;text-decoration:none}.document-action a:hover{background:var(--green)}.caution{max-width:730px;margin-top:1.2rem;color:var(--muted);font-size:.82rem}@media(max-width:600px){.document-action{align-items:start;flex-direction:column}}
</style>
