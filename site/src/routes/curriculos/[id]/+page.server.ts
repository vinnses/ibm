import { error } from '@sveltejs/kit';
import { curriculumView } from '$lib/server/curriculum';
import type { PageServerLoad } from './$types';
export const load: PageServerLoad = ({ params }) => {
  if (params.id === 'curriculum-2011') return curriculumView(2011);
  if (params.id === 'curriculum-2023') return curriculumView(2023);
  error(404, 'Grade não encontrada');
};
