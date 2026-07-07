"""
Atomic concept extractor - produces graph-usable ConceptUnits
"""

import json
import requests
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime
import hashlib

try:
    import PyPDF2
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

class AtomicExtractor:
    def __init__(self, api_key: str, model: str = "openrouter/sonoma-sky-alpha"):
        self.api_key = api_key
        self.model = model
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"

        # Relation types dictionary - closed set
        self.relation_types = {
            "extends": "B is a broader framework; A extends B with refinements",
            "part_of": "A is a subcomponent or module within B",
            "example_of": "A is a concrete instance illustrating B",
            "prerequisite": "B must be understood before A",
            "supports": "A provides tools/evidence enabling B",
            "contradicts": "A and B make mutually inconsistent claims"
        }

    def extract_pdf_text(self, pdf_path: str) -> str:
        """Extract text from PDF"""
        if not PDF_AVAILABLE:
            raise ImportError("PyPDF2 not available")

        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text

    def call_llm(self, prompt: str) -> str:
        """Call OpenRouter API"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1
        }

        response = requests.post(self.base_url, headers=headers, json=data)
        response.raise_for_status()

        result = response.json()
        return result["choices"][0]["message"]["content"]

    def extract_atomic_concepts(self, pdf_path: str, max_concepts: int = 8) -> List[Dict[str, Any]]:
        """Extract atomic, graph-usable concepts"""

        text = self.extract_pdf_text(pdf_path)

        # Truncate if too long
        if len(text) > 80000:
            text = text[:80000] + "...[truncated]"

        source_name = Path(pdf_path).name

        prompt = f"""
You are extracting ATOMIC knowledge units for graph construction. Each concept must be:
- ONE idea only (≤2 sentences)
- Graph-ready with typed relations
- Building blocks, not essays

Extract {max_concepts} atomic ConceptUnits from this PDF.

RELATION TYPES (closed set):
- extends: B is broader framework; A extends B
- part_of: A is subcomponent within B
- example_of: A is concrete instance of B
- prerequisite: B must be understood before A
- supports: A provides tools/evidence for B
- contradicts: A and B are inconsistent

Return ONLY valid JSON:
{{
  "concepts": [
    {{
      "id": "concept-{hashlib.md5(pdf_path.encode()).hexdigest()[:8]}-001",
      "term": "Short Label or Phrase",
      "type": "Theory|Method|Concept",
      "definition": "≤2 sentences. Compact definition only.",
      "significance": "≤2 sentences. Why it matters.",
      "relations": [
        {{"target": "Other Concept Term", "type": "extends"}}
      ],
      "examples": ["Concrete illustration if relevant"],
      "tags": ["keyword1", "keyword2"]
    }}
  ]
}}

RULES:
1. Break large ideas into multiple atomic units
2. Use only the 6 relation types above
3. Keep definitions crisp and actionable
4. Focus on building blocks, not explanations

PDF: {source_name}
Content:
{text}
"""

        try:
            response = self.call_llm(prompt)
            result = json.loads(response)

            # Add metadata to each concept
            for i, concept in enumerate(result.get("concepts", []), 1):
                concept["id"] = f"concept-{hashlib.md5(pdf_path.encode()).hexdigest()[:8]}-{i:03d}"
                concept["lineage"] = [{
                    "source": source_name,
                    "extraction_date": datetime.now().isoformat(),
                    "model": self.model
                }]
                concept["version"] = "1.0.0"

                # Ensure required fields
                concept.setdefault("examples", [])
                concept.setdefault("tags", [])
                concept.setdefault("relations", [])

            return result.get("concepts", [])

        except Exception as e:
            print(f"Error extracting from {pdf_path}: {e}")
            return []

    def process_pdf(self, pdf_path: str) -> List[Dict[str, Any]]:
        """Process single PDF and return atomic concepts"""
        print(f"Extracting atomic concepts: {Path(pdf_path).name}")
        concepts = self.extract_atomic_concepts(pdf_path)
        print(f"  -> {len(concepts)} atomic units")
        return concepts