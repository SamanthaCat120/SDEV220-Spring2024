# -*- coding: utf-8 -*-
"""
custom class Dragon()

"""

class Dragon():
    def __init__(self, name, age, breed, color, hunger, mood):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.hunger = hunger
        self.mood = mood

    def feed(self):
        self.hunger -= 1
        if self.hunger <= 0:
            print("I'm full")
        else:
            print("I'm still hungry")
    
    