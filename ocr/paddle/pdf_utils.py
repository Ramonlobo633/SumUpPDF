from pdf2image import convert_from_path
from pathlib import Path

MAX_PAGES = 5

def pdf_to_images(pdf_path: Path):
    images = convert_from_path(str(pdf_path))
    
    if len(images) > MAX_PAGES:
        raise ValueError("PDF exceeds maximum of 5 pages")

    return images