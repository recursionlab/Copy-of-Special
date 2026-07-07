"""
Contradiction Detection System for identifying logical inconsistencies between ConceptUnits.

Detects:
- Conflicting definitions of the same concept
- Contradictory relationships (A relates to B, but B contradicts A)
- Logical inconsistencies in mathematical formulations
- Semantic contradictions using NLP techniques
"""

from typing import Dict, List, Set, Tuple, Any, Optional
import json
import re
from collections import defaultdict
from difflib import SequenceMatcher


class ContradictionDetector:
    """Analyzes ConceptUnit collections for logical contradictions and conflicts."""

    def __init__(self, units: List[Dict[str, Any]]):
        self.units = units
        self.id_to_unit = {u['id']: u for u in units}
        self.type_groups = self._group_by_type()
        self.definition_patterns = self._build_definition_patterns()

    def _group_by_type(self) -> Dict[str, List[Dict[str, Any]]]:
        """Group units by their type for focused contradiction analysis."""
        groups = defaultdict(list)
        for unit in self.units:
            unit_type = unit.get('type', 'unknown')
            groups[unit_type].append(unit)
        return groups

    def _build_definition_patterns(self) -> Dict[str, List[str]]:
        """Extract key definitional patterns for contradiction detection."""
        patterns = defaultdict(list)

        negation_markers = [
            r'\b(?:not|never|no|none|without|lacks?|absent|excludes?)\b',
            r'\b(?:contradicts?|opposes?|against|contrary)\b',
            r'\b(?:impossible|cannot|unable|fails? to)\b'
        ]

        for unit in self.units:
            definition = unit.get('definition', '').lower()
            unit_id = unit['id']

            for marker in negation_markers:
                if re.search(marker, definition):
                    patterns[unit_id].append(marker)

        return patterns

    def detect_conflicting_definitions(self) -> List[Dict[str, Any]]:
        """Find concepts with similar names but conflicting definitions."""
        conflicts = []

        # Group by similar concept names/IDs
        concept_families = defaultdict(list)
        for unit in self.units:
            # Extract base concept name (before hash/version)
            base_name = re.sub(r'-[a-f0-9]{8,}$', '', unit['id'])
            base_name = re.sub(r'_v\d+$', '', base_name)
            concept_families[base_name].append(unit)

        for base_name, family_units in concept_families.items():
            if len(family_units) < 2:
                continue

            # Compare definitions within family
            for i, unit1 in enumerate(family_units):
                for unit2 in family_units[i + 1:]:
                    conflict = self._analyze_definition_conflict(unit1, unit2)
                    if conflict:
                        conflicts.append({
                            'concept_family': base_name,
                            'unit1_id': unit1['id'],
                            'unit2_id': unit2['id'],
                            'conflict_type': 'conflicting_definitions',
                            'conflict_details': conflict,
                            'severity': conflict.get('severity', 'medium')
                        })

        return conflicts

    def _analyze_definition_conflict(self, unit1: Dict[str, Any], unit2: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Analyze two units for definitional conflicts."""
        def1 = unit1.get('definition', '').lower().strip()
        def2 = unit2.get('definition', '').lower().strip()

        if not def1 or not def2:
            return None

        # Check for direct contradictions
        contradictory_pairs = [
            (r'\bis\b', r'\bis not\b'),
            (r'\bcan\b', r'\bcannot\b'),
            (r'\bhas\b', r'\blacks\b'),
            (r'\bincludes?\b', r'\bexcludes?\b'),
            (r'\ballows?\b', r'\bprevents?\b'),
            (r'\benables?\b', r'\bdisables?\b'),
            (r'\bpositive\b', r'\bnegative\b'),
            (r'\btrue\b', r'\bfalse\b'),
        ]

        conflicts_found = []
        for positive, negative in contradictory_pairs:
            if re.search(positive, def1) and re.search(negative, def2):
                conflicts_found.append(f"Contradiction: {positive.strip('\\b')} vs {negative.strip('\\b')}")
            elif re.search(negative, def1) and re.search(positive, def2):
                conflicts_found.append(f"Contradiction: {negative.strip('\\b')} vs {positive.strip('\\b')}")

        # Check similarity but with opposing language
        similarity = SequenceMatcher(None, def1, def2).ratio()
        has_negation1 = bool(re.search(r'\b(?:not|no|never|without)\b', def1))
        has_negation2 = bool(re.search(r'\b(?:not|no|never|without)\b', def2))

        if similarity > 0.6 and has_negation1 != has_negation2:
            conflicts_found.append("Similar definitions with opposing negation patterns")

        if conflicts_found:
            severity = 'high' if len(conflicts_found) > 1 else 'medium'
            return {
                'conflicts': conflicts_found,
                'similarity_score': similarity,
                'severity': severity,
                'def1_length': len(def1),
                'def2_length': len(def2)
            }

        return None

    def detect_relationship_contradictions(self) -> List[Dict[str, Any]]:
        """Find contradictory relationships between concepts."""
        contradictions = []

        # Build relationship matrix
        positive_relations = defaultdict(set)
        negative_relations = defaultdict(set)

        for unit in self.units:
            unit_id = unit['id']
            relations = unit.get('relations', [])

            for relation in relations:
                if isinstance(relation, dict):
                    target_id = relation.get('id') or relation.get('concept_id')
                    relation_type = relation.get('type', '').lower()

                    if target_id:
                        if any(neg in relation_type for neg in ['not', 'contra', 'opposite', 'against']):
                            negative_relations[unit_id].add(target_id)
                        else:
                            positive_relations[unit_id].add(target_id)

        # Find contradictions
        for unit_id in positive_relations:
            pos_targets = positive_relations[unit_id]
            neg_targets = negative_relations.get(unit_id, set())

            # Direct contradiction: A->B and A->!B
            common_targets = pos_targets & neg_targets
            for target in common_targets:
                contradictions.append({
                    'source_id': unit_id,
                    'target_id': target,
                    'contradiction_type': 'direct_relationship_contradiction',
                    'details': f"Unit {unit_id} has both positive and negative relations to {target}",
                    'severity': 'high'
                })

            # Indirect contradiction: A->B and B->!A
            for target in pos_targets:
                if target in self.id_to_unit:
                    target_negative_relations = negative_relations.get(target, set())
                    if unit_id in target_negative_relations:
                        contradictions.append({
                            'source_id': unit_id,
                            'target_id': target,
                            'contradiction_type': 'bidirectional_relationship_contradiction',
                            'details': f"Unit {unit_id} relates positively to {target}, but {target} relates negatively to {unit_id}",
                            'severity': 'medium'
                        })

        return contradictions

    def detect_mathematical_contradictions(self) -> List[Dict[str, Any]]:
        """Find contradictions in mathematical formulations."""
        contradictions = []

        # Group units with mathematical formulations by type
        math_units = [u for u in self.units if u.get('mathematical_formulation')]

        for i, unit1 in enumerate(math_units):
            for unit2 in math_units[i + 1:]:
                if unit1.get('type') == unit2.get('type'):
                    contradiction = self._analyze_math_contradiction(unit1, unit2)
                    if contradiction:
                        contradictions.append(contradiction)

        return contradictions

    def _analyze_math_contradiction(self, unit1: Dict[str, Any], unit2: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Analyze mathematical formulations for contradictions."""
        math1 = unit1.get('mathematical_formulation', '').strip()
        math2 = unit2.get('mathematical_formulation', '').strip()

        if not math1 or not math2:
            return None

        # Look for obvious contradictions in mathematical statements
        contradictory_patterns = [
            (r'=\s*0', r'>\s*0'),
            (r'=\s*0', r'<\s*0'),
            (r'>\s*0', r'<\s*0'),
            (r'=\s*\+', r'=\s*-'),
            (r'\binfinity\b', r'\bfinite\b'),
            (r'\bunique\b', r'\bmultiple\b'),
            (r'\bexists\b', r'\bnot exist'),
        ]

        conflicts = []
        for pattern1, pattern2 in contradictory_patterns:
            if re.search(pattern1, math1) and re.search(pattern2, math2):
                conflicts.append(f"Mathematical contradiction: {pattern1} vs {pattern2}")
            elif re.search(pattern2, math1) and re.search(pattern1, math2):
                conflicts.append(f"Mathematical contradiction: {pattern2} vs {pattern1}")

        if conflicts:
            return {
                'unit1_id': unit1['id'],
                'unit2_id': unit2['id'],
                'contradiction_type': 'mathematical_formulation_contradiction',
                'conflicts': conflicts,
                'severity': 'high',
                'math1': math1[:200],
                'math2': math2[:200]
            }

        return None

    def detect_semantic_contradictions(self) -> List[Dict[str, Any]]:
        """Find semantic contradictions using pattern matching."""
        contradictions = []

        # Look for antonym patterns within the same conceptual space
        antonym_pairs = [
            ('increase', 'decrease'), ('growth', 'decay'), ('expansion', 'contraction'),
            ('positive', 'negative'), ('creation', 'destruction'), ('order', 'chaos'),
            ('finite', 'infinite'), ('discrete', 'continuous'), ('static', 'dynamic'),
            ('simple', 'complex'), ('linear', 'nonlinear'), ('stable', 'unstable')
        ]

        # Group by semantic similarity
        for unit_type, units in self.type_groups.items():
            if len(units) < 2:
                continue

            for i, unit1 in enumerate(units):
                for unit2 in units[i + 1:]:
                    contradiction = self._find_semantic_contradiction(unit1, unit2, antonym_pairs)
                    if contradiction:
                        contradictions.append(contradiction)

        return contradictions

    def _find_semantic_contradiction(self, unit1: Dict[str, Any], unit2: Dict[str, Any], antonym_pairs: List[Tuple[str, str]]) -> Optional[Dict[str, Any]]:
        """Find semantic contradictions between two units."""
        def1 = unit1.get('definition', '').lower()
        def2 = unit2.get('definition', '').lower()

        contradictions_found = []

        for word1, word2 in antonym_pairs:
            if word1 in def1 and word2 in def2:
                contradictions_found.append(f"Semantic antonyms: {word1} vs {word2}")
            elif word2 in def1 and word1 in def2:
                contradictions_found.append(f"Semantic antonyms: {word2} vs {word1}")

        if contradictions_found:
            return {
                'unit1_id': unit1['id'],
                'unit2_id': unit2['id'],
                'contradiction_type': 'semantic_contradiction',
                'contradictions': contradictions_found,
                'severity': 'medium'
            }

        return None

    def analyze_all_contradictions(self) -> Dict[str, List[Dict[str, Any]]]:
        """Run all contradiction detection methods."""
        return {
            'conflicting_definitions': self.detect_conflicting_definitions(),
            'relationship_contradictions': self.detect_relationship_contradictions(),
            'mathematical_contradictions': self.detect_mathematical_contradictions(),
            'semantic_contradictions': self.detect_semantic_contradictions()
        }

    def export_contradiction_report(self, output_path: str) -> None:
        """Export contradiction analysis results to JSON file."""
        contradictions = self.analyze_all_contradictions()

        # Add summary statistics
        report = {
            'metadata': {
                'total_concepts': len(self.units),
                'total_contradictions_found': sum(len(contradiction_list) for contradiction_list in contradictions.values()),
                'analysis_date': json.dumps({}),  # Will be filled with actual timestamp
                'contradiction_types': list(contradictions.keys())
            },
            'summary': {
                contradiction_type: {
                    'count': len(contradiction_list),
                    'severity_breakdown': self._get_severity_breakdown(contradiction_list)
                }
                for contradiction_type, contradiction_list in contradictions.items()
            },
            'contradictions': contradictions
        }

        import datetime
        report['metadata']['analysis_date'] = datetime.datetime.now().isoformat()

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)

    def _get_severity_breakdown(self, contradiction_list: List[Dict[str, Any]]) -> Dict[str, int]:
        """Get breakdown of contradictions by severity."""
        breakdown = {'high': 0, 'medium': 0, 'low': 0}
        for contradiction in contradiction_list:
            severity = contradiction.get('severity', 'medium')
            breakdown[severity] = breakdown.get(severity, 0) + 1
        return breakdown