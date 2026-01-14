import unicodedata

def detect_script(text: str) -> str:
    for char in text:
        try:
            name = unicodedata.name(char)
        except ValueError:
            continue

        if "CJK" in name or "HIRAGANA" in name or "KATAKANA" in name:
            return "han"
        if "CYRILLIC" in name:
            return "cyrillic"
        if "ARABIC" in name:
            return "arabic"
        if "LATIN" in name:
            return "latin"

    return "unknown"
