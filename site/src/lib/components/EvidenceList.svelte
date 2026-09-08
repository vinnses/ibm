<script lang="ts">
  let { items, compact = false }: { items: Array<{ id: string; title: string; section: string | null; page: string | null; excerpt?: string | null; public_path?: string }>; compact?: boolean } = $props();
</script>

{#if items.length}
  <ul class:compact class="evidence-list">
    {#each items as item}
      <li>
        <a href={`/evidencias/${item.id}`}>Ver evidência — {item.title}</a>
        {#if item.section}<small>Seção: {item.section}</small>{/if}
        {#if item.page}<small>Página: {item.page}</small>{/if}
        {#if !compact && item.excerpt}<blockquote>{item.excerpt}</blockquote>{/if}
        {#if item.public_path}<a class="document-link" href={item.public_path} target="_blank">Abrir documento preservado{item.page ? ` · p. ${item.page}` : ''}</a>{/if}
      </li>
    {/each}
  </ul>
{:else}
  <p class="empty">Nenhuma evidência associada.</p>
{/if}

<style>
  .evidence-list { padding-left: 1.25rem; }
  li + li { margin-top: .55rem; }
  small { display: block; color: #59645d; }
  blockquote { margin: .5rem 0; padding-left: .75rem; border-left: 2px solid var(--red); color: var(--ink-soft); }
  .document-link { display: inline-block; margin-top: .25rem; font-size: .82rem; }
  .compact blockquote { display: none; }
  .empty { color: #69736d; font-style: italic; }
</style>
