# Q- WAP ask user for radius of a circle and find the circumference and the area of circle 
#    do question in two ways with argumnet and without argument

# .....answer without argument.......
'''
import math;
def circle():
    radious=eval(input("Enter the radius of circle= "))
    diameter=2*radious
    area=math.pi*radious*radious
    circumference=2*math.pi*radious
    print("Area of circle is= ",area)
    print("Diameter of circle is= ",diameter)
    print("circumference of circle is= ",circumference)

circle()
'''



'''
# .....answer with argument.......
import math;
def circle(radious):
    diameter=2*radious
    area=math.pi*radious*radious
    circumference=2*math.pi*radious
    print("Area of circle is= ",area)
    print("Diameter of circle is= ",diameter)
    print("circumference of circle is= ",circumference)

#circle(10)     #this is first way of argument
# radious=eval(input("Enter the vlue of radious= ")) # this is also keyboard pass
#circle(eval(input("Enter the radious of circle= ")))  # this is keyboard argument

rad=25 # this is third way of argumunt
circle(rad)
'''




'''
# .....answer with Default argument.......
import math;
def circle(radious=12): # we have decleared the value of variable while defining a function
    diameter=2*radious
    area=math.pi*radious*radious
    circumference=2*math.pi*radious
    print("Area of circle is= ",area)
    print("Diameter of circle is= ",diameter)
    print("circumference of circle is= ",circumference)
    
#circle()    #it will take the 12 as radious value

circle(25) #here we have given a new value and python always takes a latest decleared value    
'''






#.............Rerurn Concept(concept of function).................
''' The return statement in python is an extremely useful statement used to return the flow of program from the function to the function caller. The keyword return
is used to write the return statement.
Since everything in python is an object the return value can be any object such as – numeric (int, float, double) or collections (list, tuple, dictionary) or 
user defined functions and classes or packages.

The return statement has the following features -
Return statement cannot be used outside the function.
Any code written after return statement is called dead code as it will never be executed.
Return statement can pass any value implicitly or explicitly, if no value is given then None is returned.
'''





'''
#this is normal function 
def add():
        a=eval(input("Enter the number1="))
        b=eval(input("Enter the number2="))
        Add=a+b
        print("Addition of {} and {} is= {}".format(a,b,Add))
        
add()
#ms=add()      #this will not work without function but by using function we can do it
#print(ms)     # means function is not returning the value 
'''





'''
#  now we have to use the variable of function at outside the function by using return function
def add():
        a=eval(input("Enter the number1="))
        b=eval(input("Enter the number2="))
        Add=a+b # we didnt use print so nothing will be print 
        mul=a*b
        return Add,mul  #here we are just giving authorinty to user to have the ADD variable by using function name


#add() #only input will take,answer will not print


# here ......abc=Add-additon ,bcd=mul=Multiplication
# WE HAVE RETURNED TWO VALUES ,SO WE USED THE TO VARIABLE TO SAVE
abc,bcd=add() # NOTE-here we are saving the Add in abc and mul in bcd variable from return  (***return Add,mul***) 
print(abc)    # here we can see the abc means ADD and bcd means mul
print(bcd)
print(abc,bcd)
'''




'''
# Q-WAP ask user for 3 numbers and find the average (without argument) 
def avgcal(): 
    a=eval(input("Enter Number 1 = "))
    b=eval(input("Enter Number 2 = "))
    c=eval(input("Enter Number 3 = "))
    average=(a+b+c)/3
    return a,b,c,average

d,e,f,AVG=avgcal() # here we have saved the 3 returned (return a,b,c,average) variable of funtion in outside variable,  
print(d)           # and that are a=d,b=e,c=f,average=AVG
print(e)
print(f)
print(AVG)
'''




'''
# Q-WAP ask user for 3 numbers and find the average (***with argument***) 
def avgcal(a,b,c):
    sum=a+b+c 
    average=sum/3
    return sum,average

SUM,AVG=avgcal(20,30,40) # here we have saved the 2 returned (return sum,average) variable of funtion in outside variable,   
print(SUM)                         # Sum==sum and AVG==average
print(AVG)
'''




'''
# Q-WAP ask user for 3 numbers and find the Biggest Number (***without argument***) 
def bignum():
    a=eval(input("Enter the Number 1= "))
    b=eval(input("Enter the Number 2= "))
    c=eval(input("Enter the Number 3= "))
    
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

#bignum()     # here only function will run but not will print big value
#print(bignum()) # here it will return the big value

#next is call the function and save it in another variable

biggest_number=bignum()
print("The BIGGEST NUMBER is= ",biggest_number)
'''



'''
# Q-WAP ask user for 3 numbers and find the Biggest Number (***with argument***) 
def bignum(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c


#next is call the function and save it in another variable and give argument of three values

biggest_number=bignum(20,30,90)
print("The BIGGEST NUMBER is= ",biggest_number)
'''



#...Q-WAP create a 4 math function and directly return it without making the function inside the function
'''
def add(a,b):
    return(a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    return (a/b)

ADD=add(10,30)
SUB=sub(55,33)
MUL=mul(10,42)
DIV=div(55,6)
print(ADD)
print(SUB)
print(MUL)
print(DIV)
'''











































