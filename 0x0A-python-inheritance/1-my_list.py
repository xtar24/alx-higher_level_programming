#!/usr/bin/python3
"""Defines an inherited list class Mylist."""

class Mylist(list):
    """
    MyList class that inherits from list
    """

    def print_sorted(self):
        """
        Print a list in sorted ascending order.
        """
        print(sorted(self))
