"""
Test suite for hyperdimensional concept spaces
Test-driven development for quantum knowledge architecture
"""

import pytest
import numpy as np
import json
from datetime import datetime
import tempfile
import os

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quantum_knowledge.hyperdimensional_concepts import HyperdimensionalSpace, HyperConcept

class TestHyperdimensionalSpace:
    """Test suite for hyperdimensional concept space"""

    def setup_method(self):
        """Set up test fixtures"""
        self.dimensions = 512  # Smaller for testing
        self.hyperspace = HyperdimensionalSpace(dimensions=self.dimensions)

    def test_initialization(self):
        """Test hyperspace initialization"""
        assert self.hyperspace.dimensions == self.dimensions
        assert len(self.hyperspace.concepts) == 0
        assert len(self.hyperspace.entanglement_network) == 0
        assert len(self.hyperspace.observation_history) == 0

        # Test constants
        assert self.hyperspace.PLANCK_SEMANTIC > 0
        assert self.hyperspace.LIGHT_SPEED_IDEAS > 0
        assert self.hyperspace.UNCERTAINTY_CONSTANT > 0

    def test_create_hyperconcept_basic(self):
        """Test basic hyperconcept creation"""
        term = "Test Concept"
        definition = "A test concept for validation purposes"

        concept = self.hyperspace.create_hyperconcept(term, definition)

        # Validate concept properties
        assert concept.term == term
        assert concept.id.startswith("hyper-")
        assert len(concept.id) == 18  # "hyper-" + 12 hex chars
        assert concept.hyperstate.shape == (self.dimensions,)
        assert np.isclose(np.linalg.norm(concept.hyperstate), 1.0, atol=1e-6)

        # Validate quantum properties
        assert 0 <= concept.quantum_phase <= 2 * np.pi
        assert 0 <= concept.coherence_level <= 1.0
        assert isinstance(concept.superposition_components, dict)
        assert concept.uncertainty_tensor.shape == (3, 3)

        # Validate metadata
        assert concept.version == "1.0.0"
        assert concept.creation_timestamp
        assert concept.last_observation

        # Validate storage
        assert concept.id in self.hyperspace.concepts

    def test_create_hyperconcept_with_initial_state(self):
        """Test hyperconcept creation with custom initial state"""
        initial_state = np.random.normal(0, 1, self.dimensions)
        initial_state = initial_state / np.linalg.norm(initial_state)

        concept = self.hyperspace.create_hyperconcept(
            "Custom State", "Test with custom state", initial_state
        )

        assert np.allclose(concept.hyperstate, initial_state)

    def test_quantum_similarity(self):
        """Test quantum similarity calculation"""
        concept1 = self.hyperspace.create_hyperconcept("Concept A", "First test concept")
        concept2 = self.hyperspace.create_hyperconcept("Concept B", "Second test concept")

        similarity = self.hyperspace.quantum_similarity(concept1.id, concept2.id)

        # Similarity should be a float between -1 and 1
        assert isinstance(similarity, float)
        assert -1 <= similarity <= 1

        # Self-similarity should be close to 1
        self_similarity = self.hyperspace.quantum_similarity(concept1.id, concept1.id)
        assert self_similarity > 0.9

    def test_quantum_similarity_phase_effect(self):
        """Test that quantum phase affects similarity"""
        # Create concepts with same hyperstate but different phases
        state = np.random.normal(0, 1, self.dimensions)
        state = state / np.linalg.norm(state)

        concept1 = self.hyperspace.create_hyperconcept("Phase Test 1", "Test concept")
        concept2 = self.hyperspace.create_hyperconcept("Phase Test 2", "Test concept")

        # Set same hyperstate but different phases
        concept1.hyperstate = state.copy()
        concept2.hyperstate = state.copy()
        concept1.quantum_phase = 0.0
        concept2.quantum_phase = np.pi  # 180 degrees different

        similarity = self.hyperspace.quantum_similarity(concept1.id, concept2.id)

        # Phase difference should reduce similarity
        assert similarity < 0.5

    def test_entangle_concepts(self):
        """Test concept entanglement"""
        concept1 = self.hyperspace.create_hyperconcept("Entangle A", "First concept")
        concept2 = self.hyperspace.create_hyperconcept("Entangle B", "Second concept")

        # Store original states
        original_state1 = concept1.hyperstate.copy()
        original_state2 = concept2.hyperstate.copy()
        original_phase1 = concept1.quantum_phase
        original_phase2 = concept2.quantum_phase

        # Entangle with high strength
        success = self.hyperspace.entangle_concepts(concept1.id, concept2.id, strength=0.8)
        assert success

        # Check entanglement partners
        assert concept2.id in concept1.entanglement_partners
        assert concept1.id in concept2.entanglement_partners

        # Check phase synchronization
        phase_diff = abs(concept1.quantum_phase - concept2.quantum_phase)
        original_phase_diff = abs(original_phase1 - original_phase2)
        assert phase_diff < original_phase_diff  # Phases should be more synchronized

        # Check hyperstate entanglement
        hyperstate_similarity = np.dot(concept1.hyperstate, concept2.hyperstate)
        original_similarity = np.dot(original_state1, original_state2)
        assert hyperstate_similarity > original_similarity  # States should be more similar

    def test_entangle_nonexistent_concepts(self):
        """Test entanglement with non-existent concepts"""
        concept1 = self.hyperspace.create_hyperconcept("Real Concept", "Exists")

        # Try to entangle with non-existent concept
        success = self.hyperspace.entangle_concepts(concept1.id, "fake-id", strength=0.5)
        assert not success

        success = self.hyperspace.entangle_concepts("fake-id", concept1.id, strength=0.5)
        assert not success

    def test_measure_concept_definition(self):
        """Test concept measurement (definition type)"""
        concept = self.hyperspace.create_hyperconcept("Measure Test", "Test measurement")

        # Store original uncertainty
        original_uncertainty = concept.uncertainty_tensor.copy()

        result, confidence = self.hyperspace.measure_concept(concept.id, "definition")

        # Validate measurement result
        assert isinstance(result, str)
        assert 0 <= confidence <= 1

        # Check Heisenberg effect: measuring definition increases uncertainty in relationships
        assert np.trace(concept.uncertainty_tensor) > np.trace(original_uncertainty)

        # Check observation history
        assert len(self.hyperspace.observation_history) == 1
        observation = self.hyperspace.observation_history[0]
        assert observation["concept_id"] == concept.id
        assert observation["measurement_type"] == "definition"

    def test_measure_concept_relationship(self):
        """Test concept measurement (relationship type)"""
        concept1 = self.hyperspace.create_hyperconcept("Rel Test 1", "First concept")
        concept2 = self.hyperspace.create_hyperconcept("Rel Test 2", "Second concept")

        # Store original coherence
        original_coherence = concept1.coherence_level

        result, confidence = self.hyperspace.measure_concept(concept1.id, "relationship")

        # Validate result format
        assert isinstance(result, list)
        assert 0 <= confidence <= 1

        # Check results contain relationships
        for rel_id, similarity in result:
            assert rel_id in self.hyperspace.concepts
            assert isinstance(similarity, float)

        # Check Heisenberg effect: measuring relationships decreases definition coherence
        assert concept1.coherence_level < original_coherence

    def test_measure_nonexistent_concept(self):
        """Test measuring non-existent concept"""
        with pytest.raises(ValueError, match="Concept .* not found"):
            self.hyperspace.measure_concept("fake-id", "definition")

    def test_detect_emergence(self):
        """Test emergence detection"""
        concept1 = self.hyperspace.create_hyperconcept("Emerge A", "Base concept")
        concept2 = self.hyperspace.create_hyperconcept("Emerge B", "Partner concept")

        # Entangle concepts to create potential for emergence
        self.hyperspace.entangle_concepts(concept1.id, concept2.id, strength=0.9)

        emergent_props = self.hyperspace.detect_emergence(concept1.id)

        # Should return a list
        assert isinstance(emergent_props, list)

        # If emergence detected, validate structure
        for prop in emergent_props:
            assert "type" in prop
            assert "concept_pair" in prop
            assert "novel_dimensions" in prop
            assert "emergence_strength" in prop
            assert "discovery_timestamp" in prop

    def test_concept_status(self):
        """Test getting concept status"""
        concept = self.hyperspace.create_hyperconcept("Status Test", "Test status")

        status = self.hyperspace.get_concept_status(concept.id)

        # Validate status structure
        required_fields = [
            "id", "term", "coherence_level", "quantum_phase",
            "hyperstate_norm", "entanglement_count", "superposition_states",
            "dominant_state", "uncertainty_trace", "last_observation"
        ]

        for field in required_fields:
            assert field in status

        # Validate specific values
        assert status["id"] == concept.id
        assert status["term"] == concept.term
        assert status["hyperstate_norm"] == pytest.approx(1.0, abs=1e-6)
        assert status["entanglement_count"] == 0  # No entanglements yet

    def test_concept_status_nonexistent(self):
        """Test getting status of non-existent concept"""
        status = self.hyperspace.get_concept_status("fake-id")
        assert "error" in status

    def test_export_hyperconcepts(self):
        """Test exporting hyperconcepts to JSON"""
        # Create some test concepts
        concept1 = self.hyperspace.create_hyperconcept("Export Test 1", "First export test")
        concept2 = self.hyperspace.create_hyperconcept("Export Test 2", "Second export test")

        # Add some observation history
        self.hyperspace.measure_concept(concept1.id, "definition")

        # Export to temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            tmp_path = tmp_file.name

        try:
            self.hyperspace.export_hyperconcepts(tmp_path)

            # Validate export file
            assert os.path.exists(tmp_path)

            with open(tmp_path, 'r') as f:
                export_data = json.load(f)

            # Validate export structure
            assert "dimensions" in export_data
            assert "concepts" in export_data
            assert "observation_history" in export_data
            assert "export_timestamp" in export_data

            assert export_data["dimensions"] == self.dimensions
            assert len(export_data["concepts"]) == 2
            assert len(export_data["observation_history"]) >= 1

            # Validate concept serialization
            for concept_id, concept_data in export_data["concepts"].items():
                assert "hyperstate" in concept_data
                assert "uncertainty_tensor" in concept_data
                assert isinstance(concept_data["hyperstate"], list)
                assert isinstance(concept_data["uncertainty_tensor"], list)

        finally:
            # Clean up temporary file
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)

    def test_power_law_hyperstate_distribution(self):
        """Test that hyperstates follow power law distribution"""
        concept = self.hyperspace.create_hyperconcept("Power Law Test", "Test distribution")

        # Check that early dimensions have higher magnitude on average
        early_dims = concept.hyperstate[:50]
        late_dims = concept.hyperstate[-50:]

        early_mean = np.mean(np.abs(early_dims))
        late_mean = np.mean(np.abs(late_dims))

        # Early dimensions should generally have higher magnitude
        assert early_mean > late_mean

    def test_superposition_components_normalized(self):
        """Test that superposition components sum to reasonable values"""
        concept = self.hyperspace.create_hyperconcept("Superposition Test", "Test superposition")

        total_prob = sum(concept.superposition_components.values())
        assert 0.9 <= total_prob <= 1.1  # Should be close to 1.0

    def test_coherence_level_calculation(self):
        """Test coherence level calculation based on definition length"""
        short_def = "Short"
        long_def = " ".join(["word"] * 100)  # 100 words

        concept_short = self.hyperspace.create_hyperconcept("Short", short_def)
        concept_long = self.hyperspace.create_hyperconcept("Long", long_def)

        # Longer definitions should have higher coherence (up to the limit)
        assert concept_long.coherence_level >= concept_short.coherence_level

    def test_quantum_phase_deterministic(self):
        """Test that quantum phase is deterministic for same definition"""
        definition = "Deterministic test definition"

        concept1 = self.hyperspace.create_hyperconcept("Test 1", definition)
        concept2 = self.hyperspace.create_hyperconcept("Test 2", definition)

        # Same definition should produce same quantum phase
        assert concept1.quantum_phase == concept2.quantum_phase

