import os
import base64
import pandas as pd
from tqdm import tqdm
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes define what access you want - here, compose & send email
SCOPES = ['https://www.googleapis.com/auth/gmail.compose', 
           'https://www.googleapis.com/auth/gmail.send']

# Load email dataset
df = pd.read_csv("generated_emails.csv")

# Authenticate Gmail
creds = None
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
        token.write(creds.to_json())

service = build("gmail", "v1", credentials=creds)

# Create draft emails
for i, row in tqdm(df.iterrows(), total=len(df)):
    to = row["EMAIL"]
    subject = row["Subject"]
    body = row["Generated Email"]

    message = MIMEText(body, "plain", "utf-8")
    message["to"] = to
    message["subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    # --- OPTION 1: Create Draft (Safe)
    draft = service.users().drafts().create(
        userId="me", body={"message": {"raw": raw}}
    ).execute()
    print(f"✅ Draft created for {to}")

    # --- OPTION 2: Send Immediately (Uncomment to use)
    # service.users().messages().send(userId="me", body={"raw": raw}).execute()
    # print(f"📨 Sent email to {to}")

print("✅ All drafts created successfully.")
