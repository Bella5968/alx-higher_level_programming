#!/usr/bin/python3
""" Student module
"""


class Student:
    """ Student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieve a dictionary representation of a Student instance.
        If attrs is a list of strings, only attribute names contained in this
        list must be retrieved. Otherwise, all attributes must be retrieved.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
