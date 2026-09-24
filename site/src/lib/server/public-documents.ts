import { model } from '$lib/server/data';

export function publicDocumentType(type: string): string {
  if (type === 'Resolution' || type === 'Resolução') return 'Resolução';
  if (type === 'PPC') return 'Projeto pedagógico';
  if (type === 'Ficha 1' || type === 'Ficha 2') return type;
  return 'Outro documento';
}

function publicDocumentDate(value: string): string {
  if (!value || value === 'not stated') return '';
  const match = /^(\d{4})-(\d{2})-(\d{2})$/.exec(value);
  return match ? `${match[3]}/${match[2]}/${match[1]}` : value;
}

const summaries: Record<string, string> = {
  'document-2011-ppc': 'Projeto pedagógico que apresenta a organização do currículo de 2011.',
  'document-2011-resolution-34-2010': 'Ato do CEPE que estabelece o currículo pleno do bacharelado de 2011.',
  'document-2023-ppc': 'Projeto pedagógico que apresenta a organização do currículo de 2023.',
  'document-2023-resolution-75-22': 'Ato do CEPE que fixa o currículo pleno do curso de 2023.'
};

export const publicDocuments = model.factual.documents.map((document) => ({
  id: document.id,
  title: document.title,
  summary: summaries[document.id] ?? '',
  type: publicDocumentType(document.document_type),
  date: publicDocumentDate(document.document_date),
  institution: document.institution,
  fileUrl: document.public_path,
  applicabilityConfirmed: document.applicability_status === 'documented'
}));
