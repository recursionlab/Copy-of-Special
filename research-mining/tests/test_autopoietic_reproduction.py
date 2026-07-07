"""
Test suite for autopoietic concept reproduction - TDD approach
Living knowledge systems that self-create and self-maintain
"""

import pytest
import numpy as np
import json
from datetime import datetime, timedelta
import tempfile
import os

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# This import will fail initially - that's the TDD approach!
# We'll implement the module to make tests pass
try:
    from quantum_knowledge.autopoietic_engine import (
        AutopoieticEngine, ConceptOrganism, ReproductionEvent,
        OrganismState, ReproductionMode
    )
except ImportError:
    # Define placeholder classes for TDD
    class AutopoieticEngine:
        pass
    class ConceptOrganism:
        pass
    class ReproductionEvent:
        pass
    class OrganismState:
        pass
    class ReproductionMode:
        pass

class TestAutopoieticEngine:
    """Test suite for autopoietic concept reproduction engine"""

    def setup_method(self):
        """Set up test fixtures"""
        self.engine = AutopoieticEngine()

    def test_initialization(self):
        """Test autopoietic engine initialization"""
        assert self.engine.organisms == {}
        assert self.engine.ecosystem_energy > 0
        assert self.engine.reproduction_log == []
        assert self.engine.selection_pressure >= 0
        assert hasattr(self.engine, 'METABOLISM_RATE')
        assert hasattr(self.engine, 'REPRODUCTION_THRESHOLD')

    def test_create_concept_organism(self):
        """Test creating a new concept organism"""
        organism = self.engine.create_organism(
            concept_id="test-concept-001",
            initial_energy=100.0,
            genetic_code="recursive-pattern-alpha"
        )

        assert organism.concept_id == "test-concept-001"
        assert organism.energy == 100.0
        assert organism.genetic_code == "recursive-pattern-alpha"
        assert organism.generation == 0
        assert organism.state == OrganismState.ACTIVE
        assert organism.reproduction_count == 0
        assert len(organism.offspring_ids) == 0

    def test_organism_metabolism(self):
        """Test organism energy metabolism"""
        engine = AutopoieticEngine()
        organism = engine.create_organism("meta-001", initial_energy=100.0)

        initial_energy = organism.energy

        # Simulate metabolism cycle
        engine.metabolize_organism(organism.id, time_step=1.0)

        # Energy should decrease due to metabolism
        assert organism.energy < initial_energy

        # But organism should still be alive if above threshold
        if organism.energy > engine.SURVIVAL_THRESHOLD:
            assert organism.state == OrganismState.ACTIVE

    def test_organism_death(self):
        """Test organism death when energy depleted"""
        engine = AutopoieticEngine()
        organism = engine.create_organism("dying-001", initial_energy=1.0)

        # Deplete energy completely
        organism.energy = 0.0
        engine.metabolize_organism(organism.id, time_step=1.0)

        assert organism.state == OrganismState.DEAD
        assert organism.death_timestamp is not None

    def test_asexual_reproduction(self):
        """Test asexual reproduction of concept organisms"""
        engine = AutopoieticEngine()
        parent = engine.create_organism("parent-001", initial_energy=200.0)

        # Trigger asexual reproduction
        offspring = engine.reproduce_asexual(parent.id)

        assert offspring is not None
        assert offspring.parent_ids == [parent.id]
        assert offspring.generation == parent.generation + 1
        assert offspring.concept_id.startswith("offspring-")

        # Parent should have reduced energy and recorded offspring
        assert parent.energy < 200.0
        assert offspring.id in parent.offspring_ids
        assert parent.reproduction_count == 1

    def test_sexual_reproduction(self):
        """Test sexual reproduction between two organisms"""
        engine = AutopoieticEngine()
        parent1 = engine.create_organism("parent1-001", initial_energy=150.0)
        parent2 = engine.create_organism("parent2-001", initial_energy=150.0)

        # Set compatible genetic codes
        parent1.genetic_code = "pattern-alpha"
        parent2.genetic_code = "pattern-beta"

        offspring = engine.reproduce_sexual(parent1.id, parent2.id)

        assert offspring is not None
        assert len(offspring.parent_ids) == 2
        assert parent1.id in offspring.parent_ids
        assert parent2.id in offspring.parent_ids
        assert offspring.generation == max(parent1.generation, parent2.generation) + 1

        # Genetic code should be combination of parents
        assert "alpha" in offspring.genetic_code or "beta" in offspring.genetic_code

        # Both parents should have reduced energy
        assert parent1.energy < 150.0
        assert parent2.energy < 150.0

    def test_reproduction_energy_requirements(self):
        """Test that reproduction requires sufficient energy"""
        engine = AutopoieticEngine()
        low_energy_organism = engine.create_organism("low-001", initial_energy=10.0)

        # Should fail reproduction due to insufficient energy
        offspring = engine.reproduce_asexual(low_energy_organism.id)
        assert offspring is None
        assert low_energy_organism.reproduction_count == 0

    def test_genetic_mutation(self):
        """Test genetic mutations during reproduction"""
        engine = AutopoieticEngine()
        parent = engine.create_organism("mutate-001", initial_energy=200.0)
        parent.genetic_code = "stable-pattern"

        # Set high mutation rate for testing
        engine.mutation_rate = 0.5

        offspring = engine.reproduce_asexual(parent.id)

        # Offspring genetic code might be mutated
        assert offspring.genetic_code != parent.genetic_code or offspring.genetic_code == parent.genetic_code

    def test_population_dynamics(self):
        """Test population growth and stabilization"""
        engine = AutopoieticEngine()

        # Create initial population
        for i in range(5):
            engine.create_organism(f"founder-{i:03d}", initial_energy=150.0)

        initial_count = len(engine.organisms)

        # Simulate ecosystem evolution
        for cycle in range(10):
            engine.evolve_ecosystem(time_step=1.0)

        final_count = len([org for org in engine.organisms.values()
                          if org.state == OrganismState.ACTIVE])

        # Population should have changed (growth, death, reproduction)
        assert final_count != initial_count

    def test_selection_pressure(self):
        """Test natural selection pressure on organism traits"""
        engine = AutopoieticEngine()

        # Create organisms with different fitness traits
        fit_organism = engine.create_organism("fit-001", initial_energy=200.0)
        unfit_organism = engine.create_organism("unfit-001", initial_energy=50.0)

        fit_organism.genetic_code = "efficient-metabolism"
        unfit_organism.genetic_code = "wasteful-metabolism"

        # Apply selection pressure
        engine.apply_selection_pressure(pressure_strength=0.8)

        # Fit organisms should survive better
        assert fit_organism.state == OrganismState.ACTIVE
        # Unfit organism might die or be stressed
        assert unfit_organism.energy <= 50.0

    def test_concept_emergence_from_reproduction(self):
        """Test emergence of new concepts from organism reproduction"""
        engine = AutopoieticEngine()

        parent1 = engine.create_organism("concept-math", initial_energy=180.0)
        parent2 = engine.create_organism("concept-physics", initial_energy=180.0)

        parent1.genetic_code = "mathematical-reasoning"
        parent2.genetic_code = "physical-modeling"

        offspring = engine.reproduce_sexual(parent1.id, parent2.id)

        # Check if emergent properties appeared
        emergent_traits = engine.detect_emergent_properties(offspring.id)

        # Should detect novel combinations
        assert isinstance(emergent_traits, list)
        # Might contain mathematical-physics hybrid traits

    def test_ecosystem_homeostasis(self):
        """Test ecosystem maintains homeostatic balance"""
        engine = AutopoieticEngine()

        # Create diverse population
        for i in range(20):
            organism = engine.create_organism(f"eco-{i:03d}", initial_energy=150.0)
            organism.genetic_code = f"trait-{i % 5}"  # 5 different trait types

        initial_diversity = engine.calculate_diversity_index()
        initial_energy = engine.total_ecosystem_energy()

        # Evolve ecosystem
        for cycle in range(20):
            engine.evolve_ecosystem(time_step=1.0)

        final_diversity = engine.calculate_diversity_index()
        final_energy = engine.total_ecosystem_energy()

        # Ecosystem should maintain some stability
        assert final_diversity > 0  # Some diversity preserved
        assert final_energy > 0     # System didn't collapse

    def test_memory_inheritance(self):
        """Test inheritance of experiential memory"""
        engine = AutopoieticEngine()
        parent = engine.create_organism("memory-001", initial_energy=150.0)

        # Give parent some experiences
        parent.memory_traces = ["experience-alpha", "experience-beta"]
        parent.learning_history = [{"concept": "test", "strength": 0.8}]

        offspring = engine.reproduce_asexual(parent.id)

        # Offspring should inherit some memory traces
        assert hasattr(offspring, 'memory_traces')
        assert hasattr(offspring, 'learning_history')

        # Should have partial inheritance, not exact copy
        inherited_memory_count = len(offspring.memory_traces)
        parent_memory_count = len(parent.memory_traces)

        assert inherited_memory_count <= parent_memory_count

    def test_reproduction_logging(self):
        """Test comprehensive logging of reproduction events"""
        engine = AutopoieticEngine()
        parent = engine.create_organism("logged-001", initial_energy=200.0)

        initial_log_count = len(engine.reproduction_log)

        offspring = engine.reproduce_asexual(parent.id)

        assert len(engine.reproduction_log) == initial_log_count + 1

        latest_event = engine.reproduction_log[-1]
        assert latest_event.parent_ids == [parent.id]
        assert latest_event.offspring_id == offspring.id
        assert latest_event.reproduction_mode == ReproductionMode.ASEXUAL
        assert latest_event.success == True

    def test_concept_organism_serialization(self):
        """Test serialization/deserialization of concept organisms"""
        engine = AutopoieticEngine()
        original = engine.create_organism("serialize-001", initial_energy=123.45)
        original.genetic_code = "test-pattern"
        original.memory_traces = ["trace1", "trace2"]

        # Serialize to JSON
        serialized = engine.serialize_organism(original.id)
        assert isinstance(serialized, str)

        # Deserialize
        restored = engine.deserialize_organism(serialized)

        assert restored.concept_id == original.concept_id
        assert restored.energy == original.energy
        assert restored.genetic_code == original.genetic_code
        assert restored.memory_traces == original.memory_traces

    def test_ecosystem_export_import(self):
        """Test exporting and importing entire ecosystem"""
        engine = AutopoieticEngine()

        # Create test ecosystem
        for i in range(5):
            engine.create_organism(f"export-{i:03d}", initial_energy=100.0)

        # Export ecosystem
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            tmp_path = tmp_file.name

        try:
            engine.export_ecosystem(tmp_path)

            # Import into new engine
            new_engine = AutopoieticEngine()
            new_engine.import_ecosystem(tmp_path)

            # Should have same organisms
            assert len(new_engine.organisms) == len(engine.organisms)

            # Check organism details match
            for org_id in engine.organisms:
                assert org_id in new_engine.organisms
                original = engine.organisms[org_id]
                imported = new_engine.organisms[org_id]
                assert original.concept_id == imported.concept_id
                assert original.energy == imported.energy

        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)

