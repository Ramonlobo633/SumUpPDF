import json
from .base import LanguagePrediction


PROMPT_TEMPLATE = """
You are a language identification system.

Given a text extracted from OCR, identify:
1. The primary language
2. The script
3. A confidence score from 0 to 1

Respond ONLY in JSON with this schema:
{
  "language": "<ISO-639-1 code>",
  "script": "<latin|han|cyrillic|arabic|other>",
  "confidence": <float>
}

Text:
<<<
{}
>>>
"""
class LLMLanguageDetector:
    def __init__(self, llm_client):
        self.llm = llm_client
        self.name = "llm-detector"

    def detect(self, text: str) -> LanguagePrediction:
        prompt = self._build_prompt(text)

        response = self.llm.generate(prompt)

        try:
            data = json.loads(response)
            return LanguagePrediction(
                language=data["language"],
                confidence=float(data["confidence"]),
                source=self.name
            )
        except Exception:
            return LanguagePrediction(
                language="unknown",
                confidence=0.0,
                source=self.name
            )

    def _build_prompt(self, text: str) -> str:
        return PROMPT_TEMPLATE.format(text)