class TestHyperConcept:
    """Test suite for HyperConcept dataclass"""

    def test_hyperconcept_creation(self):
        """Test HyperConcept creation and validation"""
        hyperstate = np.random.normal(0, 1, 100)
        uncertainty_tensor = np.random.random((3, 3))

        concept = HyperConcept(
            id="test-concept-001",
            term="Test Concept",
            hyperstate=hyperstate,
            quantum_phase=1.57,
            coherence_level=0.8,
            entanglement_partners=["partner-001"],
            superposition_components={"literal": 0.6, "metaphorical": 0.4},
            uncertainty_tensor=uncertainty_tensor,
            creation_timestamp=datetime.now().isoformat(),
            last_observation=datetime.now().isoformat()
        )

        assert concept.id == "test-concept-001"
        assert concept.term == "Test Concept"
        assert isinstance(concept.hyperstate, np.ndarray)
        assert isinstance(concept.uncertainty_tensor, np.ndarray)

    def test_hyperconcept_list_conversion(self):
        """Test HyperConcept handles list-to-numpy conversion in __post_init__"""
        hyperstate_list = [0.1, 0.2, 0.3]
        uncertainty_list = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]

        concept = HyperConcept(
            id="test-list-001",
            term="List Test",
            hyperstate=hyperstate_list,
            quantum_phase=0.0,
            coherence_level=1.0,
            entanglement_partners=[],
            superposition_components={},
            uncertainty_tensor=uncertainty_list,
            creation_timestamp=datetime.now().isoformat(),
            last_observation=datetime.now().isoformat()
        )

        assert isinstance(concept.hyperstate, np.ndarray)
        assert isinstance(concept.uncertainty_tensor, np.ndarray)
        assert concept.hyperstate.shape == (3,)
        assert concept.uncertainty_tensor.shape == (3, 3)

if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])