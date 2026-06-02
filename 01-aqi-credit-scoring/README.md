# AQI and Credit Scoring Machine Learning Pipelines

This project implements Python machine learning pipelines for two distinct business cases:
1. Air Quality Index (AQI) Regression: Environmental AQI level predictions.
2. Banking Credit Scoring Classification: Categorizing borrowers into risk tiers.

The implementation is packaged in the Jupyter Notebook: [aqi-credit-scoring-ml.ipynb](aqi-credit-scoring-ml.ipynb).

---

## Pipeline Stages

### 1. Preprocessing and Cleaning
* Missing Value Resolution: Imputes numerical null values with column-wise mathematical means:
  ```python
  df_clean = df.fillna(df.mean(numeric_only=True))
  ```
* Categorical Encoding: Converts textual grades into ordered numeric boundaries using OrdinalEncoder.

### 2. Validation Split
Partitions datasets into features (X) and targets (y), performing an 80/20 train-test split.

### 3. Scaling and Modeling
Applies StandardScaler to normalize feature distributions before fitting classification and regression algorithms.
