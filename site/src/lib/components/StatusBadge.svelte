<script lang="ts">
  let { value }: { value: string } = $props();

  const labels: Record<string, string> = {
    proposed: 'Proposto — não revisado',
    reviewed: 'Revisado',
    contested: 'Contestado',
    indeterminate: 'Indeterminado',
    documented: 'Documentado',
    strongly_supported: 'Fortemente sustentado',
    probable: 'Provável',
    hypothesis: 'Hipótese',
    contradictory: 'Contraditório',
    not_located: 'Não localizado'
  };
</script>

<span class:warning={value === 'proposed' || value === 'contested' || value === 'indeterminate'}>
  {labels[value] ?? value}
</span>

<style>
  span { display: inline-block; padding: .2rem .5rem; border: 1px solid #789080; border-radius: 999px; background: #edf4ef; font-size: .78rem; font-weight: 700; }
  .warning { border-color: #a77524; background: #fff4d9; color: #684711; }
</style>
