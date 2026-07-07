"""
Research Mining Ingestion Pipeline
Handles PDF, Markdown, and TXT file processing with ConceptUnit extraction
"""

import json
import os
import re
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
import hashlib

# PDF processing
try:
    import PyPDF2
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# Schema validation
try:
    import jsonschema
    VALIDATION_AVAILABLE = True
except ImportError:
    VALIDATION_AVAILABLE = False

from pydantic import BaseModel, Field, ValidationError


class ConceptUnit(BaseModel):
    """Enhanced ConceptUnit model with validation"""
    id: str = Field(..., pattern=r'^[a-zA-Z0-9_-]+$')
    version: Optional[str] = "1.0.0"
    source: str
    type: str
    definition: str = Field(..., min_length=10)
    mathematical_formulation: Optional[str] = None
    relations: Optional[List[str]] = []
    examples: Optional[List[str]] = []
    prototypes: Optional[List[str]] = []
    references: Optional[List[str]] = []
    tags: Optional[List[str]] = []
    extraction_date: Optional[str] = None
    confidence_score: Optional[float] = Field(None, ge=0, le=1)
    notes: Optional[str] = None


class IngestionPipeline:
    """Main ingestion pipeline for research artifacts"""
    
    def __init__(self, schema_path: str = None):
        self.schema_path = schema_path
        self.schema = self._load_schema() if schema_path else None
        self.extracted_units = []
        
    def _load_schema(self) -> Dict[str, Any]:
        """Load JSON schema for validation"""
        try:
            with open(self.schema_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: Could not load schema: {e}")
            return None
    
    def load_pdf(self, file_path: str) -> str:
        """Extract text from PDF file"""
        if not PDF_AVAILABLE:
            raise ImportError("PyPDF2 not available. Install with: pip install PyPDF2")
        
        text = ""
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
        except Exception as e:
            print(f"Error reading PDF {file_path}: {e}")
        
        return text
    
    def load_markdown(self, file_path: str) -> str:
        """Load markdown file content"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading markdown {file_path}: {e}")
            return ""
    
    def load_txt(self, file_path: str) -> str:
        """Load text file content"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading text {file_path}: {e}")
            return ""

    def _extract_texts_from_obj(self, obj: Any, min_length: int = 30) -> List[str]:
        """Recursively extract textual content fields from a JSON object."""
        texts: List[str] = []

        if isinstance(obj, str):
            if len(obj) >= min_length:
                texts.append(obj)
            return texts

        if isinstance(obj, dict):
            for k, v in obj.items():
                # prefer known text keys
                if isinstance(k, str) and k.lower() in ('content', 'text', 'message', 'body', 'utterance', 'reply'):
                    if isinstance(v, str) and len(v) >= min_length:
                        texts.append(v)
                        continue
                texts.extend(self._extract_texts_from_obj(v, min_length))
            return texts

        if isinstance(obj, list):
            for item in obj:
                texts.extend(self._extract_texts_from_obj(item, min_length))
            return texts

        return texts

    def process_json(self, file_path: str, max_items: int = 2000) -> List[ConceptUnit]:
        """Stream-process a large JSON file and extract ConceptUnits from textual fields.

        This handles both JSON arrays and line-delimited JSON safely without loading the
        entire file into memory. The `max_items` parameter limits how many top-level
        objects are processed to avoid long runs during testing.
        """
        decoder = json.JSONDecoder()
        collected: List[ConceptUnit] = []
        processed = 0

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                # Peek first non-whitespace char
                first_chars = f.read(2)
                if not first_chars:
                    return []
                f.seek(0)
                first = first_chars.lstrip()[0]

                if first == '[':
                    # JSON array: use incremental raw_decode on buffer
                    buf = ''
                    # skip the opening '['
                    f.read(1)
                    while True:
                        chunk = f.read(65536)
                        if not chunk:
                            break
                        buf += chunk
                        idx = 0
                        while True:
                            try:
                                obj, offset = decoder.raw_decode(buf)
                            except ValueError:
                                break
                            # move buffer forward
                            buf = buf[offset:]
                            # strip any leading commas or whitespace
                            buf = buf.lstrip(',\n\r \t')

                            texts = self._extract_texts_from_obj(obj)
                            for text in texts:
                                units = self.extract_concepts(text, file_path)
                                for u in units:
                                    if self.validate_concept(u):
                                        collected.append(u)
                                        self.extracted_units.append(u)

                            processed += 1
                            if max_items and processed >= max_items:
                                return collected

                else:
                    # NDJSON or line-delimited JSON: parse line by line
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                        except Exception:
                            # try to recover JSON object fragments by skipping
                            continue

                        texts = self._extract_texts_from_obj(obj)
                        for text in texts:
                            units = self.extract_concepts(text, file_path)
                            for u in units:
                                if self.validate_concept(u):
                                    collected.append(u)
                                    self.extracted_units.append(u)

                        processed += 1
                        if max_items and processed >= max_items:
                            break

        except Exception as e:
            print(f"Error processing JSON {file_path}: {e}")

        return collected
    
    def generate_id(self, source: str, concept_type: str) -> str:
        """Generate unique ID for ConceptUnit"""
        # Create hash from source and type
        content = f"{source}-{concept_type}"
        hash_obj = hashlib.md5(content.encode())
        hash_hex = hash_obj.hexdigest()[:8]
        
        # Format: type-hash
        clean_type = re.sub(r'[^a-zA-Z0-9]', '', concept_type.lower())
        return f"{clean_type}-{hash_hex}"
    
    def extract_concepts(self, content: str, source: str) -> List[ConceptUnit]:
        """Extract concepts from text content using pattern matching"""
        concepts = []
        
        # Pattern-based extraction (can be enhanced with NLP)
        patterns = {
            'Functor': [
                r'functor[s]?\s+(?:is|are|means?)\s+(.{10,200})',
                r'(?:define|definition of)\s+functor[s]?\s*:?\s*(.{10,200})',
                r'functor[s]?\s+(?:preserves?|maps?|transforms?)\s+(.{10,200})'
            ],
            'Recursion': [
                r'recursive[ly]?\s+(?:defined|function|process)\s+(.{10,200})',
                r'recursion[s]?\s+(?:is|means?|involves?)\s+(.{10,200})',
                r'self-referential\s+(.{10,200})'
            ],
            'Autopoiesis': [
                r'autopoiesi[s]?\s+(?:is|means?)\s+(.{10,200})',
                r'self-(?:organizing|producing|maintaining)\s+(.{10,200})',
                r'autopoietic\s+system[s]?\s+(.{10,200})'
            ]
        }
        
        for concept_type, type_patterns in patterns.items():
            for pattern in type_patterns:
                matches = re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE)
                for match in matches:
                    definition = match.group(1).strip()
                    if len(definition) >= 10:  # Minimum definition length
                        try:
                            unit = ConceptUnit(
                                id=self.generate_id(source, concept_type),
                                source=source,
                                type=concept_type,
                                definition=definition,
                                extraction_date=datetime.now().isoformat(),
                                confidence_score=0.7,  # Pattern-based extraction
                                notes=f"Extracted using pattern: {pattern}"
                            )
                            concepts.append(unit)
                        except ValidationError as e:
                            print(f"Validation error for concept: {e}")
        
        return concepts
    
    def validate_concept(self, concept: ConceptUnit) -> bool:
        """Validate ConceptUnit against schema"""
        if not self.schema or not VALIDATION_AVAILABLE:
            return True  # Skip validation if schema not available
        
        try:
            # remove None values to be tolerant of partial extractions
            inst = {k: v for k, v in concept.dict().items() if v is not None}
            jsonschema.validate(inst, self.schema)
            return True
        except jsonschema.ValidationError as e:
            print(f"Schema validation failed: {e}")
            return False
    
    def process_file(self, file_path: str) -> List[ConceptUnit]:
        """Process a single file and extract ConceptUnits"""
        file_path = Path(file_path)
        
        # Load content based on file type
        if file_path.suffix.lower() == '.pdf':
            content = self.load_pdf(str(file_path))
        elif file_path.suffix.lower() == '.md':
            content = self.load_markdown(str(file_path))
        elif file_path.suffix.lower() == '.txt':
            content = self.load_txt(str(file_path))
        else:
            print(f"Unsupported file type: {file_path.suffix}")
            return []
        
        if not content:
            return []
        
        # Extract concepts
        concepts = self.extract_concepts(content, str(file_path))
        
        # Validate concepts
        valid_concepts = []
        for concept in concepts:
            if self.validate_concept(concept):
                valid_concepts.append(concept)
        
        self.extracted_units.extend(valid_concepts)
        return valid_concepts
    
    def process_directory(self, directory_path: str, recursive: bool = True) -> List[ConceptUnit]:
        """Process all supported files in a directory"""
        directory = Path(directory_path)
        all_concepts = []
        
        pattern = "**/*" if recursive else "*"
        for file_path in directory.glob(pattern):
            if file_path.is_file() and file_path.suffix.lower() in ['.pdf', '.md', '.txt', '.json']:
                print(f"Processing: {file_path}")
                # route json to process_json for streaming
                if file_path.suffix.lower() == '.json':
                    concepts = self.process_json(str(file_path), max_items=200)
                else:
                    concepts = self.process_file(str(file_path))
                all_concepts.extend(concepts)
                print(f"Extracted {len(concepts)} concepts from {file_path.name}")
        
        return all_concepts
    
    def export_concepts(self, output_path: str, format: str = 'json') -> None:
        """Export extracted ConceptUnits to file"""
        output_path = Path(output_path)
        # Ensure output directory exists
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
        except Exception:
            pass

        if format == 'json':
            data = [unit.dict() for unit in self.extracted_units]
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            raise ValueError(f"Unsupported export format: {format}")
        
        print(f"Exported {len(self.extracted_units)} ConceptUnits to {output_path}")
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get extraction statistics"""
        stats = {
            'total_concepts': len(self.extracted_units),
            'by_type': {},
            'by_source': {},
            'average_confidence': 0.0
        }
        
        if not self.extracted_units:
            return stats
        
        # Count by type
        for unit in self.extracted_units:
            stats['by_type'][unit.type] = stats['by_type'].get(unit.type, 0) + 1
            stats['by_source'][unit.source] = stats['by_source'].get(unit.source, 0) + 1
        
        # Average confidence
        confidences = [unit.confidence_score for unit in self.extracted_units if unit.confidence_score]
        if confidences:
            stats['average_confidence'] = sum(confidences) / len(confidences)
        
        return stats


# Example usage and testing
if __name__ == "__main__":
    # Initialize pipeline
    schema_path = "schemas/concept-unit-schema.json"
    pipeline = IngestionPipeline(schema_path)
    
    # Test with sample text
    sample_text = """
    A functor is a mapping between categories that preserves the structure of morphisms.
    In category theory, functors are fundamental constructs that allow us to move between different mathematical contexts.
    
    Recursive functions are functions that call themselves during their execution.
    This self-referential property allows for elegant solutions to problems that have recursive structure.
    """
    
    # Extract concepts from sample
    concepts = pipeline.extract_concepts(sample_text, "sample_text")
    print(f"Extracted {len(concepts)} concepts:")
    for concept in concepts:
        print(f"- {concept.type}: {concept.definition[:50]}...")
    # Add extracted concepts to the pipeline's internal store so they will be exported
    if concepts:
        pipeline.extracted_units.extend(concepts)
    
    # Export results
    pipeline.export_concepts("archive/extracted_concepts.json")
    
    # Show statistics
    stats = pipeline.get_statistics()
    print("\nExtraction Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")
