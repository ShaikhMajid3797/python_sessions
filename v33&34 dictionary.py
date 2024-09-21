'''
*********************************************----------------Dictionaries-----------------------*********************************************************

A Python dictionary is a data structure that stores the value in key: value pairs.

Example: Here, The data is stored in key: value pairs in dictionaries, which makes it easier to find values.

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)

Output
{1: 'Geeks', 2: 'For', 3: 'Geeks'}


Python dictionaries are essential for efficient data mapping and manipulation in programming. To deepen your understanding of dictionaries and explore 
advanced techniques in data handling, consider enrolling in our Complete Machine Learning & Data Science Program. This course covers everything from basic dictionary
operations to advanced data processing methods, empowering you to become proficient in Python programming and data analysis.

Python Dictionary Syntax
dict_var = {key1 : value1, key2 : value2, …..}

*What is a Dictionary in Python?
-Dictionaries in Python is a data structure, used to store values in key: value format. This makes it different from lists, tuples, and arrays as in a dictionary each key
has an associated value.

Note: As of Python version 3.7, dictionaries are ordered and can not contain duplicate keys.

*-How to Create a Dictionary
      -In Python, a dictionary can be created by placing a sequence of elements within curly {} braces, separated by a ‘comma’. The dictionary holds pairs of values, 
one being the Key and the other corresponding pair element being its Key:value. Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t 
be repeated and must be immutable.

Note – Dictionary keys are case sensitive, the same name but different cases of Key will be treated distinctly.

The code demonstrates creating dictionaries with different types of keys. The first dictionary uses integer keys, and the second dictionary uses a mix of string and
integer keys with corresponding values. This showcases the flexibility of Python dictionaries in handling various data types as keys.
'''

#------------------------------------------Let's see which combination is allowed and which is not allowed----------------------------------------------------
'''
# we write the data in key:value form  and here we taken the string as key and integer as value
abc={'mukhtar':40, 'muneer':35,'sameer':30,'sajid':27,'majid':23} # here mukhtar is key and 40 is value
print(abc)


#q1={1,2,3:"String"}  # FAIL -  invalid syntax
#print(q1)



#here we taken the integer as key and string as value
bcd={40:'mukhtar', 35:'muneer',30:'sameer',27:'sajid',23:'majid'} # here 40 is key and mukhtar is word
print(bcd)


# here we taken the string as key and list as value
ax={'even':[2,4,6,8],'odd':[1,3,5,7,9]}
print(ax)

#****Here we given the list as key but its not work so, NOTE - list are not allowed as the key
#az={[2,4,6,8]:'even',[1,3,5,7,9]:'odd'} # TypeError:unhashable type: 'list'
#print(az)


# here we given tuple as the key and string as a value so its ALLOWED
az={(2,4,6,8):'even',(1,3,5,7,9):'odd'} # TypeError:unhashable type: 'list'
print(az)


#here we given string as key and tuple as a value
ax={'even':(2,4,6,8),'odd':(1,3,5,7,9)}
print(ax)

# bool:str and str:bool
a1={True:'majid',True:4}
a2={'majid':True}
print(a1,a2)

# lets see dictionary inside the dictionary. and key is string and another dictionary is value.
dict1={"Item_List":{'fruits':'apple'}}  
print(dict1)  #so,its ALLOWED


# lets see dictionary inside the dictionary. and key is another dictionary and string is value.
#dict2={{'fruits':'apple'}:"Item_List"}  
#print(dict2)  #so,its ALLOWED  TypeError: inhashable type: 'dict'


# lets check the duplicates, 
d3={'A':1,'B':2,'A':1} 
print(d3) # so, Duplicates are not allowed in the dictionary. if we write it will skip by default

d4={'A':1,'B':2,'A':14} # and it will take the latest updated value of key  
print(d4)



# lets check case sensitivity 

d5={'A':1,'B':2,'A':14,'b':10}   
print(d5) #so,its case sensitive
'''

#--------------------------NOTE--------------------------------------
'''
- Dictionary is key:value pair'
- at value we can take any data type 
- at key position only list and dictionry will FAIL
- duplicate are not allowed
'''



