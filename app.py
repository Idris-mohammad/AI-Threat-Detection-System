import streamlit as st
import joblib
from src.log_monitor import stream_logs

# Load model
model = joblib.load("model/threat_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

st.set_page_config(page_title="AI Threat Detection", page_icon="🛡️")

st.title("🛡️ AI DRIVEN THREAT DETECTION SYSTEM")
st.write("Live Monitoring Systems ")

log_placeholder = st.empty()
status_placeholder = st.empty()

history = []

for log in stream_logs():

    # Predict
    log_vector = vectorizer.transform([log])
    prediction = model.predict(log_vector)[0]

    if isinstance(prediction, str):
        label = prediction.lower()
    else:
        label = "suspicious" if prediction == 1 else "normal"

    # Store last logs
    history.append(f"[{label.upper()}] {log}")
    history = history[-15:]

    log_placeholder.text("\n".join(history))

    if label == "suspicious":
        status_placeholder.error("🚨 Suspicious activity detected!")
    else:
        status_placeholder.success("✅ System operating normally")
