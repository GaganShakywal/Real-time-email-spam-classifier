import joblib
from read_emails import get_unread_emails

model = joblib.load("spam_model.pkl")

emails = get_unread_emails()

for email in emails:
    prediction = model.predict([email])[0]

    if prediction == 1:
        print("🚨 Spam email detected")
    else:
        print("✅ Legit email")
