# from flask import Flask, request
#
# app = Flask(__name__)
#
# # TODO try flask
#
# @app.route('/api/v1/submit', methods=['POST'])
# def submit_data():
#     data = request.get_json()
#     return 'Data received: {}'.format(data)
#
#
# if __name__ == '__main__':
#     app.run(port=3000)
#
#
import os
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.message("hello")
def echo(message, say):
    print(message)
    say(f"Yes <@{message['user']}>")


if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
