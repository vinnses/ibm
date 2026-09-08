import { error } from '@sveltejs/kit';
import { model, byId, evidenceViews } from '$lib/server/data';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = ({ params }) => {
  const component = byId(model.factual.component_instances, params.id);
  if (!component) error(404, 'Disciplina não encontrada');
  return {
    component,
    curriculum: byId(model.factual.curricula, component.curriculum_id),
    dependencies: component.dependency_ids.flatMap((id) => { const item = byId(model.factual.component_dependencies, id); return item ? [item] : []; }),
    evidence: evidenceViews(component.evidence_ids),
    occurrences: model.analytical.topic_occurrences.filter((item) => item.component_instance_id === component.id).map((occurrence) => ({ ...occurrence, topic: byId(model.analytical.content_topics, occurrence.topic_id), evidence: evidenceViews(occurrence.evidence_ids) }))
  };
};
