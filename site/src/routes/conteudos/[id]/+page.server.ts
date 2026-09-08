import { error } from '@sveltejs/kit';
import { model, byId } from '$lib/data';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = ({ params }) => {
  const topic = byId(model.analytical.content_topics, params.id);
  if (!topic) error(404, 'Conteúdo não encontrado');
  return { topic, domain: byId(model.analytical.content_domains, topic.domain_id), occurrences: model.analytical.topic_occurrences.filter((item) => item.topic_id === topic.id), relations: model.analytical.evolution_relations.filter((item) => [...item.source_occurrence_ids, ...item.target_occurrence_ids].some((id) => model.analytical.topic_occurrences.some((occurrence) => occurrence.id === id && occurrence.topic_id === topic.id))) };
};
