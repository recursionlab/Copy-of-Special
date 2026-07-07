"""
Quantum Superposition Engine for Concepts
Allows ideas to exist in multiple states simultaneously until observed
"""

import numpy as np
import json
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, asdict
from datetime import datetime
import cmath
from enum import Enum

class SuperpositionState(Enum):
    """Possible states a concept can exist in"""
    LITERAL = "literal"
    METAPHORICAL = "metaphorical"
    TECHNICAL = "technical"
    POETIC = "poetic"
    PHILOSOPHICAL = "philosophical"
    PRACTICAL = "practical"
    EMERGENT = "emergent"
    CONTRADICTORY = "contradictory"

@dataclass
class QuantumAmplitude:
    """Complex amplitude for a quantum state"""
    real: float
    imaginary: float

    @property
    def magnitude(self) -> float:
        return abs(complex(self.real, self.imaginary))

    @property
    def phase(self) -> float:
        return cmath.phase(complex(self.real, self.imaginary))

    @property
    def probability(self) -> float:
        return self.magnitude ** 2

@dataclass
class ConceptSuperposition:
    """A concept existing in quantum superposition"""
    concept_id: str
    amplitudes: Dict[SuperpositionState, QuantumAmplitude]
    decoherence_rate: float  # How quickly superposition collapses
    last_measurement: Optional[str] = None
    measurement_history: List[Dict] = None
    entanglement_effects: Dict[str, float] = None

    def __post_init__(self):
        if self.measurement_history is None:
            self.measurement_history = []
        if self.entanglement_effects is None:
            self.entanglement_effects = {}

