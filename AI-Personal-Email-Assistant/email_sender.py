from googleapiclient.discovery import build
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64

def send_email(service, message_body, to_email):
    try:
        message = MIMEMultipart()  # create email message
        message['to'] = to_email  # recipient email
        message['subject'] = 'Re: Your email subject'  # subject line

        msg = MIMEText(message_body)  # add message body
        message.attach(msg)

        # encode message to raw format for sending
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        send_message = service.users().messages().send(userId="me", body={'raw': raw_message}).execute()  # send email
        print(f'Sent message to {to_email} Message Id: {send_message["id"]}')
    except Exception as error:
        print(f'An error occurred: {error}')  # error handling
