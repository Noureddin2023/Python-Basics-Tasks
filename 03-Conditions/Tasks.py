# 1 : Check if 10 is bigger than 15 or not
'''
 n = 10
if n>15:
    print('10 is begger than 15')

    
Nothing

'''

# 2 : If 10 is not bigger than 15 print x is smaller than 15
'''
n = 10
if n > 15:
    print('10 is bigger than 15')
else:
    print(' 10 is smaller than 15')

    
 10 is smaller than 15


'''
# 3 : In wich cases we will use all
'''
    Using [ all ] with more than one condition
'''

# 4 : What is the differences between all , and
'''
   and = returns True only if both operands are True
   all = returns True if all the list items are True

'''

#  5 : What is the differences between any , or
'''
     or: returns True in any one of the boolean expressions passed is True
    any: returns True if any element of an iterable is True
'''

# 6 : If we need all The conditions to be true we will use ....

'''
    if
'''

# 7 : What is the differences between if , elif
''' 
    if: executed if the first condition is true
  elif: to test a new condition if previous condition isn´t true
  
'''

# 8 : What is the differences between eilf , else
'''
    eilf: to test a new condition if previous condition isn´t true
    else: to Provide another option incase the if condition is false, else code will be execute
'''

# 9 : Can we use more than one elif
'''
    yes, we can
'''

# 10 : Can we use more than one else

'''
   yes, we can with elif
   
'''

# 11 : write s simple ternary operator
'''
   n = 7
   print ('n>5') if n>7 else print('error')
   
'''


# 12 : in elif , python will check all the conditions no matter, what ?
'''
the elif conditions are applied after the if condition and Python will evalute the if condition and if it evaluates to False then it will evalute the elif blocks and execute the elif block whose expression evaluates to True. If multiple elif conditions become True, then the first elif block will be executed.

'''

# 13 : in elif we us else for  ... ?
'''
   executed all attached 'elif' statements are false.
'''


# 14 : if we have this list [2,4,6,8,10]:
         1. check to see if 4 in this list or not
     '''
         list = [2,4,6,8,10]
         if 4 in list :
         print('ok')
         ok
     '''
         2. check to see if 4 and 6 in this list or not
         '''
           x = [2,4,6,8,10]
          if 4 and 6 in x :
          print('yes')
          else:
          print('No')
          yes
    '''
         3. check to see if 3 or 6 in this list
         '''
         x = [2,4,6,8,10]
         if 3 or 6 in x :
         print('yes')
         else:
         print('No')
         yes
        '''
         4. check to see if 2,4 and 5 in this list 
'''
         x = [2,4,6,8,10]
         if  all([2 in x ,4 in x,5 in x]) :
         print('yes')
         else:
         print('No')
         No
'''
