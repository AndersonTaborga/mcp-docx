---
name: mcp-docx-encoding
description: Ensures text inputs for mcp-docx are UTF-8 and explains server NFC normalization. Use when the user reports garbled characters (mojibake) in generated .docx, or when providing text from scripts, terminals, or non-UTF-8 sources.
compatibility: Requires mcp-docx MCP server configured in Cursor.
---

# mcp-docx encoding

The mcp-docx server expects **UTF-8** text and normalizes all string inputs to **Unicode NFC** before writing. This keeps accented characters (e.g. é, á, ã) correct in the .docx.

## Rules

1. **Assume UTF-8.** When the user (or the agent) passes title, paragraphs, content_blocks, or replacement values to mcp-docx tools, the strings should already be correct Unicode (UTF-8). The server does not fix mojibake (e.g. Ã© instead of é).
2. **Do not "fix" mojibake in the skill.** Do not try to detect and replace broken sequences (e.g. Ã© → é) in user-provided strings. If the user sees wrong characters in the output, ask them to:
   - Ensure the source (file, clipboard, script) is saved or pasted as UTF-8.
   - On Windows CLI/scripts: use a terminal with UTF-8 (e.g. `chcp 65001`) or save script files as UTF-8.
3. **Server behavior.** The server normalizes to NFC so that precomposed characters (é, ñ) are stored consistently. No extra encoding steps are required in the skill beyond passing through the strings the user intends.
4. **When in doubt.** If the user reports strange characters or provides content from an unknown encoding, ask them to confirm the text is UTF-8 or to re-paste/save as UTF-8 before calling the tools again.

## Summary

- Inputs: UTF-8 strings.
- Server: normalizes to NFC; does not repair mojibake.
- If output is garbled: check input encoding and environment (terminal, file, clipboard); do not implement heuristic "fixes" in the agent.
