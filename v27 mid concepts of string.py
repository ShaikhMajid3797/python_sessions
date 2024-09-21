
'''
and we will learn in v27 lecture

7)Concatenation - Joint two strings
8)subtraction/Multiplication/Division - All will give the error
9) in - use to check the character is present in string, and use to iterate the loop using condition while condition will be as string
10) index - use to know the index number 
11) Mutable and Immutble 
12) Slicing of string
13) String Method-
                    i) uppeer()     - Convert the all lowercase characte in uppercase
                   ii) lower()      - convert the all uppercase character in lowercase 
                  iii) capitalize() - convert the only first character of first word of setence or string
                   iv) title()      - convert the all first character of all words of sentence or string 
                    v) swapcase()   - convert the capital letter into small and small letter into capital letter


                    # IMP NOTE - But,after the method operation the orignal string will not change, it will be as it is ,like   
                    
'''




'''
name='Majid'
for i in range(len(name)): # 'range' here we print the letters of string by using index number 'i'
    print("At thr index number = {}, the letter present is = {} ".format(i,name[i]))
                                                                        #'i' at this point if we used the name.index(i) it will give error, 
                                                                        # 'must be str not int' becoz we used the range which belongs to mathematical knowledge

    print(i,end=" ")    # and here we print the inxex numbers but we can print the letter using index number, <stringname>[i],
    

for i in name: #'in' here we print the letter by using the every character by 'i'
    print(i,end=" ")  # used to print letters becoz 'i' in <stringname> belongs to string knowledge  
    print(name.index(i),end=" ")  # here we can use index operator to print index number
'''



'''    

# Q - print like 'the index of p is 0' in both method
str="python"
for i in range(len(str)):
    print("The index of {} is {} ".format(str[i],i))
for i in str:
    print("The index of {} is {} ".format(i,str.index(i),))

'''



# IMP point of negetive and positive index

'''

-6  -5  -4  -3  -2  -1   ............This is negetive index of string and it start from right side with -1   (not zero)
 p   y   t   h   o   n   ...string
 0   1   2   3   4   5   ............This is positive index of string

so, we can get a letter by using negetive index also
'''

'''
str1="python"

print(str1[-1])  # ans=n
print(str1[-2])  # ans=o
print(str1[-3])  # ans=h
print(str1[-4])  # ans=t
print(str1[-5])  # ans=y
print(str1[-6])  # ans=p
'''




# Q- iterate the for loop on string,print letters using negetive index
 #    hint-make a loop of -1 to -6
str1="python"

'''
# 1st Way to print negetive index

print("1st Way to print negetive index")
for i in range(-6,0):
    print("The negetive index of {} is {}".format(str1[i],i))

# 2nd Way to print negetive index

print("2nd Way to print negetive index")
for i in range(-len(str1),0):
    print("The negetive index of {} is {}".format(str1[i],i))

# 3rd way to print negetive index

print("3rd Way to print negetive index")
for i in range(0,6):
    print("The negetive index of {} is {}".format(str1[i],i-6))
'''


'''
# Q- print 'the positive index is 0 and negetive index is -6 of letter p'  
str1="python"

for i in range(0,len(str1)):
    print("The Positive Index is {} and Negetive Index is {} of Letter {}".format(i,i-6,str1[i]))
    
# Q-Improvise it by using -length of string

for i in range(-len(str1),0):
    print("The Positive Index is {} and Negetive Index is {} of Letter {}".format(i+6,i,str1[i]))

# Q-Implement it *while* using while loop
i=0
while i<len(str1):# or we can use the total length of string +1
    print("Positive index is {} and Negetive Index is {} of Letter {}".format(i,i-(len(str1)),str1[i]))
    i=i+1
'''



# Q - Yesterday  we had done some question like how many 'a' letters present in the string by using 'in' operator, today we will do same question using 'range' operator

'''
string1="how are you where are you"
count=0

# Yesterday we done this question using 'in' operator
for i in string1:
    if i=='a':
        count=count+1
print(count)


# now we will do same question using 'range' operator
count1=0
for i in range(len(string1)):
    if string1[i]=='a':
        count1=count1+1
print(count1)
'''    


# _________________________Q- What is Mutable and Immutable Data Types?________________________________________
'''
* Mutable - The data type whose value can be change after creation. ex-List,Dictionaries and Set

* Immutable - The data types whose values cant be change or alter after creation. ex-String,Integer and Types

'''
# example - uderstand by changing the letter of string
#str="python"
#str[0]="P" # Error= 'str' object  does not support *item assignment*  
 
''' NOTE - So, Strings are IMMUTABLE '''





# _________________________Q- What is String Slicing in Python?________________________________________
'''
Python slicing is about obataining a sub-string from the given string by slicing it respectibvely frim start to end.

we use two method to do slicing-

1=slice()  ...(in build), like use slice(stop),slice(strat,stop,step)
2=[:]      ...(array slicing), like use slice[strat:stop]
'''


string1="hai how are you"
print(max(string1))
'''
-15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5  -4  -3 -2 -1
  h  a   i       h   o   w     a  r  e      y  o  u   .........letters of string
  0  1   2   3   4   5   6  7  8  9  10 11  12 13 14   .........index number
'''
#____________ARRAY[::] SLICING___________

'''
print(string1[0:10]) # it will print the characters which at 0 to 9 index number
# here start=0,stop=10-1=9 , direction= +ve

print(string1[0:10:4]) 
# here strat=0, stop=10, step=4(print every 4th letter means skip 3 letters

print(string1[:]) # Nothing mention means entire string will mention

print(string1[::]) # Nothing mention means entire string will mention and step will be 1 means every letter print

print(string1[0:10:-3]) # it will not print anything ,because -3 is not possible


print("Try Possible or Not")
print(string1[2:14:2])      #Possible
print(string1[2:14:-2])     #NOT Possible  (but it will print empty string)
print(string1[2:-14:2])     #NOT Possible  (but it will print empty string)
print(string1[2:-14:-2])    #Possible (it will print only 'i') or like if do,[9:-14:-2]
print(string1[-2:14:2])     # Possible (it will print 'o' only)  
print(string1[-2:14:-2],)    #Not Possible (but it will print empty string)
print(string1[-2:-14:-2])   #Possible  
'''




#__________________________________________________STRING METHODS__________________________________________
'''
1) uppeer()     - Convert the all lowercase characte in uppercase
2) lower()      - convert the all uppercase character in lowercase 
3) capitalize() - convert the only first character of first word of setence or string
4) title()      - convert the all first character of all words of sentence or string 
5) swapcase()   - convert the capital letter into small and small letter into capital letter


# IMP NOTE - But,after the method operation the orignal string will not change, it will be as it is ,like   

'''


'''
name="Shaikh Majid"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.swapcase())

name1="Am fRoM AnTaPuR"
print(name1.upper())
print(name1.lower())
print(name1.capitalize())
print(name1.title())
print(name1.swapcase())


# IMP NOTE - But,after the method operation the orignal string will not change, it will be as it is ,like   

print(name,name1)
'''





'''
# IMP Q- Convert 'welcome' to 'weLcome'
a="welcome"
b="we" 
c="L"
d="come"
e=b+c+d
print(e)
  
# or we can

m=a[0:2]
n=a[3:7]
o='L'
p=m+o+n
print(p)


# we can do it directly using replace method
a=a.replace('l','L')
print(a)
print(a)
'''


 