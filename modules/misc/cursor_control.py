"""
Module Name: Misc Modules
Author: Jay Telford
Date: 30/12/23
Description: Cursor control for flashing cursor.

This module provides functions to hide and show the cursor using the curses library.
"""

import curses


def hide_cursor():
    """
    Hide the cursor on the terminal.
    """
    curses.curs_set(0)


def show_cursor():
    """
    Show the cursor on the terminal.
    """
    curses.curs_set(1)
