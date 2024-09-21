'''
Python Tuple is a collection of objects separated by commas. In some ways, a tuple is similar to a Python list in terms of indexing, nested objects,
and repetition but the main difference between both is Python tuple is immutable, unlike the Python list which is mutable.

***Creating Python Tuples
           -There are various ways by which you can create a tuple in Python. They are as follows:

Using round brackets
With one item
Tuple Constructor
Create Tuples using Round Brackets ()
To create a tuple we will use () operators.
'''


'''

tup1=("Shaikh Majid",23)
print(tup1)

#-------- tuple accept every data type,
tup2=("Majid",23,23.5875,True,10+5j)

for i in tup2:
    print(i,type(i))



#--------------Tuple are immutable,
tup3=("Majid","Shaikh")
#tup4=tup3[0]="Sajid"  #TypeError: 'tuple' object does not support item assignment
#print(tup4)

# AS we can see the tuple are immutable unlike the list, List are mutable,
l1=["Majid","Shaikh"]
l2=l1[0]="Sajid"
print(l1)





#-------- NOTE - if we are creating one element of tuple and we check the type of tuple it will show the element data type. So, whenever you one element of tuple give ","

name=("Majid")  # as we can see here we have created the the tuple,
print(type(name)) # but here we got the type is 'str'

num=(10)  # same case
print(type(num))

# so at that time you need to give the "," after that one element. Let's see,
n=("Majid",)
m=(10,)
print(type(n))
print(type(m))   # now we got the type is 'tuple'


#-------Duplicates are Allowes in the tuple
num1=(11,25,11,25,658,665,8)
print(num1)




# ----------Indexing in the tuple

#negetive index  -12 -11 -10   -9  -8   -7  -6 -5  -4   -3   -2  -1
#                (55, 33,  66, 45,  85, 93, 28, 66, 5,  36,  623, 6)
#positive index    0   1   2   3    4   5    6  7   8    9   10   11
  

tup1=(55, 33,  66, 45,  85, 93, 28, 66, 5,  36,  623, 6)
for i in range(len(tup1)):
    print("Positive inedx of {} is {} and Negetive Index of {} is {}".format(tup1[i],i,tup1[i],(i-(len(tup1)))))



#---------Slicing in the tuple

alpha=(55, 33,  66, 45,  85, 93, 28, 66, 5,  36,  623, 6)
print(alpha[0:5]) # it will print 0 to 4 index

# alpha[start:end:jumpindex]

print(alpha[-4:10]) # the endind gives the flow direction

print(alpha[0:10:2]) # It will skip the every second value 

#NOTE-The jump index gives the direction to flow. Here we have given the start and end positive but the jumindex is negetive so, it will gives the empty tupe not error
print(alpha[0:10:-2]) #  




#negetive index  -12 -11 -10   -9  -8   -7  -6 -5  -4   -3   -2  -1
#                (55, 33,  66, 45,  85, 93, 28, 66, 5,  36,  623, 6)
#positive index    0   1   2   3    4   5    6  7   8    9   10   11
  

# some test of possible or not possible on tuple
print(alpha[2:11:-2],"Not Possible") # Not Possible
print(alpha[-2:11:2]) # Possible
print(alpha[2:-11:-2]) # Possible 
print(alpha[-2:-11:-2]) # Possible
print(alpha[2:-11:2]) # Not Possible
print(alpha[-2:-11:2]) # Not Possible
'''



'''
****Python Tuple Methods****
Python Tuple - max() Method
Python Tuple - min() Method
Python Tuple - index() Method
Python Tuple - len() Method
Python Tuple count() Method
Python | Reversing a Tuple
Python - Create a List of Tuples
Python | Convert a List into a Tuple
'''




'''
#-------Learn
#Python Tuple - max() Method
#Python Tuple - min() Method
#Python Tuple - index() Method
#Python Tuple - len() Method
#Python Tuple count() Method

abc=("A","a","B","b")
print(max(abc)) # according to ASCII number
print(min(abc))
print(len(abc))


alpha=(55,11,33,66,45,11,85, 93,11,28,66,11,5,11,36,623,6) 
print(max(alpha))
print(min(alpha))
print(alpha.index(623)) # use to know the index of the element of the element


# now we will count the how much '11' tuple have
print(alpha.count(11))  
'''


#Python | Reversing a Tuple
alpha=(55,11,33,66,45,11,85, 93,11,28,66,11,5,11,36,623,6) 
print(alpha[::-1])  


#Python | Convert a List into a Tuple
num1=[22,65,25,"Majid","Shaikh"]
tup1=tuple(num1)
print(tup1)

# Concatanation of tuple

a=(1,2,3,4)
b=(4,5,6,7)
c=a+b
print(c)


