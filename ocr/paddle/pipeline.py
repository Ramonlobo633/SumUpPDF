from pathlib import Path
from PIL import Image

from reader import PaddleOCRReader
from pdf_utils import pdf_to_images
from postprocess import clean_text

class OCRPipeline:
    def __init__(self, lang="en"):
        self.reader = PaddleOCRReader(lang=lang)

    def process(self, file_path: Path) -> str:
        if file_path.suffix.lower() == ".pdf":
            images = pdf_to_images(file_path)
        else:
            images = [Image.open(file_path)]

        all_lines = []

        for image in images:
            lines = self.reader.read_image(image)
            all_lines.extend(lines)

        return clean_text(all_lines)

if __name__ == "__main__":
    pipeline = OCRPipeline(lang="en")
    result = pipeline.process(Path("/home/ramonlobo/workspace/paddleocr/ai_pdf_summarizer/pdf_summarizer/test.png"))
    print(result)