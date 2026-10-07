import joblib
import os
from read_emails import get_unread_emails

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "spam_model.pkl")

model = joblib.load(MODEL_PATH)
print("✅ Model loaded")

emails = get_unread_emails()

for email in emails:
    text = email["subject"] + " " + email["body"]
    prediction = model.predict([text])[0]

    label = "🚨 SPAM" if prediction == 1 else "✅ NOT SPAM"

    print(f"📧 From: {email['from']}")
    print(f"📝 Subject: {email['subject']}")
    print(f"📌 Result: {label}")
    print("-" * 70)
