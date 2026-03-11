---
name: mcp-docx-merge-extract
description: Uses merge_documents, extract_text, and get_document_info from mcp-docx. Use when the user wants to combine several .docx into one, get plain text from a .docx, or get word count, paragraph count, or a short preview of a document.
compatibility: Requires mcp-docx MCP server configured in Cursor.
---

# mcp-docx merge and extract

Use these mcp-docx tools for combining documents, extracting text, or reading metadata.

## merge_documents

**When:** User wants to "merge", "combine", "join", or "concatenate" several .docx files into one.

1. Get **input_paths**: ordered list of .docx file paths (first file’s styles are used for the result).
2. Get **output_path**: path for the merged .docx.
3. Call **merge_documents** with input_paths and output_path.
4. Confirm the merged file path. Note: merging is in order; first document’s styling applies.

If the user gives only one file, ask for at least one more or clarify. If they need **PDF → .docx**, use **convert_pdf_to_docx** (requires `pip install mcp-docx[pdf]`). If they need **.docx → HTML**, use **docx_to_html** (requires `pip install mcp-docx[html]`). For other format conversions, use **convert_document** with Pandoc (requires `pip install mcp-docx[pandoc]` and Pandoc on PATH).

## extract_text

**When:** User wants "plain text", "extract text", "get the text from this document", or "copy text from .docx".

1. Get **document_path**: path to the .docx.
2. Call **extract_text** with document_path.
3. The tool returns `{"text": "..."}`. Show the text to the user (or a truncated version with a note that full text was extracted).

Use for: copying content to another tool, searching in text, or saving as .txt. Do not use for editing the .docx itself (use replace_text or insert_paragraph instead).

## get_document_info

**When:** User asks "how many words", "word count", "paragraph count", "preview", or "summary of this document".

1. Get **document_path**: path to the .docx.
2. Call **get_document_info** with document_path.
3. The tool returns paragraphCount, wordCount, textPreview. Report these to the user in a short sentence.

Example: "The document has 42 paragraphs, 1,200 words. Preview: …"
