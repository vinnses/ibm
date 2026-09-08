import { model, byId } from '$lib/server/data';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = ({ url }) => {
  const curriculum = url.searchParams.get('curriculo');
  const domain = url.searchParams.get('dominio');
  const visibleTopicIds = new Set(
    model.analytical.topic_occurrences
      .filter((occurrence) => !curriculum || occurrence.component_instance_id.startsWith(`${curriculum}-`))
      .map((occurrence) => occurrence.topic_id)
  );
  const topics = model.analytical.content_topics.filter((topic) =>
    (!domain || topic.domain_id === domain) &&
    (!curriculum || visibleTopicIds.has(topic.id))
  );
  const topicCards = topics.map((topic) => ({ ...topic, domain_label: byId(model.analytical.content_domains, topic.domain_id)?.label, occurrence_count: model.analytical.topic_occurrences.filter((item) => item.topic_id === topic.id).length }));
  const relations = model.analytical.evolution_relations.map((relation) => {
    const occurrenceId = [...relation.source_occurrence_ids, ...relation.target_occurrence_ids][0];
    const occurrence = occurrenceId ? byId(model.analytical.topic_occurrences, occurrenceId) : undefined;
    return { ...relation, topic_id: occurrence?.topic_id };
  });
  return { curriculum, domain, topics: topicCards, domains: model.analytical.content_domains, relations, has_fixture: model.analytical.content_topics.some((topic) => topic.is_fixture) };
};
