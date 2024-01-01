"""
This module provides functions for displaying the contents of a directory 
in a terminal-based user interface.
"""

import os
import curses


def display_directory_contents(stdscr, current_dir, cursor_y):
    """
    Display the contents of the current directory in a terminal-based user interface.

    Args:
        stdscr (curses._CursesWindow): The curses window object.
        current_dir (str): The current directory path.
        cursor_y (int): The cursor position.
    """

    stdscr.clear()
    height, width = stdscr.getmaxyx()
    display_directory_path(stdscr, current_dir, width)
    files = get_non_dot_files(current_dir)
    start_x, start_y = calculate_start_positions(width, height, files)
    position = {"start_x": start_x, "start_y": start_y, "cursor_y": cursor_y}
    display_files(stdscr, files, position, current_dir)
    display_navigation_instructions(stdscr, height, width)
    stdscr.refresh()


def display_directory_path(stdscr, current_dir, width):
    """
    Display the current directory path.

    Args:
        stdscr (curses._CursesWindow): The curses window object.
        current_dir (str): The current directory path.
        width (int): The width of the terminal window.

    Returns:
        None
    """
    dir_path_str = f"Current Directory: {current_dir}"
    dir_path_x = max(0, (width - len(dir_path_str)) // 2)
    stdscr.addstr(1, dir_path_x, dir_path_str)


def get_non_dot_files(current_dir):
    """
    Get a list of non-dot files in the given directory.

    Args:
        current_dir (str): The path to the directory.

    Returns:
        list: A list of non-dot files in the directory.
    """
    return [f for f in os.listdir(current_dir) if not f.startswith(".")]


def calculate_start_positions(width, height, files):
    """
    Calculate the start positions for displaying files.

    Args:
        width (int): The width of the terminal window.
        height (int): The height of the terminal window.
        files (list): A list of files in the directory.

    Returns:
        tuple: The start positions (start_x, start_y).
    """
    start_x = max(0, (width - max(len(file) for file in files) - 4) // 2)
    start_y = max(2, (height - len(files) - 3) // 2)
    return start_x, start_y


def display_files(stdscr, files, position, current_dir):
    """
    Display the files in the current directory.

    Args:
        stdscr (curses._CursesWindow): The curses window object.
        files (list): A list of files in the directory.
        position (dict): A dictionary with keys 'start_x', 'start_y', and 'cursor_y'.
        current_dir (str): The current directory.
    """
    start_x = position["start_x"]
    start_y = position["start_y"]
    cursor_y = position["cursor_y"]
    for i, file in enumerate(files):
        try:
            file_encoded = file.encode("utf-8")
            path = os.path.join(current_dir, file)
            prefix = "D" if os.path.isdir(path) else "F"
            stdscr.addstr(start_y + i, start_x, prefix)
            stdscr.addstr(start_y + i, start_x + 4, file_encoded.decode("utf-8"))
            if i == cursor_y:
                file_name_length = len(file_encoded.decode("utf-8"))
                stdscr.chgat(
                    start_y + i, start_x + 4, file_name_length, curses.A_REVERSE
                )
        except curses.error:
            pass


def display_navigation_instructions(stdscr, height, width):
    """
    Display navigation instructions on the screen.

    Args:
        stdscr (curses.window): The curses window object.
        height (int): The height of the screen.
        width (int): The width of the screen.

    Returns:
        None
    """
    instructions = (
        "Use Arrow Keys to Navigate | 'Left' to Go Up | 'Right' to Go Down | "
        "'Enter' to Select | 'q' to Quit"
    )
    stdscr.addstr(height - 2, max(0, (width - len(instructions)) // 2), instructions)
