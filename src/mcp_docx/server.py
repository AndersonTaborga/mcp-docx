"""MCP server for .docx: tools exposed via FastMCP."""

import json
from mcp.server.fastmcp import FastMCP

from . import tools_edit
from . import tools_generate
from . import tools_manipulate

mcp = FastMCP(name="mcp-docx")


@mcp.tool()
def create_document(output_path: str, title: str, paragraphs: list[str]) -> str:
    """Create a new .docx from scratch with a title and list of paragraphs."""
    result = tools_generate.create_document(
        output_path=output_path,
        title=title,
        paragraphs=paragraphs,
    )
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def create_document_formatted(
    output_path: str,
    content_blocks: list[dict],
    title: str | None = None,
    subtitle: str | None = None,
    font_name: str = "Calibri",
    font_size_pt: float = 11,
) -> str:
    """Create a well-formatted .docx with title, subtitle, headings, paragraphs, and bullet lists.
    content_blocks: list of objects - {\"type\": \"heading\", \"level\": 1 or 2, \"text\": \"...\"},
    {\"type\": \"paragraph\", \"text\": \"...\"}, or {\"type\": \"list_bullet\", \"items\": [\"...\", \"...\"]}.
    Uses Calibri 11pt by default; set font_name and font_size_pt to change."""
    result = tools_generate.create_document_formatted(
        output_path=output_path,
        content_blocks=content_blocks,
        title=title,
        subtitle=subtitle,
        font_name=font_name,
        font_size_pt=font_size_pt,
    )
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def generate_from_template(template_path: str, output_path: str, data: dict) -> str:
    """Generate a .docx from a template. Template uses Jinja2 placeholders: {{ name }}, {{ date }}."""
    result = tools_generate.generate_from_template(
        template_path=template_path,
        output_path=output_path,
        data=data,
    )
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def replace_text(document_path: str, output_path: str, replacements: dict[str, str]) -> str:
    """Replace placeholders in .docx (Jinja2 {{ name }}). Saves to output."""
    result = tools_edit.replace_text(
        document_path=document_path,
        output_path=output_path,
        replacements=replacements,
    )
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def insert_paragraph(document_path: str, output_path: str, text: str) -> str:
    """Insert a paragraph at the end of an existing .docx and save to output."""
    result = tools_edit.insert_paragraph(
        document_path=document_path,
        output_path=output_path,
        text=text,
    )
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def merge_documents(input_paths: list[str], output_path: str) -> str:
    """Merge multiple .docx files into one. Uses the first file's styles."""
    result = tools_manipulate.merge_documents(
        input_paths=input_paths,
        output_path=output_path,
    )
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def extract_text(document_path: str) -> str:
    """Extract plain text from a .docx file."""
    result = tools_manipulate.extract_text(document_path=document_path)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def get_document_info(document_path: str) -> str:
    """Get basic metadata from a .docx: paragraph count, word count, text preview."""
    result = tools_manipulate.get_document_info(document_path=document_path)
    return json.dumps(result, ensure_ascii=False)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
