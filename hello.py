#!/usr/local/bin/python3

print("---- simple array/string")

strings = ['a','b','c']

print(strings)
print("".join(strings))

print("---- for loops")
names = ['tom', 'john', 'simon']

for n in names:
    print(n)

print("---- processing an array")
names[:] = [n + " " for n in names]
print("".join(names))

a = [1, 3, 5]
b = a
a[:] = [x + 2 for x in a]
print(b)

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print(str)
print(str.split('\n'))
print(str.split(' ', 1 ))

a = [2,7,5,4]
b = [x for x in a if x % 2 == 0]
for x in b:
    print(x)


# Function definition is here
def quoteme( msg ):
   "This prints a passed string into this function"
   print("\""+msg+"\"")
   return;

# Now you can call printme function
quoteme("I'm first call to user defined function!")
quoteme("Again second call to the same function")




# Python program to 
# format a output using 
# string() method 
  
cstr = "I love geeksforgeeks"
    
# Printing the center aligned   
# string with fillchr  
print ("Center aligned string with fillchr: ")  
print (cstr.center(40, '#'))  
  
# Printing the left aligned   
# string with "-" padding   
print ("The left aligned string is : ")  
print (cstr.ljust(40, '-')) 
  
# Printing the right aligned string  
# with "-" padding   
print ("The right aligned string is : ")  
print (cstr.rjust(40, '-')) 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.WARNING + "Warning: this is a warning. Continue?" + bcolors.ENDC)