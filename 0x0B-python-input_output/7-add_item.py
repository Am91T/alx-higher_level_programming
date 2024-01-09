#!/usr/bin/python3

"""
Script to add command-line arguments to a JSON file.

Example:
    ./script_name.py item1 item2
"""

import sys
import os

arg_list = sys.argv[1:]

save_JSON = __import__('5-save_to_json_file').save_to_json_file
load_JSON = __import__('6-load_from_json_file').load_from_json_file

list_arg = []
if os.path.exists('add_item.json'):
    list_arg = load_JSON('add_item.json')

save_JSON(list_arg + arg_list, "add_item.json")
