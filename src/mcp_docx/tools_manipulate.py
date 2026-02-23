"""Manipulate tools: merge_documents, extract_text, get_document_info."""

import re
import zipfile
from pathlib import Path

from .lib import ensure_dir


def _get_body_content(xml: str) -> str:
    m = re.search(r"<w:body[^>]*>([\s\S]*?)</w:body>", xml)
    return m.group(1) if m else ""


def _extract_text_from_xml(xml: str) -> str:
    parts = re.findall(r"<w:t[^>]*>([^<]*)</w:t>", xml)
    decoded = []
    for s in parts:
        s = s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
        s = s.replace("&quot;", '"').replace("&apos;", "'")
        decoded.append(s)
    return "".join(decoded)


def merge_documents(input_paths: list[str], output_path: str) -> dict:
    """Merge multiple .docx files into one. Uses the first file's styles."""
    if not input_paths:
        raise ValueError("At least one input path is required")
    output_path = str(Path(output_path).resolve())
    ensure_dir(Path(output_path))

    bodies = []
    first_path = str(Path(input_paths[0]).resolve())
    with zipfile.ZipFile(first_path, "r") as z:
        xml = z.read("word/document.xml").decode("utf-8")
        full_xml = xml
        bodies.append(_get_body_content(xml))

    for p in input_paths[1:]:
        with zipfile.ZipFile(str(Path(p).resolve()), "r") as z:
            xml = z.read("word/document.xml").decode("utf-8")
            bodies.append(_get_body_content(xml))

    merged_body = "".join(bodies)
    new_xml = re.sub(r"<w:body[^>]*>[\s\S]*?</w:body>", f"<w:body>{merged_body}</w:body>", full_xml, count=1)

    with zipfile.ZipFile(first_path, "r") as zin:
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zout:
            for name in zin.namelist():
                if name == "word/document.xml":
                    zout.writestr(name, new_xml.encode("utf-8"))
                else:
                    zout.writestr(name, zin.read(name))

    return {"outputPath": output_path, "message": f"Merged {len(input_paths)} document(s) at {output_path}"}


def extract_text(document_path: str) -> dict:
    """Extract plain text from a .docx file."""
    path = str(Path(document_path).resolve())
    with zipfile.ZipFile(path, "r") as z:
        xml = z.read("word/document.xml").decode("utf-8")
    text = _extract_text_from_xml(xml)
    return {"text": text}


def get_document_info(document_path: str) -> dict:
    """Get basic metadata: paragraph count, word count, text preview."""
    path = str(Path(document_path).resolve())
    with zipfile.ZipFile(path, "r") as z:
        xml = z.read("word/document.xml").decode("utf-8")
    para_count = len(re.findall(r"<w:p\b", xml))
    text = _extract_text_from_xml(xml)
    words = text.split()
    word_count = len(words)
    preview = " ".join(text.split())[:300].strip()
    if len(text.strip()) > 300:
        preview += "..."
    return {"paragraphCount": para_count, "wordCount": word_count, "textPreview": preview}
