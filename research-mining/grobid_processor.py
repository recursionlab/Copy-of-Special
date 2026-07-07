#!/usr/bin/env python3
"""
GROBID Enhanced PDF Processing
Integrates GROBID for enhanced scientific document processing
"""

import os
import json
import requests
import time
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from pathlib import Path
import xml.etree.ElementTree as ET
from datetime import datetime

@dataclass
class ExtractedSection:
    """Structured section from GROBID processing"""
    title: str
    content: str
    section_type: str  # introduction, methodology, results, etc.
    level: int  # heading level
    position: int  # order in document

@dataclass
class ExtractedReference:
    """Bibliographic reference from GROBID"""
    raw_text: str
    title: Optional[str] = None
    authors: List[str] = None
    journal: Optional[str] = None
    year: Optional[str] = None
    doi: Optional[str] = None

@dataclass
class ExtractedEntity:
    """Named entity or concept extracted from text"""
    text: str
    entity_type: str  # formula, figure, table, concept
    context: str
    confidence: float
    section_context: str

@dataclass
class GrobidDocument:
    """Complete GROBID processed document"""
    title: str
    abstract: str
    authors: List[str]
    sections: List[ExtractedSection]
    references: List[ExtractedReference]
    entities: List[ExtractedEntity]
    metadata: Dict[str, Any]
    processing_timestamp: str

