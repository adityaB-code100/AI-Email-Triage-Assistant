from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64, os, pickle

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def fetch_emails(max_results=5):
    service = get_gmail_service()
    results = service.users().messages().list(
        userId='me', maxResults=max_results).execute()

    messages = results.get('messages', [])
    emails = []

    for msg in messages:
        txt = service.users().messages().get(
            userId='me', id=msg['id'], format='full').execute()

        payload = txt['payload']
        parts = payload.get('parts', [])
        body = ""

        for part in parts:
            if part['mimeType'] == 'text/plain':
                data = part['body']['data']
                body += base64.urlsafe_b64decode(data).decode()

        emails.append(body)

    return emails
