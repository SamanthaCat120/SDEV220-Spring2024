# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:29:01 2024
Last updated on Tue Feb 27 23:29:01 2024

@author: Samantha Lopez
"""

import urllib
import requests

def byURL():
    wiki = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    webhandler=urllib.request.urlopen(wiki)
    
    contents = webhandler.read()
    
    print(contents)
    
def byRequest():
    wiki = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    response = requests.get(wiki)
 #   print(response.text.split())
     



def someAPI():
    url = "http://127.0.0.1:5000/contacts"
    response = requests.get(url)
    print(response.text.split("\n"))








if __name__=="__main__":
    someAPI()
 #   byRequest()
 #   byURL()
 
 