# Sentiment Analyzer

A interactive sentiment analysis demo for educational purposes. Build your own ML app, track experiments with MLflow, and deploy an inference API.

## Overview

This project demonstrates building a sentiment analysis application using Hugging Face Transformers and Gradio. Students will learn the complete MLOps pipeline: model selection, interface building, experiment tracking, deployment, and customization.

## Pré-requisitos

- **Colab**: usado apenas na demonstração do professor (Bloco 2). Esta atividade **não** depende do Colab.
- **Python instalado localmente** (3.10+) na sua máquina — os Exercícios A e B desta atividade rodam num terminal local, não dentro do Colab.

## Initial Code Structure

```
sentiment-analysis/
├── app.py                    # Starting code (to be completed by students)
├── model.py                  # Model loading, shared by app.py, mlflow_tracking.py and api/main.py
├── mlflow_tracking.py        # Exercício A (obrigatório): rastreamento de experimentos com MLflow
├── api/
│   └── main.py                # Exercício B (obrigatório): endpoint de inferência com FastAPI
├── requirements.txt          # Python dependencies (cobre app, MLflow e API)
├── requirements_train.txt    # Dependência extra (scikit-learn), só para o bônus
├── train_model.py            # Optional: Train your own model (bônus)
└── README.md                 # Instructions and challenges
```

## Getting Started

### Step 1: Run Locally

```bash
pip install -r requirements.txt
python app.py
```

`requirements.txt` já cobre tudo que é necessário na aula (app, MLflow, API). Só instale `requirements_train.txt` também se for tentar o desafio bônus de fine-tuning:

```bash
pip install -r requirements.txt -r requirements_train.txt
```

Test the interface and understand how it works.

### Step 2 (opcional/complementar): Deploy to Hugging Face Spaces

Follow the same steps as the Hot Dog Classifier demo:

