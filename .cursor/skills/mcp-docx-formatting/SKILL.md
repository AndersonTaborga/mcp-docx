---
name: mcp-docx-formatting
description: Uses create_document_formatted with content_blocks (heading, paragraph, list_bullet, optional image), title, subtitle, and default font. Use when the user asks for a "formatted" document, "with headings", "with bullet lists", "with images", or "professional" .docx output.
compatibility: Requires mcp-docx MCP server configured in Cursor.
---

# mcp-docx formatting

Use the mcp-docx tool **create_document_formatted** whenever the user wants a document with sections, headings, or bullet lists.

## When to use

- User says: "formatted document", "with titles/sections", "with bullet points", "professional document", "report with headings", "checklist", "structured document".
- Document needs: more than a single title + flat paragraphs; level 1 or 2 headings; bullet or task lists.

## Instructions

1. Obtain from the user (or infer): **output_path**, optional **title**, optional **subtitle**, and the content to put in the body.
2. Build **content_blocks** as a list of objects in order:
   - `{"type": "heading", "level": 1, "text": "..."}` for main sections (level 1) or `"level": 2` for subsections.
   - `{"type": "paragraph", "text": "..."}` for normal body text.
   - `{"type": "list_bullet", "items": ["...", "..."]}` for bullet lists.
   - `{"type": "image", "path": "/path/to/image.png", "width_inches": 2.0}` for images (requires `pip install mcp-docx[images]`).
3. Call **create_document_formatted** with:
   - `output_path` (required)
   - `content_blocks` (required)
   - `title`, `subtitle` if provided
   - `font_name`: default `"Calibri"` if not specified
   - `font_size_pt`: default `11` if not specified
4. If output_path, title, or body content is missing, ask the user before calling the tool.

## Example content_blocks

```json
[
  {"type": "heading", "level": 1, "text": "Before recording"},
  {"type": "list_bullet", "items": ["Check OBS.", "Open browser.", "Test microphone."]},
  {"type": "heading", "level": 2, "text": "Script"},
  {"type": "paragraph", "text": "Speak clearly and scroll slowly."}
]
```

Keep headings short; use paragraphs for longer text and list_bullet for items. All text is normalized to UTF-8 NFC by the server.

## Formatting best practices

- **Headings:** Use short, clear text. Level 1 for main sections, level 2 for subsections. The server adds spacing after headings automatically.
- **Paragraphs:** Prefer short paragraphs (2–4 lines). Break long text into multiple paragraph blocks instead of one block.
- **Lists:** Use list_bullet for 3+ items or when the order is a checklist; use paragraphs for flowing text.
- **Structure:** After a heading, add at least one paragraph or list before the next heading; avoid stacking headings with no content in between.
- **Title/subtitle:** Omit subtitle if not needed. The server does not apply the Word "Title" style (avoids underlines/borders); title is bold, 18pt, centered.
