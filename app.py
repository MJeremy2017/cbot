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


# TODO test ngrok with docker
# Create an ECS cluster: You can use the AWS ECS console to create a new ECS cluster for your app.
#
# Deploy your container to ECS: You can use the AWS ECS console to deploy your container to your ECS cluster.
#
# Configure a load balancer: You can use the AWS Application Load Balancer (ALB) console to configure a load balancer for your ECS cluster.
#
# Set up an SSL certificate: You can use the AWS Certificate Manager (ACM) console to request and configure an SSL certificate for your load balancer.
#
# Create a DNS record: You can create a DNS record to point your domain name to the load balancer's public IP address.
#
# Test your HTTPS endpoint: Once everything is set up, you should be able to access your app using the public HTTPS endpoint provided by your load balancer.
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
