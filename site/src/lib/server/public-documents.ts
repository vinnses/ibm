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

export const publicDocuments = model.factual.documents.map((document) => ({
  id: document.id,
  title: document.title,
  type: publicDocumentType(document.document_type),
  date: publicDocumentDate(document.document_date),
  institution: document.institution,
  fileUrl: document.public_path,
  applicabilityConfirmed: document.applicability_status === 'documented'
}));
