


#________________________________________________________***_________________________STRING_________________________***________________________________________________________



#----------------------------- How to read the sting -----------------------------------

'''
-string='Majid'-------------its called single quotes
-string="Majid"-------------its called double quotes
-string= """SHAIKH
              MAJID"""------------its called triple quotes
                            or we call it doc string which is use to give some information to user about your code




****
Now we will know some keyword about string,
1) type - to know the type of the data #
2) len  - to know the length of the string
3) max  - to know the which character is maximum order number which is based on ASCII(American Standerd CODE For Information Interchange)
4) min  - to know the which character is minimum order number which is based on ASCII(American Standerd CODE For Information Interchange)
5) ord  - to convert character to standerd value of that character according to ASCII
6) chr  - to convert ord value to standerd character of that value according to ASCII

and we will learn in v27 lecture

7)Concatenation - Joint two strings
8)subtraction/Multiplication/Division - All will give the error
9) in - use to check the character is present in string, and use to iterate the loop using condition while condition will be as string
10) index - use to know the index number 
11) Mutable and Immutble 
12) Slicing of string
'''


'''
name="Majid"

print(type(name))
print(len(name))
print(max(name))
print(min(name))

print(ord('M'))
print(ord('a'))
print(ord('j'))
print(ord('i'))
print(ord('d'))

print(chr(77))
print(chr(97))
print(chr(106))
print(chr(105))
print(chr(100))
'''


'''
# IF WE HAVE TO USE THE STRING IN LOOP CONDITION ,WE CANT USE STRING DIRECTLY BECAUSE 'range' BELONGS TO MATH NOT ENGLISH,SO WE CAN USE ONLY LENGTH BY USING 'len' KEYWORD
for i in range(len("MAJID")): # here the length of word is 5
    print(i)
'''



#************** USE OF in KEYWORD *******************
'''
----the 'in' leyword in python return the TRUE if the character present inside the python object,Else it will return FALSE 
-it has two purposes :
    1)to check if a value is present in the 
            -list,
            -tuple
            -range
            -string, etc.
    2)To iterate through a sequence in a *for* loop
'''


'''
#EXAMPLE-

name="MAJID"
print('M' in name)   # if the letter is present inside the string it will answer in the boolean like TRUE.and if letter is not present in the string it will print FALSE  
print('A' in name)
print('J' in name)
print('I' in name)
print('D' in name)

# in above 5 lines we can see only letter is varrying like M then A and J......so here we can use LOOP to print it by making generalized expression
# like----- 
for i in name: # its called generalized expression
    print(i) 
    print(i,end="") # to stop to write in new character in new line 

#NOTE- for i in range(1,10): -------- whenever we use 'range' function we need proviede only mathematical value
#NOTE- for i in name:        -------- whenever we use 'in' or we use it for only string
 
'''



'''
# Q- WAP using 'in' operator using for loop,to print thr ord number of string character 
name="MAJID"

for i in name:
    print("The ASSIC value if {} is {} ".format(i,ord(i)))
'''   


'''
# PRINT A TO Z CHARACTER IN LOWECASE AND UPPERCASE AND PRINT THE ORD NUMBER OF EVERY CODE

import string; # here we import the string package and .
up=string.ascii_uppercase #here we use the ascii_uppercase method to print A to Z
lo=string.ascii_lowercase

for i in up:
    print("The ord of {} is {} ".format(i,ord(i)))
 
for i in lo:
    print("The ord of {} is {} ".format(i,ord(i)))

 
for i in string.punctuation:
    print("The ord of {} is {} ".format(i,ord(i)))


for i in range(33,127):  # the ascii number start from 33 and end 126 of useful character.means total 93 characters 
    print("The character at {} is {}".format(i,chr(i)))
'''



'''
# Q- WAP find  number of 'a' letter in given string
str="hai how are you and hou do yo do"
count=0
for i in str:
    if i=="a":
        count=count+1
print(count)
print(str[6 ])
'''


# Q- WAP find  number of vowel letter in given string

'''
str="hai how are you"
count=0
for i in str:
    if i=='a' or i=='e'or i=='i'or i=='o'or i=='u': #here i used the the or condition and wrote 5 vovel but we can ,but we can use 'in' keyword and measure it,like below  
        count=count+1
print(count)


#str="hai how are you"
count=0
for i in str:
    if i in'aeiou':
        count=count+1
print(count)
'''



#IMP Q-WAP find  number of unique vowel letter in given string (unique men=ans if letter double come so it shoult not count)
'''
str1=""  # like we were using count in the before program here we will group the vowels in epty string  
str2="hai how are you"
for i in str2:
    if i in "aeiou":
        str1=str1+i
print(str1)
'''



#_____________________________________________STRING CONCATENATION_________________________________________________________

''' if we joint or group two strings is called concatenation'''

'''
a=" Shaikh "
b="Majid"
c=a+b                      # c and d both are same
d=" Shaikh " + "Majid"
print(c)
print(d)
if c==d:
    print("YES")

               #errors are,
#print(c-d)    #unsupported operand
#print(c/d)    #unsupported operand

#print(c*d)     #cant multiply sequence by non-int of type 'str'......means we cant multiply two string but we can multiply integer and string like,
print(c*3)

'''




#_____________________________________________STRING INDEX_________________________________________________________
''' strings are ordered sequence of character data. Indexing allow you to access individual characters in a string directly by using a numeric value.
string indexing is zero-based:the first character in the string has index 0,the next is 1,and so on
'''

ms="shaikh majid"

'''
print(ms.index("s"))
print(ms.index("h"))
print(ms.index("a"))
print(ms.index("i"))
print(ms.index("k"))
print(ms.index("h")) #here 'h' is repeated,so we print h index it will print 01 but if we check using index it will show 5
print(ms.index("m"))
print(ms.index("a"))
print(ms.index("j"))
print(ms.index("i"))
print(ms.index("d"))

print(ms[5],ms[6])
'''




# or we can print the index and letter using loop
for i in range (0,len(ms)): # or we can give  condition 'len(ms)' only
    print("The index number of {} is {}".format(ms[i],i))

for i in ms:
    print(i)


for i in ms:
    print(ms.index(i))










