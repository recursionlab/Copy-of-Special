"""
LLM-based intelligent concept extraction using OpenRouter API
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

class LLMExtractor:
    def __init__(self, api_key: str, model: str = "openrouter/sonoma-sky-alpha"):
        self.api_key = api_key
        self.model = model
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"

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

    def extract_concepts(self, pdf_path: str, max_concepts: int = 5) -> List[Dict[str, Any]]:
        """Extract intelligent concepts from PDF using LLM"""

        # Extract PDF text
        text = self.extract_pdf_text(pdf_path)

        # Truncate if too long (keep first 100k chars for context)
        if len(text) > 100000:
            text = text[:100000] + "...[truncated]"

        prompt = f"""
You are an expert researcher analyzing academic papers. Extract the {max_concepts} most important concepts from this PDF.

For each concept, provide:
1. A clear, complete definition (1-2 sentences)
2. Why it's significant to the field
3. How it relates to other concepts in the paper
4. A confidence score (0.0-1.0) for extraction quality

Return ONLY valid JSON in this format:
{{
  "concepts": [
    {{
      "id": "concept-{hashlib.md5(pdf_path.encode()).hexdigest()[:8]}-001",
      "type": "determine from content (Functor/Recursion/Autopoiesis/Theory/Method)",
      "definition": "complete definition here",
      "significance": "why this matters",
      "relations": ["list of related concepts"],
      "confidence_score": 0.95,
      "source": "{Path(pdf_path).name}"
    }}
  ]
}}

PDF Content:
{text}
"""

        try:
            response = self.call_llm(prompt)
            # Parse JSON response
            result = json.loads(response)

            # Add metadata
            for concept in result.get("concepts", []):
                concept["version"] = "1.0.0"
                concept["extraction_date"] = datetime.now().isoformat()
                concept["mathematical_formulation"] = None
                concept["examples"] = []
                concept["prototypes"] = []
                concept["references"] = []
                concept["tags"] = []
                concept["notes"] = f"Extracted using LLM: {self.model}"

            return result.get("concepts", [])

        except Exception as e:
            print(f"Error extracting from {pdf_path}: {e}")
            return []

    def process_pdf(self, pdf_path: str) -> List[Dict[str, Any]]:
        """Process single PDF and return concepts"""
        print(f"Processing with LLM: {pdf_path}")
        concepts = self.extract_concepts(pdf_path)
        print(f"Extracted {len(concepts)} concepts")
        return concepts