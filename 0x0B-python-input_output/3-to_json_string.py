#!/usr/bin/python3

"""
This module convert data structures
or objects into a format
"""

import json


def to_json_string(my_obj):
    """Method return the JSON file"""
    json_obj = json.dumps(my_obj)
    return json_obj
