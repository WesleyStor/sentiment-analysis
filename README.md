# Sentiment Analyzer

A interactive sentiment analysis demo for educational purposes. Build your own ML app and deploy to Hugging Face Spaces!

## Overview

This project demonstrates building a sentiment analysis application using Hugging Face Transformers and Gradio. Students will learn the complete MLOps pipeline: model selection, interface building, deployment, and customization.

## Initial Code Structure

```
sentiment-analysis/
├── app.py              # Starting code (to be completed by students)
├── requirements.txt    # Python dependencies
├── train_model.py      # Optional: Train your own model (challenge)
└── README.md          # Instructions and challenges
```

## Getting Started

### Step 1: Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Test the interface and understand how it works.

### Step 2: Deploy to Hugging Face Spaces

Follow the same steps as the Hot Dog Classifier demo:

1. Create Space at [hf.co/new-space](https://hf.co/new-space)
2. Choose **Gradio** SDK
3. Push files via git

---

## 🎯 Challenge 1: Visual Customization

**Time:** 10-15 minutes

Modify the app to make it more visually appealing:

1. Change the emoji in the app title
2. Add a subtitle/description about ML and sentiment analysis
3. Change color scheme using Gradio's theme options

**Concepts:** User interface design, Gradio customization

---

## 🎯 Challenge 2: Enhanced Output

**Time:** 15-20 minutes

Improve the output display to show more details:

1. Modify the output to show both label and confidence score
2. Add a score display (e.g., "Confidence: 95%")
3. Create a custom function that formats the result better

**Hint:** The pipeline returns `{'label': 'POSITIVE', 'score': 0.95}`

**Concepts:** Output formatting, working with model predictions

---

## 🎯 Challenge 3: Multi-Language Support

**Time:** 20-25 minutes

Add support for Portuguese language:

1. Research and find a Portuguese sentiment model on Hugging Face Hub
2. Modify the pipeline to use a multi-language or Portuguese-specific model
3. Add a language selector dropdown
4. Handle both English and Portuguese text

**Suggested Models to research:**
- `cardiffnlp/twitter-xlm-roberta-base-sentiment` (multi-language)
- `brazilsilva/pt-sentiment-analysis` (Portuguese-specific)

**Concepts:** Model selection, internationalization, research skills

---

## 🔥 Bonus Challenge (Optional)

**Time:** 30+ minutes

Implement your own training pipeline using the IMDB dataset:

1. Load the IMDB dataset from Hugging Face `datasets`
2. Fine-tune a pre-trained model (e.g., BERT, DistilBERT)
3. Save and load your custom model
4. Replace the default pipeline with your fine-tuned model

**Concepts:** Transfer learning, fine-tuning, dataset loading

---

## Educational Goals

By completing these challenges, students will learn:

1. **MLOps Fundamentals**: Model deployment, versioning, CI/CD
2. **Gradio Interface**: Building interactive ML applications
3. **Transformers Pipeline**: Using pre-trained models
4. **Model Selection**: Finding and evaluating models on Hugging Face Hub
5. **Customization**: Adapting code for specific needs

---

## Timeline Guide

| Activity | Time | Difficulty |
|----------|------|------------|
| Initial setup & local testing | 15 min | Easy |
| Challenge 1: Visual Customization | 15 min | Easy |
| Challenge 2: Enhanced Output | 20 min | Medium |
| Challenge 3: Multi-Language | 30 min | Medium-Hard |
| Bonus: Train your own model | 45+ min | Hard |
| **Total (required)** | **~2.5 hours** | |
| **Total (with bonus)** | **~3.5 hours** | |

---

## Common Issues & Solutions

### Error: "Model not found"
**Solution:** Check internet connection, try a different model

### Slow inference
**Solution:** Use smaller models (DistilBERT instead of BERT), use GPU in Spaces

### App doesn't update
**Solution:** Push changes to git, wait for Space rebuild (~2 min)

---

## Resources

- [Hugging Face Hub Models](https://huggingface.co/models)
- [Gradio Documentation](https://www.gradio.app/docs)
- [Transformers Pipeline](https://huggingface.co/docs/transformers/pipeline_tutorial)
- [Sentiment Analysis Task](https://huggingface.co/tasks/text-classification)

---

## Teacher Notes

This activity is designed for a ~3 hour class:
- **15 min**: Demo Hot Dog Classifier (teacher shows)
- **2.5 hours**: Students complete Challenges 1-3
- **15 min**: Share results and Q&A

All models used are free and publicly available on Hugging Face Hub.
