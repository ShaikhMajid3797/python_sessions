#_____________________________________WHAT WE HAVE LEARN TILL_________________________________________________
'''
*Basic Syntax

*Data Types

*Type Casting

*Overviev if Package
    -like Random and Math

*eval,input,sep='' and end=''

*Conditional Statement (if,elif,else,break)

*Function
    -without argument
    -with argument
    -default argument
    -function in function
    -return function
*try and exception

* For Loop

* While Loop  
'''



#NOTE- Here we compleate the Basic python and the next DATA STRUCTURE topic of python are
'''
-string
-list
-dictionary
-tuple
-set
-lambda function
-file handling
'''
# NOTE - then the 3rd level of python will we OOPs(Object Oriented Programming)
'''
-Class
-Object
-Method
-Inheritance
-Polymorphism
-Data Abstraction
-Encapsulation
'''






#___________________________________________________________________WHILE LOOP___________________________________________________________________
'''
*in any loop we need three things that are
-initialization 
-condition 
-increment/decrement


-----so in *For* loop we take these three condition on one line like *for i in range(1,10)*
                                                - where,
                                                    -'for i' is initialization
                                                    -'10' is condition (when we have to come out of loop)
                                                    - and +10 is increment


-----but in while loop we need to declear these three thing individually
-example of WHILE LOOP like
-if i have to print first 10 numbers (0 to 9) so,

    i=o                     # its initialization
    
    while <condition>       # if condition will be true then it will go inside like if else
        statement 1         # we can write our code here
        statement q         

        i=i+1               # this is increament or decrement
_____________________________________________________________________________________________________________
*FOR LOOP*

for i in range (1,10):
    print(i)

*WHILE LOOP*

i=0

while <condition>:       # as we can see we wrote all three things in one line in for loop
    print(i)             # but here we have to wrote theree lines
    i=i+1

'''


#for j in range(0,10):
 #   print(j,end='  ')

# Q-WAP print number 10 to 20
'''
i=10    
while i<=20:
    print(i,end='  ')
    i=i+1
'''


'''
# Q-WAP print number -1 to -10
i=-1   
while i>-11 :
    print(i,end='  ')
    i=i-1
'''
    

# NOTE- the above condition is very confusion but we have another way like
'''
i=-1
while True: # if we write true here it will enter in the loop
    print(i,end=" ")
    i=i-1
    if i==-11:
        break
'''

'''
i=0    
while i>=0:
    print(i,end='  ')
    i=i+1
    if i==50:
        break  # THis is another solution of break the loop
'''


'''
# Q- ask the user for the 5 times number and print the square of that number
i=0
while i<5:
    num=eval(input("Enter the Number = "))
    print("The Square of {} is {}".format(num,num*num))
    i=i+1
'''

'''
# Q- take a random number 5 times between 10 to 20 and find its square
import random;
i=0
while i<5:
    val=random.randint(10,20)
    print("The Square of {} is {} ".format(val,val*val))
    i=i+1
'''





'''
# Q-WAP take a random number 10 times between 10 to 20 and print it even or odd.first solve in for loop and the while loop

for i in range (10,21):
    if i%2==0:
        print("FOR>>> {} is EVEN ".format(i))
    else:
        print("FOR>>> {} is ODD".format(i))
        
        
j=10
while j<21:
    if j%2==0:
        print("WHILE>>> {} is EVEN ".format(j))
    else:
        print("WHILE>>> {} is ODD".format(j))
    j=j+1 
'''



'''
# Q-WAP calculate the sum of first 10 natural number using for and while loop... ans should 55
val=0
for i in range (1,11):
    val=val+i
print("*FOR* The sum of 10 natural number is = ",val)

num=0
j=1
while j<11:
    num=num+j
    j=j+1

print("*WHILE* The sum of 10 natural number is =",num)
'''

'''
# Q-WAP take a 10 random numbers between 1 to 100 and sum that 10 number.first solve in for loop and the while loop

import random;

num=0

for i in range(1,11):
    ran=random.randint(1,100)
    num=num+ran

print("FOR LOOP ANS =",num)

number=0
j=0
while j<11:
    rannum=random.randint(1,100)
    number=number+rannum
    j=j+1
print("WHILE LOOP ANS = ",number)    
'''







# Q-WAP take a 10 random numbers between 1 to 100 and count how many are greater than 50.first solve in for loop and the while loop
'''
import random;
grt=0
less=0
for i in range(1,11):
    val=random.randint(1,100)
    if val>50:
        grt=grt+1
    else:
        less=less+1
print("FOR>>>> total number greater than 50 = ",grt)
print("FOR>>>> total number less than 50 = ",less)


grtnum=0
lessnum=0

import random;
j=0
while j<10:
    num=random.randint(1,100) 
    if num>50:
        print(num,end=" ")
        grtnum=grtnum+1
    else:
        lessnum=lessnum+1
    j=j+1
print("WHILE>>>> total number greater than 50 = ",grtnum)
print("WHILE>>>> total number less than 50 = ",lessnum)
'''





# Q-WAP take a 10 random numbers between 0 to 10 and count how many are greater than 5 and equal to 0.first solve in for loop and the while loop
'''
import random;
grt5=0
zero=0
for i in range(1,11):
    val=random.randint(0,10)
    if val>5:
        print(val,end=" ")
        grt5=grt5+1
    elif val==0:
        zero=zero+1
print("FOR>>>> total number greater than 5 = ",grt5)
print("FOR>>>> total number equal to zero = ",zero)


grtnum5=0
zeronum=0

import random;
j=0
while j<10:
    num=random.randint(0,10) # NOTE- if we use randint method for 2 times in program at a time,it gives same number
    if num>5:
        print(num,end=" ")
        grtnum5=grtnum5+1
    elif num==0:
        zeronum=zeronum+1
    j=j+1
print("WHILE>>>> total number greater than 5 = ",grtnum5)
print("WHILE>>>> total number equal to zero = ",zeronum)
'''




# Q- Take a random number from random package between 1 to 10.And ask the user to enter number between 1 to 10. 
# If  the number == random number
# -            print("You Won")
#  else:
#    print("You Lossed") 
# give 3 chance to user to guess the random number,Using While Loop

'''
import random;
ran=random.randint(1,10)
i=1
while i<4:
    print(ran)
    num=eval(input("Enter a Random Number Between 1 to 10 = "))
    if num>10 or num<1:
        print("You have enterd wrong number,try again")
    elif num==ran:
        print("You Won The Game\nYou have Entered {} and Random Number is {}".format(num,ran))
        break
    elif i<3:
        print("ohh! you are Wrong\nYou have Lossed the chance and you have only {} chance left".format(3-i))
    elif i==3:
        print("You Lossed The Game\nYou have no chance")
    i=i+1
'''    




'''
#Q- above question. only make question of if else

def condition(num,ran,): # here we done 2 argumnt becoz this is not decleared 
    if num>10 or num<1:
        print("You have enterd wrong number,try again")
    elif num==ran:
        print("You Won The Game\nYou have Entered {} and Random Number is {}".format(num,ran))
        
    elif i<3:
        print("ohh! you are Wrong\nYou have Lossed the chance and you have only {} chance left".format(3-i))
    elif i==3:
        print("You Lossed The Game\nYou have no chance")


import random;
ran=random.randint(1,10)
i=1
while i<4:
    print(ran)
    num=eval(input("Enter a Random Number Between 1 to 10 = "))
    condition(num,ran)
    if num==ran:
        break  # we cant use break outside the loop,thats why we again take one conditon to break the loop
    i=i+1
'''









      


































    
    
    
    
    
    
    
    
    
    
    
    
    
    