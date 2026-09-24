<svelte:head>
  <title>Grades curriculares · Informática Biomédica UFPR</title>
  <meta name="description" content="Escolha uma das grades curriculares de Informática Biomédica da UFPR para consultar disciplinas, fichas e documentos formais." />
  <meta property="og:title" content="Grades curriculares · Informática Biomédica UFPR" />
  <meta property="og:description" content="Consulte as grades de 2011 e 2023, suas disciplinas, fichas e documentos formais." />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Dados, Documentos e Análises sobre IBM/UFPR" />
  <meta property="og:locale" content="pt_BR" />
  <meta property="og:url" content="https://ibm.tail6629d6.ts.net/curriculos" />
</svelte:head>

<main class="grades">
  <p class="eyebrow">Informática Biomédica · UFPR</p>
  <h1>Grades curriculares</h1>
  <p class="lead">Escolha um currículo para consultar as disciplinas por período, as Fichas 1 disponíveis e os documentos que definem a grade.</p>
  <div class="options">
    <a href="/curriculos/curriculum-2011"><span>Currículo</span><strong>2011</strong><p>Consulte a grade histórica e suas fontes formais.</p><em>Explorar grade ↗</em></a>
    <a href="/curriculos/curriculum-2023"><span>Currículo</span><strong>2023</strong><p>Consulte a grade mais recente documentada no acervo e suas fontes formais.</p><em>Explorar grade ↗</em></a>
  </div>
</main>

<style>
  .grades{max-width:980px}.eyebrow{margin:0 0 .45rem;color:var(--green);font-size:.75rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase}h1{margin:0;font-size:clamp(2.3rem,5vw,3.8rem)}.lead{max-width:700px;color:var(--muted)}.options{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem;margin-top:2rem}.options a{display:flex;flex-direction:column;min-height:235px;padding:1.5rem;border:1px solid var(--line);border-radius:14px;background:var(--surface);color:var(--ink);text-decoration:none}.options a:hover{border-color:var(--green);background:var(--soft)}.options span{color:var(--muted);font-size:.76rem;text-transform:uppercase;letter-spacing:.08em}.options strong{margin:.25rem 0;font-family:Georgia,"Times New Roman",serif;font-size:2.8rem;line-height:1.1}.options p{margin:.5rem 0 1rem;color:var(--muted);font-size:.88rem}.options em{margin-top:auto;color:var(--green-dark);font-size:.83rem;font-style:normal;font-weight:750}@media(max-width:660px){.options{grid-template-columns:1fr}.options a{min-height:0}}
</style>
