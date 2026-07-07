"""
Advanced concept extractors for specific research domains
"""

import re
from typing import List, Dict, Any, Optional
from datetime import datetime
from .pipeline import ConceptUnit


class FunctorExtractor:
    """Specialized extractor for functor concepts"""
    
    def __init__(self):
        self.patterns = [
            # Category theory definitions
            r'(?:A\s+)?functor\s+F\s*:\s*([A-Z])\s*→\s*([A-Z])\s+(.{20,400})',
            
            # Programming contexts
            r'functor[s]?\s+in\s+(?:Haskell|functional\s+programming)\s+(.{20,400})',
            
            # Mathematical definitions
            r'(?:endofunctor|bifunctor|contravariant\s+functor)\s+(.{20,400})',
            
            # Composition preservation
            r'functor[s]?\s+preserve[s]?\s+composition\s+(.{20,400})',
        ]
        
        self.math_patterns = [
            r'F\s*\(\s*g\s*∘\s*f\s*\)\s*=\s*F\s*\(\s*g\s*\)\s*∘\s*F\s*\(\s*f\s*\)',
            r'F\s*\(\s*id[A-Z]\s*\)\s*=\s*id[A-Z]',
        ]
    
    def extract(self, content: str, source: str) -> List[ConceptUnit]:
        """Extract functor concepts with enhanced context"""
        concepts = []
        
        for pattern in self.patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE)
            for match in matches:
                definition = match.group(-1).strip()  # Last group is definition
                
                # Extract mathematical formulation if present
                math_context = self._extract_math_context(content, match.start(), match.end())
                
                # Determine functor subtype
                functor_type = self._classify_functor_type(definition)
                
                concept = ConceptUnit(
                    id=f"functor-{hash(definition) % 10000}",
                    source=source,
                    type="Functor",
                    definition=definition,
                    mathematical_formulation=math_context,
                    tags=[functor_type, "category theory"],
                    confidence_score=0.85,
                    extraction_date=datetime.now().isoformat(),
                    notes=f"Functor subtype: {functor_type}"
                )
                concepts.append(concept)
        
        return concepts
    
    def _extract_math_context(self, content: str, start: int, end: int) -> Optional[str]:
        """Extract mathematical formulation around the match"""
        # Look for math patterns in surrounding context
        context_start = max(0, start - 200)
        context_end = min(len(content), end + 200)
        context = content[context_start:context_end]
        
        for pattern in self.math_patterns:
            match = re.search(pattern, context)
            if match:
                return match.group(0)
        
        return None
    
    def _classify_functor_type(self, definition: str) -> str:
        """Classify the type of functor based on definition"""
        definition_lower = definition.lower()
        
        if 'contravariant' in definition_lower:
            return 'contravariant'
        elif 'covariant' in definition_lower:
            return 'covariant'
        elif 'endofunctor' in definition_lower:
            return 'endofunctor'
        elif 'bifunctor' in definition_lower:
            return 'bifunctor'
        else:
            return 'functor'


class RecursionExtractor:
    """Specialized extractor for recursion concepts"""
    
    def __init__(self):
        self.patterns = [
            # Kleene's recursion theorem
            r'(?:Kleene.{0,30})?(?:second\s+)?recursion\s+theorem\s+(.{30,500})',
            
            # Fixed point theory
            r'fixed\s+point[s]?\s+(?:theorem|combinator|operator)\s+(.{30,500})',
            
            # Self-reference
            r'self-referential\s+(?:function|definition|structure)\s+(.{30,500})',
            
            # Computational recursion
            r'recursive\s+(?:algorithm|function|procedure)\s+(.{30,500})',
        ]
    
    def extract(self, content: str, source: str) -> List[ConceptUnit]:
        """Extract recursion concepts with mathematical context"""
        concepts = []
        
        for pattern in self.patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE)
            for match in matches:
                definition = match.group(1).strip()
                
                # Check for specific recursion types
                recursion_type = self._classify_recursion_type(definition)
                
                concept = ConceptUnit(
                    id=f"recursion-{hash(definition) % 10000}",
                    source=source,
                    type="Recursion",
                    definition=definition,
                    tags=[recursion_type, "recursion theory", "self-reference"],
                    confidence_score=0.8,
                    extraction_date=datetime.now().isoformat(),
                    notes=f"Recursion type: {recursion_type}"
                )
                concepts.append(concept)
        
        return concepts
    
    def _classify_recursion_type(self, definition: str) -> str:
        """Classify the type of recursion"""
        definition_lower = definition.lower()
        
        if 'kleene' in definition_lower:
            return 'kleene-recursion'
        elif 'fixed point' in definition_lower:
            return 'fixed-point'
        elif 'tail recursion' in definition_lower:
            return 'tail-recursion'
        elif 'mutual recursion' in definition_lower:
            return 'mutual-recursion'
        else:
            return 'general-recursion'


class AutopoiesisExtractor:
    """Specialized extractor for autopoiesis concepts"""
    
    def __init__(self):
        self.patterns = [
            # Maturana and Varela definitions
            r'(?:Maturana|Varela).{0,50}autopoiesi[s]?\s+(.{30,500})',
            
            # Self-organization
            r'self-(?:organizing|producing|maintaining)\s+system[s]?\s+(.{30,500})',
            
            # Structural coupling
            r'structural\s+coupling\s+(.{30,500})',
            
            # Living systems
            r'(?:living|biological)\s+system[s]?\s+(?:as\s+)?autopoietic\s+(.{30,500})',
        ]
    
    def extract(self, content: str, source: str) -> List[ConceptUnit]:
        """Extract autopoiesis concepts"""
        concepts = []
        
        for pattern in self.patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE)
            for match in matches:
                definition = match.group(1).strip()
                
                concept = ConceptUnit(
                    id=f"autopoiesis-{hash(definition) % 10000}",
                    source=source,
                    type="Autopoiesis",
                    definition=definition,
                    tags=["autopoiesis", "self-organization", "systems theory"],
                    confidence_score=0.75,
                    extraction_date=datetime.now().isoformat(),
                    references=["Maturana, H. & Varela, F. (1980). Autopoiesis and Cognition."]
                )
                concepts.append(concept)
        
        return concepts


class AdvancedPipeline:
    """Enhanced pipeline with specialized extractors"""
    
    def __init__(self):
        self.extractors = {
            'functor': FunctorExtractor(),
            'recursion': RecursionExtractor(),
            'autopoiesis': AutopoiesisExtractor()
        }
    
    def extract_all_concepts(self, content: str, source: str) -> List[ConceptUnit]:
        """Extract concepts using all specialized extractors"""
        all_concepts = []
        
        for extractor_name, extractor in self.extractors.items():
            concepts = extractor.extract(content, source)
            all_concepts.extend(concepts)
            print(f"Extracted {len(concepts)} {extractor_name} concepts")
        
        return all_concepts
