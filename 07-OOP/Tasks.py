# 1 : Explain in few words what we mean by a class give and example
'''
A class is a code template for creating objects. Objects have member variables and have behaviour associated with them. In python a class is created by the keyword class . An object is created using the constructor of the class. This object will then be called the instance of the class

Example: Apple : iphone 14:

(Class) - Design:
          - Color  Red , Gold
          - Size    Normal Max
(Object)- Production:
          - Color  Gold
          - Size   Normal Max

'''

# 2 : Create a simple class names calculator

class Calculator:
    def nour(n,x,y):
        print(x+y)

m = Calculator()
m.nour(5,7)




# 3 : Create a constructor that prints Welcome message
class Calculator:


    def __init__(self):
        print('Welcom')

m = Calculator()        



# 4 : Add 2 methods to the class & mull

class Calculator:
    def sum():
        

    def mull():
    


# 5 : The sum method return the sum of 2 arguments x and y

class Calculator:
    def sum(x,y):
        result = x+y
        return result

# 6 : The mull method return the multiplication of the arguments x and y

class Calculator:
    def sum(x,y):
        result = x+y
        return result
    
    def mull(x,y):
        result = x+y
        return result

# 7 : Take an object from the class Calculator:
class Calculator:
    def sum(x,y):
        result = x+y
        return result
    
    def mull(x,y):
        result = x+y
        return result
c = Calculator



# 8 : Call the sum method with 10 , 20
class Calculator:
    def sum(self,x,y):
ß        print(x+y)
    
    def mull(x,y):
        
c = Calculator()
c.sum(10,20)




# 9 : Call the mull method with 10 , 20
class Calculator:
    def sum(self,x,y):
        print(x+y)
    
    def mull(self,x,y):
        print (x*Y)
        
c = Calculator()
c.sum(10,20)
c.mull(10,20)



# 10 : Explain in few words why we call the self in methods
'''
By using the “self” we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.
'''

# 11 : What we mean with OOP 4 Pillars
'''
  - encapsulation
  - inheritance
  - polymorphism
  - abstraction
'''

# 12 : Why we use OOP in our code
'''
    it makes code more reusable and makes it easier to work with larger programs. OOP programs prevent you from repeating code because a class can be defined once and reused many times.
'''
