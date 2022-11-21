#!/usr/bin/python3
""" private instance instatiation with some criteria"""


class Square:
    """instatiation of __size as integer only and greater than 0"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        assert isinstance(value, int), "size must be an integer"
        assert value >= 0, "size must be >= 0"
        self.__size = value

    def area(self):
        """ retruns the current area """
        return self.size ** 2

    def my_print(self):
        for i in range(self.size):
            print('#' * self.size)
        if self.size == 0:
            print()
