import { error } from '@sveltejs/kit';
import { model, byId } from '$lib/data';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = ({ params }) => {
  const curriculum = byId(model.factual.curricula, params.id);
  if (!curriculum) error(404, 'Currículo não encontrado');
  return { curriculum, components: model.factual.component_instances.filter((item) => item.curriculum_id === curriculum.id) };
};
