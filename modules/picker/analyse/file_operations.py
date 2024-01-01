"""
This module provides functions for file operations.
"""

import os


def write_selected_path(selected_path):
    """
    Write the selected path to a log file.

    Args:
        selected_path (str): The selected path to be written to the log file.

    Raises:
        OSError: If there is an error creating the log directory.
        IOError: If there is an error writing to the log file.
    """
    log_dir = "logs"
    log_file_name = "path.log"
    log_file_path = os.path.join(log_dir, log_file_name)

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    try:
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write(selected_path + "\n")
    except IOError as e:
        print(f"Error: {e}")
