"""Testes dos endpoints sem baixar o modelo do Hugging Face."""

import sys
from types import SimpleNamespace

from fastapi.testclient import TestClient


class FakeClassifier:
    def __call__(self, text):
        label = "POSITIVE" if "love" in text.lower() else "NEGATIVE"
        return [{"label": label, "score": 0.95}]


fake_classifier = FakeClassifier()
sys.modules["model"] = SimpleNamespace(load_classifier=lambda: fake_classifier)

from api import main  # noqa: E402  (importa depois de substituir a dependencia)


def test_health():
    client = TestClient(main.app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_batch_returns_one_prediction_per_text(monkeypatch):
    monkeypatch.setattr(main, "classifier", FakeClassifier())
    client = TestClient(main.app)

    response = client.post(
        "/predict/batch",
        json={"texts": ["I love this course!", "This is terrible."]},
    )

    assert response.status_code == 200
    assert response.json() == [
        {"text": "I love this course!", "label": "POSITIVE", "score": 0.95},
        {"text": "This is terrible.", "label": "NEGATIVE", "score": 0.95},
    ]
