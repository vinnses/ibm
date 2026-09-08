import { error } from '@sveltejs/kit';
import { model, byId } from '$lib/data';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = ({ params }) => {
  const evidence = byId(model.provenance.evidence, params.id);
  if (!evidence) error(404, 'Evidência não encontrada');
  return { evidence, document: byId(model.factual.documents, evidence.document_id), links: model.provenance.evidence_links.filter((item) => item.evidence_id === evidence.id) };
};
