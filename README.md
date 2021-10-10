# Parrot: Our Primary Slack Bot :parrot:
:warning: This is currently a work in progress.
In our Slack workspace, essentially the headquarters of Big Brainers, Parrot will be able to execute the following:
- :birthday: Wish happy birthday to volunteers on their special day and sometimes serve virtual cake
- :wave: Help introduce new volunteers
- :information_source: Help volunteers access relevant and important information like how many hours they've completed
- :tada: Announce volunteer and organization-wide milestones

And more! This list is quite vulnerable to growth, so please contribute by filing a pull request.

## Development :computer:
After forking and/or cloning this repository, in the repository's topmost directory:
1. Create a Python virtual environment in the directory

`python -m venv .`

2. Install required packages using `pip`

`pip install -r requirements.txt`

3. Create a `.env` file to set up the necessary environment variables (ask an admin for the values)
```
SLACK_BOT_TOKEN=<VALUE>
SLACK_SIGNING_SECRET=<VALUE>
SLACK_APP_TOKEN=<VALUE>
```
4. Ensure your Slack app configuration (manifest, scopes, etc.) is correct at api.slack.com/apps
5. Run the Slack bot!

`python main.py`

### Helpful Resources
- https://api.slack.com/methods
- https://api.slack.com/events
- https://api.slack.com/apis/connections/socket