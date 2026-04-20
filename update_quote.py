import json
import random
import sys
from pathlib import Path

# Ensure emoji output works on Windows terminals
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

SCRIPT_DIR = Path(__file__).parent


def pick_quote():
    """Pick a random quote from quotes.json."""
    quotes_path = SCRIPT_DIR / "quotes.json"
    quotes = json.loads(quotes_path.read_text(encoding="utf-8"))
    return random.choice(quotes)


def update_readme(quote_text):
    """Replace the quote block in README.md."""
    readme_path = SCRIPT_DIR / "README.md"
    content = readme_path.read_text(encoding="utf-8")

    start_tag = "<!-- QUOTE_START -->"
    end_tag = "<!-- QUOTE_END -->"

    start_idx = content.index(start_tag) + len(start_tag)
    end_idx = content.index(end_tag)

    new_quote_block = f'\n"{quote_text}"\n'
    new_content = content[:start_idx] + new_quote_block + content[end_idx:]

    readme_path.write_text(new_content, encoding="utf-8")
    print(f'Updated quote: "{quote_text}"')


def random_commit_message():
    """Pick a fun commit message."""
    messages = [
        "🤖 daily quote drop",
        "📚 today's wisdom (or lack thereof)",
        "☕ another day another quote",
    ]
    return random.choice(messages)


if __name__ == "__main__":
    quote_text = pick_quote()
    update_readme(quote_text)
    print(f"Commit message suggestion: {random_commit_message()}")
