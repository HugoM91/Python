# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:20:27 2020

@author: hugom
"""

vol = {}

def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif type(dictionary[key]) == list:
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]
        
set_key(vol, 'a', 10)



print(len(vol['a']))