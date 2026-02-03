import os, pickle, base64
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES
        )
        creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def fetch_emails(max_results=1):
    service = get_gmail_service()
    results = service.users().messages().list(
        userId='me', maxResults=max_results
    ).execute()

    emails = []

    for msg in results.get('messages', []):
        message = service.users().messages().get(
            userId='me', id=msg['id'], format='full'
        ).execute()

        body = ""
        parts = message['payload'].get('parts', [])

        for part in parts:
            if part['mimeType'] == 'text/plain':
                body += base64.urlsafe_b64decode(
                    part['body']['data']
                ).decode("utf-8")

        if body:
            emails.append(body)

    return emails
