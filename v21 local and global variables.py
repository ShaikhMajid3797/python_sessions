#...................................................LOCAL & GLOBAL VARIABLES.....................................................

'''
Variables in any programming language have a crucial role. Variables are classified into Global variables and Local variables based on their scope.
The main difference between Global and local variables is that global variables can be accessed globally in the entire program, whereas local variables
can be accessed only within the function or block in which they are defined.

*** What is a Global Variable?

-Global variables are those variables which are declared outside of all the functions or block and can be accessed globally in a program.
-It can be accessed by any function present in the program.
-Once we declare a global variable, its value can be varied as used with different functions.
-The lifetime of the global variable exists till the program executes. These variables are stored in fixed memory locations given by the compiler and do not 
 automatically clean up.
-Global variables are mostly used in programming and useful for cases where all the functions need to access the same data.


*** What is a Local Variable?

-Variables that are declared within or inside a function block are known as Local variables.
-These variables can only be accessed within the function in which they are declared.
-The lifetime of the local variable is within its function only, which means the variable exists till the function executes. Once function execution is completed,
 local variables are destroyed and no longer exist outside the function.
-The reason for the limited scope of local variables is that local variables are stored in the stack, which is dynamic in nature and automatically cleans up the data 
 stored within it.
-But by making the variable static with "static" keyword, we can retain the value of local variable.
'''




#....EXAMPLE OF GLOBAL VARIABLE

'''
a=20 # Decleared outside the function menad these are GLOBAL VARIABLES
b=30
#function start,
def add():
    return (a+b)

print(a) # we can use it before calling the function
print(b)

addition=add()
print(addition)
''' 


#....EXAMPLE OF LOCAL VARIABLE

'''
#function start,
a=250 # we can decleare the local and globle variable.it does not effect on the program
def add():
    a=55 # Decleared outside the function menad these are GLOBAL VARIABLES
    b=32
    return (a+b)

#print(a) # we can not use it Outside of function thats why its called LOCAL VARIABLES
#print(b)

addition=add()
print(addition) #ans=87
print(a) # ans =250  (not a=87) we can decleare the local and globle variable.it does not effect on the program
'''

'''
def add(a=50):
    b=32
    return (a+b)

addition=add(60) # the compiler will take the latest value of 'a' which is 60, not 50
print(addition) #ans=87
'''




#......IMP
'''
#RULE-we can not use Local variable outside the function without 'return' statemment

#QUESTION- i want to use local variable outside the function without using return statement
#ANSWER  - we use 'globle' keyword while declearing the variable inside the function block


def ab():
    global a,b
    a=100
    b=200
    print("value of addition of a and b is = ",a+b)

ab()
print(a) 
print(b)

z=100
def updated():
    global z
    z=z+800
    print("value of updated z is = ",z)
updated()
# we should get answer of z=900 and in line 99 we declear it as globle vaiable
print(z)  #ans-900
print(z*5) #ans-4500
'''



'''
n1=10
n2=20
def add():
    global n2
    n2=200
    a=n1+n2
    print("The addition of {} and {} is {}".format(n1,n2,a)) # it will take n2=200 because its globle and latest value of n2
print(n1) #ans=10
add()
#here we get the anwer of n1=10 and n2=20 but we need n2=200 
print(n1)
print(n2)
'''


#.............FUNCTION IN FUNCTION......................
'''We use one function in another function'''
# NOTE- we can use the after declear (second) function in currunt or first function like we use name in greet but name is decleare after greet 
'''
def greet():
    print("Good Morning")
    name()
def name():
    print("Myself Shaikh Majid")
    
#so,we need to call only one function which is greet() 
greet() 


# or we can use like this also
def gr():
    print("Good morning")
def nm():
    gr()
    print(" am Shaikh Majid")

nm()
'''




'''
#Q-what is the sequence of given code
print(3)
def fun1():
    print("Hellow")
    print("Good Morning")
print("10+10")
def fun2():
    print("3+5")
    print(3+5)
    fun1()
    print("Good")
print(10+10)

def fun3():
    fun2()
    fun1()
    
fun3()
'''





'''
*****Now we will guess the answer *******
3
10+10
20
3+5
8
Hellow
Good Morning
Good
Hellow
Good MOrning
'''
# i was right




'''
# Q-make 4 special function and give choise to user to choose the function

def add(a,b):
    print("Addition of {} and {} is={}".format(a,b,a+b))
def sub(a,b):
    print("Subtraction of {} and {} is={}".format(a,b,a-b))
def mul(a,b):
    print("Multiplication of {} and {} is={}".format(a,b,a*b))
def div(a,b):
    print("Division of {} and {} is={}".format(a,b,a/b))

def main():
    try:
        a1=input("Enter 1 for Addition\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 for Division\n")
        a=eval(input("Enter Number 1="))
        b=eval(input("Enter Number 2="))

        if(a1=="1"):
            add(a,b)
        elif(a1=="2"):
            sub(a,b)
        elif(a1=="3"):
            mul(a,b)
        elif(a1=="4"):
            div(a,b)
        else:
            print("you have entered something wrong")
    except Exception as e:
        print(e)    
main()
'''    
    

'''        
#.........this is another best way to write the above program
def add():
    print("Addition of {} and {} is={}".format(a,b,a+b))
def sub():
    print("Subtraction of {} and {} is={}".format(a,b,a-b))
def mul():
    print("Multiplication of {} and {} is={}".format(a,b,a*b))
def div():
    print("Division of {} and {} is={}".format(a,b,a/b))


def main():
    try:
        a1=input("Enter 1 for Addition\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 for Division\n")
        
        if(a1=="1"):
            add()
        elif(a1=="2"):
            sub()
        elif(a1=="3"):
            mul()
        elif(a1=="4"):
            div()
        else:
            print("you have entered something wrong")
    except Exception as e:
        print(e)    

a=eval(input("Enter Number 1="))
b=eval(input("Enter Number 2="))

main()
'''






# Q - WAP NUMBER OF DIVISORS PROGRAM
#   - ask the user for number and check how much are divisiors of the number
'''
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

#IMP NOTE here we declear the variable globally to use outside of the function()
#we can not declear it outside and use,yes it is true that if we declear it outside its globle but the same
#name variable inside the function automatically decleared as local, 
# so we need do declear it inside the function Gloabally by using the 'global' keyword
# # and NOTE- the return value does not declear a variable globally,we can save it another variable and can use 


# 1st TYPE - use globle below
def counter():
    global num,count,noncount #IMP NOTE here we declear the variable globally to use outside of the function()
                              #we can not declear it outside and use,yes it is true that if we declear it outside its globle but the same
                              #name variable inside the function automatically decleared as local, 
                              # so we need do declear it inside the function Gloabally by using the 'global' keyword
                              # and NOTE- the return value does not declear a variable globally,we can save it another variable and can use 
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
    
# we have two ways to use function data outside

counter()
# FIRST WAY - we have decleared the variable inside the function but we decleared it global so, we can use it outside
# - use this way if you decleared the variable inside the function
print("Total divisors of {} are {} ".format(num,count))
print("Total non-divisors of {} are {} ".format(num,noncount))
'''









'''
# 2nd TYPE - use return below
def counter():
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
    return num,count,noncount
# we have two ways to use function data outside

# FIRST WAY - here we saving the return variable by function in another variable to make it useful outside the function   
# - use this way if you decleared the variable outside the function

num1,count1,noncount1=counter()
print("mmmmm Total divisors of {} are {} ".format(num1,count1))
print("mmmmm Total non-divisors of {} are {} ".format(num1,noncount1))
'''