1. Create Space at [hf.co/new-space](https://hf.co/new-space)
2. Choose **Gradio** SDK
3. Push files via git (`app.py`, `model.py`, `requirements.txt`)

> ⚠️ Se for reaproveitar este README como README do Space, adicione o bloco de front-matter YAML (título, emoji, `sdk: gradio`, `app_file: app.py`, etc.) no topo do arquivo antes de copiar — veja o exemplo completo no README do `hotdog-classifier`. Sem ele, o Space não builda.

---

## Exercício A (obrigatório): Rastreamento de Experimentos com MLflow

**Tempo:** ~30 minutos

Rode `mlflow_tracking.py`: ele compara dois modelos de sentiment analysis (o default e `cardiffnlp/twitter-xlm-roberta-base-sentiment`) em um pequeno conjunto de frases de teste, registrando no MLflow:

- **params**: qual modelo foi usado
- **metrics**: acurácia nas frases de teste, confiança média, latência média
- **artifacts**: um JSON com os resultados detalhados

```bash
python mlflow_tracking.py
```

**Sua tarefa:** adicione um terceiro modelo à lista `MODELS_TO_COMPARE` (pode ser um dos sugeridos no Challenge 3 abaixo), rode novamente, e observe a tabela de comparação impressa ao final (via `mlflow.search_runs()`).

**Implementação desta atividade:** foi adicionado o modelo multilíngue
`nlptown/bert-base-multilingual-uncased-sentiment`. Seus rótulos de 1 a 5
estrelas são normalizados para `NEGATIVE`, `NEUTRAL` e `POSITIVE` antes do
cálculo da acurácia.

**Concepts:** experiment tracking, params/metrics/artifacts, comparação de runs.

---

## Exercício B (obrigatório): Deploy via API

**Tempo:** ~35 minutos

`api/main.py` expõe o modelo via FastAPI. Roda **localmente, num terminal** (não no Colab):

```bash
uvicorn api.main:app --reload
```

Os endpoints `/health` e `/predict` já funcionam — teste-os via Swagger UI (`http://localhost:8000/docs`) ou curl:

```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" \
     -d '{"text": "I love this course!"}'
```

**Sua tarefa:** implemente o endpoint `POST /predict/batch`, que recebe uma lista de textos e retorna uma predição para cada um (reaproveite a lógica de `/predict`).

**Implementação desta atividade:** o endpoint aceita `{"texts": ["...", "..."]}`
e devolve uma lista no mesmo formato de `/predict`, preservando a ordem dos textos.

**Concepts:** deploy de modelo, API REST, request/response schema (Pydantic).

---

## 🎯 Challenge 1: Visual Customization (aquecimento)

**Time:** 10 minutes

Modify the app to make it more visually appealing:

1. Change the emoji in the app title
2. Add a subtitle/description about ML and sentiment analysis
3. Change color scheme using Gradio's theme options

**Concepts:** User interface design, Gradio customization

---

## 🎯 Challenge 2: Enhanced Output (aquecimento)

**Time:** 15 minutes

Improve the output display to show more details:

1. Modify the output to show both label and confidence score
2. Add a score display (e.g., "Confidence: 95%")
3. Create a custom function that formats the result better

**Hint:** The pipeline returns `{'label': 'POSITIVE', 'score': 0.95}`

**Concepts:** Output formatting, working with model predictions

---

## 🎯 Challenge 3: Multi-Language Support (se sobrar tempo)

**Time:** 15 minutes

Add support for Portuguese language:

1. Modify the pipeline to use a multi-language or Portuguese-specific model
2. Add a language selector dropdown
3. Handle both English and Portuguese text

**Modelos verificados e testados (Hugging Face Hub):**
- `cardiffnlp/twitter-xlm-roberta-base-sentiment` (multilíngue, inclui português)
- `nlptown/bert-base-multilingual-uncased-sentiment` (multilíngue; atenção: retorna rótulos "1 star".."5 stars" em vez de POSITIVE/NEGATIVE — bom exemplo real de como modelos diferentes usam esquemas de rótulo diferentes)

**Concepts:** Model selection, internationalization, esquemas de rótulo diferentes entre modelos

---

## 🔥 Bonus Challenge (Optional, fora do horário de aula)

**Time:** 45+ minutes

Implement your own training pipeline using the IMDB dataset:

1. Load the IMDB dataset from Hugging Face `datasets`
2. Fine-tune a pre-trained model (e.g., BERT, DistilBERT) with `train_model.py`
3. Save and load your custom model
4. Replace the default pipeline with your fine-tuned model

**Concepts:** Transfer learning, fine-tuning, dataset loading

---

## Educational Goals

By completing this activity, students will learn:

1. **MLOps Fundamentals**: Experiment tracking, model deployment, versioning
2. **MLflow**: Logging params/metrics/artifacts, comparing runs
3. **FastAPI**: Building and testing a REST inference endpoint
4. **Gradio Interface**: Building interactive ML applications
5. **Transformers Pipeline**: Using pre-trained models
6. **Model Selection**: Finding and evaluating models on Hugging Face Hub

---

## Timeline Guide (120 minutos)

| Atividade | Tempo | Obrigatório? |
|---|---|---|
| Setup local + teste do `app.py` | 10 min | Sim |
| Challenge 1: Customização Visual | 10 min | Aquecimento |
| Challenge 2: Output com confidence score | 15 min | Aquecimento |
| **Exercício A: Rastreamento com MLflow** | 30 min | **Sim** |
| **Exercício B: Endpoint FastAPI** | 35 min | **Sim** |
| Challenge 3: Suporte multi-idioma | 15 min | Se sobrar tempo |
| Revisão da rubrica / dúvidas finais | 5 min | — |
| **Total** | **~120 min** | |
| Bônus: fine-tuning (`train_model.py`) | 45+ min | Fora da aula, entrega posterior |

---

## Checklist de entrega (rubrica)

**Obrigatório**
- [x] App Gradio (`app.py`) rodando localmente sem erros
- [x] `mlflow_tracking.py` executado com pelo menos 3 runs registrados, incluindo 1 modelo adicional escolhido pelo aluno
- [x] Print ou export da tabela de comparação (`mlflow.search_runs()`)
- [x] `api/main.py` rodando localmente, `/predict` testado via curl ou Swagger UI
- [x] Endpoint `/predict/batch` implementado
- [x] Organização do repositório e clareza do código

**Opcional / Bônus**
- [ ] Challenge 1 e/ou 2 (customização visual, output com confidence score)
- [ ] Challenge 3: suporte a português com modelo verificado
- [ ] Deploy no Hugging Face Spaces
- [ ] Bônus: fine-tuning com `train_model.py` (entrega posterior, fora do horário de aula)

---

## Common Issues & Solutions

### Error: "Model not found"
**Solution:** Check internet connection, try a different model

### Slow inference
**Solution:** Use smaller models (DistilBERT instead of BERT), use GPU in Spaces

### App doesn't update
**Solution:** Push changes to git, wait for Space rebuild (~2 min)

### `ModuleNotFoundError: No module named 'sklearn'` ao rodar `train_model.py`
**Solution:** o bônus precisa de `requirements_train.txt` também: `pip install -r requirements.txt -r requirements_train.txt`

---

## Resources

- [Hugging Face Hub Models](https://huggingface.co/models)
- [Gradio Documentation](https://www.gradio.app/docs)
- [Transformers Pipeline](https://huggingface.co/docs/transformers/pipeline_tutorial)
- [Sentiment Analysis Task](https://huggingface.co/tasks/text-classification)
- [MLflow Tracking](https://mlflow.org/docs/latest/tracking.html)
- [FastAPI](https://fastapi.tiangolo.com/)

---

## Teacher Notes

Esta atividade é a **atividade prática avaliativa** do bloco das 14:45–16:45 (120 minutos), após os alunos já terem visto no `hotdog-classifier`: ciclo de vida de ML/MLOps (Bloco 1), rastreamento de experimentos com MLflow (Bloco 2) e deploy via FastAPI/Hugging Face Spaces + monitoramento (Bloco 3).

Os Exercícios A (MLflow) e B (API) são obrigatórios e reforçam diretamente o que foi demonstrado nos Blocos 2 e 3. Os Challenges 1–3 são aquecimento/extensão, não o núcleo avaliado.

All models used are free and publicly available on Hugging Face Hub.
