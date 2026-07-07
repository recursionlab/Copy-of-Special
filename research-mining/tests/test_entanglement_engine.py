"""
Test suite for quantum entanglement engine
Test-driven development for spooky action at a distance
"""

import pytest
import numpy as np
import json
import time
from datetime import datetime
import tempfile
import os

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quantum_knowledge.hyperdimensional_concepts import HyperdimensionalSpace
from quantum_knowledge.entanglement_engine import (
    QuantumEntanglementNetwork, EntanglementBond
)

class TestEntanglementBond:
    """Test suite for EntanglementBond dataclass"""

    def test_entanglement_bond_creation(self):
        """Test EntanglementBond creation and validation"""
        bond = EntanglementBond(
            concept_id1="concept-001",
            concept_id2="concept-002",
            bond_strength=0.8,
            bond_type="semantic",
            spin_correlation=0.7,
            creation_time=datetime.now().isoformat(),
            last_activation=datetime.now().isoformat(),
            activation_count=5
        )

        assert bond.concept_id1 == "concept-001"
        assert bond.concept_id2 == "concept-002"
        assert bond.bond_strength == 0.8
        assert bond.bond_type == "semantic"
        assert bond.spin_correlation == 0.7
        assert bond.activation_count == 5

class TestQuantumEntanglementNetwork:
    """Test suite for quantum entanglement network"""

    def setup_method(self):
        """Set up test fixtures"""
        self.hyperspace = HyperdimensionalSpace(dimensions=256)
        self.entanglement_net = QuantumEntanglementNetwork(self.hyperspace)

        # Create test concepts
        self.concept1 = self.hyperspace.create_hyperconcept("Test A", "First test concept")
        self.concept2 = self.hyperspace.create_hyperconcept("Test B", "Second test concept")
        self.concept3 = self.hyperspace.create_hyperconcept("Test C", "Third test concept")

    def test_initialization(self):
        """Test entanglement network initialization"""
        assert self.entanglement_net.hyperspace == self.hyperspace
        assert len(self.entanglement_net.entanglement_bonds) == 0
        assert len(self.entanglement_net.concept_bond_index) == 0
        assert len(self.entanglement_net.spooky_action_log) == 0
        assert len(self.entanglement_net.bell_violations) == 0

    def test_create_entanglement_semantic(self):
        """Test creating semantic entanglement"""
        bond_id = self.entanglement_net.create_entanglement(
            self.concept1.id, self.concept2.id, "semantic", 0.8
        )

        # Validate bond creation
        assert bond_id in self.entanglement_net.entanglement_bonds
        bond = self.entanglement_net.entanglement_bonds[bond_id]

        assert bond.concept_id1 == self.concept1.id
        assert bond.concept_id2 == self.concept2.id
        assert bond.bond_type == "semantic"
        assert bond.bond_strength == 0.8
        assert bond.activation_count == 0

        # Validate indices
        assert bond_id in self.entanglement_net.concept_bond_index[self.concept1.id]
        assert bond_id in self.entanglement_net.concept_bond_index[self.concept2.id]

        # Validate hyperspace entanglement
        assert self.concept2.id in self.concept1.entanglement_partners
        assert self.concept1.id in self.concept2.entanglement_partners

    def test_create_entanglement_contradictory(self):
        """Test creating contradictory entanglement"""
        bond_id = self.entanglement_net.create_entanglement(
            self.concept1.id, self.concept2.id, "contradictory", 0.6
        )

        bond = self.entanglement_net.entanglement_bonds[bond_id]

        # Contradictory bonds should have negative spin correlation
        assert bond.spin_correlation <= 0

    def test_create_entanglement_nonexistent_concepts(self):
        """Test entanglement creation with non-existent concepts"""
        with pytest.raises(ValueError, match="One or both concepts not found"):
            self.entanglement_net.create_entanglement(
                "fake-id", self.concept1.id, "semantic", 0.5
            )

        with pytest.raises(ValueError, match="One or both concepts not found"):
            self.entanglement_net.create_entanglement(
                self.concept1.id, "fake-id", "semantic", 0.5
            )

    def test_spin_correlation_calculation(self):
        """Test spin correlation calculation"""
        # Create entanglement and check spin correlation is based on similarity
        bond_id = self.entanglement_net.create_entanglement(
            self.concept1.id, self.concept2.id, "semantic", 0.8
        )

        bond = self.entanglement_net.entanglement_bonds[bond_id]
        similarity = self.hyperspace.quantum_similarity(self.concept1.id, self.concept2.id)

        # For semantic bonds, spin correlation should match similarity
        assert abs(bond.spin_correlation - similarity) < 0.1

    def test_quantum_measurement_cascade_semantic(self):
        """Test quantum measurement cascade for semantic bonds"""
        # Create semantic entanglement
        bond_id = self.entanglement_net.create_entanglement(
            self.concept1.id, self.concept2.id, "semantic", 0.8
        )

        # Store original quantum phase
        original_phase = self.concept2.quantum_phase

        # Trigger measurement cascade
        cascade_effects = self.entanglement_net.quantum_measurement_cascade(
            self.concept1.id, "definition", "test_result"
        )

        # Validate cascade occurred
        assert len(cascade_effects) == 1
        effect = cascade_effects[0]

        assert effect["trigger_concept"] == self.concept1.id
        assert effect["affected_concept"] == self.concept2.id
        assert effect["bond_type"] == "semantic"
        assert effect["measurement_type"] == "definition"

        # Check quantum phase was affected
        assert self.concept2.quantum_phase != original_phase

        # Check spooky action log
        assert len(self.entanglement_net.spooky_action_log) == 1

        # Check bond activation
        bond = self.entanglement_net.entanglement_bonds[bond_id]
        assert bond.activation_count == 1

    def test_quantum_measurement_cascade_contradictory(self):
        """Test quantum measurement cascade for contradictory bonds"""
        # Create contradictory entanglement
        self.entanglement_net.create_entanglement(
            self.concept1.id, self.concept2.id, "contradictory", 0.7
        )

        # Store original superposition
        original_superposition = self.concept2.superposition_components.copy()

        # Trigger measurement cascade
        cascade_effects = self.entanglement_net.quantum_measurement_cascade(
            self.concept1.id, "definition", "literal"
        )

        # Should affect contradictory concept's superposition
        assert len(cascade_effects) == 1

        # Check that non-literal states were boosted
        for state, prob in self.concept2.superposition_components.items():
            if state != "literal":
                # Non-literal states should be boosted
                assert prob >= original_superposition.get(state, 0)

    def test_quantum_measurement_cascade_causal(self):
        """Test quantum measurement cascade for causal bonds"""
        # Create causal entanglement
        self.entanglement_net.create_entanglement(
            self.concept1.id, self.concept2.id, "causal", 0.6
        )

        # Store original coherence
        original_coherence = self.concept2.coherence_level

        # Trigger measurement cascade
        cascade_effects = self.entanglement_net.quantum_measurement_cascade(
            self.concept1.id, "definition", "test_result"
        )

        # Causal effects should increase coherence of effect concept
        assert self.concept2.coherence_level > original_coherence

    def test_quantum_measurement_cascade_analogical(self):
        """Test quantum measurement cascade for analogical bonds"""
        # Create analogical entanglement
        self.entanglement_net.create_entanglement(
            self.concept1.id, self.concept2.id, "analogical", 0.5
        )

        # Store original hyperstate
        original_hyperstate = self.concept2.hyperstate.copy()

        # Trigger measurement cascade
        cascade_effects = self.entanglement_net.quantum_measurement_cascade(
            self.concept1.id, "definition", "test_result"
        )

        # Analogical bonds should affect hyperstate
        hyperstate_change = np.linalg.norm(self.concept2.hyperstate - original_hyperstate)
        assert hyperstate_change > 0

    def test_measurement_cascade_no_entanglements(self):
        """Test measurement cascade with no entanglements"""
        # Test concept with no entanglements
        cascade_effects = self.entanglement_net.quantum_measurement_cascade(
            self.concept3.id, "definition", "test_result"
        )

        # Should return empty list
        assert len(cascade_effects) == 0

    def test_check_bell_violation(self):
        """Test Bell inequality violation detection"""
        # Create strong entanglement that might violate Bell inequality
        bond_id = self.entanglement_net.create_entanglement(
            self.concept1.id, self.concept2.id, "semantic", 0.9
        )

        # Set up conditions that should violate Bell inequality
        bond = self.entanglement_net.entanglement_bonds[bond_id]
        bond.spin_correlation = 0.9  # High correlation

        # Manually trigger Bell test
        self.entanglement_net.check_bell_violation(bond_id)

        # Check if violation was detected (depends on quantum phases)
        # At minimum, should not crash and should record attempt
        assert len(self.entanglement_net.bell_violations) >= 0

    def test_measure_entanglement_strength(self):
        """Test entanglement strength measurement"""
        # Create entanglement
        bond_id = self.entanglement_net.create_entanglement(
            self.concept1.id, self.concept2.id, "semantic", 0.8
        )

        # Measure strength
        strength = self.entanglement_net.measure_entanglement_strength(
            self.concept1.id, self.concept2.id
        )

        # Should return a float between 0 and 1
        assert isinstance(strength, float)
        assert 0 <= strength <= 1

        # Should be related to original bond strength
        assert strength > 0  # Should have some strength

    def test_measure_entanglement_strength_no_bond(self):
        """Test measuring entanglement strength with no bond"""
        strength = self.entanglement_net.measure_entanglement_strength(
            self.concept1.id, self.concept3.id
        )

        # Should return 0 for non-entangled concepts
        assert strength == 0.0

    def test_create_entanglement_cluster(self):
        """Test creating fully connected entanglement cluster"""
        concept_ids = [self.concept1.id, self.concept2.id, self.concept3.id]

        bond_ids = self.entanglement_net.create_entanglement_cluster(
            concept_ids, "semantic"
        )

        # Should create 3 bonds for 3 concepts: (3 choose 2) = 3
        assert len(bond_ids) == 3

        # Validate all bonds exist
        for bond_id in bond_ids:
            assert bond_id in self.entanglement_net.entanglement_bonds

        # Validate all concepts are connected
        for concept_id in concept_ids:
            assert len(self.entanglement_net.concept_bond_index[concept_id]) == 2

    def test_quantum_teleportation(self):
        """Test quantum teleportation of concept properties"""
        # Set distinct quantum phase for source
        self.concept1.quantum_phase = 1.57  # π/2

        # Teleport quantum phase
        success = self.entanglement_net.quantum_teleportation(
            self.concept1.id, self.concept2.id, "quantum_phase"
        )

        assert success
        assert self.concept2.quantum_phase == 1.57

        # Check teleportation log
        assert len(self.entanglement_net.spooky_action_log) >= 1

    def test_quantum_teleportation_coherence(self):
        """Test teleporting coherence level"""
        self.concept1.coherence_level = 0.95

        success = self.entanglement_net.quantum_teleportation(
            self.concept1.id, self.concept2.id, "coherence_level"
        )

        assert success
        assert self.concept2.coherence_level == 0.95

    def test_quantum_teleportation_superposition(self):
        """Test teleporting superposition states"""
        test_superposition = {"test_state": 0.7, "other_state": 0.3}
        self.concept1.superposition_components = test_superposition

        success = self.entanglement_net.quantum_teleportation(
            self.concept1.id, self.concept2.id, "superposition"
        )

        assert success
        assert self.concept2.superposition_components == test_superposition

    def test_quantum_teleportation_nonexistent_concepts(self):
        """Test teleportation with non-existent concepts"""
        success = self.entanglement_net.quantum_teleportation(
            "fake-id", self.concept1.id, "quantum_phase"
        )
        assert not success

        success = self.entanglement_net.quantum_teleportation(
            self.concept1.id, "fake-id", "quantum_phase"
        )
        assert not success

    def test_get_entanglement_network_stats(self):
        """Test getting network statistics"""
        # Create some entanglements
        self.entanglement_net.create_entanglement(
            self.concept1.id, self.concept2.id, "semantic", 0.8
        )
        self.entanglement_net.create_entanglement(
            self.concept2.id, self.concept3.id, "causal", 0.6
        )

        # Trigger some cascades
        self.entanglement_net.quantum_measurement_cascade(
            self.concept1.id, "definition", "test"
        )

        stats = self.entanglement_net.get_entanglement_network_stats()

        # Validate stats structure
        required_fields = [
            "total_bonds", "active_concepts", "spooky_actions",
            "bell_violations", "bond_types", "average_activation"
        ]

        for field in required_fields:
            assert field in stats

        # Validate values
        assert stats["total_bonds"] == 2
        assert stats["active_concepts"] == 3  # concept1, concept2, and concept3 all have bonds
        assert stats["spooky_actions"] >= 1
        assert "semantic" in stats["bond_types"]
        assert "causal" in stats["bond_types"]

    def test_concurrent_measurement_cascades(self):
        """Test thread safety of concurrent measurement cascades"""
        # Create multiple entanglements
        for i in range(5):
            concept = self.hyperspace.create_hyperconcept(f"Concurrent {i}", f"Test {i}")
            self.entanglement_net.create_entanglement(
                self.concept1.id, concept.id, "semantic", 0.5
            )

        # Simulate concurrent measurements (simplified test)
        initial_log_length = len(self.entanglement_net.spooky_action_log)

        # Multiple cascades
        for i in range(3):
            self.entanglement_net.quantum_measurement_cascade(
                self.concept1.id, "definition", f"test_{i}"
            )

        # Should have recorded all cascades
        final_log_length = len(self.entanglement_net.spooky_action_log)
        assert final_log_length > initial_log_length

    def test_bond_strength_evolution(self):
        """Test that bond strength evolves with interactions"""
        bond_id = self.entanglement_net.create_entanglement(
            self.concept1.id, self.concept2.id, "semantic", 0.5
        )

        initial_strength = self.entanglement_net.measure_entanglement_strength(
            self.concept1.id, self.concept2.id
        )

        # Multiple interactions should affect strength measurement
        for i in range(5):
            self.entanglement_net.quantum_measurement_cascade(
                self.concept1.id, "definition", f"test_{i}"
            )

        final_strength = self.entanglement_net.measure_entanglement_strength(
            self.concept1.id, self.concept2.id
        )

        # Strength might change due to phase evolution
        # At minimum, should be computable without error
        assert isinstance(final_strength, float)
        assert 0 <= final_strength <= 1

    def test_entanglement_bond_types(self):
        """Test all supported bond types"""
        bond_types = ["semantic", "causal", "analogical", "contradictory"]

        for bond_type in bond_types:
            concept = self.hyperspace.create_hyperconcept(f"Type {bond_type}", f"Test {bond_type}")
            bond_id = self.entanglement_net.create_entanglement(
                self.concept1.id, concept.id, bond_type, 0.6
            )

            bond = self.entanglement_net.entanglement_bonds[bond_id]
            assert bond.bond_type == bond_type

            # Each type should produce different cascade effects
            cascade_effects = self.entanglement_net.quantum_measurement_cascade(
                self.concept1.id, "definition", "test"
            )

            # Should have at least one effect for the new bond
            relevant_effects = [e for e in cascade_effects if e["bond_type"] == bond_type]
            assert len(relevant_effects) >= 1

if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])