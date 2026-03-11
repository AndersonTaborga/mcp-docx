"""Smoke test: one MCP round-trip (create_document). Run: python tests/test_mcp_smoke.py"""
import asyncio
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "out" / "test_optional"
OUT.mkdir(parents=True, exist_ok=True)


async def main():
    from mcp import ClientSession, StdioServerParameters, stdio_client
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    params = StdioServerParameters(
        command=sys.executable,
        args=["-u", "-m", "mcp_docx.server"],
        cwd=str(ROOT),
        env=env,
    )
    async with stdio_client(params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.call_tool("create_document", {
                "output_path": str(OUT / "smoke.docx"),
                "title": "Smoke",
                "paragraphs": ["OK"],
            })
            text = (result.content[0].text if result.content else "") or ""
            print("isError:", result.isError)
            print("text:", text[:200])
            if not result.isError and text:
                data = json.loads(text)
                print("outputPath exists:", Path(data.get("outputPath", "")).is_file())
                print("Smoke OK")
            else:
                print("Smoke FAIL")
                sys.exit(1)


if __name__ == "__main__":
    import anyio
    anyio.run(main)
