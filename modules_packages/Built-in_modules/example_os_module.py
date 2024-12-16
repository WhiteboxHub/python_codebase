import os

# Get the current working directory
print(os.getcwd())  # Output: /path/to/current/directory

# List files and directories in the current directory
print(os.listdir())  # Output: ['file1.py', 'file2.py', 'directory1']

# Create a new directory
os.mkdir("new_directory")
