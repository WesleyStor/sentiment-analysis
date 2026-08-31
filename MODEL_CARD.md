# Hugging Face Model Card for Sentiment Analysis Model

This model is trained for educational purposes as part of an MLOps course.

## Model Details

- **Task**: Text Classification / Sentiment Analysis
- **Model Type**: DistilBERT (or your choice)
- **Language**: English (or Portuguese if adapted)
- **Training Data**: IMDB Movie Reviews

## Usage

```python
from transformers import pipeline

# Load the fine-tuned model
model_path = "./sentiment-model"  # or "YOUR_USERNAME/your-model-name"
pipeline = pipeline("sentiment-analysis", model=model_path)

# Make predictions
result = pipeline("I love this product!")
print(result)
```

## Training

The model was trained using the script `train_model.py` which:

1. Loads the IMDB dataset
2. Fine-tunes a pre-trained DistilBERT model
3. Evaluates on test set
4. Saves the fine-tuned model

## Evaluation Metrics

After training, the model achieves:
- Accuracy: ~90-95% on IMDB test set
- F1 Score: ~0.90-0.95

## License

MIT License - Educational use only

## Citation

```bibtex
@article{maas2011learning,
  title={Learning word vectors for sentiment analysis},
  author={Maas, Andrew L. and Daly, Raymond E. and Pham, Peter T. and Huang, Dan and Ng, Andrew Y.},
  journal={Proceedings of the 49th annual meeting of the association for computational linguistics: Human language technologies},
  pages={142--150},
  year={2011}
}
```
