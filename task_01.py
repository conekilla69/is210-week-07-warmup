#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""A fibonacci sequence"""


a, b = 0, 1
max_int = 10
def fibonacci():
    while b < 10:
        b = a+b
    return (b, end=',')


    
    
