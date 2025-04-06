from googleapiclient.errors import HttpError
def fetch_emails(service, label_ids=['INBOX']):
    try:
        results = service.users().messages().list(userId='me', labelIds=label_ids).execute()
        messages = results.get('messages', [])
        email_data = []
        if not messages:
            print("No messages found.")
        else:
            for message in messages[:10]:  
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                email_data.append(msg)
        return email_data
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None
