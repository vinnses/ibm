<script lang="ts">
  import { byId, evidenceFor, model } from '$lib/data';
  let { ids }: { ids: string[] } = $props();
  let evidence = $derived(evidenceFor(ids));
</script>

{#if evidence.length}
  <ul class="evidence-list">
    {#each evidence as item}
      {@const document = byId(model.factual.documents, item.document_id)}
      <li>
        <a href={`/evidencias/${item.id}`}>{document?.title ?? item.id}</a>
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
