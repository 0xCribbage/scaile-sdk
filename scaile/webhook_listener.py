import json
import hashlib
import hmac
import time
import requests
from flask import Flask, request, jsonify
from .configs import Config
from .logging import logger

app = Flask(__name__)

# Max retries if webhook processing fails
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds

def verify_signature(payload, signature):
    """Verify the HMAC signature of the webhook request."""
    expected_signature = hmac.new(
        key=Config.WEBHOOK_SECRET.encode(),
        msg=payload,
        digestmod=hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(expected_signature, signature)

@app.route("/webhook", methods=["POST"])
def handle_webhook():
    """Handle incoming webhook requests with retries and security."""
    payload = request.data
    received_signature = request.headers.get("X-Signature")

    # Security: Verify the signature
    if not verify_signature(payload, received_signature):
        logger.error("Webhook signature verification failed!")
        return jsonify({"error": "Unauthorized"}), 403

    data = json.loads(payload)
    event_type = data.get("event")

    logger.info(f"Received webhook event: {event_type}")

    for attempt in range(MAX_RETRIES):
        try:
            # Process the webhook data (custom logic goes here)
            process_webhook(data)

            logger.info("Webhook processed successfully!")
            return jsonify({"status": "success"}), 200

        except Exception as e:
            logger.error(f"Webhook processing failed: {str(e)}")
            if attempt < MAX_RETRIES - 1:
                logger.info(f"Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                return jsonify({"error": "Failed after retries"}), 500

def process_webhook(data):
    """Custom logic to handle different webhook events."""
    if data.get("event") == "new_data":
        logger.info("Processing new data event...")
        # Add your logic here (e.g., update database)
    elif data.get("event") == "delete_data":
        logger.info("Processing delete event...")
        # Delete from database or take action
    else:
        logger.warning(f"Unknown event type: {data.get('event')}")

if __name__ == "__main__":
    app.run(port=5000, debug=Config.DEBUG)
