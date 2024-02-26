# -*- coding: utf-8 -*-
"""
Last updated on Sat Feb 17 17:18:03 2024

@author: Samantha Lopez


flute python custom class


"""

import random

in_tune = 5

class Flute:
    def __init__(self, key, material, manufacturer, is_openhole):
        self.__key = key
        self.__material = material
        self.__manufactuerer = manufacturer
        self.__is_openhole = True
        
    def get_key(self):
        return self.__key
    
    def set_key(self, new_key):
        self.__key = new_key
    
    def get_material(self):
        return self.__material
    
    def set_material(self, new_material):
        self.__material = new_material
    
    def get_manufacturer(self):
        return self.__manufacturer
    
    def set_manufacturer(self, new_manufacturer):
        self.__manufacturer = new_manufacturer
    
    def get_is_openhole(self):
        return self.__is_openhole
    
    def set_is_openhole(self, new_is_openhole):
        self.__is_openhole = new_is_openhole
    
    def play(self):
        in_tune = random.randint(1, 10)
        
        if in_tune in (1, 2, 3):
            print(f"You're a little flat; pull out.")
                
        elif in_tune in (4, 5, 6, 7):
            print(f"You're in tune!")
                
        else:
            print(f"You're a little sharp; push in.")
            
        if self.__is_openhole:
            print(f"and your tone has improved!")

        
    def play(self):
        in_tune = random.randint(1,10)
        
        if in_tune in (1, 2, 3):
            print("You're a little flat; pull out.")
                
        elif in_tune in (4, 5, 6, 7):
            print("You're in tune!")
                
        else:
            print("You're a little sharp; push in.")
            
        if self.__is_openhole == True:
                print("and your tone has improved!")
                
        else:
            pass
                
            
# Example usage
my_flute=Flute(key='C', material='silver-plated', manufacturer='Yamaha', is_openhole=True)

my_flute.play()

# Using setter methods to set the material to "platinum" and the manufacturer to "Miyazawa"
my_flute.set_material('platinum')
my_flute.set_manufacturer('Miyazawa')

# Verify changes using getter methods
print(my_flute.get_material())
print(my_flute.get_manufacturer())

if my_flute.get_material() == 'platinum':
    print(f'You could purchase a small house with that flute.')
