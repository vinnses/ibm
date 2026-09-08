export type ReviewState = 'proposed' | 'reviewed' | 'contested' | 'indeterminate';
export type DocumentaryState = 'documented' | 'probable' | 'contradictory' | 'not_located' | 'indeterminate';
export type EvidenceStrength = 'documented' | 'strongly_supported' | 'probable' | 'hypothesis' | 'indeterminate';
export type ChangeType = 'maintained' | 'expanded' | 'reduced' | 'moved' | 'fragmented' | 'merged' | 'new' | 'removed' | 'indeterminate';

export interface Curriculum { id: string; label: string; year: number; validity: string; evidence_ids: string[]; notes: string; documentary_state: DocumentaryState }
export interface ComponentInstance { id: string; curriculum_id: string; code: string; name: string; recommended_period: number | null; workload_hours: number | null; nature: string; dependency_ids: string[]; evidence_ids: string[]; evidence_state: DocumentaryState; notes: string }
export interface ComponentDependency { id: string; curriculum_id: string; from_component_ids: string[]; to_component_id: string; relation: 'prerequisite' | 'corequisite' | 'equivalence' | 'hidden_requirement' | 'other'; requirement_text: string; evidence_ids: string[]; documentary_state: DocumentaryState; notes: string }
export interface PreservedDocument { id: string; title: string; institution: string; document_type: string; document_date: string; original_url: string; repository_path: string; sha256: string; documentary_state: DocumentaryState; applicability_status: EvidenceStrength; applicability_note: string; public_path: string; asset_path: string; media_type: string }
export interface ContentDomain { id: string; label: string; description: string; review_state: ReviewState; provenance_note: string; is_fixture: boolean }
export interface ContentTopic { id: string; label: string; domain_id: string; description: string; aliases: string[]; review_state: ReviewState; identification_provenance: string; evidence_ids: string[]; is_fixture: boolean }
export interface TopicOccurrence { id: string; topic_id: string; component_instance_id: string; evidence_text: string; evidence_ids: string[]; locator: string; evidence_strength: EvidenceStrength; notes: string; review_state: ReviewState; is_fixture: boolean }
export interface EvolutionRelation { id: string; source_occurrence_ids: string[]; target_occurrence_ids: string[]; change_type: ChangeType; evidence_strength: EvidenceStrength; evidence_ids: string[]; notes: string; review_state: ReviewState; is_fixture: boolean }
export interface Evidence { id: string; document_id: string; page: string | null; section: string | null; cell_range: string | null; normalized_excerpt: string | null; applicability_note: string; documentary_state: DocumentaryState; notes: string }
export interface Claim { id: string; statement: string; layer: 'factual' | 'analytical'; evidence_ids: string[]; review_state: ReviewState; notes: string }
export interface EvidenceLink { id: string; evidence_id: string; target_type: 'curriculum' | 'component_instance' | 'component_dependency' | 'content_domain' | 'content_topic' | 'topic_occurrence' | 'evolution_relation' | 'claim'; target_id: string; purpose: string }

export interface ContentModel {
  schema_version: '1.0.0';
  generated_at: string;
  generated_by: string;
  fixture_notice: string;
  factual: { curricula: Curriculum[]; component_instances: ComponentInstance[]; component_dependencies: ComponentDependency[]; documents: PreservedDocument[] };
  analytical: { content_domains: ContentDomain[]; content_topics: ContentTopic[]; topic_occurrences: TopicOccurrence[]; evolution_relations: EvolutionRelation[] };
  provenance: { claims: Claim[]; evidence: Evidence[]; evidence_links: EvidenceLink[] };
}
