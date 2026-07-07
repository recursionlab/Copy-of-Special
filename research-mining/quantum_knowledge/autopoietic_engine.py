"""
Autopoietic Concept Reproduction Engine
Living knowledge systems that self-create and self-maintain
"""

import numpy as np
import json
import uuid
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from enum import Enum
import random
import copy

class OrganismState(Enum):
    """States a concept organism can be in"""
    ACTIVE = "active"
    DORMANT = "dormant"
    REPRODUCING = "reproducing"
    DYING = "dying"
    DEAD = "dead"

class ReproductionMode(Enum):
    """Modes of reproduction"""
    ASEXUAL = "asexual"
    SEXUAL = "sexual"
    FRAGMENTATION = "fragmentation"
    BUDDING = "budding"

@dataclass
class LearningEvent:
    """Record of a learning event"""
    stimulus: str
    strength: float
    timestamp: str
    success: bool

@dataclass
class ReproductionEvent:
    """Record of a reproduction event"""
    parent_ids: List[str]
    offspring_id: str
    reproduction_mode: ReproductionMode
    energy_cost: float
    genetic_mutations: List[str]
    success: bool
    timestamp: str

@dataclass
class ConceptOrganism:
    """A living concept organism that can reproduce and evolve"""
    concept_id: str
    initial_energy: float  # Changed from energy to match test expectations
    genetic_code: str
    generation: int = 0
    age: float = 0.0
    state: OrganismState = OrganismState.ACTIVE
    reproduction_count: int = 0
    parent_ids: List[str] = None
    offspring_ids: List[str] = None
    memory_traces: List[str] = None
    learning_history: List[LearningEvent] = None
    birth_timestamp: str = None
    death_timestamp: Optional[str] = None
    id: str = None  # Organism ID for tracking

    def __post_init__(self):
        if self.parent_ids is None:
            self.parent_ids = []
        if self.offspring_ids is None:
            self.offspring_ids = []
        if self.memory_traces is None:
            self.memory_traces = []
        if self.learning_history is None:
            self.learning_history = []
        if self.birth_timestamp is None:
            self.birth_timestamp = datetime.now().isoformat()

        # Set energy from initial_energy for compatibility
        self.energy = self.initial_energy

    def age_cycle(self, time_step: float = 1.0):
        """Age the organism by one time step"""
        self.age += time_step

        # Aging reduces energy efficiency
        aging_factor = max(0.0, 1.0 - (self.age / 1000.0))  # Decline after age 1000
        if aging_factor < 1.0:
            energy_loss = self.energy * (1.0 - aging_factor) * 0.01
            self.energy = max(0.0, self.energy - energy_loss)

    def learn_from_stimulus(self, stimulus: str, strength: float) -> LearningEvent:
        """Learn from a stimulus and update memory"""
        # Learning consumes energy
        energy_cost = strength * 5.0
        success = self.energy >= energy_cost

        if success:
            self.energy -= energy_cost
            self.memory_traces.append(stimulus)

            # Strengthen existing memory or create new
            existing_memory = next(
                (mem for mem in self.learning_history if mem.stimulus == stimulus),
                None
            )

            if existing_memory:
                existing_memory.strength = min(1.0, existing_memory.strength + strength * 0.1)
            else:
                learning_event = LearningEvent(
                    stimulus=stimulus,
                    strength=strength,
                    timestamp=datetime.now().isoformat(),
                    success=True
                )
                self.learning_history.append(learning_event)

        return LearningEvent(
            stimulus=stimulus,
            strength=strength,
            timestamp=datetime.now().isoformat(),
            success=success
        )

    def calculate_fitness(self) -> float:
        """Calculate organism fitness for natural selection"""
        # Base fitness from energy
        energy_fitness = min(1.0, self.energy / 200.0)

        # Reproduction success contributes to fitness
        reproduction_fitness = min(1.0, self.reproduction_count / 10.0)

        # Experience (learning) contributes to fitness
        experience_fitness = min(1.0, len(self.memory_traces) / 20.0)

        # Age penalty (too young or too old is less fit)
        optimal_age = 100.0
        age_fitness = 1.0 - abs(self.age - optimal_age) / optimal_age
        age_fitness = max(0.0, age_fitness)

        # Weighted combination
        total_fitness = (
            0.4 * energy_fitness +
            0.3 * reproduction_fitness +
            0.2 * experience_fitness +
            0.1 * age_fitness
        )

        return total_fitness

