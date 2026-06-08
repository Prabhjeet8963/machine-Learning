# Robustness Check: Evaluating NLP Decision Boundaries with Contrast Sets

Welcome! This repository is my **AIML Class Research Project** focused on evaluating how robust NLP models *actually* are. 

Let's be real—standard test sets are kind of gaslighting us. Modern NLP models achieve 90%+ accuracy and look like absolute geniuses, but tweak just one word, and they completely fold. This project investigates model fragility using **Contrast Sets** to probe their local decision boundaries and see if they actually understand language or are just matching patterns based on vibes.

---

## What is this about?

* **The Problem:** Models rely on "shortcut learning" (e.g., seeing the word "great" and predicting "positive" without reading the rest of the sentence).
* **The Solution (Contrast Sets):** We create minimal, label-flipping perturbations of standard test examples (e.g., changing "The acting was great." to "The acting was great, but the script was awful.").
* **The Ultimate Metric (Consistency):** Accuracy is no longer enough. To pass, a model must get the original example **and** all its perturbed versions correct. No half-credits allowed—either it's 100% correct, or it's a fail.

---

## Repository Tour

This repository contains evaluations across 10 benchmark NLP datasets, plus a custom demo project:

### The Datasets
1. **[BoolQ](file:///d:/New%20Coding/AIml/contrast-sets/BoolQ):** Yes/No Reading Comprehension.
2. **[DROP](file:///d:/New%20Coding/AIml/contrast-sets/DROP):** Discrete Reasoning Over Paragraphs (math/logic).
3. **[IMDb](file:///d:/New%20Coding/AIml/contrast-sets/IMDb):** Movie review sentiment classification.
4. **[MATRES](file:///d:/New%20Coding/AIml/contrast-sets/MATRES):** Event temporal relations classification.
5. **[MC-TACO](file:///d:/New%20Coding/AIml/contrast-sets/MCTACO):** Temporal commonsense QA.
6. **[NLVR2](file:///d:/New%20Coding/AIml/contrast-sets/nlvr2):** Visual reasoning (text-to-image matching).
7. **[PERSPECTRUM](file:///d:/New%20Coding/AIml/contrast-sets/perspectrum):** Perspective and stance classification.
8. **[Quoref](file:///d:/New%20Coding/AIml/contrast-sets/quoref):** Coreference resolution QA.
9. **[ropes](file:///d:/New%20Coding/AIml/contrast-sets/ropes):** Qualitative reasoning over paragraph effects.
10. **[UD_English](file:///d:/New%20Coding/AIml/contrast-sets/UD_English):** Syntactic dependency parsing.

---

## The Demo: How Easily Models Get Fooled!!

To show contrast sets in action, I built a self-contained demonstration under `/contrast_set_demo`.

We train a Logistic Regression classifier on movie reviews using standard bigram TF-IDF features. It seems decent at first, but gets completely wrecked by the contrast set.

### How to Run the Demo

Make sure you have `scikit-learn` and `pandas` installed, then run:

```bash
python contrast_set_demo/main.py
```

### The Results (Spoiler Alert)
* **Original Accuracy:** `66.67%` (Seems okay for a small synthetic dataset!)
* **Contrast Accuracy:** `53.33%` (Drops near random-guess level)
* **Consistency Score:** **`20.00%`** (Only 3 out of 15 review pairs were handled perfectly)

**Why did it fail?**
* **Original review:** `"A terrible waste of time."` (Negative) $\rightarrow$ Model predicts **Negative** (Correct).
* **Perturbed review:** `"Not a terrible waste of time."` (Positive) $\rightarrow$ Model predicts **Negative** (Failed). It saw the words "terrible waste" and immediately panicked, completely ignoring the negation "Not".

This demo proves why standard accuracy is a lie and why we need **Consistency** metrics to evaluate real-world readiness.

---

## Credits & Academic Context

* **Research Paper:** This project replicates and explores the evaluation methodology introduced in the EMNLP 2020 paper: 
  > *Evaluating Models' Local Decision Boundaries via Contrast Sets* by Matt Gardner, Yoav Artzi, Basudev Lal, Alon Talmor, Robin Jia, Sevastianos Vassiliades, Nitish Gupta, Kevin Morrison, and Sameer Singh.
* **Data Sources:** We credit the **Allen Institute for AI (AllenAI)** and the dataset creators of BoolQ, DROP, IMDb, MATRES, MC-TACO, NLVR2, PERSPECTRUM, Quoref, ROPES, and Universal Dependencies for open-sourcing the benchmark evaluation sets.
