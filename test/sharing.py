# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 20:02:27 2023

@author: franc

sdev 220 spring 2023
"""


import flask
from people import Person
import json

application = flask.Flask(__name__)

folks = [
    Person("Sally", 34, "Salem"),
    Person("Charlie", 28, "Charlestown"),
    Person("Corey", 16, "Corydon"),
    Person("Lewie", 73, "Louisiville"),
    Person("Jeffery", 14, "Jeffersonville")
    ]


@application.route("/")
def homePage():
    page = "<!DOCTYPE html><html><head><title>Sharing API</title></head><body><h1>hello</h1><p>world</p></body></html>"
    return page


@application.route("/contacts")
def contacts():
    contacts = {}
    for f in folks:
        yield json.dumps({"name": f.name, "age": f.age, "town": f.town}) + "\n"



@application.route("/find/by-name/<name>")
def particular(name):
    print(name)
    for f in folks:
        if f.name.lower() == name:
            yield json.dumps({"name": f.name, "age": f.age, "town": f.town}) + "\n"








