# Mathematical Formulations in Machine Learning

This project details the core mathematical frameworks of machine learning model evaluation and feature preprocessing calculations.

Refer to [model-evaluation-requirements.docx](model-evaluation-requirements.docx) for the original assignment report.

---

## 1. Classification Metrics

Binary classification targets generate four key outcomes:
* True Positives (TP)
* True Negatives (TN)
* False Positives (FP) (Type I Error)
* False Negatives (FN) (Type II Error)

Given a sample size of N = 10 (TP = 4, TN = 3, FP = 1, FN = 2):

### A. Accuracy
$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} = \frac{4 + 3}{10} = 0.70 \implies 70\%$$

### B. Precision
$$\text{Precision} = \frac{TP}{TP + FP} = \frac{4}{4 + 1} = 0.80 \implies 80\%$$

### C. Recall
$$\text{Recall} = \frac{TP}{TP + FN} = \frac{4}{4 + 2} = 0.6667 \implies 66.67\%$$

### D. F1-Score
$$\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = 2 \times \frac{0.80 \times 0.6667}{0.80 + 0.6667} = 0.7273 \implies 72.73\%$$

---

## 2. Preprocessing Calculations

### A. Mean Imputation
Replaces missing NaN values with the feature's mathematical average:
$$\mathbf{X} = \{10, 12, 15, 18, 20\}$$
$$\text{Mean}(\mathbf{X}) = \frac{10 + 12 + 15 + 18 + 20}{5} = 15$$

### B. Min-Max Normalization
Scales features into the bounded range of [0, 1] to prevent scale bias in distance metrics:
$$\bar{x} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$
For example, normalizing x = 12 given min = 10 and max = 20:
$$\bar{x} = \frac{12 - 10}{20 - 10} = 0.20$$
