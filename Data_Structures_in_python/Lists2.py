# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 18:03:17 2018

@author: Ritik
"""

#to check if an item is in the list , the "in" operator can be used. It returns True if the item
#occurs  one or more times in the list , And False if it doesn't.
words =["Hello" , 'there' , 'Here ' , 'Where']
print ("Hello" in words) 
print ("hello" in words)
print ('there' in words)

print ("interval")
# to check if the item is not in the list ,we can use the not opeartor in one of the following ways
nums = [45 , 25 , 75 ,65]
print( not 4 in nums)
print(55 not in nums)
print (not 75 in nums)
print (25 not in nums)

letters = ['a' , 'b' , 'z']
if "z" in letters:
    print ("yes")
    
#we can use "insert" to add an item to the list at any position in the list
#we use "append" to add an item to the list at the last posotion
words = [ 'hello' , 'Raj']
index = 1
words.insert(index , 'Hrithik')
words.insert(3, 'Kishan')
print (words)

words.append('Choudhary')
print (words)

#this is called slicing of lists
city =["Delhi" , "new york " ,' paris' ,' london ' , 'wellington' , 'dubai']
print(len(city))
print (city [0:3])
print (city [2:5])
print (city[-1:2])