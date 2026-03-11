"""Generate tools: create_document, create_document_formatted, generate_from_template."""

from pathlib import Path

from docxtpl import DocxTemplate

from .lib import (
    create_minimal_document,
    create_document_formatted as build_formatted_doc,
    ensure_dir,
    normalize_text,
)


def create_document(output_path: str, title: str, paragraphs: list[str]) -> dict:
    """Create a new .docx from scratch with title and paragraphs."""
    output_path = str(Path(output_path).resolve())
    ensure_dir(Path(output_path))
    doc = create_minimal_document(normalize_text(title), [normalize_text(p) for p in paragraphs])
    doc.save(output_path)
    return {"outputPath": output_path, "message": f"Document created at {output_path}"}


def create_document_formatted(
    output_path: str,
    content_blocks: list[dict],
    title: str | None = None,
    subtitle: str | None = None,
    font_name: str = "Calibri",
    font_size_pt: float = 11,
) -> dict:
    """
    Create a well-formatted .docx with title, optional subtitle, and rich content.
    content_blocks: list of objects:
      - {"type": "heading", "level": 1 or 2, "text": "..."}
      - {"type": "paragraph", "text": "..."}
      - {"type": "list_bullet", "items": ["...", "..."]}
      - {"type": "image", "path": "...", "width_inches": 2.0}  (requires mcp-docx[images])
    """
    output_path = str(Path(output_path).resolve())
    ensure_dir(Path(output_path))
    doc = build_formatted_doc(
        content_blocks=content_blocks,
        title=title,
        subtitle=subtitle,
        font_name=font_name,
        font_size_pt=font_size_pt,
    )
    doc.save(output_path)
    return {"outputPath": output_path, "message": f"Formatted document created at {output_path}"}


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


_MSG_MAILMERGE = "Install with: pip install mcp-docx[mailmerge]"


def mail_merge(template_path: str, output_path: str, merge_data: dict) -> dict:
    """Fill Word mail-merge fields in a .docx template. Template uses Word merge fields (e.g. «Nome», «Data»). Requires docx-mailmerge: pip install mcp-docx[mailmerge]."""
    try:
        from mailmerge import MailMerge
    except ImportError as e:
        raise RuntimeError(f"docx-mailmerge is not installed. {_MSG_MAILMERGE}") from e
    template_path = str(Path(template_path).resolve())
    output_path = str(Path(output_path).resolve())
    ensure_dir(Path(output_path))
    normalized = {k: normalize_text(v) if isinstance(v, str) else v for k, v in merge_data.items()}
    with MailMerge(template_path) as document:
        document.merge(**normalized)
        document.write(output_path)
    return {"outputPath": output_path, "message": f"Mail-merge document saved at {output_path}"}
