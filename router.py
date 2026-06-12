from llm import ask_llm
import json

TOOLS = [
    "open_application",
    "open_website",
    "open_folder"
]

def decide_tool(prompt):

    message = f"""
You are a tool router.

Available tools:
{TOOLS}

Return ONLY valid JSON.

Examples:

User: Open Chrome

{{
    "tool": "open_application",
    "target": "chrome"
}}

User: Open Spotify

{{
    "tool": "open_application",
    "target": "spotify"
}}

User: Open GitHub

{{
    "tool": "open_website",
    "target": "github.com"
}}

User: What is binary search?

{{
    "tool": "NONE"
}}

User Request:
{prompt}
"""

    response = ask_llm(message)

    try:
        return json.loads(response)
    except:
        return {"tool": "NONE"}