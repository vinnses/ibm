import { model } from '$lib/server/data';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = () => ({ curricula: model.factual.curricula });
