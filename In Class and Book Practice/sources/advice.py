# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:58:47 2024

@author: saman
"""

from random import choice

answers = ["Yes!", "No!", "Reply hazy", "Sorry, what?"]

def give():
    """Return random advice"""
    return choice(answers)