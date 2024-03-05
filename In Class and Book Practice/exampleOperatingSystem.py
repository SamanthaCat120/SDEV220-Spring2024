# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:09:54 2024
Last updated on Mon Mar  4 18:09:54 2024

@author: Samantha Lopez
"""

import sys
from os import *
from os.path import *

print(sys.path) #site packages is where pip imports things

"""TO add to a system path:
    sys.path.append
    or
    sys.path.insert(0, C://file address and switch backslashes to forward slashes"""
#print(sys.version)

exec(open("SayHi.py", "r").read())

z = 15
equation ="(3 X 7 + 9 - 4)/z"

y = exec(equation)
print(y)

#exec(open(file.read()) is what happens every time a run button is pressed)






if __name__=="__main__":
    pass