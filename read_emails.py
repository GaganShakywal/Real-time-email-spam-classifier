import base64
from gmail_auth import gmail_authenticate

def get_unread_emails():
    service = gmail_authenticate()

    results = service.users().messages().list(
        userId='me',
        labelIds=['INBOX', 'UNREAD'],
        maxResults=5
    ).execute()

    messages = results.get('messages', [])
    emails = []

    for msg in messages:
        msg_data = service.users().messages().get(
            userId='me',
            id=msg['id'],
            format='full'
        ).execute()

        payload = msg_data['payload']
        headers = payload.get('headers', [])

        sender = subject = ""

        # 🔹 Extract headers
        for h in headers:
            if h['name'] == 'From':
                sender = h['value']
            if h['name'] == 'Subject':
                subject = h['value']

        # 🔹 Extract body
        body = ""
        if 'parts' in payload:
            for part in payload['parts']:
                if part['mimeType'] == 'text/plain':
                    data = part['body'].get('data')
                    if data:
                        body = base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')
        else:
            data = payload['body'].get('data')
            if data:
                body = base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')

        emails.append({
            "from": sender,
            "subject": subject,
            "body": body
        })

    return emails
