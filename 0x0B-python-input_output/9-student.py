#!/usr/bin/python3
class Student:
    """Class that defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of the Student instance."""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
