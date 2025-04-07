from googleapiclient.errors import HttpError

def fetch_emails(service, label_ids=['INBOX']):
    try:
        # fetch email list from the specified label
        results = service.users().messages().list(userId='me', labelIds=label_ids).execute()
        messages = results.get('messages', [])

        email_data = []
        if not messages:
            print("No messages found.")  # no messages
        else:
            for message in messages[:10]:  # limit to 10 emails
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                email_data.append(msg)
        return email_data
    except HttpError as error:
        print(f'An error occurred: {error}')  # error handling
        return None
