<script lang="ts">
  import StatusBadge from './StatusBadge.svelte';
</script>

<details class="legend">
  <summary>Como ler o mapa</summary>
  <div class="legend-grid">
    <section>
      <h3>Tipo de mudança</h3>
      <p><span class="line maintained"></span> Mantido</p>
      <p><span class="line fragmented"></span> Fragmentado / fundido</p>
      <p><span class="line indeterminate"></span> Indeterminado</p>
      <p class="note">O tipo descreve a hipótese; não indica certeza.</p>
    </section>
    <section>
      <h3>Força da evidência</h3>
      <p><span class="weight documented"></span> Documentada</p>
      <p><span class="weight probable"></span> Provável / hipótese</p>
      <p><span class="weight indeterminate"></span> Indeterminada</p>
      <p class="note">Traço e texto sempre acompanham a cor.</p>
    </section>
    <section>
      <h3>Revisão</h3>
      <p><StatusBadge value="proposed" /></p>
      <p><StatusBadge value="reviewed" /></p>
      <p><StatusBadge value="contested" /></p>
      <p class="note">“Proposto” é uma hipótese aberta à inspeção.</p>
    </section>
  </div>
</details>

<style>
  .legend { border: 1px solid var(--line); background: var(--surface); }
  summary { cursor: pointer; padding: .75rem 1rem; font-weight: 800; }
  summary:focus-visible { outline: var(--focus); outline-offset: 2px; }
  .legend-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; padding: 0 1rem 1rem; border-top: 1px solid var(--line-soft); }
  h3 { margin: .8rem 0 .45rem; font: 800 .78rem/1.2 var(--sans); letter-spacing: .06em; text-transform: uppercase; }
  p { margin: .35rem 0; font-size: .8rem; }
  .note { color: var(--ink-soft); }
  .line, .weight { display: inline-block; width: 2.8rem; margin-right: .35rem; vertical-align: middle; border-top: 3px solid var(--ink); }
  .line.fragmented { border-top-style: double; border-color: var(--red); }
  .line.indeterminate, .weight.indeterminate { border-top-style: dashed; opacity: .6; }
  .weight.documented { border-width: 5px; }
  .weight.probable { border-width: 2px; }
  @media (max-width: 700px) { .legend-grid { grid-template-columns: 1fr; } }
</style>
