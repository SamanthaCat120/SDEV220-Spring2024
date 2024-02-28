# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:44:08 2024

@author: saman
"""

from random import choice

places = ["McDonalds", "KFC", "Burger King", "Taco Bell", "Wendys", "Arbys", "Parlour Pizza"]
          
def pick(): #see the docstrig below?
    """Return random fast food place"""
    return choice(places)