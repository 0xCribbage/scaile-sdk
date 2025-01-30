import os
from scaile.client import Client
from scaile.storage import Storage  # Handles file storage (annotation tasks)
from scaile.rewards import Rewards  # Handles contributor rewards
from scaile.utils import handle_api_error

# Load API Key from environment variables
SCAILE_API_KEY = os.getenv("SCAILE_API_KEY")

def authenticate():
    """
    Authenticate with the Scaile API using the API key.
    Returns a Client object that can be used to interact with Scaile.
    """
    try:
        client = Client(api_key=SCAILE_API_KEY)
        print("✅ Authentication successful!")
        return client
    except Exception as e:
        handle_api_error(e)
        return None

class DataLabelingManager:
    """
    Manages the lifecycle of annotation tasks, including uploading and retrieving tasks.
    """
    def __init__(self, client, project_id):
        self.client = client
        self.project_id = project_id
        self.storage = Storage(client)

    def upload_annotation_task(self, file_path):
        """Uploads a new annotation task file."""
        try:
            upload_response = self.storage.upload_data(self.project_id, file_path)
            print(f"📂 File uploaded successfully: {upload_response}")
            return upload_response.get("file_id")
        except Exception as e:
            handle_api_error(e)

    def get_task_details(self, file_id):
        """Retrieves metadata about an uploaded task file."""
        try:
            task_details = self.storage.retrieve_data(self.project_id, file_id)
            print(f"📜 Task details retrieved: {task_details}")
            return task_details
        except Exception as e:
            handle_api_error(e)

    def list_tasks(self):
        """Lists all annotation task files in the project."""
        try:
            task_list = self.storage.list_files(self.project_id)
            print(f"📋 Task list: {task_list}")
            return task_list
        except Exception as e:
            handle_api_error(e)

    def delete_task(self, file_id):
        """Deletes an annotation task file."""
        try:
            delete_response = self.storage.delete_data(self.project_id, file_id)
            print(f"❌ Task deleted successfully: {delete_response}")
        except Exception as e:
            handle_api_error(e)

class RewardManager:
    """
    Manages the calculation and distribution of rewards for annotators.
    """
    def __init__(self, client, project_id):
        self.client = client
        self.project_id = project_id
        self.rewards = Rewards(client)

    def calculate_annotator_rewards(self, contributor_id):
        """Calculates the reward for a contributor based on completed tasks."""
        try:
            reward_data = self.rewards.calculate_rewards(self.project_id, contributor_id)
            print(f"💰 Calculated rewards for contributor {contributor_id}: {reward_data}")
            return reward_data
        except Exception as e:
            handle_api_error(e)

    def distribute_rewards(self, contributor_id, amount):
        """Distributes a reward to an annotator."""
        try:
            distribution_data = {"distributions": [{"contributor_id": contributor_id, "amount": amount}]}
            response = self.rewards.distribute_rewards(self.project_id, distribution_data)
            print(f"🎁 Reward of {amount} distributed to contributor {contributor_id}: {response}")
        except Exception as e:
            handle_api_error(e)

    def list_all_rewards(self):
        """Lists all rewards distributed in the project."""
        try:
            all_rewards = self.rewards.list_all_rewards(self.project_id)
            print("🏆 All rewards in the project:", all_rewards)
            return all_rewards
        except Exception as e:
            handle_api_error(e)

def main():
    """
    Main function demonstrating data labeling task uploads and reward distributions.
    """
    client = authenticate()
    if not client:
        return

    # Define project and contributor information
    project_id = "ml_annotation_project_001"
    contributor_id = "annotator_456"
    file_path = "annotation_task_01.txt"  # Example task file

    # Initialize managers
    labeling_manager = DataLabelingManager(client, project_id)
    reward_manager = RewardManager(client, project_id)

    print("\n--- 🔹 Uploading Annotation Task 🔹 ---")
    file_id = labeling_manager.upload_annotation_task(file_path)

    if file_id:
        print("\n--- 🔹 Retrieving Task Details 🔹 ---")
        labeling_manager.get_task_details(file_id)

        print("\n--- 🔹 Listing All Tasks 🔹 ---")
        labeling_manager.list_tasks()

        print("\n--- 🔹 Deleting Task 🔹 ---")
        labeling_manager.delete_task(file_id)

    print("\n--- 🔹 Calculating Contributor Rewards 🔹 ---")
    reward_manager.calculate_annotator_rewards(contributor_id)

    print("\n--- 🔹 Distributing Contributor Rewards 🔹 ---")
    reward_manager.distribute_rewards(contributor_id, 100)

    print("\n--- 🔹 Listing All Rewards 🔹 ---")
    reward_manager.list_all_rewards()

if __name__ == "__main__":
    main()
