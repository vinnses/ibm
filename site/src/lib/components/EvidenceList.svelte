<script lang="ts">
  let { items }: { items: Array<{ id: string; title: string; section: string | null; page: string | null }> } = $props();
</script>

{#if items.length}
  <ul class="evidence-list">
    {#each items as item}
      <li>
        <a href={`/evidencias/${item.id}`}>{item.title}</a>
        {#if item.section}<small>Seção: {item.section}</small>{/if}
        {#if item.page}<small>Página: {item.page}</small>{/if}
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
  .empty { color: #69736d; font-style: italic; }
</style>
