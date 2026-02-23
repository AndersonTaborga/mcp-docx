# Contributing to mcp-docx

Thank you for your interest in contributing. The project is Python-only.

## Branch workflow

- **`dev`** — All development and pull requests target this branch.
- **`main`** — Production-ready releases only. Do not open PRs directly to `main`.

When contributing, clone the repo, create a branch from `dev`, and open your pull request against `dev`.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/AndersonTaborga/mcp-docx.git
   cd mcp-docx
   ```

2. Check out the development branch:
   ```bash
   git checkout dev
   ```
   If `dev` does not exist, create it: `git checkout -b dev`.

3. Create a virtual environment and install the project in editable mode:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   # source .venv/bin/activate  # macOS/Linux
   pip install -e .
   ```

4. Run the MCP server locally (optional):
   ```bash
   python -m mcp_docx.server
   ```
   Or: `mcp-docx` (after pip install -e .).

## Project structure

```
mcp-docx/
├── src/
│   └── mcp_docx/
│       ├── __init__.py
│       ├── server.py          # FastMCP app, tool registration
│       ├── lib/
│       │   ├── __init__.py
│       │   └── docx_utils.py  # Helpers (normalize, create_minimal_document)
│       ├── tools_generate.py  # create_document, generate_from_template
│       ├── tools_edit.py      # replace_text, insert_paragraph
│       └── tools_manipulate.py # merge_documents, extract_text, get_document_info
├── templates/                 # Optional sample .docx templates
├── pyproject.toml
├── README.md
└── CONTRIBUTING.md
```

- **Tools** are implemented in `tools_*.py` and registered in `server.py` with `@mcp.tool()`.
- **Templates** use Jinja2 syntax in .docx: `{{ variable_name }}`.
- **Text encoding**: All user text is normalized to Unicode NFC in `lib/docx_utils.py`.

## Proposing a new tool

1. Implement the tool function in the appropriate `tools_*.py` module (or add a new module and import it in `server.py`).
2. In `server.py`, add a new `@mcp.tool()` function that calls your implementation and returns a JSON-serializable result (typically `json.dumps(result)`).
3. Update **README.md** with the new tool name, description, and example parameters.

Keep the tool interface simple: paths and a single data object. Document any limits (e.g. file size) in the tool docstring and in the README.

## Code style

- Use **Python 3.10+** type hints where helpful.
- Prefer the existing style (formatting, naming). You can use `ruff` or `black` for consistency.
- **Comments and docstrings** should be in English.
- When testing with accented characters, use UTF-8 for source files and terminal to avoid mojibake.

## Opening issues and pull requests

- **Issues**: Use GitHub Issues for bugs, feature ideas, or questions. Describe the problem or suggestion clearly.
- **Pull requests**: Open PRs against **`dev`**, not `main`. Include a short description and how to test.

By contributing, you agree that your contributions will be licensed under the same MIT License as the project.