class GrobidProcessor:
    """GROBID-based enhanced PDF processor"""

    def __init__(self, grobid_url: str = "http://localhost:8070"):
        """Initialize GROBID processor"""
        self.grobid_url = grobid_url
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'KnowledgeEvolution/1.0'})

    def is_grobid_available(self) -> bool:
        """Check if GROBID service is available"""
        try:
            response = self.session.get(f"{self.grobid_url}/api/isalive", timeout=5)
            return response.status_code == 200
        except:
            return False

    def process_pdf(self, pdf_path: str, extract_entities: bool = True) -> Optional[GrobidDocument]:
        """Process PDF with GROBID and extract structured content"""
        if not self.is_grobid_available():
            print("GROBID service not available, falling back to basic processing")
            return self._fallback_processing(pdf_path)

        try:
            # Process with GROBID
            with open(pdf_path, 'rb') as pdf_file:
                files = {'input': pdf_file}

                # Get full text processing
                response = self.session.post(
                    f"{self.grobid_url}/api/processFulltextDocument",
                    files=files,
                    timeout=30
                )

                if response.status_code != 200:
                    print(f"GROBID processing failed: {response.status_code}")
                    return self._fallback_processing(pdf_path)

                # Parse TEI XML response
                tei_xml = response.text
                return self._parse_tei_xml(tei_xml, pdf_path, extract_entities)

        except Exception as e:
            print(f"GROBID processing error: {e}")
            return self._fallback_processing(pdf_path)

    def _parse_tei_xml(self, tei_xml: str, pdf_path: str, extract_entities: bool) -> GrobidDocument:
        """Parse GROBID TEI XML output into structured document"""
        try:
            root = ET.fromstring(tei_xml)

            # Extract title
            title_elem = root.find('.//{http://www.tei-c.org/ns/1.0}titleStmt/{http://www.tei-c.org/ns/1.0}title')
            title = title_elem.text if title_elem is not None else "Unknown Title"

            # Extract abstract
            abstract_elem = root.find('.//{http://www.tei-c.org/ns/1.0}abstract')
            abstract = self._extract_text_content(abstract_elem) if abstract_elem is not None else ""

            # Extract authors
            authors = self._extract_authors(root)

            # Extract sections
            sections = self._extract_sections(root)

            # Extract references
            references = self._extract_references(root)

            # Extract entities if requested
            entities = []
            if extract_entities:
                entities = self._extract_entities_from_sections(sections)

            # Extract metadata
            metadata = {
                'source_file': pdf_path,
                'processing_method': 'grobid',
                'grobid_version': 'current',
                'sections_count': len(sections),
                'references_count': len(references),
                'entities_count': len(entities)
            }

            return GrobidDocument(
                title=title,
                abstract=abstract,
                authors=authors,
                sections=sections,
                references=references,
                entities=entities,
                metadata=metadata,
                processing_timestamp=datetime.now().isoformat()
            )

        except ET.ParseError as e:
            print(f"XML parsing error: {e}")
            return self._fallback_processing(pdf_path)

    def _extract_text_content(self, element) -> str:
        """Extract text content from XML element"""
        if element is None:
            return ""

        text_parts = []
        if element.text:
            text_parts.append(element.text)

        for child in element:
            text_parts.append(self._extract_text_content(child))
            if child.tail:
                text_parts.append(child.tail)

        return ' '.join(text_parts).strip()

    def _extract_authors(self, root) -> List[str]:
        """Extract author information from TEI"""
        authors = []
        author_elems = root.findall('.//{http://www.tei-c.org/ns/1.0}author')

        for author_elem in author_elems:
            forename_elem = author_elem.find('.//{http://www.tei-c.org/ns/1.0}forename')
            surname_elem = author_elem.find('.//{http://www.tei-c.org/ns/1.0}surname')

            forename = forename_elem.text if forename_elem is not None else ""
            surname = surname_elem.text if surname_elem is not None else ""

            if forename or surname:
                authors.append(f"{forename} {surname}".strip())

        return authors

    def _extract_sections(self, root) -> List[ExtractedSection]:
        """Extract document sections from TEI"""
        sections = []
        div_elems = root.findall('.//{http://www.tei-c.org/ns/1.0}div')

        for i, div_elem in enumerate(div_elems):
            head_elem = div_elem.find('.//{http://www.tei-c.org/ns/1.0}head')
            title = head_elem.text if head_elem is not None else f"Section {i+1}"

            content = self._extract_text_content(div_elem)

            # Determine section type
            section_type = self._classify_section_type(title, content)

            # Estimate heading level
            level = 1 if head_elem is not None else 2

            sections.append(ExtractedSection(
                title=title,
                content=content,
                section_type=section_type,
                level=level,
                position=i
            ))

        return sections

    def _classify_section_type(self, title: str, content: str) -> str:
        """Classify section type based on title and content"""
        title_lower = title.lower()

        if any(keyword in title_lower for keyword in ['introduction', 'intro']):
            return 'introduction'
        elif any(keyword in title_lower for keyword in ['method', 'approach', 'design']):
            return 'methodology'
        elif any(keyword in title_lower for keyword in ['result', 'finding', 'outcome']):
            return 'results'
        elif any(keyword in title_lower for keyword in ['discussion', 'analysis']):
            return 'discussion'
        elif any(keyword in title_lower for keyword in ['conclusion', 'summary']):
            return 'conclusion'
        elif any(keyword in title_lower for keyword in ['related work', 'background', 'literature']):
            return 'background'
        else:
            return 'content'

    def _extract_references(self, root) -> List[ExtractedReference]:
        """Extract bibliographic references from TEI"""
        references = []
        biblstruct_elems = root.findall('.//{http://www.tei-c.org/ns/1.0}biblStruct')

        for biblstruct_elem in biblstruct_elems:
            # Extract title
            title_elem = biblstruct_elem.find('.//{http://www.tei-c.org/ns/1.0}title')
            title = title_elem.text if title_elem is not None else None

            # Extract authors
            author_elems = biblstruct_elem.findall('.//{http://www.tei-c.org/ns/1.0}author')
            authors = []
            for author_elem in author_elems:
                forename_elem = author_elem.find('.//{http://www.tei-c.org/ns/1.0}forename')
                surname_elem = author_elem.find('.//{http://www.tei-c.org/ns/1.0}surname')

                forename = forename_elem.text if forename_elem is not None else ""
                surname = surname_elem.text if surname_elem is not None else ""

                if forename or surname:
                    authors.append(f"{forename} {surname}".strip())

            # Extract other metadata
            journal_elem = biblstruct_elem.find('.//{http://www.tei-c.org/ns/1.0}title[@level="j"]')
            journal = journal_elem.text if journal_elem is not None else None

            date_elem = biblstruct_elem.find('.//{http://www.tei-c.org/ns/1.0}date')
            year = date_elem.get('when') if date_elem is not None else None

            # Extract raw text for fallback
            raw_text = self._extract_text_content(biblstruct_elem)

            references.append(ExtractedReference(
                raw_text=raw_text,
                title=title,
                authors=authors,
                journal=journal,
                year=year
            ))

        return references

    def _extract_entities_from_sections(self, sections: List[ExtractedSection]) -> List[ExtractedEntity]:
        """Extract entities and concepts from sections"""
        entities = []

        for section in sections:
            # Simple entity extraction - can be enhanced with NLP
            content_words = section.content.split()

            # Look for mathematical formulas (simple heuristic)
            for i, word in enumerate(content_words):
                if any(char in word for char in ['=', '+', '-', '*', '/', '^']):
                    context_start = max(0, i-5)
                    context_end = min(len(content_words), i+5)
                    context = ' '.join(content_words[context_start:context_end])

                    entities.append(ExtractedEntity(
                        text=word,
                        entity_type='formula',
                        context=context,
                        confidence=0.7,
                        section_context=section.title
                    ))

            # Look for capitalized terms (potential concepts)
            for i, word in enumerate(content_words):
                if (word[0].isupper() and len(word) > 3 and
                    not word.endswith('.') and word.isalpha()):

                    context_start = max(0, i-3)
                    context_end = min(len(content_words), i+3)
                    context = ' '.join(content_words[context_start:context_end])

                    entities.append(ExtractedEntity(
                        text=word,
                        entity_type='concept',
                        context=context,
                        confidence=0.5,
                        section_context=section.title
                    ))

        return entities

    def _fallback_processing(self, pdf_path: str) -> GrobidDocument:
        """Fallback processing when GROBID is not available"""
        filename = Path(pdf_path).stem

        return GrobidDocument(
            title=f"Document: {filename}",
            abstract="Abstract not available (fallback mode)",
            authors=[],
            sections=[ExtractedSection(
                title="Full Document",
                content="Content extraction requires GROBID service",
                section_type="content",
                level=1,
                position=0
            )],
            references=[],
            entities=[],
            metadata={
                'source_file': pdf_path,
                'processing_method': 'fallback',
                'note': 'GROBID service not available'
            },
            processing_timestamp=datetime.now().isoformat()
        )

    def export_to_knowledge_format(self, document: GrobidDocument, output_path: str) -> Dict[str, Any]:
        """Export processed document to knowledge evolution format"""
        concepts = []

        # Create concepts from sections
        for section in document.sections:
            if len(section.content) > 50:  # Skip very short sections
                concept = {
                    'label': section.title,
                    'definition': section.content[:500],  # Truncate for quality
                    'source_evidence': f"{document.title} - {section.title}",
                    'metadata': {
                        'section_type': section.section_type,
                        'document_title': document.title,
                        'authors': document.authors,
                        'processing_method': 'grobid'
                    }
                }
                concepts.append(concept)

        # Create concepts from entities (high-confidence ones)
        for entity in document.entities:
            if entity.confidence > 0.6:
                concept = {
                    'label': entity.text,
                    'definition': f"Entity of type {entity.entity_type}: {entity.context}",
                    'source_evidence': f"{document.title} - {entity.section_context}",
                    'metadata': {
                        'entity_type': entity.entity_type,
                        'confidence': entity.confidence,
                        'document_title': document.title,
                        'processing_method': 'grobid_entity_extraction'
                    }
                }
                concepts.append(concept)

        # Export result
        result = {
            'document_metadata': document.metadata,
            'processing_timestamp': document.processing_timestamp,
            'extracted_concepts': concepts,
            'total_concepts': len(concepts),
            'document_info': {
                'title': document.title,
                'authors': document.authors,
                'sections_count': len(document.sections),
                'references_count': len(document.references)
            }
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"Exported {len(concepts)} concepts to {output_path}")
        return result


