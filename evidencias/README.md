# Evidências da atividade avaliativa

## Exercício A - MLflow

O script `mlflow_tracking.py` foi executado com três modelos. Todos obtiveram
acurácia `1.0` nas quatro frases de teste:

| Modelo | Acurácia | Confiança média | Latência média (s) |
|---|---:|---:|---:|
| `nlptown/bert-base-multilingual-uncased-sentiment` | 1.0 | 0.815129 | 0.023962 |
| `cardiffnlp/twitter-xlm-roberta-base-sentiment` | 1.0 | 0.949174 | 0.169187 |
| `default-distilbert-sst2` | 1.0 | 0.963921 | 0.217595 |

O arquivo `01_mlflow_tres_runs.png` mostra os três runs registrados e suas
métricas na interface do MLflow.

## Exercício B - FastAPI

O endpoint `POST /predict/batch` foi testado no Swagger UI com dois textos e
retornou HTTP 200, preservando a ordem das entradas:

```json
[
  {
    "text": "I love this course!",
    "label": "POSITIVE",
    "score": 0.9998835325241089
  },
  {
    "text": "This was a terrible experience.",
    "label": "NEGATIVE",
    "score": 0.9989833235740662
  }
]
```

O arquivo `02_fastapi_predict_batch.png` mostra a requisição e a resposta 200.

## App Gradio

O `app.py` foi executado localmente e classificou a frase de exemplo como
`POSITIVE`, com confiança arredondada de 100%. A execução está registrada em
`03_gradio_app_funcionando.png`.
