#!/usr/bin/python3

"""This module saves a Python object to a JSON file"""

import json


def save_to_json_file(my_obj, filename):
    """Saves a Python object to a JSON file."""
    with open(filename, 'w', encoding='UTF-8') as file:
        file.write(json.dumps(my_obj))
