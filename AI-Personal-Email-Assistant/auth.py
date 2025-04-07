import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError  # for handling Slack API errors

# load environment variables
load_dotenv()

# google api scopes for reading and sending emails
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send']

def authenticate_google():
    """authenticate and create google api service"""
    creds = None
    # check if token.json exists for credentials
    if os.path.exists('token.json'):
        with open('token.json', 'r') as token:
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # if no valid credentials, authenticate user
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # refresh expired token
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=5280)  # run oauth flow

        # save credentials for next run
        with open('token.json', 'w') as token:
            json.dump({
                'token': creds.token,
                'refresh_token': creds.refresh_token,
                'token_uri': creds.token_uri,
                'client_id': creds.client_id,
                'client_secret': creds.client_secret,
                'scopes': creds.scopes
            }, token)

    # return google api service
    service = build('gmail', 'v1', credentials=creds)
    return service


def authenticate_slack():
    slack_token = os.getenv("SLACK_API_TOKEN")  # get slack token from env variable
    if not slack_token:
        raise ValueError("Slack API token not found")  # raise error if token is missing

    # initialize slack client with token
    client = WebClient(token=slack_token)
    return client
