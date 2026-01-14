OCR_LANG_MAP = {
    "en": "en",
    "pt": "pt",
    "es": "es",
    "zh": "ch",
    "ru": "ru",
}

def map_to_paddle(lang: str) -> str:
    return OCR_LANG_MAP.get(lang, "en")