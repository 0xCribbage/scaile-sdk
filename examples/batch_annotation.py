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

def create_batch_annotations(client, annotations_data):
    """
    Create a batch of annotations using the Scaile API.
    """
    try:
        created_annotations = []
        for data in annotations_data:
            annotation = Annotation.create(data)
            created_annotations.append(annotation)
            print(f"Annotation created successfully: {annotation}")
        return created_annotations
    except Exception as e:
        handle_api_error(e)

def main():
    """
    Main entry point for the batch annotation example.
    """
    # Authenticate with the Scaile API
    client = authenticate()

    if client:
        # Example batch annotation data
        annotations_data = [
            {"text": "First batch annotation", "labels": ["label1", "label2"]},
            {"text": "Second batch annotation", "labels": ["label3", "label4"]},
            {"text": "Third batch annotation", "labels": ["label5", "label6"]},
        ]
        
        # Create batch annotations
        create_batch_annotations(client, annotations_data)

if __name__ == "__main__":
    main()
