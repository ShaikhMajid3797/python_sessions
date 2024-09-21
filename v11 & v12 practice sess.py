# exercise, ask the User Basic salary, DA and HRA of user and calculate total amount

'''
bassal=eval(input("Enter your Basic salary\n"))       #we use here evaluation function (eval())  because it allow us to get some expression from user
da=eval(input("\nEnter your HRA Amount\n"))         #but int only allow one digit
hra=eval(input("Enter your DA Amount\n"))
totsal=bassal+da+hra
print("*****Your Total Salary is",totsal," ******")
'''

#a=eval(input("Enter a expression\n"))  #we use here evaluation function (eval())  because it allow us to get some expression from user 
#print(a)                               #but int only allow one digit

'''
# Q:- ask user to salary and tax and calculate the tax


sal=eval(input("Enter your salary\n"))
per=eval(input("Enter tax percentege\n"))
taxpay=(sal*per)/100
print("You need to pay",taxpay)
'''

#take a random input as a input and calculate a square of that value 
'''import random
num1=random.randint(1,100)
print("square of",num1,"is",num1*num1)
print("square of {} is {} ".format(num1,num1*num1))
'''

'''

#ask user for distance and ask distance per charge and calculate total charge 
dis=eval(input("Enter the total distance in KM"))
charge=eval(input("Enter thr distance per charge KM"))
totchg=dis*charge
print("total charge is ",totchg)

'''

'''
#Conversation between manager and customer

import time #when we have to execute code one after another so use time package of sleep packagec
bill=eval(input("Enter your total bill in Doller "))
time.sleep(2)
print("\nMANAGER:- Doller are not accepted here\n")
time.sleep(2)
print("USER:- Then what is accepted here\n")
time.sleep(2)
print("MANAGER:- Only Indian Rupees\n")
time.sleep(2)
print("USER:- How much rupee of one Dooler\n")
time.sleep(2)
print("MANAGER:- 80\n")
time.sleep(2)
print("USER:-How much is my total bill\n")
time.sleep(2)
print("total bill is in Rupees is ",bill*80)
'''
#print(dir(time))  dictionary of time package


#conversation between father and son
import time
print("FATHER:-hey....Majid,What you think to do\n")
time.sleep(2)
print("SON:-I want to pursue Data science course\n")

time.sleep(2)
print("FATHER:-oh! that is very nice\nMay i know your jee rank?\n")
time.sleep(2)
rank=eval(input())
print("SON:-My JEE rank is\n",rank)

time.sleep(2)
print("FATHER:-ohh! its to high,how you will get admission?\n")
time.sleep(2)
print("SON:-i will get admisson through management quota\n")
time.sleep(2)

print("FATHER:-ohhh! that is very nice\nWhich college did you chosed?\n")
time.sleep(2)
print("SON:-NARESH IT\n")
time.sleep(2)

print("FATHER:-what is the fees per sem?\n")
fees=eval(input())
print("SON:- Total fees is {}  are there\n".format(fees))
time.sleep(2)

print("FATHER:-How many sem?")
sem=eval(input())
time.sleep(2)
print("SON:- Total sem is {}  are there\n".format(sem))
time.sleep(2)

print("FATHER:-what is the the Total fees of all sem?\n")
feesem=fees*sem
time.sleep(2)
print("SON:-Total fees per sem is {}  are there\n".format(feesem))

