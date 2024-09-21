
#-----------------count------------------
'''
#  we can count the element how much we have
list1=[10,20, 30,10, 40, 50]

print(list1.count(30))

#------------index------------------
# if we have to know the index of the element
print(list1.index(10))

# Q -   find index of 2nd 10
# here we will find the first index and then we will at that index number in the next index operation
mm=list1.index(10)

print(list1.index(10,mm+1)) # here we mentioned that search 10 and start from the next letter(+1) of the first 10 
'''




#--------------append() method-----------------------------
#Elements can be added to the List by using the built-in append() function. Only one element at a time can be added to the list by using the append() method,
#for the addition of multiple elements with the append() method, loops are used.
# NOTE -using append(x), we can add element at the end of the list. If we have to add the element at desired position we need to insert() method

'''
list1=[10,20, 30, 40, 50]
print(list1)
list1.append(60) # we can add only one element at a time
print(list1)


# if we append list inside the list,
list1.append([99,98,97])
print(list1)


for i in range(1,10):
    list1.append(i)
print(list1)



# Q - input list [1,2,3,4,5] and create new list of square of numbers [1,4,9,16,25]
a=[1,2,3,4,5]
b=[]

# using range

#for i in range(len(a)):
 #   c=a[i]*a[i]
  #  b.append(c)
#print(b)

# using in
for i in a:
    d=i*i
    b.append(d)
print(b)



# Q - capitalized the first letter of all string and save in list
list_1=["hyderabad","bengluru","delhi"]
ss=[]     
for i in range(len(list_1)):
    r=list_1[i].capitalize()
    ss.append(r)
print(ss)

for i in range(len(list_1)):
    print(list_1[i].capitalize())

#ones again we add the 3 words
for i in list_1:
    print(i.capitalize())
    ss.append(i.capitalize())
print(ss)

# Q - Re trive the elements those have #
ab=["h#d","bang#luru","delhi"]
cd=[]
for i in ab:
    if "#" in i:
        cd.append(i)
print(cd)
'''



#------------------list comprehension------------------------
'''
-code in single line >> speed the code
-A Python list comprehension consists of brackets containing the expression, which is executed for each element along with the 'for' loop to iterate over 
each element in the python list,

syntax:-

new_list=[expression(element) for element in oldList if condition]

-expression: Represents the operation you want to execute on every item within the iterable.
-element: The term “variable” refers to each value taken from the iterable.
-iterable: specify the sequence of elements you want to iterate through.(e.g., a list, tuple, or string).
-condition: (Optional) A filter helps decide whether or not an element should be added to the new list.
Return:The return value of a list comprehension is a new list containing the modified elements that satisfy the given criteria.

Python List comprehension provides a much more short syntax for creating a new list based on the values of an existing list.
'''

'''
a=[1,2,3,4,5]

b=[i*i for i in a ] # here we didnt apply any condition.we just calculate ( and condition is optional)
print(b)

# after applying condition
ab=["h#d","bang#luru","delhi"]

cd=[i for i in ab if "#" in i]
print(cd)

# Q - capital first letter  
list_1=["hyderabad","bengluru","delhi"]
ss=[i.capitalize() for i in list_1 ] # here we did not given any condition and and done the expression at the start
print(ss)    


# Q - create a list of 0 to 20 numbers using list comperhension
num20=[i for i in range(0,21)]
print(num20)


#  Q - find the elements which size is less then 3 , using 3 method , for (range) loop,for (in) loop and list comprehension
ax=['aabc','abc','ab','a'] 

# 1st ans
am=[]
for i in range(len(ax)):
    if len(ax[i])<3:
        am.append(ax[i])
print(am) 

aw=[]
for i in ax:
    if len(i)<3:
        aw.append(i)
print(aw)

# 3rd ans
asd=[i for i in ax if len(i)<3]
print(asd)



# Q - find which number is even and which number is odd and make special list for both on 3 method 
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i%2==0:
        print("{} is Even".format(i))
    else:
        print("{} is Odd".format(i))

#ans by meth 1 for (range) loop
ev1=[]
od1=[]
for i in range(len(a)):
    if a[i]%2==0:
        ev1.append(a[i])
    else:
        od1.append(a[i])
print("ans type1 EVEN LIST IS = ",ev1,"ODD LIST IS = ",od1)

#ans by meth2 for (in) loop
ev2=[]
od2=[]
for i in a:
    if i%2==0:
        ev2.append(i)
    else:
        od2.append(i)
print("ans type 2 EVEN LIST IS = ",ev2,"ODD LIST IS = ",od2)

#ans by meth 3 list comprehension
ev3=[i for i in a if i%2==0]
od3=[i for i in a if i%2!=0]
print("ans type 3 EVEN LIST IS = ",ev3,"ODD LIST IS = ",od3)

# in above list comprehension we used the line code , but we can use else also in the [].......like,

# NOTE Syntax :-  [<if_output> <if condition> <else> <else output> <for loop>]

list5=[ "Even {}".format(i) if i%2==0 else "Odd {}".format(i) for i in a] 
print(list5)

'''




