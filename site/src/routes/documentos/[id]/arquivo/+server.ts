import { error, redirect } from '@sveltejs/kit';
import { model, byId } from '$lib/data';
import type { RequestHandler } from './$types';

export const GET: RequestHandler = ({ params }) => {
  const document = byId(model.factual.documents, params.id);
  if (!document) error(404, 'Documento não autorizado para publicação');
  redirect(307, document.asset_path);
};
