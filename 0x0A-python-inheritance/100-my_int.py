#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """override == operator with != behaviour."""
        return self.real != value

    def __ne__(self, value):
        """overrode != opeartor with == behaviour."""
        return self.real == value
