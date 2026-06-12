import pandas as pd
import numpy as np
import re
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
from nltk.corpus import stopwords
from urllib.parse import urlparse
import requests
import nltk
import os

# -----------------------------
# NLTK SETUP
# -----------------------------
try:
    nltk.data.find('corpora/stopwords')
except:
    nltk.download('stopwords')

STOPWORDS = set(stopwords.words("english"))

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI-Powered Phishing Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

.main-title {
    text-align:center;
    font-size:3.5rem;
    font-weight:800;
    color:#38bdf8;
    margin-bottom:0px;
}

.sub-title {
    text-align:center;
    color:#cbd5e1;
    font-size:1.1rem;
    margin-bottom:30px;
}

.card {
    background: rgba(255,255,255,0.05);
    padding:20px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
}

.metric-card {
    background:#111827;
    padding:15px;
    border-radius:15px;
    margin-bottom:10px;
}

.safe-box {
    background:rgba(34,197,94,0.2);
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:#22c55e;
    font-size:24px;
    font-weight:bold;
}

.phishing-box {
    background:rgba(239,68,68,0.2);
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:#ef4444;
    font-size:24px;
    font-weight:bold;
}

.stButton > button {
    width:100%;
    height:55px;
    border:none;
    border-radius:12px;
    background:linear-gradient(90deg,#06b6d4,#3b82f6);
    color:white;
    font-size:18px;
    font-weight:bold;
}

.stButton > button:hover {
    transform:scale(1.02);
    transition:0.3s;
}

section[data-testid="stSidebar"] {
    background-color:#111827;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# CLEAN EMAIL
# -----------------------------
def clean_email_body(email_body):
    email_body = re.sub(r'[^a-zA-Z\s]', '', str(email_body))
    email_body = ' '.join(
        [
            word.lower()
            for word in email_body.split()
            if word.lower() not in STOPWORDS
        ]
    )
    return email_body

# -----------------------------
# URL FEATURE EXTRACTION
# -----------------------------
def extract_url_features(email_body):
    urls = re.findall(r'(https?://[^\s]+)', str(email_body))

    features = []

    for url in urls:

        parsed_url = urlparse(url)

        domain_length = len(parsed_url.netloc)
        path_length = len(parsed_url.path)

        features.append(domain_length)
        features.append(path_length)

        if parsed_url.scheme in ['http', 'https']:
            features.append(1)
        else:
            features.append(0)

        try:
            response = requests.get(url, timeout=3)
            features.append(response.status_code)

        except:
            features.append(0)

    return np.mean(features) if features else 0

# -----------------------------
# TRAIN MODEL
# -----------------------------
def train_model(data):

    data['cleaned_body'] = data['email_body'].apply(
        clean_email_body
    )

    data['url_features'] = data['email_body'].apply(
        extract_url_features
    )

    X = pd.concat(
        [
            data['cleaned_body'],
            data['url_features']
        ],
        axis=1
    )

    X.columns = [
        'email_body',
        'url_features'
    ]

    y = data['label']

    vectorizer = CountVectorizer()

    model = make_pipeline(
        vectorizer,
        MultinomialNB()
    )

    model.fit(
        X['email_body'],
        y
    )

    joblib.dump(
        model,
        'phishing_model.pkl'
    )

# -----------------------------
# PREDICTION
# -----------------------------
def predict_phishing(model, email_body):

    cleaned_body = clean_email_body(
        email_body
    )

    prediction = model.predict(
        [cleaned_body]
    )

    return (
        "Phishing"
        if prediction[0] == 1
        else "Safe"
    )

# -----------------------------
# EMAIL STATISTICS
# -----------------------------
def get_email_stats(email_text):

    words = len(email_text.split())

    urls = re.findall(
        r'(https?://[^\s]+)',
        email_text
    )

    url_count = len(urls)

    domains = set()

    for url in urls:
        try:
            domains.add(
                urlparse(url).netloc
            )
        except:
            pass

    suspicious_keywords = [
        "urgent",
        "verify",
        "password",
        "bank",
        "account",
        "click",
        "login",
        "reward",
        "winner",
        "free",
        "limited",
        "update",
        "security"
    ]

    keyword_count = sum(
        email_text.lower().count(k)
        for k in suspicious_keywords
    )

    return (
        words,
        url_count,
        len(domains),
        keyword_count
    )

# -----------------------------
# RISK SCORE
# -----------------------------
def calculate_risk_score(
    url_count,
    keyword_count
):

    score = min(
        (
            url_count * 15
            +
            keyword_count * 5
        ),
        100
    )

    return score

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🛡️ Navigation")

page = st.sidebar.radio(
    "Select Section",
    [
        "Email Scanner",
        "Model Training",
        "About Project"
    ]
)

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    """
    <div class='main-title'>
    🛡️ AI-Powered Phishing Detection System
    </div>
    <div class='sub-title'>
    Detect Email Threats Using Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = None

try:
    model = joblib.load(
        "phishing_model.pkl"
    )
    model_status = "Loaded"

except:
    model_status = "Not Found"

# -----------------------------
# EMAIL SCANNER PAGE
# -----------------------------
if page == "Email Scanner":

    left_col, right_col = st.columns(
        [3, 1]
    )

    with left_col:

        st.markdown(
            "<div class='card'>",
            unsafe_allow_html=True
        )

        st.subheader(
            "📧 Email Analysis"
        )

        email_input = st.text_area(
            "Paste Email Content",
            height=250,
            placeholder="Paste suspicious email content here..."
        )

        if st.button(
            "🔍 Analyze Email"
        ):

            if not email_input:

                st.warning(
                    "Please enter an email body."
                )

            elif model is None:

                st.error(
                    "No trained model found."
                )

            else:

                result = predict_phishing(
                    model,
                    email_input
                )

                words, urls, domains, keywords = (
                    get_email_stats(
                        email_input
                    )
                )

                risk_score = calculate_risk_score(
                    urls,
                    keywords
                )

                st.subheader(
                    "Threat Score"
                )

                st.progress(
                    risk_score
                )

                st.write(
                    f"Risk Score: {risk_score}%"
                )

                if result == "Safe":

                    st.markdown(
                        """
                        <div class='safe-box'>
                        ✅ SAFE EMAIL
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                else:

                    st.markdown(
                        """
                        <div class='phishing-box'>
                        ⚠️ PHISHING DETECTED
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                st.markdown("---")

                c1, c2, c3, c4 = st.columns(4)

                c1.metric(
                    "Words",
                    words
                )

                c2.metric(
                    "URLs",
                    urls
                )

                c3.metric(
                    "Domains",
                    domains
                )

                c4.metric(
                    "Keywords",
                    keywords
                )

    with right_col:

        st.markdown(
            "<div class='card'>",
            unsafe_allow_html=True
        )

        st.subheader(
            "📊 System Status"
        )

        st.metric(
            "Model Status",
            model_status
        )

        st.metric(
            "Algorithm",
            "Naive Bayes"
        )

        st.metric(
            "Vectorizer",
            "CountVectorizer"
        )

        st.metric(
            "URL Analysis",
            "Enabled"
        )

        st.metric(
            "Threat Engine",
            "Active"
        )

# -----------------------------
# MODEL TRAINING PAGE
# -----------------------------
elif page == "Model Training":

    st.subheader(
        "🧠 Train Detection Model"
    )

    uploaded_file = st.file_uploader(
        "Upload CSV Dataset",
        type=["csv"]
    )

    if uploaded_file:

        data = pd.read_csv(
            uploaded_file
        )

        if (
            'email_body'
            in data.columns
            and
            'label'
            in data.columns
        ):

            st.success(
                f"Dataset Loaded ({len(data)} records)"
            )

            st.dataframe(
                data.head()
            )

            if st.button(
                "🚀 Train Model"
            ):

                with st.spinner(
                    "Training..."
                ):

                    train_model(
                        data
                    )

                st.success(
                    "Model trained and saved successfully!"
                )

        else:

            st.error(
                "Dataset must contain 'email_body' and 'label' columns."
            )

# -----------------------------
# ABOUT PAGE
# -----------------------------
elif page == "About Project":

    st.subheader(
        "ℹ️ About Project"
    )

    st.markdown("""
### AI-Powered Phishing Detection System

This project uses:

- Machine Learning
- CountVectorizer
- Multinomial Naive Bayes
- URL Feature Analysis
- Streamlit Dashboard

### Features

✅ Email Threat Detection  
✅ URL Analysis  
✅ Dataset Training  
✅ Risk Scoring  
✅ Modern Cybersecurity UI  
✅ Real-Time Email Statistics

### Technology Stack

- Python
- Streamlit
- Scikit-Learn
- Pandas
- NLTK
- Requests
""")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")

st.markdown(
    """
    <div style='text-align:center;color:#94a3b8'>
    🛡️ AI-Powered Phishing Detection System<br>
    Developed using Machine Learning & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)