import os
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.command("/chat")
def echo(ack, say, command):
    ack()
    print(command)
    say(f"{command['text']}")


if __name__ == "__main__":
    app.start(port=3000)
