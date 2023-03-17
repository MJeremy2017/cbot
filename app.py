import logging
from slack_bolt import App

logging.basicConfig(level=logging.DEBUG)

app = App()


@app.middleware  # or app.use(log_request)
def log_request(logger, body, next):
    logger.debug(body)
    return next()


@app.command("/chat")
def chatgpt(ack, say, body):
    # TODO add gpt
    print('s', say)
    print('b', body)
    user_id = body["user_id"]
    ack(f"Hi <@{user_id}>!")



@app.error
def global_error_handler(error, body, logger):
    logger.exception(error)
    logger.info(body)


if __name__ == "__main__":
    app.start(3000)