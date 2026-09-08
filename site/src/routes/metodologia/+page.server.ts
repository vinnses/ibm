import { model } from '$lib/server/data';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = () => ({
  evidence_count: model.provenance.evidence.length,
  document_count: model.factual.documents.length,
  sample_evidence: model.provenance.evidence.slice(0, 6).map((item) => ({ id: item.id, excerpt: item.normalized_excerpt }))
});
