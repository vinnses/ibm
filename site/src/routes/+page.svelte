<script lang="ts">
  import CurriculumView from '$lib/components/CurriculumView.svelte';
  let { data } = $props();
</script>
<CurriculumView {data} />
