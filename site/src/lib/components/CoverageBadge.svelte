<script lang="ts">
  let { state, label, detail = '' }: { state: string; label: string; detail?: string } = $props();

  const symbols: Record<string, string> = {
    sufficient: '●',
    not_located: '○',
    applicability_indeterminate: '◐',
    contradictory: '×',
    indeterminate: '?'
  };
</script>

<span class="coverage" data-state={state} title={detail} aria-label={`${label}. ${detail}`}>
  <span aria-hidden="true">{symbols[state] ?? '?'}</span> {label}
</span>

<style>
  .coverage { display: inline-flex; align-items: center; gap: .35rem; max-width: 100%; padding: .18rem .48rem; border: 1px solid var(--line); background: var(--paper); color: var(--ink-soft); font-size: .72rem; font-weight: 750; line-height: 1.3; }
  [data-state='not_located'] { border-style: dashed; }
  [data-state='applicability_indeterminate'] { background: var(--amber-soft); border-color: var(--amber); color: #5b3c00; }
  [data-state='contradictory'] { background: var(--red-soft); border-color: var(--red); color: var(--red-dark); }
  [data-state='sufficient'] { background: var(--green-soft); border-color: var(--green); color: var(--green-dark); }
</style>
