import { byId, evidenceViews, model } from '$lib/server/data';
import type { ComponentInstance, DocumentaryState, EvidenceStrength } from '$lib/model';

export type CoverageState = 'sufficient' | 'not_located' | 'applicability_indeterminate' | 'contradictory' | 'indeterminate';

const occurrenceById = new Map(model.analytical.topic_occurrences.map((item) => [item.id, item]));

export function componentOccurrenceRecords(componentId: string) {
  return model.analytical.topic_occurrences.filter((item) => item.component_instance_id === componentId);
}

export function componentDocumentRecords(component: ComponentInstance) {
  const evidenceIds = new Set([
    ...component.evidence_ids,
    ...componentOccurrenceRecords(component.id).flatMap((item) => item.evidence_ids)
  ]);
  const documentIds = new Set(
    [...evidenceIds].flatMap((id) => {
      const evidence = byId(model.provenance.evidence, id);
      return evidence ? [evidence.document_id] : [];
    })
  );
  return [...documentIds].flatMap((id) => {
    const document = byId(model.factual.documents, id);
    return document ? [document] : [];
  });
}

export function componentCoverage(component: ComponentInstance): { state: CoverageState; label: string; detail: string } {
  const documents = componentDocumentRecords(component);
  const fichas = documents.filter((item) => item.document_type === 'Ficha 1' || item.document_type === 'Ficha 2');
  const notes = component.notes.toLocaleLowerCase('pt-BR');

  if (component.evidence_state === 'contradictory' || documents.some((item) => item.documentary_state === 'contradictory')) {
    return { state: 'contradictory', label: 'Fonte contraditória', detail: 'Há conflito documental registrado; inspecione as evidências.' };
  }
  if (fichas.length && fichas.some((item) => item.applicability_status === 'documented' || item.applicability_status === 'strongly_supported')) {
    return { state: 'sufficient', label: 'Cobertura suficiente', detail: 'Existe Ficha vinculada com aplicabilidade sustentada para esta unidade histórica.' };
  }
  if (fichas.length) {
    return { state: 'applicability_indeterminate', label: 'Aplicabilidade indeterminada', detail: 'Existe Ficha preservada, mas sua aplicabilidade a este currículo não foi estabelecida.' };
  }
  if (notes.includes('não localizada') || notes.includes('não localizado') || notes.includes('não consta') || component.nature !== 'coded_component') {
    return { state: 'not_located', label: 'Documento não localizado', detail: 'Ficha aplicável não localizada; ausência pública não prova inexistência.' };
  }
  return { state: 'indeterminate', label: 'Cobertura indeterminada', detail: 'O conjunto documental não permite classificar a cobertura com segurança.' };
}

export function richEvidenceViews(ids: string[]) {
  return evidenceViews(ids).map((view) => {
    const evidence = byId(model.provenance.evidence, view.id);
    const document = evidence ? byId(model.factual.documents, evidence.document_id) : undefined;
    return {
      ...view,
      excerpt: evidence?.normalized_excerpt ?? null,
      applicability: evidence?.applicability_note ?? '',
      documentary_state: evidence?.documentary_state ?? ('indeterminate' as DocumentaryState),
      document_id: document?.id ?? '',
      document_type: document?.document_type ?? '',
      document_applicability: document?.applicability_status ?? ('indeterminate' as EvidenceStrength),
      public_path: document?.public_path ?? ''
    };
  });
}

export function mapViewModel() {
  const components = model.factual.component_instances.map((component) => {
    const occurrences = componentOccurrenceRecords(component.id);
    const topics = occurrences.flatMap((occurrence) => {
      const topic = byId(model.analytical.content_topics, occurrence.topic_id);
      return topic ? [{ id: topic.id, label: topic.label, domain_id: topic.domain_id, review_state: topic.review_state }] : [];
    });
    const dependencies = component.dependency_ids.flatMap((id) => {
      const dependency = byId(model.factual.component_dependencies, id);
      return dependency ? [{ id: dependency.id, relation: dependency.relation, requirement_text: dependency.requirement_text, documentary_state: dependency.documentary_state }] : [];
    });
    return {
      ...component,
      coverage: componentCoverage(component),
      topics,
      topic_ids: [...new Set(topics.map((topic) => topic.id))],
      domain_ids: [...new Set(topics.map((topic) => topic.domain_id))],
      review_states: [...new Set(topics.map((topic) => topic.review_state))],
      evidence_strengths: [...new Set(occurrences.map((item) => item.evidence_strength))],
      dependencies,
      evidence: richEvidenceViews([...new Set([...component.evidence_ids, ...occurrences.flatMap((item) => item.evidence_ids)])])
    };
  });

  const occurrences = model.analytical.topic_occurrences.map((occurrence) => ({
    ...occurrence,
    evidence: richEvidenceViews(occurrence.evidence_ids)
  }));

  const relations = model.analytical.evolution_relations.map((relation) => {
    const sourceOccurrences = relation.source_occurrence_ids.flatMap((id) => occurrenceById.get(id) ?? []);
    const targetOccurrences = relation.target_occurrence_ids.flatMap((id) => occurrenceById.get(id) ?? []);
    return {
      ...relation,
      source_component_ids: [...new Set(sourceOccurrences.map((item) => item.component_instance_id))],
      target_component_ids: [...new Set(targetOccurrences.map((item) => item.component_instance_id))],
      topic_ids: [...new Set([...sourceOccurrences, ...targetOccurrences].map((item) => item.topic_id))],
      evidence: richEvidenceViews(relation.evidence_ids)
    };
  });

  return {
    curricula: model.factual.curricula,
    components,
    domains: model.analytical.content_domains,
    topics: model.analytical.content_topics,
    occurrences,
    relations,
    summary: {
      components: components.length,
      topics: model.analytical.content_topics.length,
      occurrences: occurrences.length,
      relations: relations.length,
      gaps: components.filter((item) => item.coverage.state === 'not_located').length,
      applicability_indeterminate: components.filter((item) => item.coverage.state === 'applicability_indeterminate').length
    }
  };
}
