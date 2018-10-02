# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:32:44 2017

@author: Ritik
"""

# Operator Name symbol less than< ; greater than> , less than or equal to<= , greaterthan or qual to >= ,
# equal to == , not equal to!=
the_sun_is_up=True
the_sun_is_yellow=False
my_bool=True
print(my_bool)

sf_population  = 50000
sf_area = 100
rio_population  = 100000
rio_area = 50

sf_density = sf_population / sf_area
rio_density = rio_population / rio_area
print(rio_density)
print (sf_density)
print(rio_density > sf_density) #no need to use bool function,just use operator to check if statement is true or false
bool(1)
bool("78")

bool(0)
bool(0.242)

int(56.78) #working wih floATS AND INTERGERS
float(97)
print("hello world")
int(56.789)

"hello" #working with strings
"hello " + " there "
c="hi,There"
print(c)
here="cool"
print(here)
print(c + " you\'re " + here)
c.lower() #these are called methods
c.upper() # add double bracket for function to work
len(c) # len calculates the number of value in strigs
d =input("In which class do you read?") #input value only produces string
Your_class_after_one_year=int(d) + 1 #so,for integer we need to  convert string into integerby int(d)
print (d)
print(Your_class_after_one_year)
print(type(c))

#three same number coded in different ways
print(type(633))
print(type("633"))
print(type(633.0))
c.title() #makes first letter of every word capital as in titles
"One kilo, two kilo ,three kilo".count("kilo") #count method returns the number of times a string has been used

user_name=input("what is your name?\n") # \n is used for a line break in python
print( " Hello, "+ user_name)

len("1234")
