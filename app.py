"""
Module Name: Main App
Author: Jay Telford
Date: 30/12/23 - v0.0.001-alpha
Description: Primary app that is run for the program.

This module contains the main function that serves as the entry point for the program. 
It uses the curses library to create a terminal-based user interface. 
The main function displays the contents of the current directory, 
allows the user to navigate through directories, 
and writes the selected path to a file.

Functions:
- main(stdscr): The main function that runs the program.

Usage:
To run the program, execute the following command:
    python app.py
"""

import os
import curses
from modules.picker.analyse.navigation import navigate_directory
from modules.picker.analyse.display import display_directory_contents
from modules.picker.analyse.file_operations import write_selected_path
from modules.first_run.sym_link import check_and_create_symlink


def main(stdscr):
    """
    The main function that runs the program.

    Args:
        stdscr: The curses screen object.
    """

    # Check for symbolic link
    check_and_create_symlink(stdscr)

    # Set up the screen
    current_dir = os.path.expanduser("~")
    cursor_y = 0
    prev_dirs = []

    while True:
        display_directory_contents(stdscr, current_dir, cursor_y)

        key = stdscr.getch()
        if key == ord("q"):
            break
        if key == ord("\n"):
            write_selected_path(current_dir)

        current_dir, cursor_y, _ = navigate_directory(
            current_dir, cursor_y, prev_dirs, key
        )


if __name__ == "__main__":
    curses.wrapper(main)
