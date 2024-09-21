'''
try:
    num1=10
    num2=0
    r=num1/num2 #10/0 means #its zero define error
    print(r)
except:
       print("there is some eroor,please check")    #this will print because we got eroor in the try block
       
try:
    n1=100
    n2=65
    v=n1-n2+r   #HERE i used the equation which is already in the try block  (6line)
    print(v)

except:
    print("there is error")
    

rr=v*10  #HERE out side the try exept block we use the variable which is inside the try exception block
print("your result is",rr)
# error will be NameEroor:name 'v'is not defined
#() missing error is caould not handle by try-except
'''




#lets try if all try block are correct 
try:
    num1=10
    num2=2
    r=num1/num2 
    print(r)
except:
       print("there is some eroor,please check")    
       
try:
    n1=100
    n2=65
    v=n1-n2+r   #answeris=100-65=35+5=40HERE i used the equation which is already in the try block  (6line)
    print(v)

except:  #here by using print we giving  some sentence
    print("there is error")
    

rr=v*10  #40*10=400 ......HERE out side the try exept block we use the variable which is inside the try exception block
print("your result is",rr) 
#now again we will try this error in the try and exept block
try:
    n1=eval(input("Enter 1st number\n"))
    n2=eval(input("Enter 2nd number\n"))
    n3=eval(input("Enter 3rd number\n"))
    avg=(n1+n2+n3)/0 # in this line we will create error of name-error and zerodivide error
    print("The average of {},{} and {} is {}".format(n1,n2,n3,avg))
except Exception as a:  #above program  by using print we giving  some sentence but we can also use Exception word and then it will print
    print(a)#the actual error.it will print division by zero
    print("found error")
#NOTE:-whenever we have to write an own error we can use print and write error in that, but if we have to write the actual error we can
       #,use Exception word aftre except and save error in variable and print it
       #and if we get more than one error in try it will stop at first code
       #try execute only with the except.both shoud together 
# now after getting an error the error will execute again after the exception block the normal program will execute.ist facility   
print("hiii......am Shaikh Majid")


    