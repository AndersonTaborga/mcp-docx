"""Shared helpers for .docx operations."""

import unicodedata
from pathlib import Path

from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH


def normalize_text(s: str) -> str:
    """Normalize text to Unicode NFC for consistent accented characters."""
    return unicodedata.normalize("NFC", s)


def ensure_dir(path: Path) -> None:
    """Ensure parent directory exists."""
    path.parent.mkdir(parents=True, exist_ok=True)


def create_minimal_document(title: str, paragraphs: list[str]) -> Document:
    """Create a new Document with title and paragraphs."""
    doc = Document()
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title_p.add_run(normalize_text(title))
    run.bold = True
    run.font.size = Pt(24)
    for text in paragraphs:
        doc.add_paragraph(normalize_text(text))
    return doc
