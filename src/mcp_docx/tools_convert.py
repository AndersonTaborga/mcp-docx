"""Conversion tools: PDF to docx, docx to HTML, and Pandoc conversion."""

from pathlib import Path

from .lib import ensure_dir

_MSG_PDF = "Install with: pip install mcp-docx[pdf]"
_MSG_HTML = "Install with: pip install mcp-docx[html]"
_MSG_PANDOC = "Install with: pip install mcp-docx[pandoc]. Pandoc binary must be on PATH."


def convert_pdf_to_docx(pdf_path: str, output_path: str) -> dict:
    """Convert a PDF file to .docx. Requires pdf2docx (pip install mcp-docx[pdf])."""
    try:
        from pdf2docx import Converter
    except ImportError as e:
        raise RuntimeError(f"pdf2docx is not installed. {_MSG_PDF}") from e
    pdf_path = str(Path(pdf_path).resolve())
    output_path = str(Path(output_path).resolve())
    ensure_dir(Path(output_path))
    cv = Converter(pdf_path)
    cv.convert(output_path)
    cv.close()
    return {"outputPath": output_path, "message": f"Converted PDF to docx at {output_path}"}


def docx_to_html(document_path: str) -> dict:
    """Convert a .docx file to HTML. Returns HTML string and optional messages. Requires mammoth (pip install mcp-docx[html])."""
    try:
        import mammoth
    except ImportError as e:
        raise RuntimeError(f"mammoth is not installed. {_MSG_HTML}") from e
    path = str(Path(document_path).resolve())
    with open(path, "rb") as f:
        result = mammoth.convert_to_html(f)
    return {"html": result.value, "messages": getattr(result, "messages", [])}


def convert_document(input_path: str, output_path: str, output_format: str) -> dict:
    """Convert a document to another format using Pandoc (e.g. docx, html, md). Requires pypandoc and Pandoc on PATH (pip install mcp-docx[pandoc])."""
    try:
        import pypandoc
    except ImportError as e:
        raise RuntimeError(f"pypandoc is not installed. {_MSG_PANDOC}") from e
    input_path = str(Path(input_path).resolve())
    output_path = str(Path(output_path).resolve())
    ensure_dir(Path(output_path))
    pypandoc.convert_file(input_path, output_format, outputfile=output_path)
    return {"outputPath": output_path, "message": f"Converted to {output_format} at {output_path}"}
