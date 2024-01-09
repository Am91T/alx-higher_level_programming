#!/usr/bin/python3
"""This module appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file."""
    with open(filename, 'a', encoding="UTF8") as file:
        return file.write(text)