class SuperpositionEngine:
    """Engine for managing quantum superposition of concepts"""

    def __init__(self):
        self.superpositions: Dict[str, ConceptSuperposition] = {}
        self.decoherence_events: List[Dict] = []
        self.interference_patterns: List[Dict] = []

        # Quantum constants for meaning space
        self.SEMANTIC_PLANCK = 1.616e-35  # Smallest unit of meaning
        self.CONSCIOUSNESS_FREQUENCY = 40.0  # Hz, gamma wave binding

    def create_superposition(self, concept_id: str, term: str,
                           initial_states: Dict[str, float] = None) -> ConceptSuperposition:
        """Create a new concept in quantum superposition"""

        if initial_states is None:
            # Default superposition across common states
            initial_states = {
                SuperpositionState.LITERAL.value: 0.4,
                SuperpositionState.METAPHORICAL.value: 0.3,
                SuperpositionState.TECHNICAL.value: 0.2,
                SuperpositionState.EMERGENT.value: 0.1
            }

        # Convert probabilities to quantum amplitudes
        amplitudes = {}
        for state_name, probability in initial_states.items():
            state = SuperpositionState(state_name)

            # Create complex amplitude from probability
            magnitude = np.sqrt(probability)
            # Random phase for quantum coherence
            phase = np.random.uniform(0, 2 * np.pi)

            amplitude = QuantumAmplitude(
                real=magnitude * np.cos(phase),
                imaginary=magnitude * np.sin(phase)
            )
            amplitudes[state] = amplitude

        # Normalize amplitudes
        total_prob = sum(amp.probability for amp in amplitudes.values())
        normalization = np.sqrt(1.0 / total_prob) if total_prob > 0 else 1.0

        for amplitude in amplitudes.values():
            amplitude.real *= normalization
            amplitude.imaginary *= normalization

        # Decoherence rate based on concept complexity
        decoherence_rate = min(0.1, len(term.split()) * 0.01)

        superposition = ConceptSuperposition(
            concept_id=concept_id,
            amplitudes=amplitudes,
            decoherence_rate=decoherence_rate
        )

        self.superpositions[concept_id] = superposition
        return superposition

    def measure_concept(self, concept_id: str, observer: str = "system") -> Tuple[SuperpositionState, float]:
        """Measure concept, collapsing wave function to single state"""

        if concept_id not in self.superpositions:
            raise ValueError(f"Concept {concept_id} not in superposition")

        superposition = self.superpositions[concept_id]

        # Calculate probabilities for each state
        probabilities = {}
        for state, amplitude in superposition.amplitudes.items():
            probabilities[state] = amplitude.probability

        # Quantum measurement (probabilistic collapse)
        states = list(probabilities.keys())
        probs = list(probabilities.values())

        # Normalize probabilities
        total_prob = sum(probs)
        if total_prob > 0:
            probs = [p / total_prob for p in probs]
        else:
            probs = [1.0 / len(probs)] * len(probs)

        # Random selection based on quantum probabilities
        measured_state = np.random.choice(states, p=probs)
        confidence = probabilities[measured_state]

        # Record measurement
        measurement_record = {
            "timestamp": datetime.now().isoformat(),
            "measured_state": measured_state.value,
            "confidence": float(confidence),
            "observer": observer,
            "pre_measurement_entropy": self.calculate_superposition_entropy(concept_id)
        }

        superposition.measurement_history.append(measurement_record)
        superposition.last_measurement = measured_state.value

        # Apply decoherence (partial collapse)
        self.apply_decoherence(concept_id, measured_state, strength=0.8)

        print(f"Measured {concept_id}: {measured_state.value} (confidence: {confidence:.3f})")

        return measured_state, float(confidence)

    def apply_decoherence(self, concept_id: str, collapsed_state: SuperpositionState,
                         strength: float = 0.5):
        """Apply decoherence, reducing superposition"""

        if concept_id not in self.superpositions:
            return

        superposition = self.superpositions[concept_id]

        # Strengthen the collapsed state, weaken others
        for state, amplitude in superposition.amplitudes.items():
            if state == collapsed_state:
                # Boost measured state amplitude
                boost_factor = 1.0 + strength * 0.5
                amplitude.real *= boost_factor
                amplitude.imaginary *= boost_factor
            else:
                # Reduce other state amplitudes
                reduction_factor = 1.0 - strength * 0.3
                amplitude.real *= reduction_factor
                amplitude.imaginary *= reduction_factor

        # Renormalize
        self.normalize_superposition(concept_id)

        # Record decoherence event
        decoherence_event = {
            "concept_id": concept_id,
            "collapsed_state": collapsed_state.value,
            "strength": strength,
            "timestamp": datetime.now().isoformat(),
            "remaining_entropy": self.calculate_superposition_entropy(concept_id)
        }

        self.decoherence_events.append(decoherence_event)

    def create_quantum_interference(self, concept_id1: str, concept_id2: str,
                                  interaction_type: str = "constructive") -> Dict:
        """Create quantum interference between two superposed concepts"""

        if concept_id1 not in self.superpositions or concept_id2 not in self.superpositions:
            raise ValueError("Both concepts must be in superposition")

        superposition1 = self.superpositions[concept_id1]
        superposition2 = self.superpositions[concept_id2]

        interference_result = {
            "concept_pair": [concept_id1, concept_id2],
            "interaction_type": interaction_type,
            "timestamp": datetime.now().isoformat(),
            "amplitude_changes": {}
        }

        # Find common superposition states
        common_states = set(superposition1.amplitudes.keys()) & set(superposition2.amplitudes.keys())

        for state in common_states:
            amp1 = superposition1.amplitudes[state]
            amp2 = superposition2.amplitudes[state]

            # Calculate interference
            if interaction_type == "constructive":
                # Amplitudes add constructively
                phase_alignment = 0  # In-phase
            elif interaction_type == "destructive":
                # Amplitudes add destructively
                phase_alignment = np.pi  # Out-of-phase
            else:  # "random"
                phase_alignment = np.random.uniform(0, 2 * np.pi)

            # Create interference effect
            interference_magnitude = 0.1  # Small interference effect

            # Apply phase-shifted interference to first concept
            phase_factor = cmath.exp(1j * phase_alignment)
            interference_amp = interference_magnitude * (amp2.real + 1j * amp2.imaginary) * phase_factor

            original_amp1 = amp1.real + 1j * amp1.imaginary
            new_amp1 = original_amp1 + interference_amp

            amp1.real = new_amp1.real
            amp1.imaginary = new_amp1.imag

            interference_result["amplitude_changes"][state.value] = {
                "original_magnitude": abs(original_amp1),
                "new_magnitude": abs(new_amp1),
                "phase_shift": float(np.angle(new_amp1) - np.angle(original_amp1))
            }

        # Renormalize both superpositions
        self.normalize_superposition(concept_id1)
        self.normalize_superposition(concept_id2)

        self.interference_patterns.append(interference_result)

        print(f"{interaction_type.title()} interference: {concept_id1} <-> {concept_id2}")

        return interference_result

    def normalize_superposition(self, concept_id: str):
        """Normalize superposition amplitudes to maintain probability conservation"""

        if concept_id not in self.superpositions:
            return

        superposition = self.superpositions[concept_id]

        # Calculate total probability
        total_prob = sum(amp.probability for amp in superposition.amplitudes.values())

        if total_prob > 0:
            normalization = np.sqrt(1.0 / total_prob)

            for amplitude in superposition.amplitudes.values():
                amplitude.real *= normalization
                amplitude.imaginary *= normalization

    def calculate_superposition_entropy(self, concept_id: str) -> float:
        """Calculate quantum entropy of superposition"""

        if concept_id not in self.superpositions:
            return 0.0

        superposition = self.superpositions[concept_id]

        # Von Neumann entropy for quantum state
        probabilities = [amp.probability for amp in superposition.amplitudes.values()]
        probabilities = [p for p in probabilities if p > 1e-10]  # Remove near-zero probs

        if not probabilities:
            return 0.0

        entropy = -sum(p * np.log2(p) for p in probabilities)
        return float(entropy)

    def evolve_superposition(self, concept_id: str, time_step: float = 0.1):
        """Evolve superposition according to Schrödinger equation"""

        if concept_id not in self.superpositions:
            return

        superposition = self.superpositions[concept_id]

        # Simple Hamiltonian evolution (conceptual frequencies)
        state_frequencies = {
            SuperpositionState.LITERAL: 1.0,
            SuperpositionState.METAPHORICAL: 1.2,
            SuperpositionState.TECHNICAL: 0.8,
            SuperpositionState.POETIC: 1.5,
            SuperpositionState.PHILOSOPHICAL: 0.6,
            SuperpositionState.PRACTICAL: 1.1,
            SuperpositionState.EMERGENT: 2.0,
            SuperpositionState.CONTRADICTORY: -0.5  # Negative frequency
        }

        for state, amplitude in superposition.amplitudes.items():
            if state in state_frequencies:
                frequency = state_frequencies[state]

                # Time evolution: ψ(t) = ψ(0) * exp(-iEt/ℏ)
                phase_evolution = frequency * time_step * 2 * np.pi

                # Apply time evolution
                current_amp = amplitude.real + 1j * amplitude.imaginary
                evolved_amp = current_amp * cmath.exp(-1j * phase_evolution)

                amplitude.real = evolved_amp.real
                amplitude.imaginary = evolved_amp.imag

        # Natural decoherence over time
        decoherence_factor = np.exp(-superposition.decoherence_rate * time_step)

        # Apply gradual decoherence (approach classical mixture)
        for amplitude in superposition.amplitudes.values():
            amplitude.real *= decoherence_factor
            amplitude.imaginary *= decoherence_factor

        self.normalize_superposition(concept_id)

    def get_superposition_status(self, concept_id: str) -> Dict:
        """Get comprehensive status of concept superposition"""

        if concept_id not in self.superpositions:
            return {"error": "Concept not in superposition"}

        superposition = self.superpositions[concept_id]

        # Calculate state probabilities
        state_probs = {}
        for state, amplitude in superposition.amplitudes.items():
            state_probs[state.value] = amplitude.probability

        # Find dominant state
        dominant_state = max(state_probs.items(), key=lambda x: x[1])

        return {
            "concept_id": concept_id,
            "state_probabilities": state_probs,
            "dominant_state": dominant_state[0],
            "dominant_probability": float(dominant_state[1]),
            "entropy": self.calculate_superposition_entropy(concept_id),
            "decoherence_rate": superposition.decoherence_rate,
            "measurement_count": len(superposition.measurement_history),
            "last_measurement": superposition.last_measurement,
            "coherence_time": float(1.0 / superposition.decoherence_rate) if superposition.decoherence_rate > 0 else float('inf')
        }

    def export_superpositions(self, filepath: str):
        """Export all superpositions to JSON"""

        export_data = {
            "superpositions": {},
            "decoherence_events": self.decoherence_events,
            "interference_patterns": self.interference_patterns,
            "export_timestamp": datetime.now().isoformat()
        }

        for concept_id, superposition in self.superpositions.items():
            # Convert to serializable format
            superposition_dict = {
                "concept_id": superposition.concept_id,
                "amplitudes": {},
                "decoherence_rate": superposition.decoherence_rate,
                "last_measurement": superposition.last_measurement,
                "measurement_history": superposition.measurement_history,
                "entanglement_effects": superposition.entanglement_effects
            }

            for state, amplitude in superposition.amplitudes.items():
                superposition_dict["amplitudes"][state.value] = {
                    "real": amplitude.real,
                    "imaginary": amplitude.imaginary,
                    "magnitude": amplitude.magnitude,
                    "phase": amplitude.phase,
                    "probability": amplitude.probability
                }

            export_data["superpositions"][concept_id] = superposition_dict

        with open(filepath, 'w') as f:
            json.dump(export_data, f, indent=2)

        print(f"Exported {len(self.superpositions)} superpositions to {filepath}")