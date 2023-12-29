import os
import curses

def browse_directory(stdscr, current_dir):
    cursor_y = 0
    selected_dir = None
    SELECTED_PATH = ""
    prev_dirs = []

    while True:
        stdscr.clear()

        # Get the terminal size
        height, width = stdscr.getmaxyx()

        # Display the current directory path centered at the top
        dir_path_str = f"Current Directory: {current_dir}"
        dir_path_x = max(0, (width - len(dir_path_str)) // 2)
        stdscr.addstr(1, dir_path_x, dir_path_str)  # Directory path at y = 1

        # List non-dot files and directories
        files = [f for f in os.listdir(current_dir) if not f.startswith('.')]

        # Handle the case when the files list is empty
        if files:
            list_width = max(len(file) for file in files) + 4  # +4 for spacing and prefix
        else:
            list_width = 4  # Default width when there are no files

        # Calculate the starting x position to center the list
        start_x = max(0, (width - list_width) // 2)

        # Calculate the height of the list and determine the starting y position to center it vertically
        list_height = len(files)
        start_y = max(2, (height - list_height - 3) // 2)  # -3 for directory path and instructions

        for i, file in enumerate(files):
            try:
                # Encode the file name to UTF-8
                file_encoded = file.encode("utf-8")
                path = os.path.join(current_dir, file)
                
                # Display the prefix in the prefix column
                prefix = "D" if os.path.isdir(path) else "F"
                stdscr.addstr(start_y + i, start_x, prefix)

                # Display the file or directory name in the main column
                stdscr.addstr(start_y + i, start_x + 4, file_encoded.decode("utf-8"))  # +4 for spacing

                if i == cursor_y:
                    # Highlight the selected item
                    file_name_length = len(file_encoded.decode("utf-8"))
                    stdscr.chgat(start_y + i, start_x + 4, file_name_length, curses.A_REVERSE)
            except curses.error:
                pass  # Handle any curses errors (e.g., text too long)

        # Updated instructions with "Enter to Save"
        instructions = "Use Arrow Keys to Navigate  |  'Left' to Go Up  |  'Right' to Go Down  |  'Enter' to Save  |  'q' to Quit"
        stdscr.addstr(height - 2, max(0, (width - len(instructions)) // 2), instructions)

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_DOWN:
            # Move the cursor down
            if cursor_y < len(files) - 1:
                cursor_y += 1
        elif key == curses.KEY_UP:
            # Move the cursor up
            if cursor_y > 0:
                cursor_y -= 1
        elif key == curses.KEY_LEFT:
            # Left arrow key - navigate up the directory structure
            if prev_dirs:
                current_dir = prev_dirs.pop()
                cursor_y = 0
        elif key == curses.KEY_RIGHT:
            # Right arrow key - navigate down the directory structure
            selected_dir = os.path.join(current_dir, files[cursor_y])
            if os.path.isdir(selected_dir):
                prev_dirs.append(current_dir)
                current_dir = selected_dir
                cursor_y = 0
        elif key == ord('q'):
            # 'q' key - quit the program
            break
        elif key == ord('\n'):  # Enter key
            # Save the current directory path to SELECTED_PATH and log it
            SELECTED_PATH = current_dir
            log_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'path.log')
            try:
                with open(log_file_path, 'a') as log_file:
                    log_file.write(SELECTED_PATH + '\n')
            except Exception as e:
                # Print the exception to stdscr or handle it as needed
                stdscr.addstr(0, 0, f"Error: {e}")

def main(stdscr):
    curses.curs_set(0)  # Set cursor style to 0 (invisible)
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(True)

    home_dir = os.path.expanduser("~")
    browse_directory(stdscr, home_dir)

    # Set the cursor style to normal (visible) before exiting
    curses.curs_set(1)

if __name__ == "__main__":
    curses.wrapper(main)

