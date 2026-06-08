# Contrast Set Demo

This project demonstrates the concept of **Contrast Sets** for evaluating NLP models, inspired by the [AllenAI Contrast Sets](https://github.com/allenai/contrast-sets) and [LIT](https://github.com/leo-liuzy/LIT_auto-gen-contrast-set) papers.

## Overview

Standard test sets often fail to expose the brittleness of NLP models. Models may rely on spurious correlations (e.g., seeing the word "not" and assuming negative sentiment, or ignoring the second half of a sentence).

**Contrast Sets** are created by making small, linguistically consistent perturbations to test examples that change the true label. A robust model should handle these perturbations correctly.

## Implementation

1.  **Model**: A simple Logistic Regression model with TF-IDF features (using bigrams), trained on a small synthetic dataset of movie reviews.
2.  **Contrast Set**: A manually created set of examples where each original sentence is paired with a perturbed version (e.g., adding a negation or a "but" clause).

## How to Run

```bash
python main.py
```

## Expected Results

The model will likely perform well on the **Original** examples but fail on some **Contrast** examples.

Example failure mode:
*   **Original**: "The acting was great." (Positive) -> Model predicts Positive (Correct)
*   **Contrast**: "The acting was great, but the script was awful." (Negative) -> Model might still predict Positive because it sees "great" and "acting" and ignores the "but... awful" part or weighs "great" too heavily.

This demonstrates why contrast sets are a valuable tool for rigorous evaluation.
