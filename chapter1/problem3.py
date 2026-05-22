import os

# Specify the directory path
path = "/"

# Get the list of files and folders
contents = os.listdir(path)

# Print each item
for item in contents:
    print(item)