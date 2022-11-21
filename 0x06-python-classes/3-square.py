#!/usr/bin/python3
""" private instance instatiation with some criteria"""


class Square:
    """instatiation of __size as integer only and greater than 0"""
    def __init__(self, size=0):
        assert isinstance(size, int), "size must be an integer"
        assert size >= 0, "size must be >= 0"
        self.__size = size

    def area(self):
        """ retruns the current area """
        return self.__size ** 2
