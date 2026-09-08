import { mapViewModel } from '$lib/server/review';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = () => ({ summary: mapViewModel().summary });
