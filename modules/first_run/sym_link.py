"""
This module contains functions for creating and checking symbolic links.
"""

import os
import subprocess
import curses
from modules.misc.cursor_control import hide_cursor, show_cursor


def create_symlink(stdscr):
    """
    Create a symbolic link if it doesn't exist.

    Args:
        stdscr: The curses window object.
    """
    hide_cursor()  # Hide the cursor
    symlink_path = "/usr/local/bin/ptree"
    if not os.path.islink(symlink_path):
        stdscr.addstr("Symbolic link not found. Create it? (y/n): ")
        stdscr.refresh()
        curses.echo()
        create_link = ""
        while True:
            key = stdscr.getch()
            if key == ord("\n"):  # Enter key
                break
            create_link += chr(key)
        curses.noecho()
        if create_link.lower().strip() == "y":
            try:
                subprocess.run(
                    ["sudo", "ln", "-s", os.path.abspath(__file__), symlink_path],
                    check=True,
                )
                stdscr.addstr(
                    1,
                    0,
                    f"Symbolic link created at {symlink_path}\nPress Enter to continue.",
                )
            except subprocess.CalledProcessError as e:
                stdscr.addstr(
                    1,
                    0,
                    f"Failed to create symbolic link: {e}\nPress Enter to continue.",
                )
        else:
            stdscr.addstr(1, 0, "No symbolic link created.\nPress Enter to continue.")
        stdscr.getkey()  # Wait for Enter key press before exiting
    show_cursor()  # Show the cursor


def check_and_create_symlink(stdscr):
    """
    Check if a symbolic link exists and create it if it doesn't.

    Args:
        stdscr: The curses window object.
    """
    try:
        create_symlink(stdscr)
    except OSError as e:  # Catch a specific exception
        stdscr.addstr(0, 0, f"An error occurred: {e}")
        stdscr.getkey()  # Wait for Enter key press before exiting
