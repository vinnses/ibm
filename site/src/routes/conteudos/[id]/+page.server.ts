import { error } from '@sveltejs/kit';
import { model, byId } from '$lib/server/data';
import { richEvidenceViews } from '$lib/server/review';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = ({ params }) => {
  const topic = byId(model.analytical.content_topics, params.id);
  if (!topic) error(404, 'Conteúdo não encontrado');
  const occurrences = model.analytical.topic_occurrences.filter((item) => item.topic_id === topic.id).map((occurrence) => {
    const component = byId(model.factual.component_instances, occurrence.component_instance_id);
    return { ...occurrence, component, curriculum: component ? byId(model.factual.curricula, component.curriculum_id) : undefined, evidence: richEvidenceViews(occurrence.evidence_ids) };
  });
  const relations = model.analytical.evolution_relations.filter((item) => [...item.source_occurrence_ids, ...item.target_occurrence_ids].some((id) => model.analytical.topic_occurrences.some((occurrence) => occurrence.id === id && occurrence.topic_id === topic.id))).map((relation) => ({ ...relation, evidence: richEvidenceViews(relation.evidence_ids) }));
  return { topic, domain: byId(model.analytical.content_domains, topic.domain_id), evidence: richEvidenceViews(topic.evidence_ids), occurrences, relations };
};
