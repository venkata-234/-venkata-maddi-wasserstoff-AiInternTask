import os
from flask import Flask, jsonify, request, render_template
from auth import authenticate_google, authenticate_slack
from email_fetcher import fetch_emails
from email_content import generate_reply
from email_sender import send_email
from slack_integration import send_to_slack

app = Flask(__name__)  # initialize flask app

google_service = authenticate_google()  # authenticate google
slack_client = authenticate_slack()  # authenticate slack

def get_sender_email(headers):
    """
    extract sender's email from headers
    """
    for header in headers:
        if header['name'] == 'From':
            email_address = header['value']
            if '<' in email_address:
                email_address = email_address.split('<')[1].split('>')[0]
            return email_address
    return None

@app.route('/')  # home route
def home():
    return render_template('index.html')  # render homepage

@app.route('/process_and_reply', methods=['GET'])  # process emails
def process_and_reply():
    emails = fetch_emails(google_service)  # fetch emails
    if not emails:
        return jsonify({"message": "No new emails found."})  # no emails

    email_content = emails[0]['snippet']  # get email content
    reply = generate_reply(email_content)  # generate reply

    sender_email = get_sender_email(emails[0]['payload']['headers'])  # get sender email
    if not sender_email:
        return jsonify({"message": "No 'From' address found."})  # no sender email

    send_email(google_service, reply, sender_email)  # send reply
    send_to_slack(slack_client, "#all-my-k", reply)  # send to slack

    return jsonify({"message": "Replied and sent to Slack."})  # success message

if __name__ == "__main__":  # run app
    app.run(debug=True, host="0.0.0.0", port=5280)  # start flask server
