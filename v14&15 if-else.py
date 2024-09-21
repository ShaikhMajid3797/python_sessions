#===============================IF-ELSE STAEMENT(CONDITIONAL STATEMENT)================================================

'''
try:
    name=input("Enter Your Name ")        
    if name=="majid":
        print("Hii.....Majid")

    else:
            print("Your not allowed")
except Exception as a:
    print("ppppp",a)

if name=="majid":
        print("Hii.....Majid")

#else:
 #   print("Your not allowed") # and we can use if only 
            
print("\nProgram is going on") #this line is not depend on the if else statement.it will execute independently.
'''

'''
print("Hiiii.....Shaikh Majid")
num1=eval(input("Enter the num1 "))
num2=eval(input("Enter the num2 "))
if num1==num2:
    print("your true\nwe will do the addition")
    print("the addition of {} and {} is {} ".format(num1,num2,num1+num2))
else:
    print("your wrong")
    print("the multiplication of {} and {} is {} ".format(num1,num2,num1*num2))
'''


'''
#   % - its called module operator or reminder operator.used to check the reminder
n1=eval(input("Enter the Number "))
    
try:
    if (n1%2==0): #we can write condition under () also
        print("its EVEN Number and it is=",n1)
    else:
        print("You have entered ODD Number and it is=",n1)

except Exception as a:
    print("Error is ",a)
    
'''


'''
#Q= WAP get a random number and check its even or odd
import random
rannum=random.randint(1,100)
print(rannum)
if(rannum%2==0):
    print("This is Even Number and it is ",rannum)
else:
    print("This is ODD Number and it is ",rannum)
'''    

'''
# Q-WAP get a random number between 1 to 20 and if random number is between 1 to 99 print won or you lossed
try:
    import random
    num1=random.randint(1,200)
    print(num1)
    if(num1>=1 and num1<=99): #(0<num1<99)
        print("You have won the game")
    else:
        print("You lossed ")
except Exception as e:
    print(e)
    
'''


'''
# Q-WAP ask user for enter a number and if number is greater than or equal to 0 print positive or negetive
try:
    number=eval(input('Enter a number'))
    if(number>0):
        print("its POSITIVE")
    elif(number==0):
        prnit("Ist ZERO")
    else:
        print("its NEGETIVE")
except Exception as e:
    print(e)
'''



'''
# Q-WAP ask user for enter for percentage and if percentage is greater than 90 print A,between 70 to 90 print B, between 50 to 70 print D or E
try:
    per=eval(input("Enter your Percentage "))
    if (per<0 or per>100):
        print("You have entered wrong digit")
    elif(per>=90):
        print("GRADE 'A' ")
    elif(per>=70 and per<90):
        print("GRADE 'B'")
    elif(per>=50 and per<70):
        print("GRADE 'C'")
    else:
        print("You are Failed")
except Exception as e:
    print(e)
'''





'''
# WAP ask user for salary and salary grater than 10 lakh apply 10% tax and if tha salary greater than 7 and less than 10 apply 5% tax
#    and if the salary greater than 4.5 and less than 7 lakh apply 2.5%tax and if salary less than 2.5 lakh your tax free
#        OR
#Q=WAP ask user for salary and percentage of tax and deduct thr amount frim salary and peint the exact tax amount 
#  
try:
    sal=eval(input("Enter your salary "))
    if(sal>=1000000):
        taxsal=eval(input("Enter a tax percentage "))
        print("Your salary is {} and we applied 10% tax on it\nSo,you have to pay {} ".format(sal,(sal*taxsal)/100))
    elif(sal>=700000):
        taxsal=eval(input("Enter a tax percentage "))
        print("Your salary is {} and we applied 5% tax on it\nSo,you have to pay {} ".format(sal,(sal*taxsal)/100))
    elif(sal>=450000):
        taxsal=eval(input("Enter a tax percentage "))
        print("Your salary is {} and we applied 2.5% tax on it \nSo,you have to pay {}".format(sal,(sal*taxsal)/100))
    else:
        print("You are Taxfree")    
    
except Exception as e:
    print(e)

'''


'''
# .................Make a Calculator...............
# ask user to select the operation and ask for two numbers and calculate

op=str(input("Which operation you want to perform\nADDITION\nSUBTRACTION\nMUltiplication\nDIVISION\n"))
num1=eval(input("Enter the Num1 "))
num2=eval(input("Enter the Num2 "))

if (op=="Addition" or op=="ADDITION" or op=="addition"):
    print("We are doing Addition operation")
    print("Addition of {} and {} is {} ".format(num1,num2,num1+num2))

elif (op=="SUBTRACTION" or op=="Subtraction" or op=="subtraction"):
    print("We are doing Subtraction operation")
    print("Subtraction of {} and {} is {} ".format(num1,num2,num1-num2))    

elif (op=="MULTIPLICATION" or op=="Multiplication" or op=="multiplication"):
    print("We are doing Multiplication operation")
    print("Multiplication of {} and {} is {} ".format(num1,num2,num1*num2))   

elif (op=="Division" or op=="DIVISION" or op=="division"):
    print("We are doing Division operation")
    print("Division of {} and {} is {} ".format(num1,num2,num1/num2))   
else:
    print("you have entered something wrong")
'''    




#...........NESTED IF ELSE.................
#A nested if is an if statement that is the target of another if statement. Nested if statements mean an if statement inside another if statement.
# #Yes, Python allows us to nest if statements within if statements. i.e., we can place an if statement inside another if statement.
'''
num=eval(input("Enter a number "))
if(num>=0):
    if(num==0):
        print("It's Zero")
    else:
        print("Its Positive")
else:
    print("It's Negetive Number")
'''    





'''
#Q-ask gender to user  and devide in category according to age 


gen=str(input("Enter your Gender \nMale or Female\n"))
if (gen=="Male" or gen=="MALE" or gen=="male"):
    age=eval(input("Enter your Age "))
    if(age>=60):
        print("You are Male and Seneior Citizen because your age is ",age)
    elif(age>=30):
        print("You are Male and Man because your age is ",age)
    elif(age>=20):
        print("You are Male and Young Boy because your age is ",age)
    elif(age>=13):
        print("You are Male and Teenage because your age is ",age)
    elif(age>=0):
        print("You are Male and Boy because your age is ",age)
    else:
        print("you have written something wrong")

elif (gen=="Female" or gen=="FEMALE" or gen=="female"):
    age=eval(input("Enter your Age "))
    if(age>=60):
        print("You are Female and Seneior Citizen because your age is ",age)
    elif(age>=30):
        print("You are Female and Women because your age is ",age)
    elif(age>=20):
        print("You are Female and Young Girl because your age is ",age)
    elif(age>=13):
        print("You are Female and Teenage Girl because your age is ",age)
    elif(age>=0):
        print("You are Female and Girl because your age is ",age)
    else:
        print("You have entered something wrong")


    
    
    
# Q- ask the user for 3 numbers and find the biggest one between them

a=eval(input("Enter a number 1 "))
b=eval(input("Enter a number 2 "))
c=eval(input("Enter a number 3 "))

if(a>b and a>c):
    print("Number 1={} is the Biggest number between {},{} and {} ".format(a,a,b,c))
elif(b>a and b>c):
    print("Number 2= {} is the Biggest number between {},{} and {} ".format(b,a,b,c))
elif(c>a and c>b):
    print("Number 3= {} is the Biggest number between {},{} and {} ".format(c,a,b,c))
elif(a==b==c):
    print("all are same ")
else:
    print('you have entered something wrong')
        
'''




 









