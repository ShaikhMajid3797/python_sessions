#..................................FUNCTION  (Without Argument)...................................

'''Python Functions is a block of statements that return the specific task. The idea is to put some commonly or repeatedly done tasks together and make a function 
so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.

Some Benefits of Using Functions-
-Increase Code Readability 
-Increase Code Reusability
'''


'''
#....Q- take three numbers from the users and find the average inside the average
 
def average():
    num1=eval(input("enter the number 1 "))
    num2=eval(input("enter the number 2 "))
    num3=eval(input("Enter the number 3 "))
    print("Average of {},{} and {} is {}".format(num1,num2,num3,(num1+num2+num3)/3))

average()
'''





'''
#....Q-WAP ask user for the total bill and ask for the tip

def total_bill():
    try:
        totbil=eval(input("Enter the total bill "))
        tip=eval(input("Enter the tip you want to pay "))
        print("Toatal Bill is ",totbil+tip)
    except Exception as e:
        print(e)
        
total_bill()
'''




'''
#......Q-WAP ask the user for random number between 1 to 100 and find its even or odd

print("Hellow Majid")
print("We are trying new question ")
def evenorodd ():
    try:
        import random;
        num1=random.randint(1,100)
        if(num1%2==0):
            print("{} is EVEN number ".format(num1))
        else:
            print("{} is ODD number ".format(num1))
    except Exception as e:
        print(e)
        
evenorodd()
print("We have done it")
'''



'''
#..............Q-WAP make function of all 4 basic mathematical function and use it on user call

try:
    def add():
        print("{} + {} = {}".format(num1,num2,num1+num2))
    def sub():
        print("{} - {} = {}".format(num1,num2,num1-num2))
    def mul():
        print("{} * {} = {} ".format(num1,num2,num1*num2))
    def div():
        print("{} / {} = {}".format(num1,num2,num1/num2))

except Exception as e:
        print(e)


    
num1=eval(input("Enter the num1 ")) 
num2=eval(input("Enter the num2 "))
op=input("Enter which operation you have to do Addition,Subtraction,Multiplication and Division\n")

if(op=="ADDITION" or op=="Addition" or op=="addition"):
    add();
elif(op=="SUBTRACTION" or op=="Subtraction" or op=="subtraction"):
    sub();
elif(op=="MULTIPLICATION" or op=="multiplication" or op=="multiplication"):
    mul();
elif(op=="DIVISION" or op=="Division" or op=="division"):
    div();
else:
    print("you have entered something wrong")
    
# NOTE- if we done something wrong in the funtion but we can kno it after execution of that function
'''





'''
#..................................FUNCTION  (With Argument)...................................
#Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.
# in without argument we declare the specific variable and the store some vlaues in that then we use that variables.But in the without argument function we 
# dont declare the variable, we directly use and we enter the values or words while calling the function


def even_odd(x):              # like here we use x variable .x is called arguments
    if(x%2==0):               
        print("EVEN")         
    else:                     
        print("ODD")
even_odd(25) #and we use a value which by default save in x and after that the function will work
#print(x) NOTE- we cant use that x vvariable out of the function
'''



'''
def add(x,y):
    print("Addition of {} and {} is {}".format(x,y,x*y))
    
#add(2.33) .....if we give one value in argument..... TypeError: add() missing 1 required positional argument: 'y'
'''




'''
def add():#we given 0 argument here 
    print("Addition of {} and {} is {}".format(x,y,x*y))

add(200,300) #     this errr will get------TypeError: add() takes 0 positional arguments but 2 were given
'''




'''
def avrg(a,b,c):
    print("The average of {},{} and {} is {} ".format(a,b,c,(a+b+c)/3))

avrg(10,20,30)

#...// - its called is FLOOR DIVISION if use like 20//3 it will ans without reminder like 6 
#...% - its called modules which use to know the remider after division like 20%3=2

def square(a):
    print("Square of {} is {} ".format(a,a*a))

square(12)

'''



'''
#...Q-WAP ask user for one number and get random number.if both are same print YOU WON

import random;

def randgame(a):
    #a=eval(input("Enter a number between 1 to 100 "))  #we dont need this line in the function
    b=random.randint(1,20)
    print("the RNADOME NUMBER IS = ",b) 
    if (b==a):
        print("You Won")
    else:
        print("You Lossed")
    
    
#randgame(10) # This is Direct Pass 
# WE have 2 types of providing a vlaue like DIRECT PASS and KEYBOARD PASS
# but we have another way that is KEYBOARD PASS 

randgame(eval(input("Enter a number betweeen 1 to 20= ")))

#val=10 #this is another way in which we strore a user value in the variable and enter that variable in the argument
#randgame(val)
'''


'''
#.......Q- WAP ask the user for salary and tax percentage and output the exact how much amount he need to pay

def saltax(a,b):
    print("Your salary is {} and you entered {} percent tax you have to pay \n so, you have to pay {}".format(a,b,(a*b)/100))

# we can pass the value like this 
#saltax(eval(input("Your total Salary= ")),eval(input("how much tax you have to pay= ")))

# or we have anothor way and that is we will take values by user and save it in the variable and use that variable in argument of function,like this,
sal=eval(input("Enter thr salary= "))
tax=eval(input("Enter the hoe much tax percentage you have to pay= "))
#now we will call the function and use this two varable as a argument
saltax(sal,tax)
'''


#...................................Default Parameter Function..............................
'''
#if we declear the one parameter in the function argument it is called default parameter
def mul10(a,b=10): 
    print("the value of {}*{} is={} ".format(a,b,a*b))

mul10(2)


#but if we providing again the value to default vlaue it will take recent given value like this,
mul10(2,12)
'''


'''
#This is normal function and argumnt
def avg(num1,num2,num3):
    print("The average of {},{} and {} is {} ".format(num1,num2,num3,(num1+num2+num3)/3))

avg(100,200,300)

#but if we declear the one parameter between two parameters it will give error like this,
def avg(num1,num2=200,num3): # we shoud write default parameter at the last only 
    print("The average of {},{} and {} is {} ".format(num1,num2,num3,(num1+num2+num3)/3))

avg(100,300) #ERROR WILL BE :- parameter without a default follows parameter with a default
'''



