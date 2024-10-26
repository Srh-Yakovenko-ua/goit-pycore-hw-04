import sys
from pathlib import Path
from colorama import init, Fore

"""
Directory Structure Display Script

This script displays the directory structure of a specified path in a tree-like format 
with color-coded icons for directories and files.

Usage:

1. Activate the virtual environment:
    - On macOS/Linux:
        source venv/bin/activate
    - On Windows:
        venv\Scripts\activate

2. Install the required library:
    - With `pip`:
        pip install colorama
    - If `pip` is not available, use `pip3`:
        pip3 install colorama

3. Run the script with a directory path as an argument:
    python scan_directory.py <path_to_directory>

Example:
    python scan_directory.py /path/to/your/directory

5. Deactivate the virtual environment after running the script:
    - On macOS/Linux/Windows:
        deactivate

The script displays:
- Directories in blue with an icon 📁
- Files in green with an icon 📄
- Errors (e.g., if the path does not exist) in red

Example Output:
📁 my_project/
├── 📁 src/
│   ├── 📄 main.py
│   └── 📄 utils.py
└── 📁 assets/
    ├── 📄 logo.png
    └── 📁 icons/
        └── 📄 icon.svg
"""


# Initialize colorama for color
init(autoreset=True)


def display_directory_structure(directory_path, prefix=""):
    """
    Recursively displays the directory structure with color formatting for directories and files.

    Args:
        directory_path (str): The path to the directory.
        prefix (str): The prefix string for indentation and connectors.
    """
    path = Path(directory_path)

    # Check if the path exists and is a directory
    if not path.exists() or not path.is_dir():
        print(
            Fore.RED + f"Path '{directory_path}' does not exist or is not a directory."
        )
        return

    # Get the list of all entries in the directory
    entries = list(path.iterdir())
    entries_count = len(entries)

    for index, item in enumerate(entries):
        # Determine if the item is the last in the directory for appropriate connector
        connector = "└── " if index == entries_count - 1 else "├── "

        # If the item is a directory, display it in blue and call the function recursively
        if item.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}📁 {item.name}/")
            # Recursive call with an updated prefix to add indentation
            new_prefix = prefix + ("    " if index == entries_count - 1 else "│   ")
            display_directory_structure(item, new_prefix)
        # If the item is a file, display it in green
        else:
            print(f"{prefix}{connector}{Fore.GREEN}📄 {item.name}")


if __name__ == "__main__":
    # Check for command-line argument
    if len(sys.argv) != 2:
        print(Fore.RED + "Please specify the path to the directory.")
        sys.exit(1)

    # Get the directory path from the command-line argument
    directory_path = sys.argv[1]

    # Display the directory structure
    display_directory_structure(directory_path)