#-----------insert-----------
'''

# NOTE -using append(x), we can add element at the end of the list. If we have to add the element at desired position we need to insert() method
list1=[10,20, 30, 40, 50]

print(list1)
list1.insert(0,80)   # list.index(a,b) - where, a = on which index you have to insert the vlaue , b=which data you have insert  
print(list1)            # - and we can add only one element using insert method at desired location




#--------------------extend--------------
#Other than append() and insert() methods, there's one more method for the Addition of elements, extend(), this method is used to add multiple elements at the same time 
#at the end of the list.
# NOTE: append() and extend() methods can only add elements at the end.
list1=[10,20, 30, 40, 50]
print(list1)
list1.extend([10,"A","MAJID"]) # NOTE- add element using the [] 
print(list1)



# in concatenation of two list we need to make another variable to save new list but in extend we can insert the another list in the list

a=[1,2,3,4]
b=['a','f','s']
a.extend(b)
print(a)

#-------------iterable in python------------
# ieteate means we are adding the object in list one by one 

a.extend("Python") # here we iterate the python now the all letters will save in the list 
print(a) 
a.append("Python")
#a.extend(10) #TypeError: int object is not iterable it takes in list[]. and if we have to iterate string we can
print(a) 







# append() vs entend() vs concatanation

1)Append
        -when we do apppend the append data type can be any type int,str or list

    -list1=[1,2,3,4]
    -list2=['a','c','d']
    -list1.append(list2)
    -list1=[1,2,3,4,['a','c','d']]    

2)Extend
        -extend update the element of any other list in currunt list.
       
        -list1=[1,2,3,4]
        -list2=['a','c','d']
        -list1.extend(list2)
        -list1=[1,2,3,4,'a','c','d']    

3)concatenation 
                -in concatanation we need to make 1 new variable to save the concaneted list but in extend we dont need any new variable
                
                -list1=[1,2,3,4]
                -list2=['a','c','d']
                -list3=list1+list2
                -list3=[1,2,3,4,'a','c','d']    


'''





'''
#--------------------------reverse------------------------------
list1=[10,20, 30, 40, 50]

# we can reverse the all element of the list
list1.reverse()
print(list1)

#--------------------remove--------------
# if we have to remove the element of the list we can use remove method
list1.remove(50) # we need to mention the element in the () not index number of that value
print(list1)
'''

#------------pop method--------------------
#pop() function can also be used to remove and return an element from the list, but by default it removes only the last elementof the list, to remove an element from,
# a specific position of the List, the index of the element is passed as an argument to the pop() method.


'''
list1=[10,"m",55,"wwwe",44.36]
print(list1)

list1.pop() #by default it removes only the last elementof the list, 
print(list1)

#to remove an element from,a specific position of the List, the index of the element is passed as an argument to the pop() method.
list1.pop(2)
print(list1)



# -------del - use to delete the whole list

#NOTE - del(list) is a leyword not method 

del(list1[1]) # index 1 - 'm' will be delete  
print(list1)
del(list1)
#print(list1) #NameError : name 'list1' is not defined.Did you mean:'list'
  




#----------------sort------------------
#Sort the list in ascending order and return None.
#The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).
#If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.
#The reverse flag can be set to sort in descending order.

# if we have to sort out the list of same datatype in acending order we can use sort()
listt=[5,66,1,44,2,88,9,5,48,5,95,585,255,5,]
listt.sort()
print(listt)

listal=["z","f","r","y","w","c","c","a","A"]
listal.sort()
print(listal)

# IMP if we have to sort out the list of same data type in decending we can use 'list.sort(reverse=list)' 

listt=[5,66,1,44,2,88,9,5,48,5,95,585,255,5,]
listt.sort(reverse=listt)
print(listt)

listal=["z","f","r","y","w","c","c","a","A"]
listal.sort(reverse=listt)
print(listal)

# NOTE - we cant sort the list which content more than one data type,
#a=[3,2,1,"c","b","a"]
#a.sort()
#print(a) # TypeError: '<' not supported betweeen instances of 'str' and 'int'
'''




#_-------------------------------------zip--------------------------------------
# Q - if we have two list name and age and both element are releted to each othe like 'Ram age is 25'

'''
name=["Ram","Robert","Rahim"]
age=[25,35,45]

for i in range(len(name)):
    print("{} age is {} ".format(name[i],age[i]))

# we need here two list ......we can use the zip method to solve this question like,
for i,j in zip(name,age):
    print(i,j)

# Q - add element using list comprehension and zip
ad=[100,200,300]
af=[25,50]

add=[i+j  for i,j in zip(ad,af)]
print(add)
'''


# Q - take five question in a list and take 5 answers in the another list and . print every question and get answer from user.if answer is match by answer which
#     present in the answer list if its correct give 1 mark . and finally print how much aanswer are correct or wrong and how much marks you got
'''
qes=["Who is PM of India :- ","Who is President of India :- ","Who is President of USA :- ","Who is the CM of Delhi :- ","Who is CM of Maharashtra :- " ]
ans=["Narendra Modi","Draupadi Murmu","Joe Biden","Arvind Kejrival","Eknath Shinde"]

mark=0
for i,j in zip(qes,ans):
    print("")
    question=input(i)
    if question == j or question == j.lower():
        print("Your answer is correct")
        mark=mark+1
    else:
        print("Your Wrong")

print("your {} answers are correct and {} answer are wrong\nYour got total mark is {}".format(mark,len(qes)-mark,mark))
'''


# Q - find max value of list
ax=[66,35,2,58,5,5,8,8,5,96,98,85,556,69,9,85,66,6]
max=0
for i in ax:
    if i>max:
        max=i
print(max) 
