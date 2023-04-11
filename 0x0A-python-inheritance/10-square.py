#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle

class square(Retangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
        size(int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
