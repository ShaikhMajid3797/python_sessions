# Q-Hacker Rank Quesion
'''
-if n is odd print Weird
-if n is even and in the inclusive range of 2 to 5,print Not Weired
-if n is even and in the inclusive range of 6 to 20,print Weired
- if n is even and greater than 20, print not weired 
'''

'''
n=eval(input("Enter a number= "))
if n%2!=0:
    print("Weired")
elif n%2==0 and n>1 and n<6:
    print("Not Weired")
elif n%2==0 and n>5 and n<20:
    print("Weired")
elif n%2==0 and n>20:
    print("Not Weired")
else:
    print("You have entered something wrong")
'''    



# Q-WAP ask the user for 10 natural numbers and sum it

'''
num=0
for i in range(1,11):
   print("The Addition of {} and {} is {} ".format(num,i,num+i))
   num=num+i

print("The sum of Natural 1 to 10 NUmbers is ",num)

'''
#NOTE- IMP point to solve question like above question
#-Whenever if you want to implement count program
#- initialize one variable=0 at outside of the program(num=0)
# - indside the loop based on problem update the variable
# - like num=num+i





'''
for m in range(10):
    print(m)
print(m) #NOTE-here we can see,we can use variable of loop we can use ooutside,unlike function 
'''
#NOTE-sum is in-built keyword so we cant use it as a varable name




'''
# Q- Count how much number are even in between 1 to 100
even=0
odd=0
for i in range(1,101):
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("Total Even numbers in 1 to 100 are ",even)
print("Total Odd numbers in 1 to 100 are ",odd)
'''


# Q- Count how much number are even and odd in  Random number in range of 1 to 100 in 100 chances
'''
import random;

even=0
odd=0

for i in range (1,101):
    num=random.randint(1,100)
    if num%2==0:
        even=even+1
    else:
        odd=odd+1
        
print("Total Even Numbers = ",even)
print("Total Odd Numbers = ",odd)
'''



# Q -  WAP ask the user to enter for random number between 1 to 99 
#   - iterate the loop for 10 times
#   - count how much times the number is coming  greater than 50
'''
count50=0
for i in range(1,11):
    num=eval(input("Chance {} \nEnter a random number between 1 to 99 = ".format(i)))
    if num>50:
        count50=count50+1
print("You have entered {} times greater than 50 Numbers".format(count50))
'''

'''
# Q - WAP NUMBER OF DIVISORS PROGRAM
#   - ask the user for number and check how much are divisiors of the number

num=eval(input("Enter a number = "))
count=0
noncount=0
for i in range(1,num+1):
    if num%i==0:
        print("The divisor of {} is {}".format(num,i))
        count=count+1
    else:
        print("The Nondivisor of {} is {}".format(num,i))
        noncount=noncount+1
        
print("The total divisors of {} are {}".format(num,count))
print("The total Non-divisors of {} are {}".format(num,noncount))

'''




'''
#Q-Creat a function on abouve program and return value

def counter():
    num=eval(input("Enter a number = "))
    #NOTE-whenever you are going to initialize the counter,alwayz initialize it insode the function
    count=0
    noncount=0
    for i in range(1,num+1):
        if num%i==0:
            print("The divisor of {} is {}".format(num,i))
            count=count+1
        else:
            print("The Nondivisor of {} is {}".format(num,i))
            noncount=noncount+1
    return num,count,noncount

num1,num2,num3=counter()        

print(" FUNCTION The total divisors of {} are {}".format(num1,num2))
print("FUNCTION The total Non-divisors of {} are {}".format(num1,num3))

'''




#Q - make special function for if else condition in above code and use it

def condition(num,i,count,noncount):# here we given argumnt of 4 variable because we did not declear it inside or outside the function.without it we will get Nameerror 
    if num%i==0:
            print("The divisor of {} is {}".format(num,i))
            count=count+1
    else:
            print("The Nondivisor of {} is {}".format(num,i))
            noncount=noncount+1
    return num,count,noncount 


def counter():
    num=eval(input("Enter a number = "))
    #NOTE-whenever you are going to initialize the counter,alwayz initialize it insode the function
    count=0
    noncount=0
    for i in range(1,num+1):
        
        num,count,noncount=condition(num,i,count,noncount) #hre we saved return of condition() funtion in new 3 variable num1,num2,num3
        #here we return it 
        #bcoz we need it    
    print(" FUNCTION The total divisors of {} are {}".format(num,count))
    print("FUNCTION The total Non-divisors of {} are {}".format(num,noncount))
    return num,count,noncount #return of counter() function

counter() # here we can end the function and we can get print also


#NOTE- here i have taken just example to understand the return rules 

#num4,num5,num6=counter() #here we return of counter() saved in another 3 variable(num4,num5,num6) to use outside of the counter function again 
#print(" FUNCTION The total divisors of {} are {}".format(num4,num5))
#print("FUNCTION The total Non-divisors of {} are {}".format(num4,num6))



# break vs continue vs pass

print("Now Break")
for i in range(8):
    if i==4:
        break  #whenever this cindition met in the loop it stop the iteratio if the loop and it not print more numbers 
    print(i)


print("Now CONTINUE")
for i in range(9):
    if i==4:
        continue  # here we use continue to skip(ignore) that iteration if the condition met means here it will skip to print 4 and it wll go for the next iteration of loop to print 5  
    print(i)   
    
print("Now PASS")
for i in range(9):
    if i==5:
        pass # we use pass to skip this condition for some time like if we got condition out of range it will just pass not give the error
    print(i)

age=eval(input("Enter your age :- "))
for i in range(5):
    if age>12 and age<18:
        print("Welcome")
    else:
        pass  # here we didnt think which condition we have to apply we skip this iteration for some time then we will make program
               # if we entered the age greater than the 18 it will just pass that iteration it will not goves error
               







