# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 00:00:19 2024
Last updated on Wed Feb 28 00:00:19 2024


"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 19:59:46 2023

@author: franc

sdev 220 spring 2023
"""


class Person():
    def __init__(self, name, age, town):
        self.name = name
        self.age = age
        self.town = town
        
    def __eq__(self, other):
        if isinstance(other, Person):
            return (self.age == other.age)
        
    def __repr__(self):
        return f"{self.name} is {self.age} years old and lives in {self.town}."