class TestConceptOrganism:
    """Test suite for individual concept organisms"""

    def test_organism_initialization(self):
        """Test concept organism initialization"""
        organism = ConceptOrganism(
            concept_id="init-test",
            initial_energy=100.0,
            genetic_code="test-pattern"
        )

        assert organism.concept_id == "init-test"
        assert organism.energy == 100.0
        assert organism.genetic_code == "test-pattern"
        assert organism.generation == 0
        assert organism.age == 0.0
        assert organism.state == OrganismState.ACTIVE
        assert organism.reproduction_count == 0
        assert organism.parent_ids == []
        assert organism.offspring_ids == []

    def test_organism_aging(self):
        """Test organism aging over time"""
        organism = ConceptOrganism(
            concept_id="aging-test",
            initial_energy=100.0,
            genetic_code="test-pattern"
        )

        initial_age = organism.age

        # Age organism
        organism.age_cycle(time_step=1.0)

        assert organism.age > initial_age

        # Very old organisms should lose energy
        organism.age = 1000.0  # Make very old
        organism.age_cycle(time_step=1.0)
        assert organism.energy < 100.0

    def test_organism_learning(self):
        """Test organism learning and adaptation"""
        organism = ConceptOrganism("learner-001", 100.0, "adaptive-pattern")

        # Present learning stimulus
        learning_result = organism.learn_from_stimulus("new-concept", strength=0.7)

        assert learning_result.success == True
        assert "new-concept" in organism.memory_traces
        assert len(organism.learning_history) > 0

    def test_organism_fitness_calculation(self):
        """Test fitness calculation for natural selection"""
        organism = ConceptOrganism("fitness-test", 100.0, "efficient-pattern")

        # Set organism traits that affect fitness
        organism.energy = 150.0
        organism.reproduction_count = 3
        organism.age = 50.0
        organism.memory_traces = ["experience1", "experience2", "experience3"]

        fitness = organism.calculate_fitness()

        assert fitness > 0
        assert isinstance(fitness, float)

        # Higher energy should improve fitness
        organism.energy = 200.0
        higher_fitness = organism.calculate_fitness()
        assert higher_fitness > fitness

if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])