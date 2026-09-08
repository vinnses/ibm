import { mapViewModel } from '$lib/server/review';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = ({ url }) => ({
  ...mapViewModel(),
  initial_component: url.searchParams.get('disciplina'),
  initial_topic: url.searchParams.get('conteudo')
});
