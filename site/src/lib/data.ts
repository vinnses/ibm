import rawModel from '$lib/data/generated/content-model.json';
import type { ContentModel, Evidence } from '$lib/model';

export const model = rawModel as ContentModel;

export const byId = <T extends { id: string }>(items: T[], id: string): T | undefined =>
  items.find((item) => item.id === id);

export function evidenceFor(ids: string[]): Evidence[] {
  return ids.flatMap((id) => {
    const item = byId(model.provenance.evidence, id);
    return item ? [item] : [];
  });
}
