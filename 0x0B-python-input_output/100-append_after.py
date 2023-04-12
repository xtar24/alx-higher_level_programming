#!/usr/bin/python3
"""Defines a text file insertin function."""


def append_after(filename="", search_string="", new_string=""):
    """insert text after each line containing a given string in a file.
    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): the string to imsert.
    """
    text =""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text =+ new_string
        with open(filename, "w") as w:
            w.write(text)
