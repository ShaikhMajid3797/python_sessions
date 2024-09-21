'''
# Q-WAP print hellow three times using for loop
for i in range(3):
    print("Hello Majid ",i)
'''


      
'''
# Q- print AAA BB CCC in 3 loop
for i in range(3):
    print("A")
for j in range(2):
    print("B")
for k in range(3):
    print("C")
'''


'''
# Q- print AAA BB CCC in 1 loop
for j in range(7):
    if j<3:
        print("A")
    elif j>2 and j<5:
        print("B")
    elif j>4 and j<8:
        print("C")   
'''


'''
# Q-#  print A B A B A B  CCC in 1 loop
for i in range (10):
    if i==1:
        print("A")
    elif i==2:
        print("B")
    elif i==3:
        print("A")
    elif i==4:
        print("B")
    elif i==5:
        print("A")
    elif i==6:
        print("B")
    elif i>6 and i<10:
        print("C")
        
        
# Q-#  print A B A B A B  CCC in 2 loop

for i in range(3):
    print(" A","\n","B")
for j in range(3):
    print("C")   
'''      
        

'''
# Q-get a square of the number 10 to 15 using loop
for i in range(10,16):
    print("Square of {} is {} ".format(i,i*i))
'''    
    


'''    
# Q- get two numbers from the user and find the square between all numbers
a=eval(input("Enter the Number 1= "))
b=eval(input("Enter the Number 2= "))
for i in range(a,b+1):
    print("Square of {} is {} ".format(i,i*i))
'''



'''
# write same code in function without argumnet
def square():
    a=eval(input("Enter the Number 1= "))
    b=eval(input("Enter the Number 2= "))
    for i in range(a,b+1):
        print("Square of {} is {} ".format(i,i*i)) 

square()
'''

'''
# write same code in function with argumnet
def square(a,b):
    for i in range(a,b+1):
        print("Square of {} is {} ".format(i,i*i)) 
    
square(10,20)
'''

'''
# write same code in function default  argumnet
def square(b,a=0):
    for i in range(a,b+1):
        print("Square of {} is {} ".format(i,i*i)) 
    
square(30)
'''

'''
#NOTE- we can directly take input in loop condition block 
for i in range(eval(input("Enter a Numer1=")),eval(input("Enter a  Number2="))+1):
    print("The Square of {} is {} ".format(i,i*i))
'''        


'''
# Q- WAP ask the user 5 times for 5 number and find the square of given number

for i in range(5):
    num=eval(input("Enter the Number {}= ".format(i+1)))
    print("The Square of {} is {} ".format(num,num*num))
'''    



'''
# Q - ask user for 5 times random number between 1 to 20 and find out the srquare of that number
import random;
for i in range(5):
    num=random.randint(1,20)
    print("The Square of {} is {}".format(num,num*num))
'''    


'''
# Q-print which number is odd and which number is even between 10 to 30
for i in range (10,30):
    if i%2==0:
        print("{} is EVEN NUMBER".format(i))
    else:
        print("{} is ODD NUMBER".format(i))
'''        




'''
# Q- get a random number 5 times between 10 to 30 and find it EVEN or ODD 
import random;
for num in range(5):
       a=random.randint(10,30)
       if a%2==0:
           print("{} is EVEN NUMBER".format(a))
       else:
           print("{} is ODD NUMBER".format(a)) 
'''               


'''
# Q- get a random number 5 times between 10 to 30 and find it EVEN or ODD using function and loop 
def even_odd():
    if a%2==0:
           print("{} is EVEN NUMBER".format(a))
    else:
           print("{} is ODD NUMBER".format(a)) 


import random;
for num in range(5):
       a=random.randint(10,30)
       even_odd()
'''



# Q-ask the user for random number between 1 to 10 for 3 times and take random number once throuh random package and try to match it.if its match print win or if not match print loss
# give 3 chances to user to give number
import random;
random_number=random.randint(1,10) 

for i in range(3):
    num=eval(input("Enter a Number between 1 to 10 = "))
    
    if num>10 or num<1:
        print(" You have entered wrong number,You have lossed this chance")
    
    elif random_number==num:
        print("You Won the game\nRandom Number is={} \n\nAnd you have entered={}".format(random_number,num))
        break #we use break word to stop the loop here because our required from the loop is complited
    
    elif i==2:
        print("*****You Lossed the game*****")
    
    else:
        print("\nYou have Lossed this chance and you have only {} \n And you have entered={}".format((2-i),num))
        
    
    













