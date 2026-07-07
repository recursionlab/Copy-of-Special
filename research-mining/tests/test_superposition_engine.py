"""
Test suite for quantum superposition engine
Test-driven development for wave function collapse and interference
"""

import pytest
import numpy as np
import json
import cmath
from datetime import datetime
import tempfile
import os

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quantum_knowledge.superposition_engine import (
    SuperpositionEngine, SuperpositionState, QuantumAmplitude, ConceptSuperposition
)

class TestQuantumAmplitude:
    """Test suite for QuantumAmplitude dataclass"""

    def test_quantum_amplitude_creation(self):
        """Test quantum amplitude creation and properties"""
        amplitude = QuantumAmplitude(real=0.6, imaginary=0.8)

        assert amplitude.real == 0.6
        assert amplitude.imaginary == 0.8
        assert amplitude.magnitude == pytest.approx(1.0, abs=1e-6)  # sqrt(0.6^2 + 0.8^2)
        assert amplitude.probability == pytest.approx(1.0, abs=1e-6)  # magnitude^2

    def test_quantum_amplitude_phase(self):
        """Test quantum amplitude phase calculation"""
        # Real amplitude (phase = 0)
        amp_real = QuantumAmplitude(real=1.0, imaginary=0.0)
        assert amp_real.phase == pytest.approx(0.0, abs=1e-6)

        # Imaginary amplitude (phase = π/2)
        amp_imag = QuantumAmplitude(real=0.0, imaginary=1.0)
        assert amp_imag.phase == pytest.approx(np.pi/2, abs=1e-6)

        # Negative real (phase = π)
        amp_neg = QuantumAmplitude(real=-1.0, imaginary=0.0)
        assert abs(amp_neg.phase) == pytest.approx(np.pi, abs=1e-6)

    def test_quantum_amplitude_probability(self):
        """Test probability calculation"""
        amplitude = QuantumAmplitude(real=0.5, imaginary=0.5)
        expected_prob = 0.5**2 + 0.5**2  # 0.5
        assert amplitude.probability == pytest.approx(expected_prob, abs=1e-6)

class TestConceptSuperposition:
    """Test suite for ConceptSuperposition dataclass"""

    def test_concept_superposition_creation(self):
        """Test concept superposition creation"""
        amplitudes = {
            SuperpositionState.LITERAL: QuantumAmplitude(0.6, 0.0),
            SuperpositionState.METAPHORICAL: QuantumAmplitude(0.8, 0.0)
        }

        superposition = ConceptSuperposition(
            concept_id="test-concept-001",
            amplitudes=amplitudes,
            decoherence_rate=0.1
        )

        assert superposition.concept_id == "test-concept-001"
        assert len(superposition.amplitudes) == 2
        assert superposition.decoherence_rate == 0.1
        assert superposition.measurement_history == []
        assert superposition.entanglement_effects == {}