#----------------- max and min in dictionaries
'''
abc={'mukhtar':40, 'muneer':35,'sameer':30,'sajid':27,'majid':23} # here mukhtar is key and 40 is value
print(abc)
print(max(abc))  # ans is sameer
print(min(abc))

                                    # now sammer is 5 
abc1={'mukhtar':40, 'muneer':35,'sameer':5,'sajid':27,'majid':23} # here mukhtar is key and 40 is value
print(abc1)
print(max(abc1))
print(min(abc1))



bcd={40:'mukhtar', 35:'muneer',30:'sameer',27:'sajid',23:'majid'} # here 40 is key and mukhtar is word
print(bcd)
print(max(bcd))
print(min(bcd))
#NOTE: so the min and max depend on the only *key* value 
'''


#---------------sum

#NOTE:- when we apply sum of dictionry so it will add the key (1 and 4) only not value (2,6)
'''
dic1={1:2,4:6}
print(sum(dic1))
dic2={3:'majid',6:'sajid'}
print(sum(dic2))

# NOTE- sum is possible when the two keys are interger only
#dic3={'majid':3,'sajid':6}
#print(sum(dic3)) # TypeError: unsupported operand types(s) for +: 'int' and 'str'



#---------------------'in' operator
dict1={'ram':25,'rahim':35,'robert':45}
print('ram' in dict1) # using 'in' operator we dedicate to only key not value

print(25 in dict1) # FAIL
#print('ram':25 in dict1) #FAIL and ERROR

# we can see in loop, using 'in' we can get only key
for i in dict1:
    print(i)
    
#--------------------index operator

d1={'ram':25,'rahim':35,'robert':45,}
#print(d1[1]) #here we cant call the data by index because its pair

print(d1["ram"])  # the it will provode the correspoding value which is linked with key

for i in d1:
    print(i) # here we will get only the key
    
for i in d1:
    print(d1[i]) # here we will get only the value
    
for i in d1:
    print(i,d1[i]) # here we will get the key and value both

# Q - can get this same thin uding range operator--------------------ans is NO
for i in range(len(d1)):
    print(i)  # we will get 0 1 2
    print(d1[i])  # so, it is not possible to get the key and value of dictionary using range 
'''     




#----------------------Create Empty Dictionary and Update----------------
'''
# like we update in string and list 
str1="" # empty string
for i in 'apple':
    print(i)
    str1=str1+i
print(str1)

# list update
l1=[i for i in range(20)]
print(l1)

#OR
l2=[]
for i in range(20):
    l2.append(i)
print(l2)


# so in same way we can update the DIctionary also
# step 1:- take empty dictionary
dic1={}
#step2:- update it ..........syntax :- dic_name[key]=value
dic1["Fruit"]="Apple"         #_-------------------------------------------V-I-M-P-------------------------------------------------------- 
dic1[33]=6
dic1[23]="majid"
#step3:- use it(print)
print(dic1)


#-Q- take a empty dictionary and udate your details inside it
bio={}
bio["First Name"]="Majid"
bio["Middle Name"]="Mahemood"
bio["Sir Name"]="Shaikh"
bio["Mobile Number"]=7666331460
bio["Adress"]="Antapur Tq.Degloor Dist.Nanded"
bio["Education"]="Btech in Computer Science & Engineering"
print(bio)

'''

'''
# WAP create a dictionary on basis of two list
name=['ram','rahim','robert']
age=[22,24,56]
dict1={}


print("By using 'in' operator")
for i,j in zip(name,age):
    print(i,j)
                          #dict1[name[i]]=age[i] # we dont need to use here index(name[i]) we can directly tale i and j because we used in operatop in the loop
    dict1[i]=j  
print(dict1)


print("By using 'range' operator")
dic2={}
for i in range(len(name)):
    dic2[name[i]]=age[i]
print(dic2)
'''





#-----------------------------------Dictionary Comprehension-----------------------------------------------------
#-----in above question we used the for loop but we can write answer in one line like,
'''
name=['ram','rahim','robert']
age=[22,24,56]

print( "By using comprehension")
dic3={i:j for i,j in zip(name,age)}
print(dic3)

dic4={name[i]:age[i] for i in range(len(name))}
print("using range in dictionary comprehension\n",dic4)
'''





# Q - WAP take 5 random number and make a dictionary of even and odd with even odd list number
import random;
evl=[]
odd=[]
for i in range(5):
    inp=random.randint(0,5)
    if inp%2==0:
        evl.append(inp)
    else:
        odd.append(inp)

dictx={}
dictx["EVEN"]=evl
dictx["ODD"]=odd

print(dictx)






