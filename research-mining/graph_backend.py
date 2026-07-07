#!/usr/bin/env python3
"""
Graph Backend for Knowledge Evolution Engine v2.1
Neo4j integration replacing in-memory storage
"""

import json
import yaml
from typing import Dict, List, Optional, Any
from datetime import datetime
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable, AuthError
import logging

from knowledge_evolution_v2_1 import (
    ConceptUnit, ConceptRelation, ConceptContradiction,
    ConceptState, QualityTier, RefinementPriority
)

class GraphBackedKnowledgeEngine:
    """Neo4j-backed knowledge evolution engine"""

    def __init__(self, config_path: str = "config.yaml"):
        """Initialize with configuration"""
        self.config = self._load_config(config_path)
        self.driver = None
        self._setup_database()

    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from YAML file"""
        try:
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            # Fallback to default configuration
            return {
                'database': {
                    'neo4j_uri': 'bolt://localhost:7687',
                    'neo4j_user': 'neo4j',
                    'neo4j_password': 'knowledge123'
                }
            }

    def _setup_database(self):
        """Initialize Neo4j connection and constraints"""
        try:
            self.driver = GraphDatabase.driver(
                self.config['database']['neo4j_uri'],
                auth=(
                    self.config['database']['neo4j_user'],
                    self.config['database']['neo4j_password']
                )
            )

            # Verify connection
            with self.driver.session() as session:
                session.run("RETURN 1")

            # Create constraints and indexes
            self._create_schema()
            logging.info("Neo4j connection established successfully")

        except (ServiceUnavailable, AuthError) as e:
            logging.warning(f"Neo4j not available: {e}. Falling back to in-memory storage.")
            self.driver = None

    def _create_schema(self):
        """Create Neo4j constraints and indexes"""
        if not self.driver:
            return

        constraints_and_indexes = [
            # Unique constraints
            "CREATE CONSTRAINT concept_id_unique IF NOT EXISTS FOR (c:Concept) REQUIRE c.id IS UNIQUE",

            # Indexes for performance
            "CREATE INDEX concept_label_index IF NOT EXISTS FOR (c:Concept) ON (c.label)",
            "CREATE INDEX concept_quality_tier_index IF NOT EXISTS FOR (c:Concept) ON (c.quality_tier)",
            "CREATE INDEX concept_state_index IF NOT EXISTS FOR (c:Concept) ON (c.state)",
            "CREATE INDEX concept_generation_index IF NOT EXISTS FOR (c:Concept) ON (c.generation)",
        ]

        with self.driver.session() as session:
            for query in constraints_and_indexes:
                try:
                    session.run(query)
                except Exception as e:
                    logging.debug(f"Schema creation query failed (may already exist): {e}")

    def store_concept(self, concept: ConceptUnit) -> bool:
        """Store concept in Neo4j with full schema properties"""
        if not self.driver:
            return False

        try:
            with self.driver.session() as session:
                # Convert concept to dict for storage
                concept_data = {
                    'id': concept.id,
                    'label': concept.label,
                    'definition_full': concept.definition_full,
                    'source_evidence': concept.source_evidence,
                    'lineage': concept.lineage,
                    'generation': concept.generation,
                    'state': concept.state.value,
                    'quality_tier': concept.quality_tier.value,
                    'refinement_priority': concept.refinement_priority.value,
                    'timestamp': concept.timestamp,

                    # Metrics (embedded in ConceptUnit in v2.1)
                    'support_strength': concept.support_strength,
                    'definition_completeness': concept.definition_completeness,
                    'refinement_potential': concept.refinement_potential,
                    'evidence_strength': concept.evidence_strength,
                    'merge_count': concept.merge_count,
                    'refinement_attempts': concept.refinement_attempts,
                    'successful_refinements': concept.successful_refinements
                }

                # Create or update concept
                session.run("""
                    MERGE (c:Concept {id: $id})
                    SET c += $concept_data
                """, id=concept.id, concept_data=concept_data)

                # Store relations
                for relation in concept.relations:
                    session.run("""
                        MATCH (source:Concept {id: $source_id})
                        MATCH (target:Concept {id: $target_id})
                        MERGE (source)-[r:RELATES {type: $relation_type}]->(target)
                        SET r.evidence = $evidence,
                            r.confidence = $confidence
                    """,
                    source_id=concept.id,
                    target_id=relation.target_id,
                    relation_type=relation.type,
                    evidence=relation.evidence,
                    confidence=relation.confidence
                    )

                # Store contradictions
                for contradiction in concept.contradictions:
                    session.run("""
                        MATCH (source:Concept {id: $source_id})
                        MATCH (target:Concept {id: $target_id})
                        MERGE (source)-[r:CONTRADICTS]->(target)
                        SET r.basis = $basis,
                            r.resolution_confidence = $resolution_confidence
                    """,
                    source_id=concept.id,
                    target_id=contradiction.with_id,
                    basis=contradiction.contradiction_basis,
                    resolution_confidence=contradiction.resolution_confidence
                    )

                return True

        except Exception as e:
            logging.error(f"Failed to store concept {concept.id}: {e}")
            return False

    def get_concept(self, concept_id: str) -> Optional[ConceptUnit]:
        """Retrieve concept from Neo4j"""
        if not self.driver:
            return None

        try:
            with self.driver.session() as session:
                result = session.run("""
                    MATCH (c:Concept {id: $concept_id})
                    OPTIONAL MATCH (c)-[rel:RELATES]->(target:Concept)
                    OPTIONAL MATCH (c)-[contra:CONTRADICTS]->(contra_target:Concept)
                    RETURN c,
                           collect(DISTINCT {
                               type: rel.type,
                               target_id: target.id,
                               evidence: rel.evidence,
                               confidence: rel.confidence
                           }) as relations,
                           collect(DISTINCT {
                               with_id: contra_target.id,
                               contradiction_basis: contra.basis,
                               resolution_confidence: contra.resolution_confidence
                           }) as contradictions
                """, concept_id=concept_id)

                record = result.single()
                if not record:
                    return None

                # Reconstruct ConceptUnit from Neo4j data
                c = record['c']
                relations_data = [r for r in record['relations'] if r['target_id']]
                contradictions_data = [r for r in record['contradictions'] if r['with_id']]

                # Create relations and contradictions objects
                relations = [
                    ConceptRelation(
                        type=r['type'],
                        target_id=r['target_id'],
                        evidence=r['evidence'],
                        confidence=r['confidence']
                    ) for r in relations_data
                ]

                contradictions = [
                    ConceptContradiction(
                        with_id=r['with_id'],
                        contradiction_basis=r['contradiction_basis'],
                        resolution_confidence=r['resolution_confidence']
                    ) for r in contradictions_data
                ]

                # Reconstruct ConceptUnit
                concept = ConceptUnit(
                    id=c['id'],
                    label=c['label'],
                    definition_full=c['definition_full'],
                    source_evidence=c['source_evidence']
                )

                # Set additional properties
                concept.lineage = c.get('lineage', [])
                concept.generation = c.get('generation', 0)
                concept.state = ConceptState(c['state'])
                concept.quality_tier = QualityTier(c['quality_tier'])
                concept.refinement_priority = RefinementPriority(c['refinement_priority'])
                concept.relations = relations
                concept.contradictions = contradictions
                concept.timestamp = c['timestamp']

                # Set embedded metrics (v2.1 style)
                concept.support_strength = c.get('support_strength', 0.0)
                concept.definition_completeness = c.get('definition_completeness', 0.0)
                concept.refinement_potential = c.get('refinement_potential', 0.0)
                concept.evidence_strength = c.get('evidence_strength', 0.0)
                concept.merge_count = c.get('merge_count', 0)
                concept.refinement_attempts = c.get('refinement_attempts', 0)
                concept.successful_refinements = c.get('successful_refinements', 0)

                return concept

        except Exception as e:
            logging.error(f"Failed to retrieve concept {concept_id}: {e}")
            return None

    def get_all_concepts(self) -> List[ConceptUnit]:
        """Retrieve all concepts from Neo4j"""
        if not self.driver:
            return []

        try:
            with self.driver.session() as session:
                result = session.run("MATCH (c:Concept) RETURN c.id as id")
                concept_ids = [record['id'] for record in result]

                # Get each concept with full data
                concepts = []
                for concept_id in concept_ids:
                    concept = self.get_concept(concept_id)
                    if concept:
                        concepts.append(concept)

                return concepts

        except Exception as e:
            logging.error(f"Failed to retrieve all concepts: {e}")
            return []

    def get_concepts_by_quality_tier(self, tier: QualityTier) -> List[ConceptUnit]:
        """Get concepts filtered by quality tier"""
        if not self.driver:
            return []

        try:
            with self.driver.session() as session:
                result = session.run("""
                    MATCH (c:Concept {quality_tier: $tier})
                    RETURN c.id as id
                """, tier=tier.value)

                concept_ids = [record['id'] for record in result]
                concepts = []
                for concept_id in concept_ids:
                    concept = self.get_concept(concept_id)
                    if concept:
                        concepts.append(concept)

                return concepts

        except Exception as e:
            logging.error(f"Failed to retrieve concepts by tier {tier}: {e}")
            return []

    def get_graph_stats(self) -> Dict[str, Any]:
        """Get comprehensive graph statistics"""
        if not self.driver:
            return {}

        try:
            with self.driver.session() as session:
                # Count nodes and relationships
                stats_result = session.run("""
                    MATCH (c:Concept)
                    OPTIONAL MATCH ()-[rel:RELATES]->()
                    OPTIONAL MATCH ()-[contra:CONTRADICTS]->()
                    RETURN
                        count(DISTINCT c) as total_concepts,
                        count(DISTINCT rel) as relation_count,
                        count(DISTINCT contra) as contradiction_count
                """)

                stats = stats_result.single()

                # Quality tier distribution
                tier_result = session.run("""
                    MATCH (c:Concept)
                    RETURN c.quality_tier as tier, count(c) as count
                """)

                tier_counts = {record['tier']: record['count'] for record in tier_result}

                # State distribution
                state_result = session.run("""
                    MATCH (c:Concept)
                    RETURN c.state as state, count(c) as count
                """)

                state_counts = {record['state']: record['count'] for record in state_result}

                return {
                    'total_concepts': stats['total_concepts'],
                    'relation_count': stats['relation_count'],
                    'contradiction_count': stats['contradiction_count'],
                    'quality_tier_distribution': tier_counts,
                    'state_distribution': state_counts
                }

        except Exception as e:
            logging.error(f"Failed to get graph stats: {e}")
            return {}

    def close(self):
        """Close Neo4j connection"""
        if self.driver:
            self.driver.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()