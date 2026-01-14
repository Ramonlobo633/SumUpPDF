from paddleocr import PaddleOCR

class PaddleOCRReader:
    def __init__(self, lang="en"):
        self.ocr = PaddleOCR(
            use_angle_cls=True,
            lang=lang
        )

    def read_image(self, image):
        """
        image: PIL Image or numpy array
        returns: list of text lines
        """
        result = self.ocr.predict(image)

        lines = []
        for page in result:
            for item in page:
                text = item[1][0]
                lines.append(text)

        return lines