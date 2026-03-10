---
name: mcp-docx-templates
description: Uses generate_from_template and replace_text for template-based .docx generation. Use when the user has or mentions a .docx template with placeholders, or wants to fill in variables (name, date, etc.) in an existing document.
compatibility: Requires mcp-docx MCP server configured in Cursor.
---

# mcp-docx templates

Use mcp-docx tools when the user wants to **fill a template** or **replace placeholders** in an existing .docx.

## When to use

- User has a .docx file with placeholders like `{{ name }}`, `{{ date }}` (Jinja2 syntax).
- User says: "fill this template", "generate from template", "replace name and date", "use this document as template".

## generate_from_template

Use when: user provides (or you can assume) a **template file** and a **data object** (key-value) to fill placeholders.

1. Get **template_path**: path to the .docx template (must contain `{{ variable }}` placeholders).
2. Get **output_path**: where to save the generated file.
3. Get **data**: JSON object mapping placeholder names to values, e.g. `{"name": "Jane", "date": "2025-01-15"}`. All string values are normalized to UTF-8 NFC by the server.
4. Call **generate_from_template** with template_path, output_path, data.
5. Tell the user the file was written to output_path.

If the user says "replace X and Y" but does not have a separate template file, treat the existing document as the template: use **replace_text** (see below) or, if the doc is the template, use **generate_from_template** with that document as template_path.

## replace_text

Use when: user has an **existing .docx** and wants to replace specific placeholders (same Jinja2 `{{ key }}` in the document) and **save to a new file**.

1. Get **document_path**: path to the existing .docx.
2. Get **output_path**: path for the new file (do not overwrite without explicit user request).
3. Get **replacements**: object mapping placeholder names to new values, e.g. `{"name": "Jane", "date": "2025-01-15"}`.
4. Call **replace_text** with document_path, output_path, replacements.
5. Confirm where the new file was saved.

## Encoding

All text inputs should be UTF-8. The server normalizes to Unicode NFC. If the user pastes or provides data that looks like mojibake (e.g. Ã© instead of é), ask them to provide the correct UTF-8 text or check their source encoding; do not try to "fix" mojibake in the skill. See mcp-docx-encoding for details.
