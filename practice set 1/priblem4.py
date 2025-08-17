import os

# Specify the directory (use '.' for current directory)
directory = "/"

try:
    # Get the list of all files and directories
    contents = os.listdir(directory)
    
    print(f"Contents of directory '{directory}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"Error: Directory '{directory}' not found.")

except PermissionError:
    print(f"Error: Permission denied to access '{directory}'.")

