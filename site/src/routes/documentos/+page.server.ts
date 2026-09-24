import { publicDocuments } from '$lib/server/public-documents';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = () => ({
  documents: publicDocuments.filter((document) =>
    document.type !== 'Ficha 1' && document.type !== 'Ficha 2'
  ).sort((a, b) =>
    a.type.localeCompare(b.type, 'pt-BR') ||
    a.title.localeCompare(b.title, 'pt-BR') ||
    a.id.localeCompare(b.id)
  )
});
