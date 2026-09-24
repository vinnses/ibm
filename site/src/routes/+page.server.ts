import { curriculumView } from '$lib/server/curriculum';
import type { PageServerLoad } from './$types';
export const load: PageServerLoad = () => curriculumView(2023);
