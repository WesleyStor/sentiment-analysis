"""Exercicio obrigatorio: Endpoint de inferencia via FastAPI.

Rodar localmente (a partir da raiz do repositorio, fora do Colab):
    uvicorn api.main:app --reload

Testar /health e /predict:
    curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" \
         -d '{"text": "I love this course!"}'
    ou abrir http://localhost:8000/docs (Swagger UI)

TODO (aluno): implementar /predict/batch.
"""
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from model import load_classifier

app = FastAPI(title="Sentiment Analysis API")
classifier = load_classifier()


class TextInput(BaseModel):
    text: str


class BatchInput(BaseModel):
    texts: List[str]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(payload: TextInput):
    result = classifier(payload.text)[0]
    return {"text": payload.text, "label": result["label"], "score": result["score"]}


@app.post("/predict/batch")
def predict_batch(payload: BatchInput):
    # TODO (aluno): implemente este endpoint.
    # Deve retornar uma lista de predicoes, uma para cada texto em payload.texts,
    # no mesmo formato do /predict (reaproveite a logica acima).
    raise NotImplementedError("Implemente o endpoint /predict/batch")
