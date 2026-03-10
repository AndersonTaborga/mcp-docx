---
name: mcp-docx-document-structures
description: Provides ready-made structures (meeting minutes, project report, presentation script, checklist) and maps them to content_blocks for create_document_formatted. Use when the user asks for meeting minutes, a report, a presentation script, or a task/checklist document.
compatibility: Requires mcp-docx MCP server configured in Cursor.
---

# mcp-docx document structures

Use **create_document_formatted** with the content_blocks below. Ask the user for output_path and any missing content (date, names, topics, etc.).

## 1. Meeting minutes

- **title:** "Meeting minutes" (or user-provided)
- **content_blocks** (order):
  - heading 1: "Date" → paragraph with date
  - heading 1: "Attendees" → list_bullet of names
  - heading 1: "Topics" → list_bullet or paragraphs per topic
  - heading 1: "Action items" → list_bullet of tasks

Ask user for: date, attendees, topics, action items. Fill in or use placeholders.

## 2. Project report

- **title:** user-provided (e.g. "Q1 Project Report")
- **subtitle:** optional (e.g. "Confidential")
- **content_blocks:**
  - heading 1: "Summary" → paragraph(s)
  - heading 1: "Section 1" (rename as needed) → paragraph or list_bullet
  - heading 2: "Subsection" if needed
  - heading 1: "Next steps" → list_bullet

Ask for: title, summary, section titles and content, next steps.

## 3. Presentation script

- **title:** e.g. "Presentation script – [Topic]"
- **subtitle:** optional (e.g. "Duration: 15 min")
- **content_blocks:** for each segment, in order:
  - heading 2: "0:00 – 0:30 – Introduction" (time range + segment name)
  - paragraph: "What to say: …"
  - list_bullet: "What to do on screen: …" (e.g. "Show slide 1", "Open browser")

Repeat for each time block. Ask for: title, list of segments (time range, what to say, what to do).

## 4. Checklist / task list

- **title:** e.g. "Pre-launch checklist" or user-provided
- **content_blocks:**
  - one or more list_bullet blocks with items (each item = one task)

Optionally one heading 1 before the list (e.g. "Tasks"). Ask for: title, list of tasks.

---

After choosing a structure, build the **content_blocks** array and call **create_document_formatted** with output_path, title (and subtitle if any), and content_blocks. Use mcp-docx-formatting for the exact JSON shape of each block type.
