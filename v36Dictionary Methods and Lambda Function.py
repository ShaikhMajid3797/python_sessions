#-------------------------------------------------Dictionary Methods---------------------------------------------------------------

'''
clear(): This method removes all items from the dictionary, leaving it empty.

copy(): Returns a shallow copy of the dictionary.

fromkeys(): Creates a new dictionary with keys from a given sequence and values set to a value provided.

get(): Returns the value for a key if it exists in the dictionary. If the key is not found, it returns None or a default value if specified.

items(): Returns a view object that displays a list of dictionary's (key, value) tuple pairs.

keys(): Returns a view object that displays a list of all the keys in the dictionary.

pop(): Removes the element with the specified key and returns its value.

popitem(): Removes the last inserted key-value pair and returns it as a tuple.

setdefault(): Returns the value of a key if it is in the dictionary; if not, it inserts the key with a specified value.

update(): Updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs.

values(): Returns a view object that displays a list of all the values in the dictionary.'''


'''
1)'clear'
2)'copy'
3)'fromkeys'  
4)'get'
5)'items' ------done in v35
6)'keys'  ------done in v35
7)'pop'
8)'popitem'
9)'setdefault'
10)'update'
11)'values' -----done in v35
'''





#---------------------clear and copy--------------------------

'''
dic1={'ram':25,'robert':35,'rahim':45}
dic2={}
dic2=dic1.copy()
dic1.clear()
print(dic1)  # it should be empty
print(dic2)



dic1={'ram':25,'robert':35,'rahim':45}
dic2={'majid':23}
dic1.copy()
print(dic1)
print(dic2)  # the data which is already stored in the dic2 diction will erase before copy then all data of dic1 will copy
'''



#---------------------pop, popitem  and del------------------------------
'''
dic1={'ram':25,'robert':35,'rahim':45}
dd=dic1.pop('ram')  # the pop delete the **specify** only not other or not by default last key
print(dd)
print(dic1)


dic1={'ram':25,'robert':35,'rahim':45}
ss=dic1.popitem() # the popiten doesnt take any argumnet so by default it delete the last key:value of dictionary
print(ss)
print(dic1)


dic1={'ram':25,'robert':35,'rahim':45}


del(dic1['rahim'])  # but here we can delete the only specify key

# here we deleted the dile so it will giev name error :not defined
#del(dic1) # here the total dictionary will delete 

print(dic1)
'''




#----------------------fromkeys and get--------
'''

dic1={'ram':25,'robert':35,'rahim':45}
dic0=['Majid','sajid']
dic9={}.fromkeys(dic0,22)

print(dic9)

# another example of formkeys iterable... list,
odd=[1,2,3,4,5,6,7,8,9]
# now we are creating the new list using the formkeys
odddic={}.fromkeys(odd,"odd")
print(odddic)


#---------get
dic1={'ram':25,'robert':35,'rahim':45}
print(dic1.get('ram')) # by using the 'get' we can give the 'key' and get the 'value' of that key.....25

ww=dic1.get('ram')
print(ww) #25

# and we can directly got it like,
print(dic1['robert'])

print(dic1.get(25)) # NOTE-if we give the 'value'  at the place of the 'key' and it will give 'None' ...... not error

#NOTE- but if we give the key which is not present in the dictionary and try to find out by 'dictionary['key']', it will give key error like,
print(dic1["Majid"])  # so this is the diffrence between 'get' and 'dictionary['key']'


print(dic1.get("majid")) # NOTE- if we key name and that is not present in the dictionary it will give 'None' ......not error
'''


#----------------------------------9)'setdefault'
'''

d1={}
d1.setdefault('Majid',"CSE Student") # here we given key and value also
print(d1)

d1.setdefault("Sajid") # here we did not given any 'value', so it will take NONE by default
print(d1)
d1.setdefault('Courses',["DS","WD","CC"])

d1.setdefault("Majid",88)
print(d1)
# NOTE -  we cant change the value of key ehich is alrady decleared using the setdefault. but we can change it normally

'''

#--------------------update
'''

dic1={'a':3,'b':5,'c':6,'d':8}
dic2={'a':54,'b':5,'c':99,'d':8,'f':88}
dic1.update(dic2)
print(dic1)  # so we can update the keys of the dictionary by using updated dictionary 

dic3={'a':3,'b':5,'c':6,'d':8}
dic4={'a':54,'b':5,'c':99,'d':8,'f':88}  # NOTE-duplicates are not allowed in the dictionaries
dic4.update(dic3)
print(dic4)


a1=[(9,7),(5,6),("MAjid",23)] # IMP NOTE - here we given the tuple inside the list and we got it as a [(key:value)] in the dictionary
b1={}
b1.update(a1)
print(b1)
'''





#-------------------------------------------------------------------Lambda Function---------------------------------------------------------------------------


#------------------one argument lambda function

'''
def add(x):
    return(x+10)
print(add(33))

# we write same program in lamda function,

# before writing a lambda function we ask 2 question to ourself,
#---1--- How many argumnet are presennt or we need?  : 2...(x,y)
#---2--- What are you returning ? : (x+y)
# and lambda function format is : lambda <argumnet>:<output>


add1=lambda x:x+10  # here we written lambda function, and saved in the 'add1' variable 
print(add1(10)) # and we called it by giving the one argumnet


# Q- am giving the normal (def) function by using it implement lambda function
def square(x):
    return x*x 

print("Answer by def function",square(4))

# answer in lambda
lam_square=lambda x:x*x
print("Answer by Lambda",lam_square(8))


# Q- am giving the normal (def) function by using it implement lambda function
def cube(x):
    return x*x*x 
print(cube(6))
# answer in lambda
lam_cube=lambda a:a*a*a
print(lam_cube(9))
'''


#---------------Two argumnet lambda function 
'''
# def function of two argument
def add(x,y):
    return x+y
print(add(5,9))

# same lambda function of two argumnet

add1=lambda a,b:a+b
print(add1(55,21))

# Q-----Averege of three numbers using lambda
avg=lambda a,b,c:(a+b+c)/3
print(avg(10,40,30))

# implement average function c as default parameter
avg2=lambda a,b,c=20:round((a+b+c)/3,2) # here w eround it means it will peovide only two number after decimal
print(avg2(51,99)) 

'''

#---------------------if else in lambda function

# format: lambda <arguments>:<if_output> if <condition> else <else_output>

# Q-create a grater function uding lambda function 
gre=lambda a,b: a if a>b else b 
print(gre(5,14))






