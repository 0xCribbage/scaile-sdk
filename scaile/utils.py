import logging

class Utils:
    """
    Provides helper functions such as data validation, API response handling, and error logging.
    """

    @staticmethod
    def validate_data(data: dict, required_fields: list):
        """
        Validates that all required fields are present in the data.

        :param data: Dictionary to validate.
        :param required_fields: List of required field names.
        :return: True if validation passes, raises ValueError otherwise.
        """
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
        return True

    @staticmethod
    def handle_api_response(response):
        """
        Processes API responses, raising errors for unsuccessful requests.

        :param response: Response object from the API request.
        :return: Parsed JSON data for successful responses.
        :raises: Exception for failed responses with appropriate error messages.
        """
        if response.status_code >= 200 and response.status_code < 300:
            return response.json()
        else:
            try:
                error_data = response.json()
                error_message = error_data.get("message", "Unknown error")
            except Exception:
                error_message = response.text
            raise Exception(f"API request failed with status {response.status_code}: {error_message}")

    @staticmethod
    def setup_logging(log_level=logging.INFO):
        """
        Configures logging for the SDK.

        :param log_level: Logging level (e.g., logging.DEBUG, logging.INFO).
        """
        logging.basicConfig(
            level=log_level,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        logging.info("Logging is configured.")

    @staticmethod
    def log_error(error_message: str):
        """
        Logs an error message.

        :param error_message: The error message to log.
        """
        logging.error(error_message)

    @staticmethod
    def log_info(info_message: str):
        """
        Logs an informational message.

        :param info_message: The info message to log.
        """
        logging.info(info_message)
