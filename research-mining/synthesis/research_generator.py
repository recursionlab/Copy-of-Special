"""
Research Question Generator - automatically generates research questions from gaps and contradictions.

Generates:
- Gap-based research questions
- Contradiction-resolution questions
- Bridge-building questions
- Exploratory questions from isolated concepts
"""

from typing import Dict, List, Set, Tuple, Any, Optional
import json
import re
from collections import defaultdict, Counter
import random


class ResearchQuestionGenerator:
    """Generates research questions from gap analysis and contradiction detection."""

    def __init__(self, units: List[Dict[str, Any]], gaps: Dict[str, List[Dict[str, Any]]],
                 contradictions: Dict[str, List[Dict[str, Any]]]):
        self.units = units
        self.gaps = gaps
        self.contradictions = contradictions
        self.id_to_unit = {u['id']: u for u in units}
        self.question_templates = self._load_question_templates()

    def _load_question_templates(self) -> Dict[str, List[str]]:
        """Load templates for different types of research questions."""
        return {
            'gap_based': [
                "What relationships exist between {concept1} and {concept2}?",
                "How does {concept1} influence or relate to {concept2}?",
                "What mediating factors connect {concept1} to {concept2}?",
                "Can {concept1} and {concept2} be unified under a common framework?",
                "What are the missing links between {concept1} and {concept2}?",
                "How might {concept1} and {concept2} interact in practice?",
                "What would a formal relationship between {concept1} and {concept2} look like?"
            ],
            'orphaned_concepts': [
                "How does {concept} relate to the broader theoretical framework?",
                "What role does {concept} play in the overall conceptual system?",
                "What other concepts might {concept} naturally connect to?",
                "Is {concept} a fundamental building block or a derived concept?",
                "How can {concept} be integrated into existing theoretical models?",
                "What empirical evidence supports the importance of {concept}?",
                "Does {concept} represent a gap in current understanding?"
            ],
            'contradiction_resolution': [
                "How can the contradiction between {concept1} and {concept2} be resolved?",
                "Under what conditions might both {concept1} and {concept2} be valid?",
                "Is the contradiction between {concept1} and {concept2} apparent or fundamental?",
                "What synthesis could reconcile {concept1} and {concept2}?",
                "Do {concept1} and {concept2} operate at different levels of analysis?",
                "What evidence would resolve the tension between {concept1} and {concept2}?",
                "Could {concept1} and {concept2} be complementary rather than contradictory?"
            ],
            'bridge_building': [
                "What intermediate concepts could bridge {concept1} and {concept2}?",
                "How might {concept1} evolve toward {concept2}?",
                "What transformation maps {concept1} to {concept2}?",
                "Can {concept1} and {concept2} be seen as parts of a larger pattern?",
                "What higher-order concept encompasses both {concept1} and {concept2}?",
                "How do {concept1} and {concept2} relate within a dynamic system?",
                "What experimental design could test the relationship between {concept1} and {concept2}?"
            ],
            'exploratory': [
                "What are the implications of {concept} for {domain}?",
                "How might {concept} change our understanding of {field}?",
                "What predictions does {concept} make about {phenomena}?",
                "How can {concept} be measured or quantified?",
                "What are the practical applications of {concept}?",
                "How does {concept} scale across different contexts?",
                "What are the boundary conditions for {concept}?"
            ],
            'mathematical': [
                "What mathematical structure underlies {concept}?",
                "How can {concept} be formalized mathematically?",
                "What computational model captures {concept}?",
                "Is there a metric space for {concept}?",
                "What symmetries or invariances characterize {concept}?",
                "How can {concept} be represented algebraically?",
                "What differential equations govern {concept}?"
            ]
        }

    def generate_gap_based_questions(self) -> List[Dict[str, Any]]:
        """Generate research questions from identified gaps."""
        questions = []

        # Questions from orphaned concepts
        for orphan in self.gaps.get('orphaned_concepts', []):
            concept_id = orphan['id']
            concept_type = orphan.get('type', 'unknown')

            templates = self.question_templates['orphaned_concepts']
            for template in templates[:3]:  # Limit per concept
                question = template.format(concept=concept_type or concept_id)
                questions.append({
                    'question': question,
                    'type': 'orphaned_concept',
                    'source_concept': concept_id,
                    'priority': 'medium',
                    'rationale': f"Concept {concept_id} lacks relationships to other concepts"
                })

        # Questions from missing bidirectional relations
        for missing_rel in self.gaps.get('missing_bidirectional_relations', []):
            from_id = missing_rel['from_id']
            to_id = missing_rel['to_id']
            from_type = missing_rel.get('from_type', from_id)
            to_type = missing_rel.get('to_type', to_id)

            templates = self.question_templates['gap_based']
            template = random.choice(templates)
            question = template.format(concept1=from_type, concept2=to_type)

            questions.append({
                'question': question,
                'type': 'missing_bidirectional_relation',
                'source_concepts': [from_id, to_id],
                'priority': 'high',
                'rationale': f"Asymmetric relationship detected between {from_id} and {to_id}"
            })

        # Questions from isolated clusters
        for cluster in self.gaps.get('isolated_clusters', []):
            if cluster['size'] > 1:
                concept_types = cluster.get('concept_types', [])
                main_types = [t for t in concept_types if t and t != 'unknown'][:2]

                if len(main_types) >= 2:
                    templates = self.question_templates['bridge_building']
                    template = random.choice(templates)
                    question = template.format(concept1=main_types[0], concept2=main_types[1])

                    questions.append({
                        'question': question,
                        'type': 'isolated_cluster',
                        'source_cluster': cluster['cluster_id'],
                        'priority': 'medium',
                        'rationale': f"Isolated cluster of {cluster['size']} concepts needs integration"
                    })

        return questions

    def generate_contradiction_questions(self) -> List[Dict[str, Any]]:
        """Generate research questions from identified contradictions."""
        questions = []

        # Questions from conflicting definitions
        for conflict in self.contradictions.get('conflicting_definitions', []):
            unit1_id = conflict['unit1_id']
            unit2_id = conflict['unit2_id']
            concept_family = conflict.get('concept_family', 'concept')

            templates = self.question_templates['contradiction_resolution']
            template = random.choice(templates)
            question = template.format(concept1=unit1_id, concept2=unit2_id)

            questions.append({
                'question': question,
                'type': 'conflicting_definitions',
                'source_concepts': [unit1_id, unit2_id],
                'priority': 'high',
                'rationale': f"Conflicting definitions detected in {concept_family} concept family"
            })

        # Questions from relationship contradictions
        for contradiction in self.contradictions.get('relationship_contradictions', []):
            source_id = contradiction['source_id']
            target_id = contradiction['target_id']

            templates = self.question_templates['contradiction_resolution']
            template = random.choice(templates)
            question = template.format(concept1=source_id, concept2=target_id)

            questions.append({
                'question': question,
                'type': 'relationship_contradiction',
                'source_concepts': [source_id, target_id],
                'priority': 'high',
                'rationale': contradiction.get('details', 'Contradictory relationships detected')
            })

        # Questions from mathematical contradictions
        for math_contradiction in self.contradictions.get('mathematical_contradictions', []):
            unit1_id = math_contradiction['unit1_id']
            unit2_id = math_contradiction['unit2_id']

            templates = self.question_templates['mathematical']
            template = random.choice(templates)
            concept_type = self.id_to_unit.get(unit1_id, {}).get('type', 'concept')
            question = template.format(concept=concept_type)

            questions.append({
                'question': question,
                'type': 'mathematical_contradiction',
                'source_concepts': [unit1_id, unit2_id],
                'priority': 'high',
                'rationale': f"Mathematical formulation contradiction requires formal resolution"
            })

        return questions

    def generate_exploratory_questions(self, concept_types: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Generate exploratory research questions for concept types."""
        questions = []

        # Get concept type distribution
        if not concept_types:
            type_counts = Counter(unit.get('type', 'unknown') for unit in self.units)
            # Focus on most common types
            concept_types = [t for t, count in type_counts.most_common(10) if t != 'unknown']

        # Identify domains from tags and sources
        all_tags = []
        all_sources = []
        for unit in self.units:
            all_tags.extend(unit.get('tags', []))
            source = unit.get('source', '')
            if source:
                all_sources.append(source)

        common_domains = Counter(all_tags).most_common(5)
        domain_keywords = [domain for domain, _ in common_domains]

        # Generate exploratory questions
        for concept_type in concept_types[:5]:  # Limit number
            templates = self.question_templates['exploratory']

            for i, template in enumerate(templates[:3]):  # Limit per type
                if '{domain}' in template or '{field}' in template or '{phenomena}' in template:
                    if domain_keywords:
                        domain = random.choice(domain_keywords)
                        question = template.format(concept=concept_type, domain=domain,
                                                field=domain, phenomena=domain)
                    else:
                        continue
                else:
                    question = template.format(concept=concept_type)

                questions.append({
                    'question': question,
                    'type': 'exploratory',
                    'concept_type': concept_type,
                    'priority': 'low',
                    'rationale': f"Exploratory investigation of {concept_type} implications"
                })

        return questions

    def generate_bridge_questions(self, concept_pairs: Optional[List[Tuple[str, str]]] = None) -> List[Dict[str, Any]]:
        """Generate questions for building bridges between concepts."""
        questions = []

        if not concept_pairs:
            # Find pairs of concepts that could benefit from bridging
            concept_pairs = self._identify_bridge_candidates()

        for concept1, concept2 in concept_pairs[:10]:  # Limit number
            templates = self.question_templates['bridge_building']
            template = random.choice(templates)

            # Get concept types for better questions
            type1 = self.id_to_unit.get(concept1, {}).get('type', concept1)
            type2 = self.id_to_unit.get(concept2, {}).get('type', concept2)

            question = template.format(concept1=type1, concept2=type2)

            questions.append({
                'question': question,
                'type': 'bridge_building',
                'source_concepts': [concept1, concept2],
                'priority': 'medium',
                'rationale': f"Potential bridge opportunity between {type1} and {type2}"
            })

        return questions

    def _identify_bridge_candidates(self) -> List[Tuple[str, str]]:
        """Identify pairs of concepts that could benefit from bridging."""
        candidates = []

        # Look for concepts in different types but similar domains
        type_groups = defaultdict(list)
        for unit in self.units:
            unit_type = unit.get('type', 'unknown')
            type_groups[unit_type].append(unit)

        # Find cross-type pairs with similar tags or sources
        types = list(type_groups.keys())
        for i, type1 in enumerate(types):
            for type2 in types[i+1:]:
                group1 = type_groups[type1]
                group2 = type_groups[type2]

                # Sample concepts from each group
                for unit1 in group1[:3]:  # Limit sampling
                    for unit2 in group2[:3]:
                        # Check for potential connection
                        tags1 = set(unit1.get('tags', []))
                        tags2 = set(unit2.get('tags', []))

                        if tags1 & tags2:  # Shared tags suggest potential connection
                            candidates.append((unit1['id'], unit2['id']))

        return candidates[:20]  # Limit total candidates

    def generate_all_questions(self) -> Dict[str, List[Dict[str, Any]]]:
        """Generate all types of research questions."""
        return {
            'gap_based_questions': self.generate_gap_based_questions(),
            'contradiction_questions': self.generate_contradiction_questions(),
            'exploratory_questions': self.generate_exploratory_questions(),
            'bridge_questions': self.generate_bridge_questions()
        }

    def rank_questions_by_priority(self, questions: Dict[str, List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
        """Rank all questions by priority and potential impact."""
        all_questions = []
        for category, question_list in questions.items():
            for q in question_list:
                q['category'] = category
                all_questions.append(q)

        # Priority scoring
        priority_scores = {'high': 3, 'medium': 2, 'low': 1}

        # Add impact scoring based on concepts involved
        for q in all_questions:
            base_score = priority_scores.get(q.get('priority', 'medium'), 2)

            # Boost score for questions involving multiple concepts
            concept_boost = len(q.get('source_concepts', [])) * 0.5

            # Boost score for mathematical or formal questions
            if 'mathematical' in q.get('type', ''):
                base_score += 1

            # Boost score for contradiction resolution
            if 'contradiction' in q.get('type', ''):
                base_score += 1

            q['impact_score'] = base_score + concept_boost

        # Sort by impact score
        return sorted(all_questions, key=lambda x: x['impact_score'], reverse=True)

    def export_research_questions(self, output_path: str) -> None:
        """Export research questions to JSON file."""
        questions = self.generate_all_questions()
        ranked_questions = self.rank_questions_by_priority(questions)

        report = {
            'metadata': {
                'total_questions': sum(len(qs) for qs in questions.values()),
                'generation_date': None,  # Will be filled
                'categories': list(questions.keys()),
                'top_priority_count': len([q for q in ranked_questions if q.get('priority') == 'high'])
            },
            'summary': {
                category: len(question_list) for category, question_list in questions.items()
            },
            'questions_by_category': questions,
            'ranked_questions': ranked_questions[:50]  # Top 50 questions
        }

        import datetime
        report['metadata']['generation_date'] = datetime.datetime.now().isoformat()

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)