#_____________________________________WHAT WE HAVE TO LEARN BASIC OF PYTHON_________________________________________________
'''
*Basic Syntax

*Data Types

*Type Casting

*Overviev if Package
    -like Random and Math

*eval,input,sep='' and end=''

*Conditional Statement (if,elif,else,break)

*Function
    -without argument
    -with argument
    -default argument
    -function in function
    -return function
*try and exception

* For Loop

* While Loop  
'''


#NOTE- Here we compleate the Basic python and the next DATA STRUCTURE topic of python are
'''
-string
-list
-dictionary
-tuple
-set
-lambda function
-file handling
'''

# NOTE - then the 3rd level of python will we OOPs(Object Oriented Programming)
'''
-Class
-Object
-Method
-Inheritance
-Polymorphism
-Data Abstraction
-Encapsulation
'''


#____________________________________________________________________________________________________________________________________

'''
we have learned Data Types,
1= integer
   a=binary(2)
   b=octa(8)
   c=hexa (16)

2= float 
3= string
   a= single quouts
   b= double quouts
   c= tripple quouts........when we have to write some information,then we use the tripple quouts
   
'''
number1= True
num2= False
print(type(number1))
print(type(num2))
nm= 100 #here we save 100 integer in the nm
mn=nm # here we save nm in mn variable
print(mn) # so here we use mn to print it


a=100  # here  we save 100 in a
b=200  # here we save 200 in b
a=b    # here b saved in a so now a=200
b=a    # again we save a=200 in b ,so b=200
b=500  # here we declear the new b variable and saved 500
print(a,b) # here python will take both latest variable value , so a will be third line value a=200 and bwill be latest value of b=500




#        ***complex conjugate***
#                - here we use a letter in the numericle like 3+5j....j indicate the the complex data type
#                  - its always use din numericle

comp= 3+5j      #-always use the j after number to define the complex 

# lets see thr type of it
print(type(comp)) 

# now see the f=directory of complex conjugate
print(dir(comp))

# so we have seen in the directory we have seen some methods like conjugate ,imag,real
# - CONJUGATE= by using conjugate method we can change the sign of imaginary number(+5j converted to -5j) 
# - IMAG= by using image methon we an know the  imaginary number (+5)
# - REAL= by using real we can know the real number which is(3)

print(comp.real)   #<pname>.<methodname>
print(comp.imag)
print(comp.conjugate())



#now we will define it in another way that is complex(real,imag)

comp2=complex(10,50) # here we did not define any j to define complex , we directly use the cmplex
print(comp2)  # so here 10 is real value and 50 is imaginary value


cmp=(complex()) # if we did not  mention any value inight thr complex it will consider all 0.its also called defsult argumrnt
print(cmp) # it will provide 0j not 0+0j



 