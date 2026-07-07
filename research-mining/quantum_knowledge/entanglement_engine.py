"""
Quantum Entanglement Engine for Concepts
Instantaneous cross-domain knowledge updates and spooky action at a distance
"""

import numpy as np
import json
from typing import Dict, List, Tuple, Set, Optional
from dataclasses import dataclass
from datetime import datetime
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from .hyperdimensional_concepts import HyperConcept, HyperdimensionalSpace

@dataclass
class EntanglementBond:
    """Represents a quantum entanglement between concepts"""
    concept_id1: str
    concept_id2: str
    bond_strength: float  # 0.0 to 1.0
    bond_type: str  # 'semantic', 'causal', 'analogical', 'contradictory'
    spin_correlation: float  # -1.0 to 1.0 (Bell's theorem violation)
    creation_time: str
    last_activation: str
    activation_count: int = 0

class QuantumEntanglementNetwork:
    """Network of entangled concepts with instant updates"""

    def __init__(self, hyperspace: HyperdimensionalSpace):
        self.hyperspace = hyperspace
        self.entanglement_bonds: Dict[str, EntanglementBond] = {}
        self.concept_bond_index: Dict[str, Set[str]] = {}  # concept_id -> bond_ids
        self.spooky_action_log: List[Dict] = []
        self.bell_violations: List[Dict] = []
        self.update_lock = threading.Lock()

    def create_entanglement(self, concept_id1: str, concept_id2: str,
                          bond_type: str = 'semantic',
                          strength: float = 0.8) -> str:
        """Create quantum entanglement between two concepts"""

        if concept_id1 not in self.hyperspace.concepts or concept_id2 not in self.hyperspace.concepts:
            raise ValueError("One or both concepts not found in hyperspace")

        # Generate unique bond ID
        bond_id = f"bond-{hash(f'{concept_id1}-{concept_id2}-{bond_type}') % 1000000:06d}"

        # Calculate spin correlation based on concept similarity
        concept1 = self.hyperspace.concepts[concept_id1]
        concept2 = self.hyperspace.concepts[concept_id2]

        similarity = self.hyperspace.quantum_similarity(concept_id1, concept_id2)

        # Spin correlation: similar concepts have correlated spins
        if bond_type == 'contradictory':
            spin_correlation = -abs(similarity)  # Anti-correlated
        else:
            spin_correlation = similarity  # Correlated

        bond = EntanglementBond(
            concept_id1=concept_id1,
            concept_id2=concept_id2,
            bond_strength=strength,
            bond_type=bond_type,
            spin_correlation=spin_correlation,
            creation_time=datetime.now().isoformat(),
            last_activation=datetime.now().isoformat()
        )

        # Store bond
        self.entanglement_bonds[bond_id] = bond

        # Update indices
        if concept_id1 not in self.concept_bond_index:
            self.concept_bond_index[concept_id1] = set()
        if concept_id2 not in self.concept_bond_index:
            self.concept_bond_index[concept_id2] = set()

        self.concept_bond_index[concept_id1].add(bond_id)
        self.concept_bond_index[concept_id2].add(bond_id)

        # Apply entanglement to hyperspace
        self.hyperspace.entangle_concepts(concept_id1, concept_id2, strength)

        print(f"Created {bond_type} entanglement: {concept1.term} <-> {concept2.term}")
        return bond_id

    def quantum_measurement_cascade(self, concept_id: str, measurement_type: str,
                                  measurement_result: any) -> List[Dict]:
        """Instant updates to entangled concepts when one is measured"""

        cascade_effects = []

        if concept_id not in self.concept_bond_index:
            return cascade_effects

        with self.update_lock:
            # Find all entangled concepts
            bond_ids = self.concept_bond_index[concept_id]

            for bond_id in bond_ids:
                bond = self.entanglement_bonds[bond_id]

                # Determine the entangled partner
                partner_id = bond.concept_id2 if bond.concept_id1 == concept_id else bond.concept_id1
                partner_concept = self.hyperspace.concepts[partner_id]

                # Calculate spooky action effect
                effect_strength = bond.bond_strength * abs(bond.spin_correlation)

                # Apply instantaneous update based on bond type
                if bond.bond_type == 'semantic':
                    # Similar semantic concepts align their quantum phases
                    measured_concept = self.hyperspace.concepts[concept_id]
                    phase_diff = measured_concept.quantum_phase - partner_concept.quantum_phase
                    phase_correction = effect_strength * phase_diff * 0.5

                    partner_concept.quantum_phase += phase_correction

                elif bond.bond_type == 'contradictory':
                    # Contradictory concepts anti-align
                    if measurement_type == 'definition':
                        # Boost opposite superposition states
                        for state, prob in partner_concept.superposition_components.items():
                            if state != measurement_result:
                                partner_concept.superposition_components[state] *= (1 + effect_strength * 0.1)

                elif bond.bond_type == 'causal':
                    # Causal concepts update coherence levels
                    if measurement_type == 'definition':
                        # Measuring cause increases effect's coherence
                        partner_concept.coherence_level *= (1 + effect_strength * 0.1)

                elif bond.bond_type == 'analogical':
                    # Analogical concepts share hyperstate features
                    measured_concept = self.hyperspace.concepts[concept_id]
                    hyperstate_influence = effect_strength * 0.05
                    partner_concept.hyperstate = (
                        (1 - hyperstate_influence) * partner_concept.hyperstate +
                        hyperstate_influence * measured_concept.hyperstate
                    )

                # Record spooky action
                spooky_event = {
                    "trigger_concept": concept_id,
                    "affected_concept": partner_id,
                    "bond_id": bond_id,
                    "bond_type": bond.bond_type,
                    "effect_strength": effect_strength,
                    "measurement_type": measurement_type,
                    "timestamp": datetime.now().isoformat()
                }

                self.spooky_action_log.append(spooky_event)
                cascade_effects.append(spooky_event)

                # Update bond activation
                bond.last_activation = datetime.now().isoformat()
                bond.activation_count += 1

                # Check for Bell inequality violation
                self.check_bell_violation(bond_id)

        return cascade_effects

    def check_bell_violation(self, bond_id: str):
        """Check if entanglement violates Bell inequalities (non-local hidden variables)"""
        bond = self.entanglement_bonds[bond_id]

        concept1 = self.hyperspace.concepts[bond.concept_id1]
        concept2 = self.hyperspace.concepts[bond.concept_id2]

        # Calculate CHSH inequality test
        # S = |E(a,b) - E(a,b') + E(a',b) + E(a',b')| ≤ 2 (classical)
        # Quantum mechanics can violate this up to 2√2 ≈ 2.828

        # Use quantum phases as measurement angles
        a = concept1.quantum_phase
        b = concept2.quantum_phase
        a_prime = a + np.pi/4
        b_prime = b + np.pi/4

        # Correlation functions (simplified quantum correlation)
        E_ab = bond.spin_correlation * np.cos(a - b)
        E_ab_prime = bond.spin_correlation * np.cos(a - b_prime)
        E_a_prime_b = bond.spin_correlation * np.cos(a_prime - b)
        E_a_prime_b_prime = bond.spin_correlation * np.cos(a_prime - b_prime)

        S = abs(E_ab - E_ab_prime + E_a_prime_b + E_a_prime_b_prime)

        if S > 2.0:  # Bell inequality violation detected!
            violation = {
                "bond_id": bond_id,
                "concept_pair": [bond.concept_id1, bond.concept_id2],
                "CHSH_value": float(S),
                "classical_limit": 2.0,
                "quantum_advantage": float(S - 2.0),
                "detection_time": datetime.now().isoformat(),
                "interpretation": "Non-local hidden variables ruled out"
            }

            self.bell_violations.append(violation)
            print(f"Bell violation detected! S = {S:.3f} > 2.0")

    def measure_entanglement_strength(self, concept_id1: str, concept_id2: str) -> float:
        """Measure current entanglement strength between concepts"""

        # Find bond between concepts
        bond_id = None
        if concept_id1 in self.concept_bond_index:
            for bid in self.concept_bond_index[concept_id1]:
                bond = self.entanglement_bonds[bid]
                if bond.concept_id2 == concept_id2 or bond.concept_id1 == concept_id2:
                    bond_id = bid
                    break

        if not bond_id:
            return 0.0

        bond = self.entanglement_bonds[bond_id]

        # Calculate current entanglement based on quantum states
        concept1 = self.hyperspace.concepts[concept_id1]
        concept2 = self.hyperspace.concepts[concept_id2]

        # Phase coherence measure
        phase_coherence = np.cos(concept1.quantum_phase - concept2.quantum_phase)

        # Hyperstate overlap
        hyperstate_overlap = np.dot(concept1.hyperstate, concept2.hyperstate)

        # Combine with original bond strength
        current_strength = bond.bond_strength * (abs(phase_coherence) + abs(hyperstate_overlap)) / 2

        return float(current_strength)

    def create_entanglement_cluster(self, concept_ids: List[str],
                                  cluster_type: str = 'semantic') -> List[str]:
        """Create fully connected entanglement cluster"""
        bond_ids = []

        for i, concept_id1 in enumerate(concept_ids):
            for concept_id2 in concept_ids[i+1:]:
                bond_id = self.create_entanglement(concept_id1, concept_id2,
                                                 bond_type=cluster_type,
                                                 strength=0.6)
                bond_ids.append(bond_id)

        print(f"Created entanglement cluster of {len(concept_ids)} concepts with {len(bond_ids)} bonds")
        return bond_ids

    def quantum_teleportation(self, source_concept_id: str, target_concept_id: str,
                            property_name: str) -> bool:
        """Quantum teleportation of concept properties"""

        if source_concept_id not in self.hyperspace.concepts or target_concept_id not in self.hyperspace.concepts:
            return False

        source = self.hyperspace.concepts[source_concept_id]
        target = self.hyperspace.concepts[target_concept_id]

        # Teleport specific properties
        if property_name == 'quantum_phase':
            target.quantum_phase = source.quantum_phase
        elif property_name == 'coherence_level':
            target.coherence_level = source.coherence_level
        elif property_name == 'superposition':
            target.superposition_components = source.superposition_components.copy()

        # Log teleportation event
        teleportation_event = {
            "source": source_concept_id,
            "target": target_concept_id,
            "property": property_name,
            "timestamp": datetime.now().isoformat(),
            "success": True
        }

        self.spooky_action_log.append(teleportation_event)
        return True

    def get_entanglement_network_stats(self) -> Dict:
        """Get comprehensive network statistics"""
        return {
            "total_bonds": len(self.entanglement_bonds),
            "active_concepts": len(self.concept_bond_index),
            "spooky_actions": len(self.spooky_action_log),
            "bell_violations": len(self.bell_violations),
            "bond_types": {
                bond_type: len([b for b in self.entanglement_bonds.values() if b.bond_type == bond_type])
                for bond_type in ['semantic', 'causal', 'analogical', 'contradictory']
            },
            "average_activation": np.mean([b.activation_count for b in self.entanglement_bonds.values()]) if self.entanglement_bonds else 0
        }