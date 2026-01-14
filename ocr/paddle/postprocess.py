import re

def clean_text(lines: list[str]) -> str:
    text = "\n".join(lines)

    # normalize spaces
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{2,}", "\n\n", text)

    return text.strip()
