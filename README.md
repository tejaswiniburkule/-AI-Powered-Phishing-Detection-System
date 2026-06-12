# 🛡️ AI-Powered Phishing Detection System

<div align="center">
  
### Intelligent Email Threat Detection Using Machine Learning

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge\&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge\&logo=scikitlearn)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Phishing_Detection-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

---

### 🔐 Detect • Analyze • Protect

An advanced Machine Learning-powered phishing detection system that analyzes email content and URLs to identify potential phishing attacks in real time through a modern cybersecurity dashboard.

</div>

---

# 📌 Overview

Phishing attacks remain one of the most common cybersecurity threats, targeting users through deceptive emails, fake login pages, and malicious links.

This project leverages:

* 🧠 Machine Learning
* 📧 Email Content Analysis
* 🔗 URL Feature Extraction
* 📊 Real-Time Risk Assessment
* 🖥️ Interactive Streamlit Dashboard

to classify incoming emails as:

✅ Safe

⚠️ Phishing

---

# 🚀 Features

### Email Analysis Engine

* Email text preprocessing
* Stopword removal
* Text normalization
* Feature extraction

### URL Intelligence

* Domain length analysis
* URL path inspection
* Protocol verification
* URL status validation
* Suspicious URL detection

### Machine Learning Detection

* CountVectorizer
* Multinomial Naive Bayes
* Real-time predictions
* Custom dataset training

### Cybersecurity Dashboard

* Modern dark theme UI
* Risk scoring system
* Threat level visualization
* Email statistics
* Interactive model training

---

# 🏗️ System Architecture

```text
┌─────────────────┐
│   Email Input   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Text Cleaning   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Feature Extraction │
│ • Keywords      │
│ • URLs          │
│ • Domains       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ CountVectorizer │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Naive Bayes ML  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Prediction      │
│ Safe / Phishing │
└─────────────────┘
```

---

# 🛠️ Tech Stack

| Category         | Technology       |
| ---------------- | ---------------- |
| Language         | Python           |
| Framework        | Streamlit        |
| Machine Learning | Scikit-Learn     |
| NLP              | NLTK             |
| Data Processing  | Pandas, NumPy    |
| URL Analysis     | Requests, urllib |
| Model Storage    | Joblib           |

---

# 📂 Project Structure

```bash
AI-Phishing-Detection/
│
├── app.py
├── phishing_model.pkl
├── logo.JPEG
├── dataset.csv
├── requirements.txt
├── README.md
│
└── assets/
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Phishing-Detection.git

cd AI-Phishing-Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

# 📊 Sample Prediction

### Safe Email

```text
Meeting scheduled tomorrow at 10 AM.
Please bring the project report.
```

Prediction:

```text
SAFE
```

---

### Phishing Email

```text
Your bank account has been suspended.

Verify immediately:

https://secure-bank-login-verification.com
```

Prediction:

```text
PHISHING
```

---

# 🧠 Machine Learning Pipeline

```python
Email Text
    ↓
Text Cleaning
    ↓
CountVectorizer
    ↓
MultinomialNB
    ↓
Prediction
```

---

# 🔍 Risk Assessment Parameters

The application evaluates:

* Suspicious keywords
* URL count
* Domain count
* URL structure
* Protocol validity
* Reachability status

These factors contribute to the overall threat score.

---

# 📸 Dashboard Preview

```text
🛡 AI-Powered Phishing Detection System

┌────────────────────────────────────┐
│ Email Scanner                      │
├────────────────────────────────────┤
│ Paste Email Content                │
│                                    │
│ [ Analyze Email ]                  │
└────────────────────────────────────┘

Threat Score: ███████████░░░░ 72%

⚠️ PHISHING DETECTED
```

---

# 🔮 Future Enhancements

* Deep Learning Models (LSTM/BERT)
* Email Header Analysis
* Attachment Scanning
* Domain Reputation APIs
* Real-Time Threat Intelligence
* Browser Extension Integration
* SIEM Integration
* Enterprise Dashboard

---

# 👩‍💻 Author

### Tejaswini Burkule

B.Tech Artificial Intelligence & Machine Learning

Cybersecurity Enthusiast | AI Developer | Security Researcher

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

🔐 Contribute to improving phishing detection

---

<div align="center">

### 🛡️ Secure the Inbox. Stop Phishing Before It Strikes.

Made with ❤️ using Python, Streamlit & Machine Learning

</div>
