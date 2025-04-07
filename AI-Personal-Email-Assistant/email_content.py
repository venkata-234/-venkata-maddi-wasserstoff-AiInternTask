# email_content.py

def generate_reply(email_content):
    """
    generate a custom reply based on email content
    """
    if not email_content:
        return "Sorry, I could not understand your message."  # no content

    email_content = email_content.lower()  # convert to lowercase for easier matching

    if "order" in email_content:
        return "Thank you for reaching out regarding your order! We are processing it and will update you shortly."
    elif "issue" in email_content:
        return "Sorry for the inconvenience! Our support team will assist you shortly."
    elif "help" in email_content:
        return "How can I assist you further? Please let me know your issue or question."
    else:
        return "Thank you for your email. We'll get back to you as soon as possible."  # default reply
