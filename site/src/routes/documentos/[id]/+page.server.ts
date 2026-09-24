import { error } from '@sveltejs/kit';
import { publicDocuments } from '$lib/server/public-documents';
import type { PageServerLoad } from './$types';
export const load: PageServerLoad = ({ params }) => {
  const document = publicDocuments.find((item) => item.id === params.id);
  if (!document) error(404, 'Documento não encontrado');
  return { document };
};
