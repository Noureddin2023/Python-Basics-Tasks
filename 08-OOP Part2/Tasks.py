# 1. Create a new class names SciCalc with 3 methods , sum , mull , power all of them takes 2 argument x, y
class SciCalc:
    def sum(x,y):
        pass
    def mull(x,y):
        pass
    def power(x,y)



# 2. Sum return the sum of x and y

class SciCalc:
    def sum(self,x,y):
        return x+y
        
    def mull(x,y):
        pass
    def power(x,y):

c = SciCalc()
c.sum(5,2)

print(c.sum(5,2))


# 3. Mull return the multiplication of x and y
class SciCalc:
    def sum(self,x,y):
        return x+y 
    def mull(self,x,y):
        return x*y
    def power(self,x,y):
        return x**y
    
c = SciCalc()
c.sum(5,2)

print(c.sum(5,2))



# 4. The power return x power y
class SciCalc:
    def sum(x,y):
        result=(x+y)
        gitreturn result
    def mull(x,y):
        return x*y
        
    def power(x,y):
        result=(x**y)
        return result   



# 5. Take an object from the class and call the 3 methods with any numbers
class SciCalc:
    def sum(self,x,y):
        return x+y
        
    def mull(self,x,y):
        return x*y
        
    def power(self,x,y):
        return x**y
    
c = SciCalc()
c.sum(5,2)
c.mull(5,5)
c.power(2,2)
print(c.sum(5,2))
print(c.mull(5,5))
print(c.power(2,2))
# 6. Can we inherit from the class we created in the first task Calc



# 7. Inherit from the Calc class , now remove the unneeded code the the SciCalc after inheriting

class Calc:
    def mull(self,x,y):
        return x*y
        
    def power(self,x,y):
        return x**y

class SciCalc(Calc):
    def sum(self,x,y):
        return x+y



# 8. call the 3 methods again from the SciCalc object

class Calc:
    def mull(self,x,y):
        return x*y
        
    def power(self,x,y):
        return x**y

class SciCalc(Calc):
    def sum(self,x,y):
        return x+y
        
   
    
c = SciCalc()
c.sum(5,2)
c.mull(5,5)
c.power(2,2)
print(c.sum(5,2))
print(c.mull(5,5))
print(c.power(2,2))



# 9. Now you should see the same result as before

yes

7
25
4


# 10. Explain in few words what happened after inheriting
'''
 In place of writing the same code, again and again, we can simply inherit the properties of one class into the other
'''
