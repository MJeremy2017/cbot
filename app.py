import logging
from slack_bolt import App
import openai
import os

logging.basicConfig(level=logging.DEBUG)

app = App()
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.middleware
def log_request(logger, body, next):
    logger.debug(body)
    return next()


# TODO wrap in docker
@app.command("/chat")
def chatgpt(ack, say, body):
    ack("Coffee is brewing ...")
    user_id = body["user_id"]
    text = body['text']
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.6,
        max_tokens=1000
    )
    say(f"Hi <@{user_id}>\n {response.choices[0].text}")


@app.error
def global_error_handler(error, body, logger):
    logger.exception(error)
    logger.info(body)


if __name__ == "__main__":
    app.start(3000)
