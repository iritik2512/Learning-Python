# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:10:38 2018

@author: Ritik
"""

# the range function creates sequential lists of numbers
numbers = list(range(10))
print (numbers)


 #the range function takes three arguments : the begining value ,the ending value and the step
a = range (10, 30, 2) # creates a range from 10 to 30 every 2 steps
print (list(a))


z= list (range (50,90,5))
print (z)

nums =list(range (6))
print (nums[4])
print (nums)


nums = list (range(5,10))
print (len(nums))
 
 
#lambda is used to creates one line function which is especially used with map ,reduce and filter function
nums=[1,2,6]
g = lambda x: x*5
print(g(nums[2]))