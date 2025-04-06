from slack_sdk.errors import SlackApiError
def send_to_slack(slack_client, channel, message):
    try:
        response = slack_client.chat_postMessage(
            channel=channel,
            text=message
        )
        print(f"Message sent to Slack: {response['ts']}")
    except SlackApiError as e:
        print(f"Error sending message to Slack: {e.response['error']}")
