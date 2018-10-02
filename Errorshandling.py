# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 14:26:18 2017

@author: Ritik
"""

#How to make errors accepted
x = 0
y = 0
# this script "print (x/y)"  will show Zero Division Error
#but we can make this error accepted by using try & except function
try:
    z = x/y
except ZeroDivisionError:
    z=0
print (z)

print ("5 + 2=" , 5+2)