#!/usr/bin/python3
""" private instance instatiation with some criteria"""


class Square:
    """instatiation of __size as integer only and greater than 0"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        assert isinstance(value, int), "size must be an integer"
        assert value >= 0, "size must be >= 0"
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            assert isinstance(value, tuple) and \
                    (value[0] >= 0 and value[1] >= 0)
            self.__position = value
        except (IndexError, TypeError, AssertionError):
            print("position must be a tuple of 2 positive integers")
            exit(1)

    def area(self):
        """ retruns the current area """
        return self.size ** 2

    def my_print(self):
        if self.position[1] > 0:
            print()
        for i in range(self.size):
            print(self.position[0] * ' ' + '#' * self.size)
        if self.size == 0:
            print()
