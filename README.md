# 🛡️ AI-Powered Threat Detection System

An AI-driven real-time log monitoring system that detects suspicious activity from system authentication logs using Machine Learning.

This project streams Linux logs live, analyzes them using a trained NLP model, and visualizes threats through an interactive dashboard.

Built as part of hands-on cybersecurity + AI engineering practice.

---

## 🚀 Features

✅ Real-time log monitoring using `journalctl`
✅ Machine Learning–based threat classification
✅ Detects failed logins, authentication anomalies, suspicious behavior
✅ Interactive Streamlit dashboard
✅ Live status updates (Normal / Suspicious)
✅ Modular architecture for future extensions
✅ Ready for deployment and portfolio demonstration

---

## 🧠 How It Works

1️⃣ Logs are streamed live from the system
2️⃣ Logs are cleaned and normalized
3️⃣ Text is vectorized using NLP feature extraction
4️⃣ ML model classifies activity
5️⃣ Dashboard displays threat status instantly

```
System Logs
     ↓
Log Monitor
     ↓
Preprocessing
     ↓
Vectorizer
     ↓
ML Model
     ↓
Streamlit Dashboard
```

---

## 🏗️ Project Structure

```
ai_threat_detection/
│
├── app.py                 # Streamlit dashboard
│
├── data/
│   ├── raw_logs.csv
│   └── processed_logs.csv
│
├── model/
│   ├── threat_model.pkl
│   └── vectorizer.pkl
│
├── results/
│   └── confusion_matrix.png
│
├── src/
│   ├── detect.py
│   ├── log_monitor.py
│   ├── preprocessor.py
│   ├── train_model.py
│   └── log_collector.py
│
├── screenshots/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Threat-Detection-System.git
cd AI-Threat-Detection-System
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the System

### Start Dashboard

```bash
streamlit run app.py
```

### Generate Logs (Example)

In another terminal:

```bash
sudo journalctl -n 20
```

Try incorrect password attempts to trigger detection.

---

## 🧩 Machine Learning Pipeline

* Text Vectorization — TF-IDF
* Classification Model — Scikit-learn
* Binary Labels:

  * Normal
  * Suspicious

---

## 🔐 Security Use Cases

* SOC analyst training
* Insider threat simulation
* Authentication anomaly detection
* Cybersecurity portfolio demonstration
* AI security experimentation

---

## 🚧 Future Improvements

* Threat scoring system
* Email/SMS alerting
* Windows log monitoring
* SIEM integration
* Docker deployment
* Cloud hosted dashboard
* Deep learning model upgrade

---

## 👤 Author

**Idris_Chennari**

Aspiring Security Analyst & AI Security Builder
Focused on practical threat detection systems and defensive tooling.

---

## ⭐ If you found this project useful

Consider starring the repository 🙂
