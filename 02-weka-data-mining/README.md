# Weka Tool Data Mining and Algorithms Evaluation

This project documents empirical data mining experiments conducted using the Weka (Waikato Environment for Knowledge Analysis) explorer tool.

Refer to [weka-data-mining-requirements.docx](weka-data-mining-requirements.docx) for the original lab report document.

---

## Experiments

### 1. Regression Tasks
* Objective: Evaluate house price predictions using Linear Regression.
* Evaluation Splits: Compares 10-Fold Cross-Validation, 50% split, and 66% split testing.

### 2. Classification Boundaries
* Objective: Compare decision boundaries on multi-class datasets.
* Dataset: IRIS flower dataset (150 instances, 3 target classes).
* Models Evaluated:
  * J48 Decision Tree: C4.5 algorithm optimizing Information Gain.
  * REPTree (Reduced Error Pruning): Information gain splits with back-fitting reduced-error pruning.
  * OneR (One Rule): Baseline classifier generating a single rule on the single attribute with the lowest training error.

### 3. Unsupervised Clustering
* Objective: Centroid-based partitioning using SimpleKMeans.
* Evaluates the impact of cluster bounds (k=3 for actual species count) and random initialization seeds on centroid convergence.
