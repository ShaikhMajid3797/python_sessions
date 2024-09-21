#______________________________________________________________________________LIST STARTED________________________________________________________________________

'''

Python Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and ArrayList in Java). In simple language,
a list is a collection of things, enclosed in [ ] and separated by commas. 
-The list is a sequence data type which is used to store the collection of data. Tuples and String are other types of sequence data types.
-list can be any data type (heteogenous) (all 5 types string,integer,float,boolean and complex)



We will learn,
-type
-max
-min
-len
-in (for loop)
-range
-index
-mutable
-slice
-methods

'''

'''
#-list can be any data  type (all 5 types string,integer,float,boolean and complex)
d=[1,22.4,"A","B",True,10+5j]
#print(a,b,c,d)

e=[100,100,100] # means duplicate are allowed
f=["Majid",[1,2,3,4]] # LIst in list also allowed
#print(e,f)

a=[1,2,3,4]
print(type(a))
print(max(a))
print(min(a))
print(len(a))


b=["A","B","C","D"]
print(type(b))
print(max(b))
print(min(b))
print(len(b))

c=[1,2,3,4,"A","B","C","D"]
print(type(c))
#print(max(c)) # '>' not supported between instances of 'str' and 'int'
#print(min(c))  # '<' not supported between instances of 'str' and 'int'
print(len(c))

d=[1,22.4,"A","B",True,10+5j]
print(type(d[0]))
print(type(d[1]))
print(type(d[2]))
print(type(d[3]))
print(type(d[4]))
print(type(d[5]))

# or we can use loop here
print("Loop")
for i in d:
    print(type(i))

#for i in range(len(d)):
 #   print(type(d[i]))


# if the list have float or integer content means all element are integer or float so we can add all content by using the sum keyword 
a=[1,2,3.22,4]
print(sum(a))
#b=[1,2,3.22,4,"A"]
#print(sum(b)) # error= unsupported operand types(s) for +: 'float' and 'str'
'''

#__________________________'in' operator in the list______________________________________
'''
d=[1,22.4,"A","B",True,10+5j]

print(1 in d)
print(22.4 in d)
print("A" in d)
print("B" in d)
print(True in d)


print("Loop (in)")
for i in d:
    print(i in d)
    print(type(i))
'''    


#__________________________'range' operator in the list______________________________________
'''
d=[1,22.4,"A","B",True,10+5j]
print("LOOP(range)")
for i in range(len(d)):
    print(type(d[i]))
'''



#__________________________Concatenation in the list______________________________________

'''
# joint two list using the + symbol
e=[100,100,100] # means duplicate are allowed
f=["Majid",1,2,3,4] # LIst in list also allowed
print(e+f)
print(f+e)
a=[1,2,3,4]
b=['a','b','c','d']
print(a+b)
print(b+a)

# here we just print the concatenation of two string. if we have to save it together we need to take another variable like,
c=a+b


# what if we apply list*3 ?
print(c*3) # it will print list 3 times


#print(c/3) # error = unsupported operand types(s) for -: 'list' and 'int'
#print(c-3) # error = unsupported operand types(s) for -: 'list' and 'int'
#print(a-b) # will be fail
#print(a*b) # will be fail
#print(a/b) # will be fail
'''



#_____________________________________________________________INDEX in List__________________________________________________

e=[10,20,30,40,50,60,70,80,90] # means duplicate are allowed
f=["Majid",1,2,3,4] # LIst in list also allowed

'''
print(e.index(30))

for i in e:
    print(i)
    print(e.index(i))


for i in range(len(e)):
    print(e[i]) #e[i] use to dedicate the one element of the list
    print(e.index(e[i])) 

print(e[-1])
print(e.index(10))
for i in range(-len(e),0):
    print(i,e[i])

for i in range(len(e)):
    print("The Poitive Index is {} and Negetive Index is {} of {} ".format(i,i-len(e),e[i]))
'''    


# Q - Find the elements which are having len<3
'''
list1=["Apple","Ball","Cat","Ab","Cd","Ef"]

for i in range(len(list1)):
    if len(list1[i])<3:
        print(i,list1[i])

# by using in operator
for i in list1:
    if len(i)<3:
        print(i,len(i))   
'''


# Q - Find the elements which are having len<3
'''
list1=["App#le","Ba#ll","Ca#t","Ab","Cd","Ef"]

for i in list1:
    if "#" in i:  # we can use the 'in' opereator in condition also
        print(i)

# answer using range operator with count #
count=0
for i in range(len(list1)):
    if "#" in list1[i]:
        print(list1[i])
        count=count+1
print(count)
'''


# IIIIMMMMPPPP
# Q -  Retrive the ball using index
'''
listt=[1,2,3,["Apple","Ball"]]
# IMP NOTE :- Here we have list in list.and in first list we have 4 elemnents. on index 3 we have 4th element which is list and that have two elements.
# so, here we need to use list[index number of that another list][index number of element]

print(listt[3][1])


# IIIIMMMMPPPP
# Q - Retrive the 'Cherry'

ls=[[[[[[["Cherry"]]]]]]] # here we applied 7 square bracket
print(ls[0][0][0][0][0][0][0])  
# retrive 'e' of cherry
print(ls[0][0][0][0][0][0][0][3])


# IIIIMMMMPPPP
# Q - Retrive the car
a=[[[["A","B",[[[1,2,3,["Car"]]]]]]]]
print(a[0][0][0][2][0][0][3][0])
'''


#____________________________________________________Mutable in List_________________________________________________
# the lsit are mutabble means we can chanege the data of the list

#n="Welcome"
#print(n[2]=="L") # that's why strings are immutable

lst=["Apple","Ball","Car","Dog","Ear"]

# now we will solve it like we make changes in string
'''
lst1=[lst[0],lst[1]]
lst2=[lst[3],lst[4]]
lst3=["Cherry"]
lst4=lst1+lst3+lst2
print(lst4) 
'''

'''
# BUT, here we dont need to do that, we can directly change
lst[2]="Cherry"
print(lst)
'''




#________________________________________________________________SLICE in List____________________________________________
'''
# +ve   0  1   2   3   4    5   6   7   8   9  10  11  12  13  14 
listt=[10 ,20, 30, 40, 50, "P","Y","T","H","O","N","a","b","c","D"]
# -ve -15 -14 -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

print(listt[2:14:3])  #p
print(listt[2:14:-3]) #np
print(listt[2:-14:3]) #np
print(listt[2:-14:-3]) #p
print(listt[-2:14:3]) #p
print(listt[-2:-14:3]) #np
print(listt[-2:-14:-3]) #p
print(listt[-2:14:-3]) #np

#NOTE if the slice is not possible means error but the compiler will five empltry [] not error


'''


#__________________________________________________________Methods in the list__________________________________________________________

'''
 'append', 
 'clear',
 'copy', 
 'count', 
 'extend', 
 'index', 
 'insert',  
 'pop',
 'remove',
 'reverse',
 'sort'
'''

#-------Clear and Copy method------------
'''
# copy() - we can copy the data of one list in another list using copy() method

list1=[10,20, 30, 40, 50]
list2=list1.copy()
print(list2)

# and we can do also
list_a=[1,2,2,3,4,5]
list_b=["a","b","c","d"]
list_b=list_b+list_a.copy()
print(list_b)

# clear() - we can delete the all element of list using the clear() method
list_b.clear()
print(list_b)
'''

 



