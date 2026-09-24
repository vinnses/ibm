import { curriculumView } from '$lib/server/curriculum';
import type { PageServerLoad } from './$types';
export const load: PageServerLoad = () => ({ curricula: [curriculumView(2011), curriculumView(2023)] });
