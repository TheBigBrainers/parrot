from dotenv import load_dotenv
import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import logging

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

client = app.client

def send_message(conversation_id, message):
    client.chat_postMessage(
        channel=conversation_id,
        text=message
    )

def get_conversation_id(channel_name):
    conversation_id = None
    for response in client.conversations_list():
        if(conversation_id is not None):
            break
        for channel in response["channels"]:
            if(channel["name"] == channel_name):
                conversation_id = channel["id"]
                break
    return conversation_id

@app.event("app_mention")
def mention_handler(body, say):
    event = body["event"]
    conversation_id = event["channel"]
    say("Hi :)")
    send_message(conversation_id, "It works!")

if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()