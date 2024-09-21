'''
here we will learn these methods 
1)casefold()
2)count()
5)replace()
3)index()
4)find()

'''


# ----------STRING-CASEFOLD-------------
''' Its another kind of lowercase function (lower()) . it is also convert the uppercase into lowercase'''


#name="Shaikh Majid"
#print(name.casefold())

#----------------Stringe-Count Method-------------
'''Its use to count the how much letter or words present in that sentence or string'''

'''
string1="Hai how are you"
print(string1.count("a"))
print(string1.count('are'))


ax="ola ola ola"
print(ax.count("ola"))   #ans=3
print(ax.count("ola "))  #ans=2=ola+space
print(ax.count("ol"))    #ans=3

# one another function of count is ,for example if we have to count how much a are present after the 4 index so code will be like,
print("How much 'a' are present after 4th index")
print(ax.count("a",4)) # it menans count 'a' after 4th index

# one another function of count is ,for example if we have to count how much a are present between the 4th index and 6th index, so code will be like,

print("How much 'a' are present between 4th index and 6th index" )
print(ax.count("a",4,6)) # it menans count 'a' between 4th index and 6th index



# Q - How much 'ola' are present in the statemnet,solve by using the if else statement not count count function
string1="ola ola ola"
count=0
for i in range(len(string1)):
    if string1[i:i+3]=="ola":
        count=count+1
print(count)

'''


#________________________REPLACE_____________________
# Q - replace 'r' with '$' 


'''
abc="restart"
print(abc.replace("r","$"))

# Q - if i have to replace only one r of the string
print(abc.replace("r","$",1)) # it means we are replacing 'r' as '$' and 1 means more than one 'r' can be present in string but only one 'r'  should be replace with '$'

# Q - if we have to change the only last 'r' of the string 
a=abc[0]
b=abc[1:].replace("r","$") # if we left empty after colon, by default it will consider as a last character 
c=a+b
print(c)


#or we can do like 
print(abc[::-1].replace("r","$",1)[::-1])
#  here we first reverse the statemnt by [::-1] and the it will become 'tratser' the we replace the first are by using the replace() function the it wll be 't$atser' and
 # then again we will revesr this currunt statement by using the [::-1] 

'''



#__________________________INDEX_________________
'''if we have to know the index of 'c' in the string we can directly know the index like,'''

'''
string1="welcome python"
print("The index of 'c' is ",string1.index("c"))

# Q - in below string find how many are present and what are the indexes of that a
str1="hai how are you and"
# we have seen the two method like first one is if else like
count=0
for i in str1:
    if i=="a":
        count+=1
print("The total a in string is ",count)
# and the seconde one is using count menthod
print(str1.count("a"))


# and we have to print the indexes of all 'a',
for i in range(len(str1)):
    if str1[i]=="a":
        print(i)    

#lets try it in index method
a=str1.index('a') # this will provide only the first occurance of string not like last program ,but we have another way ,
b=str1.index('a',2) # here we entered the start value means it will measure the 'a' from  second index
c=str1.index('a',9) # last we got the 'a' at  8 index so we will start from the next check by 9 index 
print(a,b,c)
'''





#_____________________________________FIND_____________________________________
# we can find the index number of character by using this method
st1="am from india and am in now india"
print(st1.find("i"))     # (8) it will provide the first 'i' occurence of the string ,if weve to print the 2nd 'i' index number then add the start value
print(st1.find('i',12))  # (21)

#if we try to find the string wehich is not present in the string so it will not provide the error it will give the -1,
print(st1.find("x"))



# Q - if try to find the character ehich is not present in the string, Which type of error it will give

#print(st1.index("x")) #sub string not found

print(st1.count("x")) # it will give 0 not error

print(st1.find("x")) # it will give -1 not error



