import os
from scaile.client import Client
from scaile.annotation import Annotation
from scaile.utils import handle_api_error

# Environment Variables (Typically set in the environment or .env file)
SC_AILE_API_KEY = os.getenv("SCAILE_API_KEY")

def authenticate():
    """
    Authenticate with the Scaile API using the API key.
    Returns a Client object that can be used to interact with Scaile.
    """
    try:
        client = Client(api_key=SC_AILE_API_KEY)
        print("Authentication successful!")
        return client
    except Exception as e:
        handle_api_error(e)

def create_annotation(client):
    """
    Create a new annotation using the Scaile API.
    """
    try:
        # Example data for the annotation
        data = {
            "text": "This is an example annotation",
            "labels": ["label1", "label2"]
        }
        
        # Create annotation
        annotation = Annotation.create(data)
        print(f"Annotation created successfully: {annotation}")
        return annotation
    except Exception as e:
        handle_api_error(e)

def main():
    """
    Main entry point for the quickstart example.
    """
    # Authenticate with the Scaile API
    client = authenticate()

    if client:
        # Create a new annotation
        create_annotation(client)

if __name__ == "__main__":
    main()
