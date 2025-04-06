import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send']
def authenticate_google():
    credentials_json = os.getenv("CREDENTIALS_JSON")
    if not credentials_json:
        raise ValueError("Google credentials not found in the environment variable")
    credentials_dict = json.loads(credentials_json)
    with open("credentials.json", "w") as f:
        json.dump(credentials_dict, f)
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_console()  
    service = build('gmail', 'v1', credentials=creds)
    return service
def authenticate_slack():
    slack_token = os.getenv("SLACK_API_TOKEN")
    if not slack_token:
        raise ValueError("Slack API token not found in the environment variable")
    
    client = WebClient(token=slack_token)
    return client
