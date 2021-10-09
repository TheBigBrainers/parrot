from slackeventsapi import SlackEventAdapter
from slack_sdk.web import WebClient
from dotenv import load_dotenv
import os

load_dotenv()

slack_signing_secret = os.environ.get("SLACK_SIGNING_SECRET")
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

slack_bot_token = os.environ.get("SLACK_BOT_TOKEN")
slack_client = WebClient(slack_bot_token)

@slack_events_adapter.on("app_mention")
def handle_mentions(data):
    event = data["event"]
    user = event["user"]
    slack_client.chat_postMessage(
        channel = event["channel"],
        thread_ts = event["ts"],
        text = f"Greetings, <@{user}>! :wave:"
    )

@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

slack_events_adapter.start(port=os.environ.get("PORT"))