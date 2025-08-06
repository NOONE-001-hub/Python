import os

# Specify the directory path (use '.' for current directory)
directory = '/full stack'

# Get the list of entries in the directory
entries = os.listdir(directory)

# Print each entry
for entry in entries:
    print(entry)
