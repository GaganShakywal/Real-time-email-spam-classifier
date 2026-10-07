#  Email Spam Detection System

An **end-to-end Machine Learning project** that detects spam emails using **Natural Language Processing (NLP)** and **Logistic Regression**, integrated with the **Gmail API** to classify real incoming emails in real time.

This project demonstrates how classical ML models can be combined with APIs to build **production-style intelligent systems**.
---

## Project Overview

Spam emails are a major problem in modern communication. This project:

* Trains a **Logistic Regression** model on spam/ham data
* Uses **NLP (TF-IDF)** to convert email text into numerical features
* Connects to **Gmail API** to fetch unread emails
* Predicts whether each email is **SPAM or NOT SPAM**
* Displays sender name, subject, and classification result

---

##  Technologies Used

* **Python 3.10+**
* **Scikit-learn** (Logistic Regression, GridSearchCV)
* **NLP (TF-IDF Vectorizer)**
* **Gmail API (OAuth 2.0)**
* **Google Auth & API Client Libraries**
* **Joblib** (model persistence)

---

##  Project Structure

```text
email-spam-detection-system/
│
├── data/
│   └── spam.csv                  # Training dataset
│
├── model/
│   └── spam_model.pkl             # Trained ML model
│
├── gmail_auth.py                  # Gmail OAuth authentication
├── read_emails.py                 # Fetch unread Gmail emails
├── run_spam_detector.py           # Main pipeline runner
│
├── credentials.json               # Gmail OAuth credentials (ignored in Git)
├── token.pickle                   # OAuth token (ignored in Git)
│
├── requirements.txt
└── README.md
```

Feel free to fork, improve, and experiment 

