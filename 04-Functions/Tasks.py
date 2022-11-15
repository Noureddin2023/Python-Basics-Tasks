# 1 : Create a simple function that takes 2 numbers and print their values
'''
def nour(x,y):
    print(x+y)
    
nour(5,7)

12

# 2 : Create a simple function tha takes 2 numbers and return their values

def nour(x,y):
    result=x+y
    return result
    
n=nour(5,7)
print(n)

12

# 3 : In the above return function, use keyword arguments when calling the function

def nour(x,y):
    result=x+y
    return result
    
n=nour(y=5,x=7)
print(n)

12

# 4 : In the above return function, give x and y default values of 0 and call the function with no argument

def nour(x=1,y=0):
    result=x*y
    return result
    
n=nour()
print(n)


0

# 5 : Create a function that can take any number of arguments and print the sum of them

def nour(org,*vartuple):
    result=org+sum(vartuple)
    return result
    
n=nour(2,4,8)
print(n)


14

# 6 : Create the same sum function using the lambada

nour=lambda org,*vartuple:org+sum(vartuple)
    
    
n=nour(2,4,8)
print(n)

14

# 7 : Call the lambda function at the same definition line

n=(lambda x,y:x+y)(5,7)
print(n)

12


# 8 : Write the difference between the local variable and global variable   

 If we create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
'''
 
