from slack_sdk.errors import SlackApiError

def get_channel_id(slack_client, channel_name):
    """
    fetch channel id using channel name
    """
    try:
        response = slack_client.conversations_list()  # get list of channels
        channels = response['channels']

        for channel in channels:
            if channel['name'] == channel_name:  # check for matching channel
                return channel['id']

        print(f"Channel '{channel_name}' not found.")  # if not found
        return None

    except SlackApiError as e:
        print(f"Error fetching channel list: {e.response['error']}")  # error handling
        return None


def send_to_slack(slack_client, channel, message):
    try:
        if channel.startswith('#'):  # check if channel is by name
            channel_id = get_channel_id(slack_client, channel[1:])  # get channel id
            if not channel_id:
                print(f"Error: Channel '{channel}' not found.")
                return
            channel = channel_id  # use channel id for sending message

        response = slack_client.chat_postMessage(  # send message
            channel=channel,
            text=message
        )

        print(f"Message sent to Slack: {response['message']['text']}")  # confirm send

    except SlackApiError as e:
        print(f"Error sending message to Slack: {e.response['error']}")  # error handling
