# 🛡️ AI Driven Threat Detection System

Real-time AI powered log monitoring system that detects suspicious activity using machine learning and live Linux system logs.

## Features

✔ Real-time journalctl monitoring  
✔ ML-based threat classification  
✔ Streamlit live dashboard  
✔ Suspicious activity detection  
✔ Lightweight & deployable locally  

## Tech Stack

- Python
- Scikit-learn
- Streamlit
- Journalctl
- NLP Vectorization

## Run Locally

git clone <repo>
cd AI-Threat-Detection-System
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

## Demo

Triggers detection when:

- Failed sudo authentication
- SSH anomalies
- Login activity

## Author

Built as part of AI Security Research Project
