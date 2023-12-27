"""Script to lower case all the folder titles and replace spaces and duts by underscores.
"""
import os
import sys

# Define the main function
def main(dir_path: str, recursively_flag: str = "-n") -> None:
    if recursively_flag == "-y":
        # Loop through the directory tree
        modified_dirs = []
        for root, dirs, files in os.walk(dir_path):
            # Loop through the folders in the current directory
            for folder in dirs:
                # Get the old folder name
                old_name = os.path.join(root, folder) # Changed dir_path to root
                # Lower case the folder name and replace spaces with underscores
                new_name = os.path.join(root, folder.lower().replace(" ", "_").replace(".", "_").replace(",","_").replace("__","-").replace("--","-")) # Changed dir_path to root
                # Rename the folder
                os.rename(old_name, new_name)
                modified_dirs.append(old_name)
        
        print("INFO: Renaming is done!")
        # Print the list of folders names
        print(f"INFO: This is the list of folders modified")
        print(f"INFO: {modified_dirs}")
        return None # Moved outside the loop
        
    
    # Get the list of folders names
    folders = os.listdir(dir_path)

    # Loop through the folders in the directory
    for folder in folders:
        # Get the old folder name
        old_name = os.path.join(dir_path, folder)
        # Lower case the folder name and replace spaces with underscores
        new_name = os.path.join(dir_path, folder.lower().replace(" ", "_").replace(".", "_").replace(",","_").replace("__","-").replace("--","-"))
        # Rename the folder
        os.rename(old_name, new_name)

    print("INFO: Renaming is done!")
    # Print the list of folders names
    print(f"INFO: This is the list of folders modified")
    print(f"INFO: {folders}")
    return None

# Check if the script is run directly
if __name__ == "__main__":
    # Check if the directory path is provided as an argument
    if len(sys.argv) < 1 or len(sys.argv) > 2:
        # Get the directory path from the first argument
        dir_path = sys.argv[1]
        recursive_flag = sys.argv[2]
        # Call the main function with the directory path
        main(dir_path, recursive_flag)
    else:
        # Print a suggestion about the accepted arguments
        print("ERROR")
        print("Usage: python rename_folders.py dir_path -y(optional)")
        print("dir_path: The path of the directory that contains the folders to be renamed.")
        print("-y: If you want to rename the directories inside recursively.")
        print("-n: If you want to rename only the immediate directories inside the folder.")


