# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 18:22:46 2024

Last updated on Sat Feb 24 19:56:46 2024

@author: Samantha Lopez
"""

from functools import wraps


#@todo payroll calculator: 
    #get name and hours and rate,
    #calc overtime or not,
    #and 14% taxes
    
def logger(func):
    @wraps(func)
    def logging(*args, **kwargs):
        with open("payroll.log", "a") as log:
            log.write("Just ran the " + func.__name__ + " function. \n")
            return func(*args, **kwargs)
    return logging

@logger
def getInputs():
    name = input("WHAT is your name? ")
    hours = float(input("What is your favorite colo--I mean, How many hours did you work? "))
    rate = float(input("What is your hourly worth according to corporate America? "))
    return name, hours, rate
    
@logger
def calculateGross(hours, rate):
    if hours > 40:
        gross = (hours-40) * rate * 1.5 + 40 * rate
    else:
        gross = hours * rate
    return gross
    

@logger
def deductTaxes(gross, tax_bracket):
    tax_bracket = .14
    deduction = gross * tax_bracket
    net = gross = deduction
    return net

def printCheck(net, name):
    pass











if __name__=="__main__":
    name, hours, rate = getInputs()
    print(name, hours, rate)
    gross = calculateGross(hours, rate)