
'''
we are going to learn-
1)strip() - if we have to remove the all whitespaces of string we use it
2)lstrip() - if we have to remove only left side whitespace we use l strip
3)rstrip() - if we have to remove only right side whitespace we use r strip
4)stratswith() and endswith()
5)isalpha/isnumeric/isalnum
6)Spilt
'''




#_______________________________________________String - strip() method________________________________________________
'''
When a developer wishes to remove characters or whitespace frim the begenning or end of a string,the strip() function in python comes in handy:
-the strip() function assist in removing characters from the begenning or end of the string for characters supplied as argumrnt to the strip() function.
-if the string has no whitespace and the characters argument is not supplied,the string it returned as it is.
-it is also beneficial to elimate the whitespace from the beginning and end of the argument.  
'''

'''
we are going to learn-
1)strip() - if we have to remove the all whitespaces of string we use it
2)lstrip() - if we have to remove only left side whitespace we use l strip
3)rstrip() - if we have to remove only right side whitespace we use r strip
4)stratswith() and endswith()
5)isalpha/isnumeric/isalnum
6)Spilt

When a developer wishes to remove characters or whitespace frim the begenning or end of a string,the strip() function in python comes in handy:
-the strip() function assist in removing characters from the begenning or end of the string for characters supplied as argumrnt to the strip() function.
-if the string has no whitespace and the characters argument is not supplied,the string it returned as it is.
-it is also beneficial to elimate the whitespace from the beginning and end of the argument.  
'''


'''
name ="   Shaikh Majid     "
print(name.strip())
print(name.rstrip())
print(name.lstrip())
'''



# Q - Extract the python,anaconda and nareshit from python.anaconda@nareshit.com

'''
string1="python.anaconda@nareshit.com"
print("First Name:- ",string1[:string1.find(".")])
print("Second Name:- ",string1[string1.find(".")+1:string1.find("@")])
print("Third Name:- ",string1[string1.find("@")+1:string1.find(".",string1.find(".")+1)])
                                                                  # in this find function we give the "." and then give the ','  and put the agin one find function and +1
                                                                  # it means find the "." and the skip 1st "." and start the search after "." plus one character(+1)

email="shaikh.majid@tcs.com"
print(email[:email.find(".")])
print(email[email.find(".")+1:email.find("@")])
print(email[email.find('@')+1:email.find(".",email.find(".")+1)])

print(email[0:email.find(".")])
print(email[email.find(".")+1:email.find("@")])
print(email[email.find("@")+1:email.index(".",7)])# here we have another way which is we will consider the stop of string is the "." after the 7 index number


name="Shaikh Majid Mahemood"
print(name[:name.find(" ")])
print(name[name.find(" ")+1:name.find(" ",name.find(" ")+1)])

print(name[name.index(" ",name.index(" ")+1)+1:len(name)])
           # in this we write that, start whenever we got space and skip one space and skip second space and start with first letter 
'''


# Q - Extract the given 3 and other digit after decimal point
'''
num="3.1489"
print(num[0:num.find(".")])
print(num[num.find(".")+1:])
'''

#____________________________________STARTSWTH-ENDWITH_____________________________________________

'''
st='hai how are you'
print(st.startswith('hai')) # if the string start with the word 'hai' it will give response true
print(st.startswith('ha'))  # true
print(st.startswith('h'))   # true

print(st.endswith("you")) # all true
print(st.endswith("ou"))
print(st.endswith("u"))
'''




#____________________________________________SPLIT______________________________________________
'''python string split() method splits a string into a list of string after breaking the given string by the specified separator'''

st="Shaikh Majid"
print(st.split( "h")) #here it will split the string into the list and inbracket 'h' means skip the h and devide the string into two parts when the h comes 

name="shaikh majid,from the nanded"
print(name.split(",")) # here also string will be divide into 2 parts ,before comma and after comma






#___________________________________________Some extra basic method__________________________________________________________
'''
'isalnum',
'isalpha',
'isascii',
'isdecimal',
'isdigit',
'isidentifier',
'islower',
'isnumeric',
'isprintable',
'isspace',
'istitle',
'isupper',
'''


#try this all string on above methods
'''

naam="Shikh Majid"
naam="123 Majid"
naam="1234"
naam="MAJID"
naam=" "
naam="aaa"
print(naam)
print(naam.isalnum()) # it use to check that the string is alphanumeric if its yes so it will print'True' otherwise 'False'

print(naam.isalpha()) # it use to check that the string is alphabatic if its yes so it will print'True' otherwise 'False'

print(naam.isascii()) #Return True if all characters in the string are ASCII, False otherwise.

print(naam.isdecimal())#Return True if the string is a decimal string, False otherwise.A string is a decimal string if all characters in the string are decimal and 
                        #there is at least one character in the string.

print(naam.isdigit()) #Return True if the string is a digit string, False otherwise.A string is a digit string if all characters in the string are digits and 
                        #there is at least one character in the string.

print(naam.isidentifier())#Return True if the string is a valid Python identifier, False otherwise.Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as "def" or "class".

print(naam.islower()) #Return True if the string is a lowercase string, False otherwise.A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

print(naam.isnumeric()) #Return True if the string is a numeric string, False otherwise.A string is numeric if all characters in the string are numeric and there is at least one character in the string.

print(naam.isprintable()) #Return True if the string is printable, False otherwise.A string is printable if all of its characters are considered printable in repr() or if it is empty.

print(naam.isspace())  #Return True if the string is a whitespace string, False otherwise.A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.

print(naam.isupper()) #Return True if the string is an uppercase string, False otherwise.A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.
'''
