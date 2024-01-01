"""
This module provides functions for navigating directories.
"""

import os
import curses


def navigate_directory(current_dir, cursor_y, prev_dirs, key):
    """
    Navigates the directory based on the given key.

    Args:
        current_dir (str): The current directory path.
        cursor_y (int): The current cursor position.
        prev_dirs (list): List of previous directory paths.
        key (int): The key pressed.

    Returns:
        tuple: A tuple containing the updated current directory, cursor position, and list of files.
    """
    files = [f for f in os.listdir(current_dir) if not f.startswith(".")]

    if key == curses.KEY_DOWN:
        cursor_y = min(cursor_y + 1, len(files) - 1)
    elif key == curses.KEY_UP:
        cursor_y = max(cursor_y - 1, 0)
    elif key == curses.KEY_LEFT:
        if prev_dirs:
            current_dir = prev_dirs.pop()
            cursor_y = 0
    elif key == curses.KEY_RIGHT:
        selected_dir = os.path.join(current_dir, files[cursor_y])
        if os.path.isdir(selected_dir):
            prev_dirs.append(current_dir)
            current_dir = selected_dir
            cursor_y = 0

    return current_dir, cursor_y, files
