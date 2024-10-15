#!/usr/bin/python3
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
import os

filename = 'add_item.json'

# Check if the file exists, if it does, load the existing list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add the command line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list back to the JSON file
save_to_json_file(items, filename)
