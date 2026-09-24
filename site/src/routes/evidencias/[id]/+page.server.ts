import { error, redirect } from '@sveltejs/kit';
import { model, byId } from '$lib/server/data';
import type { PageServerLoad } from './$types';
export const load: PageServerLoad = ({ params }) => {
  const evidence = byId(model.provenance.evidence, params.id);
  const document = evidence && byId(model.factual.documents, evidence.document_id);
  if (!document) error(404, 'Fonte não encontrada');
  redirect(307, `${document.public_path}${evidence?.page && /^\d+$/.test(evidence.page) ? `#page=${evidence.page}` : ''}`);
};
