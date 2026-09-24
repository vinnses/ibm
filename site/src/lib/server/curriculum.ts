import { model } from '$lib/server/data';
import type { ComponentInstance, PreservedDocument } from '$lib/model';

type Ficha = { title: string; url: string; note: string };

const additionalFichas: Record<string, Ficha> = {
  CM303: { title: 'Ficha 1 · CM303', url: '/documents/w036/CM303.pdf', note: 'Versão publicada pelo BCC; aplicação à IBM 2023 não confirmada.' },
  CM304: { title: 'Ficha 1 · CM304', url: '/documents/w036/CM304.pdf', note: 'Versão publicada pelo BCC; aplicação à IBM 2023 não confirmada.' },
  CM310: { title: 'Ficha 1 · CM310', url: '/documents/w036/CM310.pdf', note: 'Versão publicada pelo BCC; aplicação à IBM 2023 não confirmada.' },
  CM311: { title: 'Ficha 1 · CM311', url: '/documents/w036/CM311.pdf', note: 'Versão publicada pelo BCC; aplicação à IBM 2023 não confirmada.' },
  CI1169: { title: 'Ficha 1 · CI1169', url: '/documents/w036/CI1169.pdf', note: 'Versão anterior à reforma: classifica a disciplina como optativa; aplicação à IBM 2023 contraditória.' },
  CI1172: { title: 'Ficha 1 · CI1172', url: '/documents/w036/CI1172.pdf', note: 'Versão anterior à reforma: classifica a disciplina como optativa; aplicação à IBM 2023 contraditória.' }
};

// These are navigation clues based on names/codes, never formal equivalences.
const counterpartCodes: [string, string][] = [
  ['BA040', 'BA040'], ['BC056', 'BC056'], ['BF075', 'BF114'], ['BG054', 'BG079'],
  ['BQ005', 'BQ112'], ['BQ054', 'BQ083'], ['CI055', 'CI1055'], ['CI056', 'CI1056'],
  ['CI057', 'CI1057'], ['CI162', 'CI1162'], ['CI167', 'MN163'], ['CI169', 'CI1169'],
  ['CI171', 'CI1171'], ['CI172', 'CI1172'], ['CI209', 'CI1209'], ['CI215', 'CI1215'],
  ['CI218', 'CI1218'], ['CI221', 'CI1221'], ['CI316', 'CI1316'], ['MN128', 'MN162'],
  ['MN129', 'MN129']
];

function documentCode(document: PreservedDocument): string | null {
  return document.id.match(/(?:^|-)([a-z]{2}\d{2,4})(?:-|$)/i)?.[1]?.toUpperCase() ?? null;
}

function fichasFor(component: ComponentInstance): Ficha[] {
  if (component.nature === 'elective_space' || component.nature.includes('TCC') || component.code === 'CI262') return [];
  const year = component.curriculum_id === 'curriculum-2011' ? '2011' : '2023';
  const found = model.factual.documents
    .filter((document) => document.document_type === 'Ficha 1' &&
      document.repository_path.startsWith(`curriculos/${year}/`) && documentCode(document) === component.code)
    .map((document) => ({
      title: document.title,
      url: document.public_path,
      note: document.applicability_status === 'documented'
        ? 'Aplicação ao currículo documentada.'
        : `Versão localizada; aplicação ao currículo ${year} não confirmada.`
    }));
  const extra = year === '2023' ? additionalFichas[component.code] : undefined;
  return extra ? [...found, extra] : found;
}

function counterpart(component: ComponentInstance) {
  const pair = counterpartCodes.find(([oldCode, newCode]) =>
    component.curriculum_id === 'curriculum-2011' ? oldCode === component.code : newCode === component.code);
  if (!pair) return null;
  const targetYear = component.curriculum_id === 'curriculum-2011' ? 'curriculum-2023' : 'curriculum-2011';
  const targetCode = component.curriculum_id === 'curriculum-2011' ? pair[1] : pair[0];
  const peer = model.factual.component_instances.find((item) => item.curriculum_id === targetYear && item.code === targetCode);
  if (!peer) return null;
  const peerFichas = fichasFor(peer);
  return { id: peer.id, code: peer.code, name: peer.name, year: targetYear === 'curriculum-2011' ? 2011 : 2023, hours: peer.workload_hours,
    relation: peer.code === component.code ? 'Mesmo código' : 'Nome semelhante',
    ficha: peerFichas[0] ?? null };
}

export function curriculumView(year: 2011 | 2023) {
  const curriculum = model.factual.curricula.find((item) => item.year === year);
  if (!curriculum) throw new Error(`Curriculum ${year} missing`);
  const components = model.factual.component_instances
    .filter((item) => item.curriculum_id === curriculum.id)
    .map((item) => {
      const fichas = fichasFor(item);
      const special = item.nature === 'elective_space' || item.nature.includes('TCC') || item.code === 'CI262';
      return { id: item.id, code: item.code, name: item.name, period: item.recommended_period,
        hours: item.workload_hours, nature: item.nature, fichas,
        fichaState: special ? 'not_applicable' : fichas.length ? 'located' : 'not_located',
        counterpart: counterpart(item),
        prerequisites: item.dependency_ids.flatMap((id) => {
          const dependency = model.factual.component_dependencies.find((entry) => entry.id === id);
          return dependency && dependency.relation === 'prerequisite' ? [dependency.requirement_text] : [];
        }) };
    });
  const periods = Array.from({ length: 8 }, (_, index) => ({
    number: index + 1,
    components: components.filter((item) => item.period === index + 1)
  }));
  const formalDocuments = model.factual.documents
    .filter((document) => document.repository_path.startsWith(`curriculos/${year}/`) && ['PPC', 'Resolution', 'Resolução'].includes(document.document_type))
    .map((document) => ({ title: document.title, url: document.public_path }));
  return { year, periods, formalDocuments,
    summary: { coded: components.filter((item) => item.nature !== 'elective_space').length,
      fichas: components.filter((item) => item.fichaState === 'located').length,
      missing: components.filter((item) => item.fichaState === 'not_located').length } };
}
