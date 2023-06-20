#!/usr/bin/python3
"""My square module"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Create a Square
        Args: size: length of a side of Square
        """
        self.__size = size

    @property
    def size(self):
        """"The propery of size as the len of a side of Square
        Raises:
            TypeError: if size != int

