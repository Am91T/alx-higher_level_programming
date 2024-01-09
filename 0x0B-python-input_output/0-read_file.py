#!/usr/bin/python3
"""Module to read the content of the file"""

def read_file(filename=""):
    """
    Read the contents of a text file and print it to the console.

    Args:
        filename (str): The name of the text file to be read. Default is an empty string.

    Returns:
        None

    Prints the content of the file to the standard output (console).
    """
    with open(filename, 'r') as file:
        print(file.read())
