from flask import Flask, jsonify
from auth import authenticate_google, authenticate_slack
from email_fetcher import fetch_emails
from email_processor import generate_reply
from email_sender import send_email
from slack_integration import send_to_slack

app = Flask(__name__)
google_service = authenticate_google()
slack_client = authenticate_slack()
@app.route('/process_and_reply', methods=['GET'])
def process_and_reply():
    emails = fetch_emails(google_service)
    if not emails:
        return jsonify({"message": "No new emails found."})
    email_content = emails[0]['snippet']  
    reply = generate_reply(email_content)
    send_email(google_service, reply, emails[0]['payload']['headers'][0]['value'])
    send_to_slack(slack_client, "#general", reply)
    return jsonify({"message": "Replied to the email and sent a notification to Slack."})
if __name__ == "__main__":
    app.run(debug=True)
