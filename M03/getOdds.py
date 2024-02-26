# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 19:41:06 2024

@author: samantha lopez
"""
def getOdds():
    oddNums = []
    for x in range(10):
        if x % 2 != 0:
            oddNums.append(x)
    print(oddNums)
    return oddNums


if __name__ == '__main__':

    # Call the getOdds() function
    numbers = getOdds()

    # Prints 3rd numbers in list
    for i in range(2, len(numbers), 3):
        print(f'The third number is {numbers[i]}')

