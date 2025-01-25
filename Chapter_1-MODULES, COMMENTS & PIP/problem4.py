import os

# Specify the directory path
directory_path = '/Users\mahamad y\Desktop\My_Documents'

try:
    # Get the list of entries in the directory
    entries = os.listdir(directory_path)
    
    # Print each entry
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory {directory_path} does not exist.")
except PermissionError:
    print(f"Permission denied to access {directory_path}.")
