<script lang="ts">let { data } = $props();</script>
<svelte:head>
  <title>Fontes e limites · Informática Biomédica UFPR</title>
  <meta name="description" content="Entenda as fontes, versões e limites documentais usados para apresentar as grades de Informática Biomédica da UFPR." />
  <meta property="og:title" content="Fontes e limites · Informática Biomédica UFPR" />
  <meta property="og:description" content="Como interpretar as fontes, versões e relações entre as grades curriculares de Informática Biomédica da UFPR." />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Informática Biomédica · UFPR" />
  <meta property="og:locale" content="pt_BR" />
</svelte:head>
<main class="about"><p class="eyebrow">Como ler este site</p><h1>Fontes e limites</h1><p class="lead">As disciplinas e a distribuição por período vêm dos documentos formais de cada currículo. As Fichas 1 exibidas são versões públicas localizadas; nem toda versão tem aplicação à grade comprovada.</p>
  <section><h2>Grades e Fichas 1</h2><p>A Ficha 1 registra os elementos permanentes da disciplina. Uma Ficha 2 descreve uma oferta específica e não substitui a Ficha 1. “Não localizada” significa apenas que a busca pública feita até agora não encontrou uma Ficha 1; não afirma inexistência.</p></section>
  <section><h2>Relações entre grades</h2><p>Os cartões mostram apenas pares selecionados por mesmo código ou nome semelhante. Esse recurso serve para navegar entre as grades. Equivalência formal, aproveitamento e continuidade de conteúdo exigem documentação própria e não são presumidos aqui.</p></section>
  <section><h2>Documentos principais</h2><div class="source-grid">{#each data.curricula as curriculum}<div><h3>Currículo {curriculum.year}</h3><ul>{#each curriculum.formalDocuments as document}<li><a href={document.url} target="_blank" rel="noopener">{document.title} ↗</a></li>{/each}</ul></div>{/each}</div></section>
  <p class="closing">Esta é uma consulta documental independente, não uma página institucional da UFPR.</p>
</main>
<style>.about{max-width:900px}.eyebrow{margin:0 0 .5rem;color:var(--green);font-size:.78rem;font-weight:800;text-transform:uppercase;letter-spacing:.1em}h1{margin:0;font-size:clamp(2.3rem,5vw,3.5rem)}.lead{max-width:740px;color:var(--muted);font-size:1.1rem}section{margin-top:2.2rem;padding-top:1.2rem;border-top:1px solid var(--line)}h2{margin:0 0 .5rem;font-size:1.3rem}section p{max-width:740px;color:var(--muted)}.source-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem}.source-grid>div{padding:1rem;border:1px solid var(--line);border-radius:12px;background:var(--surface)}h3{margin:0}.source-grid ul{padding-left:1.2rem}.source-grid li+li{margin-top:.45rem}.closing{margin-top:2rem;color:var(--muted);font-size:.8rem}@media(max-width:600px){.source-grid{grid-template-columns:1fr}}</style>
