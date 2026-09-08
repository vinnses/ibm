import { error } from '@sveltejs/kit';
import { model, byId } from '$lib/data';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = ({ params }) => {
  const document = byId(model.factual.documents, params.id);
  if (!document) error(404, 'Documento não encontrado');
  return { document, evidence: model.provenance.evidence.filter((item) => item.document_id === document.id) };
};
