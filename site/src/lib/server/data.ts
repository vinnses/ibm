import rawModel from '$lib/data/generated/content-model.json';
import type { ContentModel } from '$lib/model';

export const model = rawModel as ContentModel;

export const byId = <T extends { id: string }>(items: T[], id: string): T | undefined =>
  items.find((item) => item.id === id);

export function evidenceViews(ids: string[]) {
  return ids.flatMap((id) => {
    const item = byId(model.provenance.evidence, id);
    if (!item) return [];
    const document = byId(model.factual.documents, item.document_id);
    return [{ id: item.id, title: document?.title ?? item.id, section: item.section, page: item.page }];
  });
}
