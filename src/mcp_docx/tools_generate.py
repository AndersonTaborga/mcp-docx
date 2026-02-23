"""Generate tools: create_document, generate_from_template."""

from pathlib import Path

from docxtpl import DocxTemplate

from .lib import create_minimal_document, ensure_dir, normalize_text


def create_document(output_path: str, title: str, paragraphs: list[str]) -> dict:
    """Create a new .docx from scratch with title and paragraphs."""
    output_path = str(Path(output_path).resolve())
    ensure_dir(Path(output_path))
    doc = create_minimal_document(normalize_text(title), [normalize_text(p) for p in paragraphs])
    doc.save(output_path)
    return {"outputPath": output_path, "message": f"Document created at {output_path}"}


def generate_from_template(template_path: str, output_path: str, data: dict) -> dict:
    """Generate .docx from template. Template uses Jinja2 placeholders: {{ name }}, {{ date }}."""
    template_path = str(Path(template_path).resolve())
    output_path = str(Path(output_path).resolve())
    ensure_dir(Path(output_path))
    normalized = {k: normalize_text(v) if isinstance(v, str) else v for k, v in data.items()}
    doc = DocxTemplate(template_path)
    doc.render(normalized)
    doc.save(output_path)
    return {"outputPath": output_path, "message": f"Document generated at {output_path}"}
