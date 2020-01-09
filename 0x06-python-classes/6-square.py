#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if not isinstance(self.__position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(self.__position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        elif isinstance(value, int):
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(self.__position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(self.__position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.__position[1] != 0:
            for k in range(self.__position[1]):
                print()
        if self.__size != 0:
            for i in range(self.__size):
                if self.__position[0] != 0:
                    for l in range(self.__position[0]):
                        print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            if self.__position[1] != 0:
                for l in range(self.__position[0]):
                    print(" ", end="")
            print()
