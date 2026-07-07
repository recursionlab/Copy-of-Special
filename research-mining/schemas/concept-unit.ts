// TypeScript interface for ConceptUnit
export interface ConceptUnit {
  id: string;
  version?: string;
  source: string;
  type: 'Functor' | 'Recursion' | 'Autopoiesis' | 'Distinction' | 'Contradiction';
  definition: string;
  mathematical_formulation?: string;
  relations?: string[];
  examples?: string[];
  prototypes?: string[];
  references?: string[];
  tags?: string[];
  extraction_date?: string; // ISO date-time string
  confidence_score?: number; // 0-1
  notes?: string;
}

// Example usage
const exampleConceptUnit: ConceptUnit = {
  id: 'functor-001',
  version: '1.0.0',
  source: 'Thinking with Functors',
  type: 'Functor',
  definition: 'A functor is a mapping between categories that preserves the structure.',
  mathematical_formulation: 'F: C → D',
  relations: ['recursion', 'morphism'],
  examples: ['List<T> -> Set<T>'],
  prototypes: ['prototypes/functor_graph_demo.ts'],
  references: ['Mac Lane, S. (1998). Categories for the Working Mathematician.'],
  tags: ['category theory', 'structure preservation'],
  extraction_date: '2025-09-14T12:00:00Z',
  confidence_score: 0.95,
  notes: 'Core concept in category theory.'
};

// Type for ConceptUnit collection
export type ConceptUnits = ConceptUnit[];
