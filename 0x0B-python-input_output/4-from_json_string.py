#!/usr/bin/python3

"""This module convert json to data structures"""

import json


def from_json_string(my_str):
    """Return an object"""
    return (json.loads(my_str))
