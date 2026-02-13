import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("data/processed_logs.csv")

X = data["raw_log"]
y = data["label"].map({"normal": 0, "suspicious": 1})

# Vectorize
vectorizer = TfidfVectorizer(ngram_range=(1,2), stop_words="english")
X_vec = vectorizer.fit_transform(X)

# Train
model = LogisticRegression()
model.fit(X_vec, y)

# Save model
joblib.dump(model, "model/threat_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("[+] Model trained and saved")
