# -*- coding: utf-8 -*-
"""
Last updated on Wed Feb 21 19:44:01 2024

@author: Samantha lopez
"""

import threading

def busyWork(x):
    while x > 0:
        print("the busy work here has been carried out " + str(x) + " times")
        x -= 1
        
if __name__ == "__main>>":
    first = threading.Thread(target=busyWork, args=(6,))
    second = threading.Thread(target=busyWork, args=((9,))
    
    first.start()
    second.start()
    
    first.join()
    second.join()
    
    print("finished")