def demo_grobid_processing():
    """Demonstrate GROBID processing capabilities"""
    print("=== GROBID Enhanced PDF Processing Demo ===")

    processor = GrobidProcessor()

    # Check GROBID availability
    if processor.is_grobid_available():
        print("SUCCESS: GROBID service is available")
    else:
        print("WARNING: GROBID service not available - using fallback mode")

    # Demo with a test file (if available)
    test_pdf = "test_document.pdf"
    if not os.path.exists(test_pdf):
        print(f"No test PDF found at {test_pdf}")
        print("To test with real documents, place PDFs in the current directory")

        # Create a mock demonstration
        mock_doc = GrobidDocument(
            title="Example Scientific Paper",
            abstract="This is an example abstract of a scientific paper...",
            authors=["John Doe", "Jane Smith"],
            sections=[
                ExtractedSection("Introduction", "This paper introduces...", "introduction", 1, 0),
                ExtractedSection("Methodology", "Our approach uses...", "methodology", 1, 1),
                ExtractedSection("Results", "We found that...", "results", 1, 2)
            ],
            references=[
                ExtractedReference("Smith, J. (2023). Related Work. Journal of AI.", "Related Work", ["J. Smith"], "Journal of AI", "2023")
            ],
            entities=[
                ExtractedEntity("machine learning", "concept", "context about ML", 0.9, "Introduction"),
                ExtractedEntity("accuracy = 0.95", "formula", "model performance", 0.8, "Results")
            ],
            metadata={'processing_method': 'demo'},
            processing_timestamp=datetime.now().isoformat()
        )

        # Export demo result
        result = processor.export_to_knowledge_format(mock_doc, "demo_grobid_extraction.json")
        print(f"Demo extraction created: {result['total_concepts']} concepts")

        return result

    else:
        # Process real PDF
        print(f"Processing {test_pdf}...")
        document = processor.process_pdf(test_pdf)

        if document:
            print(f"Successfully processed: {document.title}")
            print(f"  Authors: {', '.join(document.authors)}")
            print(f"  Sections: {len(document.sections)}")
            print(f"  References: {len(document.references)}")
            print(f"  Entities: {len(document.entities)}")

            # Export to knowledge format
            result = processor.export_to_knowledge_format(document, "grobid_extraction.json")
            return result
        else:
            print("Failed to process PDF")
            return None


if __name__ == "__main__":
    demo_grobid_processing()