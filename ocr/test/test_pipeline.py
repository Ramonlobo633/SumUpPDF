from pathlib import Path
from ocr.paddle.pipeline import OCRPipeline

def test_pipeline_instantiation():
    pipeline = OCRPipeline()
    assert pipeline is not None