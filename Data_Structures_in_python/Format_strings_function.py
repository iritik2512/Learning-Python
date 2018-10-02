i =10
while i >0:
    print(i)
    i -=2

#So far, to combine strings and non-strings, you've converted the non-strings to strings and added them.
#String formatting provides a more powerful way to embed non-strings within strings.
# String formatting uses a string's format method to substitute a number of arguments in the string.

#strings formatting can be integers and strings both
num=[17,19,29,31]
prime_num="{} {} {} , are three prime numbers under 30".format(num[1],num[2], num[0])
print(prime_num)

print("{0}{1}{0}".format("abra", "cad")) #here abra is filled twice as there are two zero in format

#strings formatting can also be done with named arguments
a ="{x}, {y}".format(x=5, y=12)
print(a)

