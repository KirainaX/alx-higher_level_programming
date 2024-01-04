#!/usr/bin/python3

# Define a class named Rectangle
class Rectangle:
    # Constructor method to initialize the width and height attributes
    def __init__(self, width=0, height=0):
        self.height = height  # Set the height attribute using the height parameter
        self.width = width    # Set the width attribute using the width parameter

    # Getter method for the width attribute
    @property
    def width(self):
        return self.__width

    # Getter method for the height attribute
    @property
    def height(self):
        return self.__height

    # Setter method for the width attribute, with input validation
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")  # Raise an error if width is not an integer
        elif value < 0:
            raise ValueError("width must be >= 0")       # Raise an error if width is negative
        else:
            self.__width = value  # Set the width attribute if validation passes

    # Setter method for the height attribute, with input validation
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer") # Raise an error if height is not an integer
        elif value < 0:
            raise ValueError("height must be >= 0")      # Raise an error if height is negative
        else:
            self.__height = value # Set the height attribute if validation passes
