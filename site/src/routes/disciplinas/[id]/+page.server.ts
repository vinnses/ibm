import { error } from '@sveltejs/kit';
import { curriculumView } from '$lib/server/curriculum';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = ({ params }) => {
  for (const year of [2011, 2023] as const) {
    const view = curriculumView(year);
    const component = view.periods.flatMap((period) => period.components).find((item) => item.id === params.id);
    if (component) return { year, component, formalDocuments: view.formalDocuments };
  }
  error(404, 'Disciplina não encontrada');
};
