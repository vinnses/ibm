import { error } from '@sveltejs/kit';
import { model, byId } from '$lib/server/data';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = ({ params }) => {
  const evidence = byId(model.provenance.evidence, params.id);
  if (!evidence) error(404, 'Evidência não encontrada');
  const document = byId(model.factual.documents, evidence.document_id);
  return { evidence, document, document_anchor: document ? `${document.public_path}${evidence.page && /^\d+$/.test(evidence.page) ? `#page=${evidence.page}` : ''}` : '', links: model.provenance.evidence_links.filter((item) => item.evidence_id === evidence.id) };
};
