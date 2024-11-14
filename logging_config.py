import logging
import os

def setup_logging():
    # Step 1: Dynamically calculate the project root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))  # Adjust path as needed
    log_file_path = os.path.join(project_root, 'logs', 'application.log')

    # Ensure the logs directory exists
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    # Step 2: Set up logging configuration dynamically
    logging.basicConfig(
        level=logging.INFO,  # Set the default logging level
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file_path),  # Set log file location dynamically
            logging.StreamHandler()  # Optional: print logs to the console
        ]
    )