class AutopoieticEngine:
    """Engine for managing autopoietic concept reproduction"""

    def __init__(self):
        self.organisms: Dict[str, ConceptOrganism] = {}
        self.reproduction_log: List[ReproductionEvent] = []
        self.ecosystem_energy: float = 10000.0
        self.selection_pressure: float = 0.1
        self.mutation_rate: float = 0.05

        # System constants
        self.METABOLISM_RATE = 0.5  # Energy consumed per time step
        self.REPRODUCTION_THRESHOLD = 100.0  # Minimum energy to reproduce
        self.SURVIVAL_THRESHOLD = 10.0  # Minimum energy to survive
        self.REPRODUCTION_COST_ASEXUAL = 50.0
        self.REPRODUCTION_COST_SEXUAL = 75.0

    def create_organism(self, concept_id: str, initial_energy: float,
                       genetic_code: str = None) -> ConceptOrganism:
        """Create a new concept organism"""
        if genetic_code is None:
            genetic_code = f"random-pattern-{random.randint(1000, 9999)}"

        organism_id = f"org-{uuid.uuid4().hex[:8]}"

        organism = ConceptOrganism(
            concept_id=concept_id,
            initial_energy=initial_energy,  # Use initial_energy parameter
            genetic_code=genetic_code
        )

        # Set the organism ID
        organism.id = organism_id

        self.organisms[organism_id] = organism
        return organism

    def metabolize_organism(self, organism_id: str, time_step: float = 1.0):
        """Process organism metabolism"""
        if organism_id not in self.organisms:
            return

        organism = self.organisms[organism_id]

        if organism.state == OrganismState.DEAD:
            return

        # Age the organism
        organism.age_cycle(time_step)

        # Metabolic energy consumption
        energy_cost = self.METABOLISM_RATE * time_step

        # Genetic efficiency affects metabolism
        if "efficient" in organism.genetic_code:
            energy_cost *= 0.8
        elif "wasteful" in organism.genetic_code:
            energy_cost *= 1.5

        organism.energy -= energy_cost

        # Check survival
        if organism.energy <= 0:
            organism.state = OrganismState.DEAD
            organism.death_timestamp = datetime.now().isoformat()
            organism.energy = 0.0

    def reproduce_asexual(self, parent_id: str) -> Optional[ConceptOrganism]:
        """Asexual reproduction of concept organism"""
        if parent_id not in self.organisms:
            return None

        parent = self.organisms[parent_id]

        # Check energy requirements
        if parent.energy < self.REPRODUCTION_THRESHOLD:
            return None

        if parent.state != OrganismState.ACTIVE:
            return None

        # Create offspring
        offspring_concept_id = f"offspring-{parent.concept_id}-{uuid.uuid4().hex[:6]}"
        offspring_genetic_code = self._mutate_genetic_code(parent.genetic_code)

        # Generate offspring ID first
        offspring_id = f"org-{uuid.uuid4().hex[:8]}"

        # Energy transfer
        energy_transfer = self.REPRODUCTION_COST_ASEXUAL
        parent.energy -= energy_transfer
        offspring_energy = energy_transfer * 0.8  # Some energy lost in process

        offspring = ConceptOrganism(
            concept_id=offspring_concept_id,
            initial_energy=offspring_energy,  # Use initial_energy parameter
            genetic_code=offspring_genetic_code,
            generation=parent.generation + 1,
            parent_ids=[parent_id]
        )

        # Set the offspring ID
        offspring.id = offspring_id

        # Inherit some memory (partial inheritance)
        inheritance_rate = 0.3
        inherited_memories = random.sample(
            parent.memory_traces,
            min(len(parent.memory_traces), int(len(parent.memory_traces) * inheritance_rate))
        )
        offspring.memory_traces = inherited_memories

        # Update parent
        self.organisms[offspring_id] = offspring
        parent.offspring_ids.append(offspring_id)
        parent.reproduction_count += 1

        # Log reproduction event
        reproduction_event = ReproductionEvent(
            parent_ids=[parent_id],
            offspring_id=offspring_id,
            reproduction_mode=ReproductionMode.ASEXUAL,
            energy_cost=energy_transfer,
            genetic_mutations=self._detect_mutations(parent.genetic_code, offspring_genetic_code),
            success=True,
            timestamp=datetime.now().isoformat()
        )
        self.reproduction_log.append(reproduction_event)

        return offspring

    def reproduce_sexual(self, parent1_id: str, parent2_id: str) -> Optional[ConceptOrganism]:
        """Sexual reproduction between two organisms"""
        if parent1_id not in self.organisms or parent2_id not in self.organisms:
            return None

        parent1 = self.organisms[parent1_id]
        parent2 = self.organisms[parent2_id]

        # Check energy requirements for both parents
        if (parent1.energy < self.REPRODUCTION_THRESHOLD or
            parent2.energy < self.REPRODUCTION_THRESHOLD):
            return None

        if (parent1.state != OrganismState.ACTIVE or
            parent2.state != OrganismState.ACTIVE):
            return None

        # Create offspring with combined genetics
        offspring_concept_id = f"hybrid-{parent1.concept_id}-{parent2.concept_id}-{uuid.uuid4().hex[:6]}"
        offspring_genetic_code = self._combine_genetic_codes(parent1.genetic_code, parent2.genetic_code)

        # Energy contribution from both parents
        energy_cost_each = self.REPRODUCTION_COST_SEXUAL / 2
        parent1.energy -= energy_cost_each
        parent2.energy -= energy_cost_each
        offspring_energy = energy_cost_each * 1.5  # Sexual reproduction bonus

        offspring_id = f"org-{uuid.uuid4().hex[:8]}"
        offspring = ConceptOrganism(
            concept_id=offspring_concept_id,
            initial_energy=offspring_energy,  # Use initial_energy parameter
            genetic_code=offspring_genetic_code,
            generation=max(parent1.generation, parent2.generation) + 1,
            parent_ids=[parent1_id, parent2_id]
        )

        # Set the offspring ID
        offspring.id = offspring_id
        self.organisms[offspring_id] = offspring

        # Inherit memories from both parents
        combined_memories = parent1.memory_traces + parent2.memory_traces
        inheritance_rate = 0.4
        inherited_memories = random.sample(
            combined_memories,
            min(len(combined_memories), int(len(combined_memories) * inheritance_rate))
        )
        offspring.memory_traces = list(set(inherited_memories))  # Remove duplicates

        # Update parents
        parent1.offspring_ids.append(offspring_id)
        parent2.offspring_ids.append(offspring_id)
        parent1.reproduction_count += 1
        parent2.reproduction_count += 1

        # Log reproduction event
        reproduction_event = ReproductionEvent(
            parent_ids=[parent1_id, parent2_id],
            offspring_id=offspring_id,
            reproduction_mode=ReproductionMode.SEXUAL,
            energy_cost=self.REPRODUCTION_COST_SEXUAL,
            genetic_mutations=self._detect_mutations(
                parent1.genetic_code + "|" + parent2.genetic_code,
                offspring_genetic_code
            ),
            success=True,
            timestamp=datetime.now().isoformat()
        )
        self.reproduction_log.append(reproduction_event)

        return offspring

    def apply_selection_pressure(self, pressure_strength: float = 0.5):
        """Apply natural selection pressure to ecosystem"""
        self.selection_pressure = pressure_strength

        active_organisms = [
            (org_id, org) for org_id, org in self.organisms.items()
            if org.state == OrganismState.ACTIVE
        ]

        # Calculate fitness for all organisms
        fitness_scores = [
            (org_id, org, org.calculate_fitness())
            for org_id, org in active_organisms
        ]

        # Sort by fitness (lowest first for selection pressure)
        fitness_scores.sort(key=lambda x: x[2])

        # Apply pressure to least fit organisms
        pressure_count = int(len(fitness_scores) * pressure_strength)

        for i in range(pressure_count):
            org_id, organism, fitness = fitness_scores[i]

            # Reduce energy proportional to poor fitness
            energy_penalty = organism.energy * (1.0 - fitness) * 0.3
            organism.energy = max(0, organism.energy - energy_penalty)

            # Check if organism dies from pressure
            if organism.energy <= self.SURVIVAL_THRESHOLD:
                organism.state = OrganismState.DEAD
                organism.death_timestamp = datetime.now().isoformat()

    def evolve_ecosystem(self, time_step: float = 1.0):
        """Evolve the entire ecosystem for one time step"""
        # Metabolize all organisms
        organism_ids = list(self.organisms.keys())
        for org_id in organism_ids:
            self.metabolize_organism(org_id, time_step)

        # Attempt reproduction for eligible organisms
        active_organisms = [
            org_id for org_id, org in self.organisms.items()
            if org.state == OrganismState.ACTIVE and org.energy >= self.REPRODUCTION_THRESHOLD
        ]

        # Random reproduction attempts
        reproduction_attempts = min(len(active_organisms) // 3, 5)

        for _ in range(reproduction_attempts):
            if len(active_organisms) == 0:
                break

            # 70% asexual, 30% sexual reproduction
            if random.random() < 0.7 or len(active_organisms) == 1:
                # Asexual reproduction
                parent_id = random.choice(active_organisms)
                self.reproduce_asexual(parent_id)
            else:
                # Sexual reproduction
                if len(active_organisms) >= 2:
                    parent1_id, parent2_id = random.sample(active_organisms, 2)
                    self.reproduce_sexual(parent1_id, parent2_id)

        # Apply selection pressure occasionally
        if random.random() < 0.3:
            self.apply_selection_pressure(self.selection_pressure)

    def detect_emergent_properties(self, organism_id: str) -> List[str]:
        """Detect emergent properties in an organism"""
        if organism_id not in self.organisms:
            return []

        organism = self.organisms[organism_id]
        emergent_traits = []

        # Check for genetic combinations that create new properties
        genetic_parts = organism.genetic_code.split("-")

        if len(genetic_parts) >= 2:
            # Look for novel combinations
            if "mathematical" in organism.genetic_code and "physical" in organism.genetic_code:
                emergent_traits.append("mathematical-physics-modeling")

            if "recursive" in organism.genetic_code and "adaptive" in organism.genetic_code:
                emergent_traits.append("self-modifying-recursion")

            if "efficient" in organism.genetic_code and "creative" in organism.genetic_code:
                emergent_traits.append("optimal-innovation")

        # High memory diversity creates meta-learning
        if len(set(organism.memory_traces)) > 10:
            emergent_traits.append("meta-learning-capability")

        # Multiple generations create evolutionary wisdom
        if organism.generation > 3:
            emergent_traits.append("evolutionary-wisdom")

        return emergent_traits

    def calculate_diversity_index(self) -> float:
        """Calculate ecosystem diversity (Shannon diversity)"""
        active_organisms = [
            org for org in self.organisms.values()
            if org.state == OrganismState.ACTIVE
        ]

        if not active_organisms:
            return 0.0

        # Count unique genetic patterns
        genetic_counts = {}
        for org in active_organisms:
            pattern = org.genetic_code  # Use full genetic code as pattern
            genetic_counts[pattern] = genetic_counts.get(pattern, 0) + 1

        # Shannon diversity index
        total = len(active_organisms)
        diversity = 0.0

        for count in genetic_counts.values():
            if count > 0:
                proportion = count / total
                diversity -= proportion * np.log(proportion)

        return diversity

    def total_ecosystem_energy(self) -> float:
        """Calculate total energy in ecosystem"""
        return sum(
            org.energy for org in self.organisms.values()
            if org.state == OrganismState.ACTIVE
        )

    def serialize_organism(self, organism_id: str) -> str:
        """Serialize organism to JSON string"""
        if organism_id not in self.organisms:
            return "{}"

        organism = self.organisms[organism_id]

        # Convert dataclass to dict
        organism_dict = asdict(organism)

        # Handle enum serialization
        organism_dict["state"] = organism.state.value

        return json.dumps(organism_dict, indent=2)

    def deserialize_organism(self, json_str: str) -> ConceptOrganism:
        """Deserialize organism from JSON string"""
        data = json.loads(json_str)

        # Convert state back to enum
        data["state"] = OrganismState(data["state"])

        # Reconstruct learning history
        if data.get("learning_history"):
            data["learning_history"] = [
                LearningEvent(**event) for event in data["learning_history"]
            ]

        return ConceptOrganism(**data)

    def export_ecosystem(self, filepath: str):
        """Export entire ecosystem to JSON file"""
        export_data = {
            "organisms": {},
            "reproduction_log": [],
            "ecosystem_energy": self.ecosystem_energy,
            "selection_pressure": self.selection_pressure,
            "mutation_rate": self.mutation_rate,
            "export_timestamp": datetime.now().isoformat()
        }

        # Serialize all organisms
        for org_id, organism in self.organisms.items():
            organism_dict = asdict(organism)
            organism_dict["state"] = organism.state.value

            # Handle learning history
            if organism.learning_history:
                organism_dict["learning_history"] = [
                    asdict(event) for event in organism.learning_history
                ]

            export_data["organisms"][org_id] = organism_dict

        # Serialize reproduction log
        for event in self.reproduction_log:
            event_dict = asdict(event)
            event_dict["reproduction_mode"] = event.reproduction_mode.value
            export_data["reproduction_log"].append(event_dict)

        with open(filepath, 'w') as f:
            json.dump(export_data, f, indent=2)

    def import_ecosystem(self, filepath: str):
        """Import ecosystem from JSON file"""
        with open(filepath, 'r') as f:
            data = json.load(f)

        # Clear current ecosystem
        self.organisms = {}
        self.reproduction_log = []

        # Import settings
        self.ecosystem_energy = data.get("ecosystem_energy", 10000.0)
        self.selection_pressure = data.get("selection_pressure", 0.1)
        self.mutation_rate = data.get("mutation_rate", 0.05)

        # Import organisms
        for org_id, org_data in data.get("organisms", {}).items():
            org_data["state"] = OrganismState(org_data["state"])

            # Reconstruct learning history
            if org_data.get("learning_history"):
                org_data["learning_history"] = [
                    LearningEvent(**event) for event in org_data["learning_history"]
                ]

            self.organisms[org_id] = ConceptOrganism(**org_data)

        # Import reproduction log
        for event_data in data.get("reproduction_log", []):
            event_data["reproduction_mode"] = ReproductionMode(event_data["reproduction_mode"])
            self.reproduction_log.append(ReproductionEvent(**event_data))

    def _mutate_genetic_code(self, genetic_code: str) -> str:
        """Apply random mutations to genetic code"""
        if random.random() > self.mutation_rate:
            return genetic_code  # No mutation

        # Simple mutation: add random suffix or modify existing
        mutations = [
            "mutated", "evolved", "adapted", "enhanced", "modified"
        ]

        if "-" in genetic_code:
            parts = genetic_code.split("-")
            parts.append(random.choice(mutations))
            return "-".join(parts)
        else:
            return f"{genetic_code}-{random.choice(mutations)}"

    def _combine_genetic_codes(self, code1: str, code2: str) -> str:
        """Combine two genetic codes for sexual reproduction"""
        # Extract key features from both codes
        parts1 = code1.split("-")
        parts2 = code2.split("-")

        # Take features from both parents
        combined_parts = []

        # Alternate features
        max_parts = max(len(parts1), len(parts2))
        for i in range(max_parts):
            if i < len(parts1) and random.random() < 0.5:
                combined_parts.append(parts1[i])
            elif i < len(parts2):
                combined_parts.append(parts2[i])

        # Apply potential mutation
        combined_code = "-".join(combined_parts)
        return self._mutate_genetic_code(combined_code)

    def _detect_mutations(self, parent_code: str, offspring_code: str) -> List[str]:
        """Detect what mutations occurred between parent and offspring"""
        parent_parts = set(parent_code.split("-"))
        offspring_parts = set(offspring_code.split("-"))

        mutations = list(offspring_parts - parent_parts)
        return mutations