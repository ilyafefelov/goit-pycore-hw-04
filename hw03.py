import sys
import os
from pathlib import Path
from colorama import init, Fore

def display_directory_structure(path, level=0):
    """
    Recursive function to display the directory structure with colored output.

    Args:
        path (Path): The path to the directory.
        level (int, optional): The level of indentation for the directory structure. Defaults to 0.
    """
    if not path.exists():
        print(Fore.LIGHTRED_EX + "Вказаний шлях не існує або не є директорією.")
        return

    if path.is_dir():
        # Print directory name in blue
        print(' ' * level * 2 + Fore.BLUE + str(path.relative_to(path.parent.parent)))
        # Recursively list subdirectories
        for item in path.iterdir():
            display_directory_structure(item, level + 1)
    else:
        # Print file name in magenta
        print(' ' * level * 2 + Fore.MAGENTA + str(path.relative_to(path.parent)))

def main():
    init()  # Initialize colorama
    if len(sys.argv) != 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії як аргумент.")
        return

    directory_path = Path(sys.argv[1])
    display_directory_structure(directory_path)

if __name__ == '__main__':
    main()
