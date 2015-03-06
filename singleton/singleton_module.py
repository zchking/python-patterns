#!/usr/bin/env python
# coding=utf-8

"""
All modules are singletons by nature because of Python's module importing steps:
    1.   Check whether a module is already imported. 
    2.   If yes, return it. 
    3.   If not, find a module, initialize it, and return it.
    4.   Initializing a module means executing code, including all module-level 
         assignments. When you import the module for the first time,  
         all initializations are done; however, if you try to import the module for   
         the second time, Python will return the initialized module.  
         Thus, the initialization will not be done, and you get a previously imported 
         module with all of its data

This part show the simple modules singleton.
"""

the_singleton_instance = 1



"""
moudle1.py

from singletons_module import the_singelton_insttance

the_singelton_insttance += 1

--------------------
moudle2.py
from singletons_module import the_singelton_insttance

print the_singelton_insttance  # will be 2


"""
