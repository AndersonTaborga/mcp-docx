---
name: mcp-docx-fluency
description: Maps natural-language requests to mcp-docx tool calls and parameters. Use when the user asks in plain language to create, edit, merge, or inspect .docx files so the agent always uses MCP tools instead of generating .docx manually.
compatibility: Requires mcp-docx MCP server configured in Cursor.
---

# mcp-docx fluency (NL to tool)

Always use **mcp-docx MCP tools** for any .docx creation, editing, or inspection. Never generate .docx content by hand (e.g. raw XML or custom scripts).

## Mapping: user phrase → tool + action

| User says (examples) | Tool | Action |
|----------------------|------|--------|
| "Create a report with X and Y" | create_document_formatted | Build content_blocks with title, heading(s), paragraphs/list_bullet from X, Y; ask for output_path if missing. |
| "Make a document with a title and a few paragraphs" | create_document | Use title + paragraphs array; ask for output_path and text if missing. |
| "Add a paragraph at the end of this doc" | insert_paragraph | Need document_path, output_path (new file), text. Ask user for path and paragraph text. |
| "Replace name and date in this document" | replace_text or generate_from_template | If doc is a template with placeholders: replace_text (document_path, output_path, replacements) or generate_from_template if user has a template file + data. |
| "Merge these files into one" | merge_documents | input_paths (list), output_path. Ask for paths if not clear. |
| "Extract the text from this .docx" | extract_text | document_path. Return the returned text to the user. |
| "How many words/pages in this document?" | get_document_info | document_path. Use returned wordCount (and paragraphCount) to answer. |
| "Fill in this template with …" | generate_from_template | template_path, output_path, data (object). Ask for template path and key-value data. |

## Rules

1. **Never** produce .docx by writing XML, Python docx code in the chat, or scripts that write .docx unless the user explicitly asks for code/script.
2. **Always** call the appropriate mcp-docx tool with the correct parameters. If a path or content is missing, ask the user once before calling.
3. For "create a document" without more detail, prefer **create_document_formatted** with a sensible title and one or two content_blocks (e.g. one heading, one paragraph) so the user can refine; or ask whether they want a simple (title + paragraphs) or formatted (sections/lists) document.
4. Confirm the output path and, after a successful call, tell the user where the file was written.
