#!/usr/bin/python3
import json
"""
This module convert data structures
or objects into a format
"""


def to_json_string(my_obj):
    """Method return the JSON file"""
    json_obj = json.dumps(my_obj)
    return json_obj
