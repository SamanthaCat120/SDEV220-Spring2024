# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 18:22:46 2024

Last updated on Sat Feb 24 19:56:46 2024

@author: Samantha Lopez
"""

import datetime
from functools import wraps
import emoji

TAX_RATE = 0.14
OVERTIME_THRESHOLD = 40
OVERTIME_MULTIPLIER = 1.5

def logger(func):
    @wraps(func)
    def logging(*args, **kwargs):
        with open("payroll.log", "a") as log:
            log.write("Just ran the " + func.__name__ + " function. \n")
            return func(*args, **kwargs)
    return logging

@logger
def getInputs():
    name = input("State your name...I mean type it? ")
    hours = float(input("How many hours did you work? "))
    rate = float(input("What is your hourly rate? "))
    need = float(input("How much did you need this week? "))
    return name, hours, rate, need

@logger
def calculateGross(hours, rate):
    if hours > OVERTIME_THRESHOLD:
        gross = (hours - OVERTIME_THRESHOLD) * rate * OVERTIME_MULTIPLIER + OVERTIME_THRESHOLD * rate
    else:
        gross = hours * rate
    return gross

@logger
def deductTaxes(gross):
    deduction = gross * TAX_RATE
    net = gross - deduction
    return net

@logger
def printCheck(net, name):
    with open(name + "_check.txt", "w") as toFile:
        toFile.write("\t\t" + str(datetime.datetime.today())[0:10] + "\n\n")
        toFile.write("pay to the order of: \t" + name + "\n")
        toFile.write("Amount: $ \t" + format(net, ".2f"))

if __name__=="__main__":
    name, hours, rate, need = getInputs()
    print(name, hours, rate)
    gross = calculateGross(hours, rate)
    net = deductTaxes(gross)
    print('Your net amount is $ ', format(net, ".2f"))
    if need <= net:
        print("Yay, you made what you need to spend this week." + emoji.emojize(":grinning_face_with_big_eyes:"))

    else:
        print(emoji.emojize(":disappointed_face:") + "I guess you'll have to work more next week.")

