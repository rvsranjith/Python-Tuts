#!/usr/bin/python3
import sys #module

class person():  #class
     _id = 12345 #uderscores used to avoid conflicts with keywords or private identifier
     name = "conventions"  # variable

def get_name(): #Function
    print("this is a function")

get_name()
print (person.name)