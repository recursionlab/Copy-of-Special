"""
Configuration file for the research mining ingestion pipeline
"""

# File type handlers
SUPPORTED_EXTENSIONS = {
    '.pdf': 'pdf',
    '.md': 'markdown',
    '.txt': 'text',
    '.markdown': 'markdown'
}

# Concept extraction patterns
EXTRACTION_PATTERNS = {
    'Functor': {
        'patterns': [
            r'(?:A\s+)?functor[s]?\s+(?:is|are|means?|refers?\s+to)\s+(.{10,300})',
            r'(?:define|definition\s+of)\s+(?:a\s+)?functor[s]?\s*:?\s*(.{10,300})',
            r'functor[s]?\s+(?:preserves?|maps?|transforms?|maintains?)\s+(.{10,300})',
            r'(?:In\s+category\s+theory,?\s+)?functor[s]?\s+(.{10,300})',
            r'functorial\s+(?:mapping|relationship|structure)\s+(.{10,300})'
        ],
        'confidence': 0.8
    },
    'Recursion': {
        'patterns': [
            r'recursive[ly]?\s+(?:defined|function|process|structure|pattern)\s+(.{10,300})',
            r'recursion[s]?\s+(?:is|means?|involves?|occurs?\s+when)\s+(.{10,300})',
            r'self-referential\s+(?:function|process|structure|definition)\s+(.{10,300})',
            r'(?:Kleene.{0,20})?recursion\s+theorem\s+(.{10,300})',
            r'(?:base\s+case|recursive\s+case)\s+(.{10,300})'
        ],
        'confidence': 0.75
    },
    'Autopoiesis': {
        'patterns': [
            r'autopoiesi[s]?\s+(?:is|means?|refers?\s+to)\s+(.{10,300})',
            r'self-(?:organizing|producing|maintaining|creating|generating)\s+system[s]?\s+(.{10,300})',
            r'autopoietic\s+(?:system[s]?|process|organization|structure)\s+(.{10,300})',
            r'(?:Maturana|Varela).{0,30}autopoiesi[s]?\s+(.{10,300})',
            r'structural\s+coupling\s+(.{10,300})'
        ],
        'confidence': 0.7
    },
    'Distinction': {
        'patterns': [
            r'distinction[s]?\s+(?:is|are|means?|involves?)\s+(.{10,300})',
            r'(?:Spencer.{0,20}Brown|Laws\s+of\s+Form).{0,30}distinction[s]?\s+(.{10,300})',
            r'recursive\s+distinction[s]?\s+(.{10,300})',
            r'(?:mark|unmarked)\s+state[s]?\s+(.{10,300})',
            r'distinction\s+operator[s]?\s+(.{10,300})'
        ],
        'confidence': 0.7
    },
    'Contradiction': {
        'patterns': [
            r'contradiction[s]?\s+(?:is|are|means?|occurs?\s+when)\s+(.{10,300})',
            r'paradox[es]?\s+(?:arises?|emerges?|occurs?)\s+(.{10,300})',
            r'self-contradiction[s]?\s+(.{10,300})',
            r'(?:logical|performative)\s+contradiction[s]?\s+(.{10,300})',
            r'inconsistenc[y|ies]\s+(.{10,300})'
        ],
        'confidence': 0.65
    }
}

# Mathematical notation patterns
MATH_PATTERNS = {
    'category_theory': [
        r'F\s*:\s*[A-Z]\s*→\s*[A-Z]',  # F: C → D
        r'Hom\([A-Z],\s*[A-Z]\)',      # Hom(A, B)
        r'∘|compose[d]?\s+with',        # composition
        r'id[A-Z]|\bidentity\s+morphism'
    ],
    'recursion_theory': [
        r'μ[a-z]\.|\bmu\s+[a-z]',      # μ-calculus
        r'f\(f\)|self-application',
        r'λ[a-z]\.|\blambda\s+[a-z]',  # lambda calculus
        r'fix\s*\(|\bfixed\s+point'
    ],
    'logic': [
        r'∀|∃|\bforall|\bexists',
        r'¬|→|∧|∨|\bnot\b|\band\b|\bor\b|\bimplies\b',
        r'⊢|\bproves?\b|\bentails?\b'
    ]
}

# Quality filters
QUALITY_FILTERS = {
    'min_definition_length': 15,
    'max_definition_length': 500,
    'min_confidence_score': 0.5,
    'exclude_patterns': [
        r'^(?:the|a|an)\s+\w+\s*$',  # Too simple
        r'^\w+\s*$',                 # Single words
        r'^[^a-zA-Z]*$'              # No letters
    ]
}

# Export settings
EXPORT_SETTINGS = {
    'default_format': 'json',
    'include_metadata': True,
    'pretty_print': True,
    'backup_on_overwrite': True
}

# Processing settings
PROCESSING_SETTINGS = {
    'chunk_size': 1000,      # Characters per processing chunk
    'overlap_size': 100,     # Overlap between chunks
    'max_file_size_mb': 50,  # Maximum file size to process
    'timeout_seconds': 30    # Processing timeout per file
}

# Schema validation
SCHEMA_VALIDATION = {
    'strict_mode': False,    # Whether to fail on validation errors
    'log_validation_errors': True,
    'auto_fix_common_errors': True
}
