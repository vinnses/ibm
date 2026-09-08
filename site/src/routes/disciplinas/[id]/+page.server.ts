import { error } from '@sveltejs/kit';
import { model, byId } from '$lib/server/data';
import { componentCoverage, richEvidenceViews } from '$lib/server/review';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = ({ params }) => {
  const component = byId(model.factual.component_instances, params.id);
  if (!component) error(404, 'Disciplina não encontrada');
  const occurrences = model.analytical.topic_occurrences.filter((item) => item.component_instance_id === component.id);
  const occurrenceIds = new Set(occurrences.map((item) => item.id));
  const relations = model.analytical.evolution_relations.filter((item) => [...item.source_occurrence_ids, ...item.target_occurrence_ids].some((id) => occurrenceIds.has(id)));
  const relatedOccurrenceIds = new Set(relations.flatMap((item) => [...item.source_occurrence_ids, ...item.target_occurrence_ids]));
  const relatedComponents = [...new Set(model.analytical.topic_occurrences.filter((item) => relatedOccurrenceIds.has(item.id) && item.component_instance_id !== component.id).map((item) => item.component_instance_id))].flatMap((id) => {
    const item = byId(model.factual.component_instances, id);
    return item ? [{ ...item, curriculum: byId(model.factual.curricula, item.curriculum_id), coverage: componentCoverage(item) }] : [];
  });
  return {
    component,
    coverage: componentCoverage(component),
    curriculum: byId(model.factual.curricula, component.curriculum_id),
    dependencies: component.dependency_ids.flatMap((id) => { const item = byId(model.factual.component_dependencies, id); return item ? [item] : []; }),
    evidence: richEvidenceViews([...new Set([...component.evidence_ids, ...occurrences.flatMap((item) => item.evidence_ids)])]),
    occurrences: occurrences.map((occurrence) => ({ ...occurrence, topic: byId(model.analytical.content_topics, occurrence.topic_id), evidence: richEvidenceViews(occurrence.evidence_ids) })),
    relations: relations.map((relation) => ({ ...relation, evidence: richEvidenceViews(relation.evidence_ids) })),
    relatedComponents
  };
};
