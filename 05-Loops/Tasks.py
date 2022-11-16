# 1 : Print numbers from 0 to 10 using while
'''
   n=0
   while n<11:print(n);n+=1



# 2 : Print numbers from 0 to 10 using for


for n in [0,1,2,3,4,5,6,7,8,9,10]:
    print(n)
    

# 3 : Stop the loop if the number = 5

for n in range (10):
    if n==5:
     break
    print(n)

print('stop')  


# 4 : Skip the 5 iteration from print

for n in range (10):
    if n==5:
     continue
    print(n)



# 5 : print multiplication table from 1 to 5

start=int(input('Enter Start Number:'))
end=int(input('Enter End Number:'))          

for n in range(start,end):
    print("------------")
    for m in range(1,6):
        print(f"{n}X{m}={n*m}")   
  


# 6 : How to get numbers from 10 to 20 using range

for n in range (10,21):
      print(n)


# 7 : How to get numbers from 10 to 100 with 3 at each step using range

for n in range (10,103,3):
      print(n)


# 8 : Get a list of even numbers from 1 to 100 using for

even_numbers_list = []
for x in range(1,101) :
   if  x%2 == 0:
      even_numbers_list.append (x)
      
print (even_numbers_list)




# 9 : Get a list of even numbers from 1 to 100 using while

n=0
while n<101:
    print(n)
    n+=2




# 10 : Get a list of even numbers from 1 to 100 using range
list(range(0,101,2))
'''
