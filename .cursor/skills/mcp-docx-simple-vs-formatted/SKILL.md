---
name: mcp-docx-simple-vs-formatted
description: Decides when to use create_document (title + paragraphs only) vs create_document_formatted (headings, lists, subtitle). Use when generating a new .docx and the structure is unclear, or when the user asks for a "simple" vs "formatted" or "structured" document.
compatibility: Requires mcp-docx MCP server configured in Cursor.
---

# mcp-docx: simple vs formatted

Choose the right mcp-docx tool so output matches the user's intent.

## Use create_document when

- Single title and a list of paragraphs only (no section headings, no bullet lists).
- User says: "simple document", "letter", "plain document", "just a title and a few paragraphs", "text only".
- Content is linear body text with no need for headings or list styling.

Parameters: `output_path`, `title`, `paragraphs` (array of strings).

## Use create_document_formatted when

- Document has sections or subsections (headings).
- Document has bullet lists, checklists, or itemized content.
- User says: "formatted", "with sections", "with headings", "report", "checklist", "script", "structured", "professional layout".
- Subtitle or default font (e.g. Calibri 11pt) is desired.

Parameters: `output_path`, `content_blocks`, optional `title`, `subtitle`, `font_name`, `font_size_pt`.

## Decision table

| User intent / content type | Tool |
|----------------------------|------|
| "Write a short letter with title and 3 paragraphs" | create_document |
| "Create a report with Introduction, Methods, Results" | create_document_formatted |
| "Make a checklist of 5 tasks" | create_document_formatted |
| "One title and two paragraphs, nothing else" | create_document |
| "Presentation script with time blocks and bullet points" | create_document_formatted |

When in doubt (e.g. "create a document about X"), prefer **create_document_formatted** so the agent can use headings and lists if the user adds structure later or expects a report-style layout.
