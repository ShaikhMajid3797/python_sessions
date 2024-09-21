'''                 Type Casting'''


'''-in type casting we convert the one data type into another data type'''



'''
    first we will see the int to - 
        -integer to  float
        -integer to string
        -integer to boolean
        -integer to complex

'''                        

'''integer to float'''

num1=100
num2=float(num1)
print(num2)
print(type(num2))

a=10
b=10.2
c=a+b
print(c)         #answer will be 20.2,so a is automatically converted into float so its implicit typecasting
   


'''integer to string'''                                
                                                                                                        
a=100  
b=str(a)
print(b)
print(type(b))

a=100
b=200
c=str(a)         # here the both integer will converted into the string and when we add both a and b the addition will not happen
d=str(b)
print(c+d) # ans = 100200



'''integer to boolean'''
#in this if the integer is 0 so it will provide False otherwise it will provide True ,no matter minus or plus 

a=100
b=bool(a)
print(b) #b=True
print(type(b))  

a=-100
b=bool(a)
print(b)  #b=True
print(type(b))  

a=000
b=bool(a)
print(b)  #b=False
print(type(b))

'''integer to complex'''
a=101  # here we decleare a is integer and then we convert it into complex
b=complex(a)
print(b) #it will print 101+0j,so the integer will consider as a real number not imaginary





'''
    second  we will see the float to - 
        -float to  int
        -float to string
        -float to boolean
        -float to complex

'''                   

''' float to  int'''     

a=1254.255 #we write here float number 
b=int(a)  
print(b) # while printing the a the digit after point will not consider
print(type(b))

#ex
ab=1.32
cd=2.45
ef=int(ab+cd)
print(ef)  #answer will be 3 only




'''     -float to string'''

ss=10.25
dd=15.65
qq=str(ss)
ww=str(dd)
print(qq)
print(ww)
print(qq+ww)# here additon will not happen between two float ,there only print as it is


'''     -float to boolean       '''

ab=20.25
ba=bool(ab)
print((ba))

dd=-20.32
cc=bool(dd)
print(cc)

ss=000
ff=bool(ss)
print(ff)

'''     float to complex'''
print("float to complex")
kk=102.32
nn=2.37
jj=complex(kk) # HERE WE GIVEN ONLY REAL NUMBER
ll=complex(nn) # here also we given only real number 
print(jj,ll) # both will only print not add 

mm=complex(kk,nn) # here we given real and imaginary bith nubers 

print(mm) # here we assining a real value is kk and imaginary value is nn



'''now 3rd one is - 
        -string to  int
        -string to float
        -string to boolean
        -string to complex
        
'''
# NOTE:- if the base value is in float but in string quots ,so it can not convert to the int
# NOTE:- if english leter is present inside the quots, we cant convert it into the int,float and complex because these three are the mathematicl function
    #      but, we can convert it into the boolean and it will answer true ,and if string is empty then it will answer false
            
        
'''         ***string to  int***     '''
#strg='apple'
#int(strg)
#print(strg)

# NOTE:- if the base value is in float but in string quots ,so it can not convert to the int                
string1='122'
string2=int(string1)
print(string2)

'''         ***string to float***     '''
print("string to float")
string11="10.5"
float(string11)
print(string11)

'''         ***string to boolean***     '''
# NOTE:- if english leter is present inside the quots, we cant convert it into the int,float and complex because these three are the mathematicl function
    #      but, we can convert it into the boolean and it will answer true ,and if string is empty then it will answer false

string11='majid' 
str22=bool(string11)
print(str22)

string00=''
str33=bool(string00)
print(str33)


'''         ***string to complex***     '''
#if the mathemathical equation is present so it will answer
'''
string0='125'
string1='225'
string4=complex(string0,string1) 
print(string4)  

#TypeError: complex() can't take second arg if first is a string

its accept only one argument is sting and another should be the float or int
'''

#error....  string0='apple'   \n string2=complex(string0)  \n print(string2)

string0=125
string1=225
string4=complex(string0,string1) 
print(string4)  




'''now 4th one is - 
        -boolean to  int
        -boolean to float
        -boolean to string
        -boolean to complex
'''

val1=True
print(int(val1))
print(float(val1))
print(str(val1))
print(complex(val1))

val2=False
print(int(val2))
print(float(val2))
print(str(val2))
print(complex(val2))

'''now 5th one is - 
        -complex to  int
        -complex to float
        -complex to string
        -complex to boolean
'''


val1=10+20j
#print(int(val1)) #reason of error :-there are two values in complex ,one is imaginary and secind one is real
#print(float(val1)) #reason of error :-there are two values in complex ,one is imaginary and secind one is real
print(str(val1))
print(bool(val1))



