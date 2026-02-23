"""Edit tools: replace_text, insert_paragraph."""

import re
import zipfile
from pathlib import Path

from docxtpl import DocxTemplate

from .lib import ensure_dir, normalize_text


def _escape_xml(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def replace_text(document_path: str, output_path: str, replacements: dict[str, str]) -> dict:
    """Replace placeholders in .docx. Template uses Jinja2 {{ name }}. Saves to output."""
    document_path = str(Path(document_path).resolve())
    output_path = str(Path(output_path).resolve())
    ensure_dir(Path(output_path))
    normalized = {k: normalize_text(v) for k, v in replacements.items()}
    doc = DocxTemplate(document_path)
    doc.render(normalized)
    doc.save(output_path)
    return {"outputPath": output_path, "message": f"Document with replacements saved at {output_path}"}


def insert_paragraph(document_path: str, output_path: str, text: str) -> dict:
    """Insert a paragraph at the end of an existing .docx."""
    document_path = str(Path(document_path).resolve())
    output_path = str(Path(output_path).resolve())
    ensure_dir(Path(output_path))
    normalized = normalize_text(text)
    escaped = _escape_xml(normalized)
    new_para = f'<w:p xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:r><w:t xml:space="preserve">{escaped}</w:t></w:r></w:p>'

    with zipfile.ZipFile(document_path, "r") as zin:
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zout:
            for name in zin.namelist():
                if name == "word/document.xml":
                    xml = zin.read(name).decode("utf-8")
                    new_xml = re.sub(r"</w:body>", f"{new_para}</w:body>", xml, count=1)
                    zout.writestr(name, new_xml.encode("utf-8"))
                else:
                    zout.writestr(name, zin.read(name))

    return {"outputPath": output_path, "message": f"Paragraph inserted, saved at {output_path}"}
