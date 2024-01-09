#!/usr/bin/python3
"""This module create an object file from a JSON"""

import json


def load_from_json_file(filename):
    """Load a json file"""
    with open(filename, 'r') as file:
        return json.load(file)
