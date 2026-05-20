"""Shared configuration constants for the verification toolkit."""

import os
from pathlib import Path

# Project root (parent of scripts/verify/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Paths
TEXTS_DIR = PROJECT_ROOT / "texts"
EXTRACTED_DIR = TEXTS_DIR / "extracted"
AUDIT_DIR = PROJECT_ROOT / "audit"
ANALYSES_DIR = AUDIT_DIR / "analyses"
VERIFICATION_DIR = AUDIT_DIR / "verification"
REPORTS_DIR = VERIFICATION_DIR / "reports"
QUOTES_DIR = VERIFICATION_DIR / "quotes"
EVIDENCE_DIR = VERIFICATION_DIR / "evidence"
SISYPHUS_EVIDENCE_DIR = PROJECT_ROOT / ".sisyphus" / "evidence"

# Fuzzy matching threshold (0-100)
# Quotes scoring below this threshold will be flagged for human review
FUZZY_THRESHOLD = 70

# File patterns
ANALYSIS_GLOB = "*.md"
SYNTHESIS_GLOB = "[0-9]*.md"
ALL_AUDIT_GLOBS = ["audit/[0-9]*.md", "audit/analyses/*.md", "README.md"]

# PDFs known to be scanned/unreadable
UNVERIFIABLE_PDFS = {
    "Hesiod-Theogony-Works-and-Days.pdf",
    "The-Poetic-Edda.pdf",
    "The-Yasna.pdf",
}

# PDF filename mapping: canonical text name -> PDF filename
PDF_MAP = {
    "atrahasis": "EpicofAtrahasis.pdf",
    "enoch": "The Complete Book of Enoch, Standard English Version - Jay Winter.pdf",
    "gilgamesh": "THE EPIC OF GILGAMESH.pdf",
    "ezekiel": "eze.pdf",
    "mahabharata": "Mahabharata.pdf",
    "mahabharata_full": "Menon_Ramesh-The-Complete-Mahabharata_-Volume-1-12.pdf",
    "popol_vuh": "PopolVuh.pdf",
    "pyramid_texts": "AncientEgyptianPyramid_Allen_SBL.pdf",
    "rig_veda": "RigVeda.pdf",
    "revelation": "bookofrevelation.pdf",
    "book_of_the_dead": "The-Book-of-the-Dead.pdf",
    "poetic_edda": "The-Poetic-Edda.pdf",
    "theogony": "Hesiod-Theogony-Works-and-Days.pdf",
    "zoroastrian": "The-Yasna.pdf",
    "yoga_sutras": "yoga-sutras-patanjali.pdf",
}
