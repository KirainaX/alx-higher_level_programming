#!/usr/bin/python3
'''Module for BaseGeometry class.'''


class BaseGeometry:
    '''A BaseGeometry class.'''
    def area(self):
        '''Method to compute this area.'''
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        '''Method for validating the value.'''
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
