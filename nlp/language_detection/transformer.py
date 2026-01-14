from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

from .base import LanguageDetector, LanguagePrediction


class TransformerLanguageDetector(LanguageDetector):
    def __init__(
        self,
        model_name: str = "papluca/xlm-roberta-base-language-detection",
        device: str | None = None,
        max_length: int = 256,
    ):
        self.name = "transformer-language-detector"
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.max_length = max_length

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.model.to(self.device)
        self.model.eval()

    @torch.no_grad()
    def detect(self, text: str) -> LanguagePrediction:
        if not text or not text.strip():
            return LanguagePrediction(
                language="unknown",
                confidence=0.0,
                source=self.name,
            )

        inputs = self.tokenizer(
            text,
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt",
        )

        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        outputs = self.model(**inputs)
        probs = F.softmax(outputs.logits, dim=-1)[0]

        confidence, idx = torch.max(probs, dim=0)
        language = self.model.config.id2label[idx.item()]

        return LanguagePrediction(
            language=language,
            confidence=float(confidence),
            source=self.name,
        )
