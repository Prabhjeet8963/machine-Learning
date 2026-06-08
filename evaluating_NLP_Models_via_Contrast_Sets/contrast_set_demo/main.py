import json
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# 1. Create a synthetic training dataset
# A mix of positive and negative sentences
train_data = [
    # Positive Examples
    ("This movie is great", "positive"),
    ("I loved this film", "positive"),
    ("What a wonderful experience", "positive"),
    ("Fantastic acting and plot", "positive"),
    ("Truly a masterpiece", "positive"),
    ("I enjoyed it a lot", "positive"),
    ("Best movie of the year", "positive"),
    ("Highly recommended", "positive"),
    ("A solid 10/10", "positive"),
    ("Beautifully shot and acted", "positive"),
    ("The acting was superb", "positive"),
    ("I was hooked from the start", "positive"),
    ("A triumph of cinema", "positive"),
    ("Brilliant direction", "positive"),
    ("A must-see for everyone", "positive"),
    ("The cinematography was breathtaking", "positive"),
    ("An emotional rollercoaster in the best way", "positive"),
    ("I couldn't take my eyes off the screen", "positive"),
    ("A perfect blend of action and drama", "positive"),
    ("The soundtrack was mesmerizing", "positive"),
    ("Incredible performance by the lead actor", "positive"),
    ("A timeless classic", "positive"),
    ("Exceeded all my expectations", "positive"),
    ("Smart, funny, and touching", "positive"),
    ("A visual spectacle", "positive"),
    ("I will definitely watch this again", "positive"),
    ("Two thumbs up", "positive"),
    ("Pure movie magic", "positive"),
    ("The script was tight and witty", "positive"),
    ("A refreshing take on the genre", "positive"),

    # Negative Examples
    ("This movie is terrible", "negative"),
    ("I hated this film", "negative"),
    ("What a waste of time", "negative"),
    ("Awful acting and plot", "negative"),
    ("Truly a disaster", "negative"),
    ("I did not enjoy it", "negative"),
    ("Worst movie of the year", "negative"),
    ("Not recommended", "negative"),
    ("A solid 0/10", "negative"),
    ("Poorly shot and acted", "negative"),
    ("The script was boring", "negative"),
    ("I fell asleep", "negative"),
    ("Predictable and dull", "negative"),
    ("Not worth the money", "negative"),
    ("The direction was weak", "negative"),
    ("I walked out of the theater", "negative"),
    ("Complete garbage", "negative"),
    ("Don't bother watching", "negative"),
    ("The plot made no sense", "negative"),
    ("Wooden acting and terrible dialogue", "negative"),
    ("I regret watching this", "negative"),
    ("Boring from start to finish", "negative"),
    ("A complete mess", "negative"),
    ("Lackluster and uninspired", "negative"),
    ("The pacing was too slow", "negative"),
    ("Overhyped and underwhelming", "negative"),
    ("I've seen better commercials", "negative"),
    ("Painfully bad", "negative"),
    ("A total snooze fest", "negative"),
    ("Save your money", "negative"),
]

df_train = pd.DataFrame(train_data, columns=["text", "label"])

print("Training data shape:", df_train.shape)

# 2. Train a simple model
# We use bigrams to hopefully capture some negation, but simple models often fail on contrast sets
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1, 2))), 
    ('clf', LogisticRegression(random_state=42))
])

print("Training model...")
pipeline.fit(df_train['text'], df_train['label'])
print("Model trained.")

# 3. Load Contrast Set
print("\nLoading Contrast Set...")
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'contrast_set.json')

try:
    with open(file_path, 'r') as f:
        contrast_data = json.load(f)
except FileNotFoundError:
    print(f"Error: contrast_set.json not found at {file_path}")
    exit(1)

# Prepare evaluation data
original_texts = [item['original'] for item in contrast_data]
original_labels = [item['original_label'] for item in contrast_data]
contrast_texts = [item['contrast'] for item in contrast_data]
contrast_labels = [item['contrast_label'] for item in contrast_data]

# 4. Evaluate
print("\n--- Evaluation on Original Examples ---")
orig_preds = pipeline.predict(original_texts)
print(classification_report(original_labels, orig_preds, zero_division=0))
orig_acc = accuracy_score(original_labels, orig_preds)
print(f"Original Accuracy: {orig_acc:.4f}")

print("\n--- Evaluation on Contrast Examples ---")
contrast_preds = pipeline.predict(contrast_texts)
print(classification_report(contrast_labels, contrast_preds, zero_division=0))
contrast_acc = accuracy_score(contrast_labels, contrast_preds)
print(f"Contrast Accuracy: {contrast_acc:.4f}")

# 5. Consistency Evaluation (The "Contrast Consistency" metric)
# A model is consistent if it predicts correctly on BOTH the original and the contrast example.
consistent_count = 0
total_pairs = len(contrast_data)

print("\n--- Detailed Analysis & Consistency Check ---")
print(f"{'ID':<3} | {'Original':<40} | {'Pred':<8} | {'Contrast':<40} | {'Pred':<8} | {'Status'}")
print("-" * 115)

for i in range(total_pairs):
    item = contrast_data[i]
    orig_pred = orig_preds[i]
    cont_pred = contrast_preds[i]
    
    orig_correct = (orig_pred == item['original_label'])
    cont_correct = (cont_pred == item['contrast_label'])
    
    is_consistent = orig_correct and cont_correct
    if is_consistent:
        consistent_count += 1
        status = "CONSISTENT"
    elif not orig_correct:
        status = "FAIL_ORIG"
    elif not cont_correct:
        status = "FAIL_CONT"
    else:
        status = "UNKNOWN" # Should not happen given logic above

    # Truncate text for display
    orig_text = (item['original'][:37] + '...') if len(item['original']) > 37 else item['original']
    cont_text = (item['contrast'][:37] + '...') if len(item['contrast']) > 37 else item['contrast']
    
    print(f"{i+1:<3} | {orig_text:<40} | {orig_pred:<8} | {cont_text:<40} | {cont_pred:<8} | {status}")

consistency_score = consistent_count / total_pairs
print("-" * 115)
print(f"\nConsistency Score: {consistency_score:.4f} ({consistent_count}/{total_pairs})")
print(f"Original Accuracy: {orig_acc:.4f}")
print(f"Contrast Accuracy: {contrast_acc:.4f}")
print("\nInterpretation:")
print("- Original Accuracy: How well the model performs on standard examples.")
print("- Contrast Accuracy: How well the model performs on the perturbed examples.")
print("- Consistency Score: The percentage of pairs where the model gets BOTH right. This is the true test of robustness.")
