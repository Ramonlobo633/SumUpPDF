
from reader import PaddleOCRReader


def extract_preview_text(file_path, max_chars=400):
    reader = PaddleOCRReader(lang="en")

    images = load_first_page(file_path)
    lines = reader.read_image(images)

    text = " ".join(lines)
    return text[:max_chars]