class TestSuperpositionEngine:
    """Test suite for superposition engine"""

    def setup_method(self):
        """Set up test fixtures"""
        self.engine = SuperpositionEngine()

    def test_initialization(self):
        """Test superposition engine initialization"""
        assert len(self.engine.superpositions) == 0
        assert len(self.engine.decoherence_events) == 0
        assert len(self.engine.interference_patterns) == 0

        # Check constants
        assert self.engine.SEMANTIC_PLANCK > 0
        assert self.engine.CONSCIOUSNESS_FREQUENCY > 0

    def test_create_superposition_default(self):
        """Test creating superposition with default states"""
        concept_id = "test-concept-001"
        term = "Test Concept"

        superposition = self.engine.create_superposition(concept_id, term)

        # Validate creation
        assert concept_id in self.engine.superpositions
        assert superposition.concept_id == concept_id

        # Check default states
        expected_states = [
            SuperpositionState.LITERAL,
            SuperpositionState.METAPHORICAL,
            SuperpositionState.TECHNICAL,
            SuperpositionState.EMERGENT
        ]

        for state in expected_states:
            assert state in superposition.amplitudes

        # Check normalization
        total_prob = sum(amp.probability for amp in superposition.amplitudes.values())
        assert total_prob == pytest.approx(1.0, abs=1e-6)

    def test_create_superposition_custom_states(self):
        """Test creating superposition with custom initial states"""
        concept_id = "test-concept-002"
        term = "Custom Concept"
        initial_states = {
            SuperpositionState.LITERAL.value: 0.7,
            SuperpositionState.POETIC.value: 0.3
        }

        superposition = self.engine.create_superposition(concept_id, term, initial_states)

        # Should have only the specified states
        assert len(superposition.amplitudes) == 2
        assert SuperpositionState.LITERAL in superposition.amplitudes
        assert SuperpositionState.POETIC in superposition.amplitudes

        # Check probabilities match (approximately, due to normalization)
        literal_prob = superposition.amplitudes[SuperpositionState.LITERAL].probability
        poetic_prob = superposition.amplitudes[SuperpositionState.POETIC].probability

        assert literal_prob > poetic_prob  # 0.7 > 0.3

    def test_superposition_normalization(self):
        """Test that superposition amplitudes are properly normalized"""
        concept_id = "test-concept-003"
        initial_states = {
            SuperpositionState.LITERAL.value: 0.5,
            SuperpositionState.METAPHORICAL.value: 0.3,
            SuperpositionState.TECHNICAL.value: 0.1
        }

        superposition = self.engine.create_superposition(concept_id, "Test", initial_states)

        # Total probability should be 1.0
        total_prob = sum(amp.probability for amp in superposition.amplitudes.values())
        assert total_prob == pytest.approx(1.0, abs=1e-6)

    def test_decoherence_rate_calculation(self):
        """Test decoherence rate calculation based on concept complexity"""
        simple_concept = self.engine.create_superposition("simple", "word")
        complex_concept = self.engine.create_superposition(
            "complex", "very complex multi word concept description"
        )

        # More complex concepts should have higher decoherence rates
        assert complex_concept.decoherence_rate >= simple_concept.decoherence_rate

    def test_measure_concept(self):
        """Test quantum measurement and wave function collapse"""
        concept_id = "test-measure-001"
        superposition = self.engine.create_superposition(concept_id, "Measure Test")

        # Store original amplitudes
        original_amplitudes = {
            state: QuantumAmplitude(amp.real, amp.imaginary)
            for state, amp in superposition.amplitudes.items()
        }

        # Perform measurement
        measured_state, confidence = self.engine.measure_concept(concept_id, "test_observer")

        # Validate measurement result
        assert isinstance(measured_state, SuperpositionState)
        assert 0 <= confidence <= 1

        # Check measurement history
        assert len(superposition.measurement_history) == 1
        measurement = superposition.measurement_history[0]
        assert measurement["measured_state"] == measured_state.value
        assert measurement["observer"] == "test_observer"

        # Check decoherence occurred
        measured_amp = superposition.amplitudes[measured_state]
        original_amp = original_amplitudes[measured_state]

        # Measured state should be strengthened
        assert measured_amp.probability >= original_amp.probability

    def test_measure_nonexistent_concept(self):
        """Test measuring non-existent concept"""
        with pytest.raises(ValueError, match="Concept .* not in superposition"):
            self.engine.measure_concept("fake-id", "observer")

    def test_measurement_probabilistic(self):
        """Test that measurement is probabilistic based on amplitudes"""
        concept_id = "test-prob-001"

        # Create superposition heavily weighted towards literal
        initial_states = {
            SuperpositionState.LITERAL.value: 0.99,
            SuperpositionState.METAPHORICAL.value: 0.01
        }

        self.engine.create_superposition(concept_id, "Probable Test", initial_states)

        # Multiple measurements should mostly return LITERAL
        literal_count = 0
        total_measurements = 50

        for _ in range(total_measurements):
            # Recreate superposition for each test
            self.engine.create_superposition(f"{concept_id}_{_}", "Test", initial_states)
            measured_state, _ = self.engine.measure_concept(f"{concept_id}_{_}", "test")

            if measured_state == SuperpositionState.LITERAL:
                literal_count += 1

        # Should be mostly literal (allow some variance)
        literal_fraction = literal_count / total_measurements
        assert literal_fraction > 0.8  # Should be > 80% given 99% initial probability

    def test_apply_decoherence(self):
        """Test decoherence application"""
        concept_id = "test-decoherence-001"
        superposition = self.engine.create_superposition(concept_id, "Decoherence Test")

        # Store original entropy
        original_entropy = self.engine.calculate_superposition_entropy(concept_id)

        # Apply decoherence
        collapsed_state = SuperpositionState.LITERAL
        self.engine.apply_decoherence(concept_id, collapsed_state, strength=0.8)

        # Check decoherence was recorded
        assert len(self.engine.decoherence_events) == 1
        event = self.engine.decoherence_events[0]
        assert event["concept_id"] == concept_id
        assert event["collapsed_state"] == collapsed_state.value

        # Entropy should decrease (more certainty)
        new_entropy = self.engine.calculate_superposition_entropy(concept_id)
        assert new_entropy < original_entropy

    def test_create_quantum_interference_constructive(self):
        """Test constructive quantum interference"""
        concept_id1 = "interference-001"
        concept_id2 = "interference-002"

        # Create two superpositions
        self.engine.create_superposition(concept_id1, "Interference A")
        self.engine.create_superposition(concept_id2, "Interference B")

        # Store original amplitudes
        original_amp1 = {
            state: amp.magnitude
            for state, amp in self.engine.superpositions[concept_id1].amplitudes.items()
        }

        # Apply constructive interference
        interference = self.engine.create_quantum_interference(
            concept_id1, concept_id2, "constructive"
        )

        # Validate interference record
        assert interference["concept_pair"] == [concept_id1, concept_id2]
        assert interference["interaction_type"] == "constructive"
        assert "amplitude_changes" in interference

        # Check interference was recorded
        assert len(self.engine.interference_patterns) == 1

        # Amplitudes should generally increase (constructive)
        changes = interference["amplitude_changes"]
        if changes:  # Only if there were common states
            for state, change in changes.items():
                # Constructive interference should generally increase magnitude
                assert "original_magnitude" in change
                assert "new_magnitude" in change

    def test_create_quantum_interference_destructive(self):
        """Test destructive quantum interference"""
        concept_id1 = "interference-003"
        concept_id2 = "interference-004"

        self.engine.create_superposition(concept_id1, "Destructive A")
        self.engine.create_superposition(concept_id2, "Destructive B")

        # Apply destructive interference
        interference = self.engine.create_quantum_interference(
            concept_id1, concept_id2, "destructive"
        )

        assert interference["interaction_type"] == "destructive"

        # Should have recorded the interference
        assert len(self.engine.interference_patterns) == 1

    def test_interference_nonexistent_concepts(self):
        """Test interference with non-existent concepts"""
        concept_id = "real-concept"
        self.engine.create_superposition(concept_id, "Real Concept")

        with pytest.raises(ValueError, match="Both concepts must be in superposition"):
            self.engine.create_quantum_interference(concept_id, "fake-id", "constructive")

        with pytest.raises(ValueError, match="Both concepts must be in superposition"):
            self.engine.create_quantum_interference("fake-id", concept_id, "constructive")

    def test_normalize_superposition(self):
        """Test superposition normalization"""
        concept_id = "normalize-test"
        superposition = self.engine.create_superposition(concept_id, "Normalize Test")

        # Artificially mess up normalization
        for amplitude in superposition.amplitudes.values():
            amplitude.real *= 2.0
            amplitude.imaginary *= 2.0

        # Check it's not normalized
        total_prob = sum(amp.probability for amp in superposition.amplitudes.values())
        assert abs(total_prob - 1.0) > 0.1

        # Normalize
        self.engine.normalize_superposition(concept_id)

        # Should be normalized again
        total_prob = sum(amp.probability for amp in superposition.amplitudes.values())
        assert total_prob == pytest.approx(1.0, abs=1e-6)

    def test_calculate_superposition_entropy(self):
        """Test von Neumann entropy calculation"""
        concept_id = "entropy-test"

        # Equal superposition should have high entropy
        equal_states = {
            SuperpositionState.LITERAL.value: 0.25,
            SuperpositionState.METAPHORICAL.value: 0.25,
            SuperpositionState.TECHNICAL.value: 0.25,
            SuperpositionState.POETIC.value: 0.25
        }

        superposition_equal = self.engine.create_superposition(concept_id + "1", "Equal", equal_states)

        # Definite state should have low entropy
        definite_states = {
            SuperpositionState.LITERAL.value: 0.99,
            SuperpositionState.METAPHORICAL.value: 0.01
        }

        superposition_definite = self.engine.create_superposition(concept_id + "2", "Definite", definite_states)

        entropy_equal = self.engine.calculate_superposition_entropy(concept_id + "1")
        entropy_definite = self.engine.calculate_superposition_entropy(concept_id + "2")

        # Equal superposition should have higher entropy
        assert entropy_equal > entropy_definite

    def test_evolve_superposition(self):
        """Test time evolution of superposition"""
        concept_id = "evolve-test"
        superposition = self.engine.create_superposition(concept_id, "Evolution Test")

        # Store original amplitudes
        original_amplitudes = {
            state: (amp.real, amp.imaginary)
            for state, amp in superposition.amplitudes.items()
        }

        # Evolve superposition
        self.engine.evolve_superposition(concept_id, time_step=0.1)

        # Amplitudes should have changed (time evolution)
        evolved_amplitudes = {
            state: (amp.real, amp.imaginary)
            for state, amp in superposition.amplitudes.items()
        }

        # At least some amplitudes should be different
        changes = sum(
            1 for state in original_amplitudes
            if (original_amplitudes[state][0] != evolved_amplitudes[state][0] or
                original_amplitudes[state][1] != evolved_amplitudes[state][1])
        )

        assert changes > 0

        # Should still be normalized
        total_prob = sum(amp.probability for amp in superposition.amplitudes.values())
        assert total_prob == pytest.approx(1.0, abs=1e-6)

    def test_get_superposition_status(self):
        """Test getting superposition status"""
        concept_id = "status-test"
        superposition = self.engine.create_superposition(concept_id, "Status Test")

        status = self.engine.get_superposition_status(concept_id)

        # Check required fields
        required_fields = [
            "concept_id", "state_probabilities", "dominant_state",
            "dominant_probability", "entropy", "decoherence_rate",
            "measurement_count", "last_measurement", "coherence_time"
        ]

        for field in required_fields:
            assert field in status

        # Validate specific values
        assert status["concept_id"] == concept_id
        assert isinstance(status["state_probabilities"], dict)
        assert 0 <= status["dominant_probability"] <= 1
        assert status["entropy"] >= 0
        assert status["measurement_count"] == 0  # No measurements yet

    def test_get_status_nonexistent_concept(self):
        """Test getting status of non-existent concept"""
        status = self.engine.get_superposition_status("fake-id")
        assert "error" in status

    def test_coherence_time_calculation(self):
        """Test coherence time calculation"""
        # High decoherence rate
        concept_id1 = "coherence-fast"
        superposition1 = self.engine.create_superposition(concept_id1, "Fast Decoherence")
        superposition1.decoherence_rate = 0.1

        # Low decoherence rate
        concept_id2 = "coherence-slow"
        superposition2 = self.engine.create_superposition(concept_id2, "Slow Decoherence")
        superposition2.decoherence_rate = 0.01

        status1 = self.engine.get_superposition_status(concept_id1)
        status2 = self.engine.get_superposition_status(concept_id2)

        # Lower decoherence rate should give longer coherence time
        assert status2["coherence_time"] > status1["coherence_time"]

    def test_export_superpositions(self):
        """Test exporting superpositions to JSON"""
        # Create test superpositions
        concept1 = self.engine.create_superposition("export-1", "Export Test 1")
        concept2 = self.engine.create_superposition("export-2", "Export Test 2")

        # Add some activity
        self.engine.measure_concept("export-1", "test_observer")
        self.engine.create_quantum_interference("export-1", "export-2", "constructive")

        # Export to temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            tmp_path = tmp_file.name

        try:
            self.engine.export_superpositions(tmp_path)

            # Validate export file
            assert os.path.exists(tmp_path)

            with open(tmp_path, 'r') as f:
                export_data = json.load(f)

            # Validate export structure
            assert "superpositions" in export_data
            assert "decoherence_events" in export_data
            assert "interference_patterns" in export_data
            assert "export_timestamp" in export_data

            assert len(export_data["superpositions"]) == 2
            assert len(export_data["decoherence_events"]) >= 1  # From measurement
            assert len(export_data["interference_patterns"]) >= 1

            # Validate superposition serialization
            for concept_id, concept_data in export_data["superpositions"].items():
                assert "amplitudes" in concept_data
                assert isinstance(concept_data["amplitudes"], dict)

                # Check amplitude serialization
                for state, amp_data in concept_data["amplitudes"].items():
                    assert "real" in amp_data
                    assert "imaginary" in amp_data
                    assert "magnitude" in amp_data
                    assert "phase" in amp_data
                    assert "probability" in amp_data

        finally:
            # Clean up temporary file
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)

    def test_superposition_states_enum(self):
        """Test SuperpositionState enum"""
        # Test all enum values
        expected_states = [
            "literal", "metaphorical", "technical", "poetic",
            "philosophical", "practical", "emergent", "contradictory"
        ]

        for state_name in expected_states:
            state = SuperpositionState(state_name)
            assert state.value == state_name

    def test_measurement_affects_entropy(self):
        """Test that measurement reduces entropy"""
        concept_id = "entropy-measurement"

        # Create balanced superposition (high entropy)
        equal_states = {
            SuperpositionState.LITERAL.value: 0.25,
            SuperpositionState.METAPHORICAL.value: 0.25,
            SuperpositionState.TECHNICAL.value: 0.25,
            SuperpositionState.POETIC.value: 0.25
        }

        self.engine.create_superposition(concept_id, "Entropy Test", equal_states)

        # Measure initial entropy
        initial_entropy = self.engine.calculate_superposition_entropy(concept_id)

        # Perform measurement (should collapse superposition)
        self.engine.measure_concept(concept_id, "entropy_observer")

        # Measure final entropy
        final_entropy = self.engine.calculate_superposition_entropy(concept_id)

        # Entropy should decrease (more certainty)
        assert final_entropy < initial_entropy

    def test_multiple_measurements_history(self):
        """Test multiple measurements create proper history"""
        concept_id = "history-test"
        self.engine.create_superposition(concept_id, "History Test")

        # Perform multiple measurements
        observers = ["observer1", "observer2", "observer3"]
        for observer in observers:
            self.engine.measure_concept(concept_id, observer)

        superposition = self.engine.superpositions[concept_id]

        # Should have recorded all measurements
        assert len(superposition.measurement_history) == len(observers)

        # Check measurement details
        for i, measurement in enumerate(superposition.measurement_history):
            assert measurement["observer"] == observers[i]
            assert "timestamp" in measurement
            assert "measured_state" in measurement
            assert "confidence" in measurement

if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])