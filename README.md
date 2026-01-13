# SumUpPDF

SumUpPDF is an educational open-source project to practice building **real-world AI systems** using OCR, NLP, and LLMs.

---

## Features

- Accepts documents with up to **5 pages** (PDF or images)
- Extracts text using **PaddleOCR**
- Detects document language
- Summarizes the content into **one page** using an LLM
- Converts the summary into **speech audio**
- Exposes everything through a REST API
- Includes automated tests and CI

This project is meant for **learning and experimentation**, but it is structured like a real product.

---

## Tech stack

**Backend**
- Python 3.10+
- FastAPI
- PaddleOCR
- Transformers / PyTorch

**Frontend**
- React ^19.2.0

**Infrastructure**
- Docker / Docker Compose
- GitHub Actions (CI)


---

## Project structure

```
SumUpPDF/
├── api/            # FastAPI app and routes
├── ocr/            # PaddleOCR integration
├── nlp/            # NLP and LLM pipelines
├── training/       # Model training and evaluation
├── tts/            # Text-to-speech module
├── metrics/        # Metrics
├── storage/        # Local data storage
├── tests/          # Unit and integration tests
├── docker/         # Dockerfiles
├── docs/           # Project documentation
└── README.md
```

---

## AI Architecture (TBD)

## Storage

Local storage is used for:

- Uploaded documents
- OCR outputs
- Generated summaries
- Audio files

Directory:

```
storage/
```