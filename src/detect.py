import joblib

model = joblib.load("model/threat_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

while True:
    log = input("\nEnter log (or type exit): ")

    if log.lower() == "exit":
        break

    vec = vectorizer.transform([log])
    prob = model.predict_proba(vec)[0][1]

    if prob > 0.5:
        print(f"🚨 Threat Detected ({prob*100:.2f}%)")
    else:
        print(f"✅ Normal Activity ({(1-prob)*100:.2f}%)")
