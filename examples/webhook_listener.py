import os
import json
from scaile.client import Client
from scaile.annotation import Annotation
from scaile.utils import handle_api_error

# Environment Variables (Typically set in the environment or .env file)
SC_AILE_API_KEY = os.getenv("SCAILE_API_KEY")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

def verify_webhook_signature(request_body, signature):
    """
    Verify the webhook signature to ensure the request is from Scaile.
    This can be done using a secret key that Scaile provides.
    """
    # Implement signature verification logic, this is a placeholder.
    return signature == WEBHOOK_SECRET

def process_webhook_event(event_data):
    """
    Handle the incoming webhook event by parsing and processing it.
    You can customize this function to handle different types of events.
    """
    try:
        event = json.loads(event_data)
        # Example: Handle a new annotation created event
        if event.get("type") == "annotation_created":
            annotation_id = event.get("data", {}).get("id")
            annotation = Annotation.get(annotation_id)
            print(f"New annotation created: {annotation}")
        else:
            print(f"Received unrecognized event type: {event.get('type')}")
    except Exception as e:
        handle_api_error(e)

def listen_for_webhooks():
    """
    Main function to simulate listening for incoming webhooks.
    In practice, this would be run on a server with a web framework like Flask.
    """
    from flask import Flask, request, abort

    app = Flask(__name__)

    @app.route("/webhook", methods=["POST"])
    def webhook():
        # Verify the webhook signature
        signature = request.headers.get("X-Signature")
        if not verify_webhook_signature(request.data, signature):
            abort(400, "Invalid signature")

        # Process the webhook event
        process_webhook_event(request.data)
        return "", 200

    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    listen_for_webhooks()
