"""Script to lower case all the folder titles and replace spaces and duts by underscores.
"""
import os
import sys

# Define the main function
def main(dir_path):
    # Get the list of folders names
    folders = os.listdir(dir_path)

    # Loop through the folders in the directory
    for folder in folders:
        # Get the old folder name
        old_name = os.path.join(dir_path, folder)
        # Lower case the folder name and replace spaces with underscores
        new_name = os.path.join(dir_path, folder.lower().replace(" ", "_").replace(".", "_"))
        # Rename the folder
        os.rename(old_name, new_name)

    print("INFO: Renaming is done!")
    # Print the list of folders names
    print(f"INFO: This is the list of folders modified")
    print(f"INFO: {folders}")

# Check if the script is run directly
if __name__ == "__main__":
    # Check if the directory path is provided as an argument
    if len(sys.argv) > 1:
        # Get the directory path from the first argument
        dir_path = sys.argv[1]
        # Call the main function with the directory path
        main(dir_path)
    else:
        # Print a suggestion about the accepted arguments
        print("Usage: python script.py dir_path")
        print("dir_path: The path of the directory that contains the folders to be renamed")


