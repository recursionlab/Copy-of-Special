"""
Bridge Proposer - suggests conceptual bridges and synthesis opportunities between disparate concepts.

Proposes:
- Intermediate concepts to bridge gaps
- Synthesis frameworks for reconciling contradictions
- Meta-concepts that unify diverse ideas
- Structural patterns across concept domains
"""

from typing import Dict, List, Set, Tuple, Any, Optional
import json
import re
from collections import defaultdict, Counter
import math


class BridgeProposer:
    """Proposes conceptual bridges and synthesis opportunities."""

    def __init__(self, units: List[Dict[str, Any]], gaps: Dict[str, List[Dict[str, Any]]],
                 contradictions: Dict[str, List[Dict[str, Any]]]):
        self.units = units
        self.gaps = gaps
        self.contradictions = contradictions
        self.id_to_unit = {u['id']: u for u in units}
        self.bridge_patterns = self._initialize_bridge_patterns()

    def _initialize_bridge_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Initialize common patterns for bridging concepts."""
        return {
            'hierarchical': {
                'description': 'Create hierarchical relationship where one concept subsumes another',
                'templates': [
                    '{concept1} as a special case of {concept2}',
                    '{concept2} as a generalization of {concept1}',
                    '{concept1} and {concept2} as instances of a higher-order {category}'
                ]
            },
            'compositional': {
                'description': 'Bridge through compositional relationships',
                'templates': [
                    '{concept1} composed of {concept2} elements',
                    '{concept2} as a component of {concept1}',
                    'System combining {concept1} and {concept2} properties'
                ]
            },
            'transformational': {
                'description': 'Bridge through transformation or process',
                'templates': [
                    'Process transforming {concept1} into {concept2}',
                    'Dynamic evolution from {concept1} to {concept2}',
                    'Transition mechanism between {concept1} and {concept2}'
                ]
            },
            'functional': {
                'description': 'Bridge through functional relationships',
                'templates': [
                    '{concept1} enables or facilitates {concept2}',
                    '{concept2} regulates or controls {concept1}',
                    'Feedback loop between {concept1} and {concept2}'
                ]
            },
            'analogical': {
                'description': 'Bridge through analogy or structural similarity',
                'templates': [
                    '{concept1} and {concept2} share structural patterns',
                    'Analogical mapping between {concept1} and {concept2}',
                    'Isomorphism connecting {concept1} and {concept2}'
                ]
            },
            'contextual': {
                'description': 'Bridge through shared contexts or environments',
                'templates': [
                    '{concept1} and {concept2} co-occur in {context}',
                    'Environmental conditions supporting both {concept1} and {concept2}',
                    'Shared ecological niche for {concept1} and {concept2}'
                ]
            },
            'mathematical': {
                'description': 'Bridge through mathematical formalization',
                'templates': [
                    'Mathematical framework unifying {concept1} and {concept2}',
                    'Formal system encompassing {concept1} and {concept2}',
                    'Algebraic structure relating {concept1} and {concept2}'
                ]
            }
        }

    def propose_gap_bridges(self) -> List[Dict[str, Any]]:
        """Propose bridges for identified gaps."""
        bridges = []

        # Bridges for orphaned concepts
        for orphan in self.gaps.get('orphaned_concepts', []):
            orphan_id = orphan['id']
            orphan_unit = self.id_to_unit.get(orphan_id)

            if not orphan_unit:
                continue

            # Find potential bridge targets based on similarity
            bridge_targets = self._find_potential_connections(orphan_unit)

            for target_id, similarity_score in bridge_targets:
                target_unit = self.id_to_unit[target_id]
                bridge = self._generate_bridge_proposal(orphan_unit, target_unit, similarity_score)
                if bridge:
                    bridge.update({
                        'bridge_type': 'orphan_integration',
                        'gap_source': 'orphaned_concept',
                        'priority': 'medium'
                    })
                    bridges.append(bridge)

        # Bridges for missing bidirectional relations
        for missing_rel in self.gaps.get('missing_bidirectional_relations', []):
            from_id = missing_rel['from_id']
            to_id = missing_rel['to_id']

            from_unit = self.id_to_unit.get(from_id)
            to_unit = self.id_to_unit.get(to_id)

            if from_unit and to_unit:
                bridge = self._generate_bridge_proposal(from_unit, to_unit, 0.8)  # High confidence for existing relation
                if bridge:
                    bridge.update({
                        'bridge_type': 'bidirectional_completion',
                        'gap_source': 'missing_bidirectional_relation',
                        'priority': 'high'
                    })
                    bridges.append(bridge)

        # Bridges for isolated clusters
        for cluster in self.gaps.get('isolated_clusters', []):
            cluster_concepts = cluster.get('concept_ids', [])
            if len(cluster_concepts) > 1:
                # Propose bridges to connect cluster to main network
                main_network_concepts = self._identify_main_network_concepts()
                cluster_bridge = self._propose_cluster_bridge(cluster_concepts, main_network_concepts)
                if cluster_bridge:
                    bridges.append(cluster_bridge)

        return bridges

    def propose_contradiction_bridges(self) -> List[Dict[str, Any]]:
        """Propose bridges to resolve contradictions."""
        bridges = []

        # Bridges for conflicting definitions
        for conflict in self.contradictions.get('conflicting_definitions', []):
            unit1_id = conflict['unit1_id']
            unit2_id = conflict['unit2_id']

            unit1 = self.id_to_unit.get(unit1_id)
            unit2 = self.id_to_unit.get(unit2_id)

            if unit1 and unit2:
                synthesis_bridge = self._generate_synthesis_bridge(unit1, unit2, conflict)
                if synthesis_bridge:
                    synthesis_bridge.update({
                        'bridge_type': 'contradiction_synthesis',
                        'priority': 'high'
                    })
                    bridges.append(synthesis_bridge)

        # Bridges for relationship contradictions
        for rel_contradiction in self.contradictions.get('relationship_contradictions', []):
            source_id = rel_contradiction['source_id']
            target_id = rel_contradiction['target_id']

            source_unit = self.id_to_unit.get(source_id)
            target_unit = self.id_to_unit.get(target_id)

            if source_unit and target_unit:
                resolution_bridge = self._generate_relationship_resolution_bridge(
                    source_unit, target_unit, rel_contradiction
                )
                if resolution_bridge:
                    bridges.append(resolution_bridge)

        return bridges

    def propose_creative_bridges(self) -> List[Dict[str, Any]]:
        """Propose creative bridges between seemingly unrelated concepts."""
        bridges = []

        # Find concept pairs with potential for creative connection
        creative_pairs = self._identify_creative_bridge_opportunities()

        for concept1, concept2, connection_basis in creative_pairs:
            unit1 = self.id_to_unit.get(concept1)
            unit2 = self.id_to_unit.get(concept2)

            if unit1 and unit2:
                creative_bridge = self._generate_creative_bridge(unit1, unit2, connection_basis)
                if creative_bridge:
                    creative_bridge.update({
                        'bridge_type': 'creative_synthesis',
                        'priority': 'low',
                        'innovation_potential': 'high'
                    })
                    bridges.append(creative_bridge)

        return bridges

    def _find_potential_connections(self, orphan_unit: Dict[str, Any]) -> List[Tuple[str, float]]:
        """Find potential connections for an orphaned concept."""
        connections = []
        orphan_tags = set(orphan_unit.get('tags', []))
        orphan_type = orphan_unit.get('type', '')
        orphan_definition = orphan_unit.get('definition', '').lower()

        for unit in self.units:
            if unit['id'] == orphan_unit['id']:
                continue

            similarity_score = 0

            # Tag similarity
            unit_tags = set(unit.get('tags', []))
            if orphan_tags and unit_tags:
                tag_similarity = len(orphan_tags & unit_tags) / len(orphan_tags | unit_tags)
                similarity_score += tag_similarity * 0.4

            # Type compatibility
            if unit.get('type') == orphan_type:
                similarity_score += 0.3

            # Definition similarity (simple keyword matching)
            unit_definition = unit.get('definition', '').lower()
            if orphan_definition and unit_definition:
                common_words = set(orphan_definition.split()) & set(unit_definition.split())
                if common_words:
                    word_similarity = len(common_words) / max(len(orphan_definition.split()), len(unit_definition.split()))
                    similarity_score += word_similarity * 0.3

            if similarity_score > 0.2:  # Threshold for potential connection
                connections.append((unit['id'], similarity_score))

        return sorted(connections, key=lambda x: x[1], reverse=True)[:5]

    def _generate_bridge_proposal(self, unit1: Dict[str, Any], unit2: Dict[str, Any],
                                confidence: float) -> Optional[Dict[str, Any]]:
        """Generate a bridge proposal between two concepts."""
        type1 = unit1.get('type', 'concept')
        type2 = unit2.get('type', 'concept')

        # Choose appropriate bridge pattern
        bridge_pattern = self._select_bridge_pattern(unit1, unit2)

        if not bridge_pattern:
            return None

        pattern_name, pattern_info = bridge_pattern
        template = pattern_info['templates'][0]  # Use first template

        bridge_description = template.format(concept1=type1, concept2=type2)

        return {
            'source_concept': unit1['id'],
            'target_concept': unit2['id'],
            'bridge_pattern': pattern_name,
            'bridge_description': bridge_description,
            'confidence_score': confidence,
            'supporting_evidence': self._gather_supporting_evidence(unit1, unit2),
            'implementation_steps': self._suggest_implementation_steps(pattern_name, unit1, unit2)
        }

    def _select_bridge_pattern(self, unit1: Dict[str, Any], unit2: Dict[str, Any]) -> Optional[Tuple[str, Dict[str, Any]]]:
        """Select the most appropriate bridge pattern for two concepts."""
        # Simple heuristics for pattern selection
        def1 = unit1.get('definition', '').lower()
        def2 = unit2.get('definition', '').lower()

        # Mathematical if either has mathematical formulation
        if unit1.get('mathematical_formulation') or unit2.get('mathematical_formulation'):
            return 'mathematical', self.bridge_patterns['mathematical']

        # Hierarchical if one definition contains the other's terms
        if any(word in def2 for word in def1.split()[:5]) or any(word in def1 for word in def2.split()[:5]):
            return 'hierarchical', self.bridge_patterns['hierarchical']

        # Functional if process/action words are present
        process_words = ['process', 'function', 'operation', 'mechanism', 'enables', 'causes']
        if any(word in def1 or word in def2 for word in process_words):
            return 'functional', self.bridge_patterns['functional']

        # Default to analogical
        return 'analogical', self.bridge_patterns['analogical']

    def _generate_synthesis_bridge(self, unit1: Dict[str, Any], unit2: Dict[str, Any],
                                 conflict: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate a synthesis bridge to resolve contradictions."""
        conflicts = conflict.get('conflict_details', {}).get('conflicts', [])

        # Analyze the nature of the contradiction
        synthesis_strategies = []

        if 'negation' in str(conflicts).lower():
            synthesis_strategies.append({
                'strategy': 'conditional_validity',
                'description': f"Both {unit1.get('type')} and {unit2.get('type')} may be valid under different conditions"
            })

        if 'similarity_score' in conflict.get('conflict_details', {}):
            score = conflict['conflict_details']['similarity_score']
            if score > 0.7:
                synthesis_strategies.append({
                    'strategy': 'complementary_aspects',
                    'description': f"{unit1.get('type')} and {unit2.get('type')} may represent complementary aspects of the same phenomenon"
                })

        # Generate synthesis proposal
        if synthesis_strategies:
            strategy = synthesis_strategies[0]
            return {
                'source_concept': unit1['id'],
                'target_concept': unit2['id'],
                'synthesis_strategy': strategy['strategy'],
                'synthesis_description': strategy['description'],
                'conflict_resolution': 'synthesis_framework',
                'confidence_score': 0.6,
                'validation_criteria': self._suggest_validation_criteria(unit1, unit2, strategy)
            }

        return None

    def _generate_relationship_resolution_bridge(self, unit1: Dict[str, Any], unit2: Dict[str, Any],
                                               contradiction: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate bridge to resolve relationship contradictions."""
        return {
            'source_concept': unit1['id'],
            'target_concept': unit2['id'],
            'bridge_type': 'relationship_resolution',
            'resolution_approach': 'contextual_differentiation',
            'description': f"Differentiate contexts where {unit1.get('type')} and {unit2.get('type')} have different relationship types",
            'priority': 'high',
            'confidence_score': 0.7,
            'implementation_steps': [
                f"Identify contexts for {unit1.get('type')}",
                f"Identify contexts for {unit2.get('type')}",
                "Map relationship types to specific contexts",
                "Validate context-dependent relationships"
            ]
        }

    def _identify_creative_bridge_opportunities(self) -> List[Tuple[str, str, str]]:
        """Identify opportunities for creative bridges between distant concepts."""
        opportunities = []

        # Group concepts by different dimensions
        type_groups = defaultdict(list)
        source_groups = defaultdict(list)

        for unit in self.units:
            unit_type = unit.get('type', 'unknown')
            source = unit.get('source', '')

            type_groups[unit_type].append(unit['id'])
            if source:
                source_groups[source].append(unit['id'])

        # Find cross-type, cross-source opportunities
        types = list(type_groups.keys())
        for i, type1 in enumerate(types):
            for type2 in types[i+2:]:  # Skip adjacent types for more creative combinations
                if len(type_groups[type1]) > 0 and len(type_groups[type2]) > 0:
                    # Sample one concept from each type
                    concept1 = type_groups[type1][0]
                    concept2 = type_groups[type2][0]
                    connection_basis = f"cross-type_synthesis_{type1}_{type2}"
                    opportunities.append((concept1, concept2, connection_basis))

        return opportunities[:10]  # Limit for creativity focus

    def _generate_creative_bridge(self, unit1: Dict[str, Any], unit2: Dict[str, Any],
                                connection_basis: str) -> Optional[Dict[str, Any]]:
        """Generate a creative bridge between distant concepts."""
        type1 = unit1.get('type', 'concept')
        type2 = unit2.get('type', 'concept')

        # Creative bridge templates
        creative_templates = [
            f"Novel framework integrating {type1} and {type2} principles",
            f"Emergent properties arising from {type1}-{type2} interaction",
            f"Meta-theory encompassing both {type1} and {type2} domains",
            f"Hybrid model combining {type1} structure with {type2} dynamics"
        ]

        template = creative_templates[0]  # Use first template

        return {
            'source_concept': unit1['id'],
            'target_concept': unit2['id'],
            'bridge_description': template,
            'connection_basis': connection_basis,
            'creativity_indicators': [
                'cross_domain_synthesis',
                'novel_framework_potential',
                'emergent_properties'
            ],
            'confidence_score': 0.4,  # Lower confidence for creative bridges
            'research_value': 'high_risk_high_reward'
        }

    def _gather_supporting_evidence(self, unit1: Dict[str, Any], unit2: Dict[str, Any]) -> List[str]:
        """Gather supporting evidence for a bridge proposal."""
        evidence = []

        # Shared tags
        tags1 = set(unit1.get('tags', []))
        tags2 = set(unit2.get('tags', []))
        shared_tags = tags1 & tags2
        if shared_tags:
            evidence.append(f"Shared tags: {', '.join(shared_tags)}")

        # Same source
        if unit1.get('source') == unit2.get('source'):
            evidence.append(f"Co-occurrence in source: {unit1.get('source', '')}")

        # Similar confidence scores
        conf1 = unit1.get('confidence_score', 0.5)
        conf2 = unit2.get('confidence_score', 0.5)
        if abs(conf1 - conf2) < 0.1:
            evidence.append(f"Similar confidence levels: {conf1:.2f}, {conf2:.2f}")

        return evidence

    def _suggest_implementation_steps(self, pattern_name: str, unit1: Dict[str, Any],
                                    unit2: Dict[str, Any]) -> List[str]:
        """Suggest implementation steps for a bridge pattern."""
        base_steps = [
            f"Define formal relationship between {unit1.get('type')} and {unit2.get('type')}",
            "Identify key properties and constraints",
            "Develop testable hypotheses",
            "Design validation experiments"
        ]

        pattern_specific = {
            'mathematical': [
                "Formalize mathematical structures",
                "Prove relationship theorems",
                "Implement computational models"
            ],
            'hierarchical': [
                "Establish subsumption relationships",
                "Define inheritance properties",
                "Validate taxonomic structure"
            ],
            'functional': [
                "Map functional dependencies",
                "Identify causal mechanisms",
                "Test functional hypotheses"
            ]
        }

        specific_steps = pattern_specific.get(pattern_name, [])
        return base_steps + specific_steps

    def _suggest_validation_criteria(self, unit1: Dict[str, Any], unit2: Dict[str, Any],
                                   strategy: Dict[str, Any]) -> List[str]:
        """Suggest criteria for validating synthesis proposals."""
        return [
            "Empirical evidence supports synthesis",
            "Logical consistency maintained",
            "Predictive power enhanced",
            "Explanatory scope increased",
            "Practical applications identified"
        ]

    def _identify_main_network_concepts(self) -> List[str]:
        """Identify concepts that are part of the main network (most connected)."""
        # Count relationships for each concept
        connection_counts = defaultdict(int)

        for unit in self.units:
            relations = unit.get('relations', [])
            connection_counts[unit['id']] = len(relations)

        # Return top connected concepts
        sorted_concepts = sorted(connection_counts.items(), key=lambda x: x[1], reverse=True)
        return [concept_id for concept_id, count in sorted_concepts[:20] if count > 0]

    def _propose_cluster_bridge(self, cluster_concepts: List[str],
                              main_network_concepts: List[str]) -> Optional[Dict[str, Any]]:
        """Propose bridge to connect isolated cluster to main network."""
        if not cluster_concepts or not main_network_concepts:
            return None

        # Find best bridge candidates
        cluster_sample = cluster_concepts[:3]  # Sample from cluster
        main_sample = main_network_concepts[:5]  # Sample from main network

        best_bridge = None
        best_score = 0

        for cluster_id in cluster_sample:
            for main_id in main_sample:
                cluster_unit = self.id_to_unit.get(cluster_id)
                main_unit = self.id_to_unit.get(main_id)

                if cluster_unit and main_unit:
                    # Calculate potential bridge score
                    score = self._calculate_bridge_score(cluster_unit, main_unit)
                    if score > best_score:
                        best_score = score
                        best_bridge = (cluster_unit, main_unit, score)

        if best_bridge:
            cluster_unit, main_unit, score = best_bridge
            return {
                'bridge_type': 'cluster_integration',
                'source_concept': cluster_unit['id'],
                'target_concept': main_unit['id'],
                'cluster_size': len(cluster_concepts),
                'integration_score': score,
                'priority': 'medium',
                'description': f"Bridge isolated cluster through {cluster_unit.get('type')} to {main_unit.get('type')} connection"
            }

        return None

    def _calculate_bridge_score(self, unit1: Dict[str, Any], unit2: Dict[str, Any]) -> float:
        """Calculate potential bridge score between two units."""
        score = 0

        # Tag overlap
        tags1 = set(unit1.get('tags', []))
        tags2 = set(unit2.get('tags', []))
        if tags1 and tags2:
            score += len(tags1 & tags2) / len(tags1 | tags2) * 0.4

        # Type compatibility
        if unit1.get('type') == unit2.get('type'):
            score += 0.3

        # Confidence scores
        conf1 = unit1.get('confidence_score', 0.5)
        conf2 = unit2.get('confidence_score', 0.5)
        score += (conf1 + conf2) / 2 * 0.3

        return score

    def generate_all_bridges(self) -> Dict[str, List[Dict[str, Any]]]:
        """Generate all types of bridge proposals."""
        return {
            'gap_bridges': self.propose_gap_bridges(),
            'contradiction_bridges': self.propose_contradiction_bridges(),
            'creative_bridges': self.propose_creative_bridges()
        }

    def export_bridge_proposals(self, output_path: str) -> None:
        """Export bridge proposals to JSON file."""
        bridges = self.generate_all_bridges()

        # Calculate summary statistics
        total_bridges = sum(len(bridge_list) for bridge_list in bridges.values())
        high_priority = sum(1 for bridge_list in bridges.values()
                          for bridge in bridge_list if bridge.get('priority') == 'high')

        report = {
            'metadata': {
                'total_bridges': total_bridges,
                'high_priority_bridges': high_priority,
                'generation_date': None,  # Will be filled
                'bridge_categories': list(bridges.keys())
            },
            'summary': {
                category: len(bridge_list) for category, bridge_list in bridges.items()
            },
            'bridge_proposals': bridges
        }

        import datetime
        report['metadata']['generation_date'] = datetime.datetime.now().isoformat()

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)