from fastapi import FastAPI

app = FastAPI(title="SumUpPDF")

@app.get("/health")
def health():
    return {"status": "ok"}