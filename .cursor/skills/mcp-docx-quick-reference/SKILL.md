---
name: mcp-docx-quick-reference
description: One-page reference for mcp-docx MCP tools. Use when the agent needs to recall tool names, parameters, or content_blocks format without loading full skill docs. Use when generating or editing .docx via mcp-docx.
compatibility: Requires mcp-docx MCP server configured in Cursor.
---

# mcp-docx quick reference

Use **only** the mcp-docx MCP tools to create or edit .docx files. Do not generate .docx manually.

## Tools (12)

| Tool | One-line purpose |
|------|------------------|
| `create_document` | New .docx with title + list of paragraphs (plain). |
| `create_document_formatted` | New .docx with title, subtitle, headings, paragraphs, bullet lists, optional images; optional font. |
| `generate_from_template` | Fill a .docx template (Jinja2 `{{ var }}`) with a JSON data object. |
| `mail_merge` | Fill Word merge fields in a .docx template (`«Nome»`, `«Data»`). Requires `[mailmerge]`. |
| `replace_text` | Replace placeholders in existing .docx; save to new path. |
| `insert_paragraph` | Append one paragraph at end of existing .docx; save to new path. |
| `merge_documents` | Concatenate several .docx into one (first file's styles). |
| `extract_text` | Return plain text from a .docx. |
| `get_document_info` | Return paragraph count, word count, short text preview. |
| `convert_pdf_to_docx` | Convert PDF to .docx. Requires `[pdf]`. |
| `docx_to_html` | Convert .docx to HTML. Requires `[html]`. |
| `convert_document` | Convert document to another format via Pandoc (docx, html, md, etc.). Requires `[pandoc]`. |

## content_blocks (for create_document_formatted)

Array of objects. Each object has `type` and:

- **heading:** `{"type": "heading", "level": 1 or 2, "text": "Section title"}`
- **paragraph:** `{"type": "paragraph", "text": "Body text."}`
- **list_bullet:** `{"type": "list_bullet", "items": ["Item one.", "Item two."]}`
- **image:** `{"type": "image", "path": "/path/to/image.png", "width_inches": 2.0}` (requires `[images]`)

Optional top-level args: `title`, `subtitle`, `font_name` (e.g. `"Calibri"`), `font_size_pt` (e.g. `11`).

## Minimal example (create_document_formatted)

```json
{
  "output_path": "C:/out/report.docx",
  "title": "Report Title",
  "subtitle": "Optional subtitle",
  "content_blocks": [
    {"type": "heading", "level": 1, "text": "Introduction"},
    {"type": "paragraph", "text": "First paragraph."},
    {"type": "heading", "level": 2, "text": "Details"},
    {"type": "list_bullet", "items": ["Point A", "Point B"]},
    {"type": "image", "path": "C:/images/logo.png", "width_inches": 2.0}
  ]
}
```

For more detail (when to use which tool, structures, encoding), use the other mcp-docx skills: mcp-docx-formatting, mcp-docx-simple-vs-formatted, mcp-docx-fluency, mcp-docx-document-structures, mcp-docx-templates, mcp-docx-merge-extract, mcp-docx-encoding.
