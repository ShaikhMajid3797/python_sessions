
#----------------------------------------------Remaining part of Lambda Dunction------------------------------------------------
'''
we have seen,
-Lambda function is nothing but function creation
-we learned one argumnet
-we learned two or multiple argumnt
-if else condition in labmda
-if else in lambda is like list comprehension 
-NOTE---Technically we can not use an'elif' statement in a lambda expression. However,we can nest if else statemnet within an else statement to achieve the same result,
        as an elif statement
'''



#-----------use of LAMBDA in list comprehension
'''

# Q - Output ['Hyd','Mumbai','Chwnnai']
l1=['hyd','mumbai','chennai']
l2=[]
# so we have two methods to solve 1) use append in loop and 2)use list comprehension
for i in l1:
    l2.append(i.capitalize())
print("Using loop----",l2)

#Using list comprehension
l3=[i.capitalize() for i in l1]
print("Using List COmprehension",l3)
'''

'''
VIMP NOTE----
- whenever we use the iteration ,
- iteration menas :- something can be iterable / you can print using the for loop
- in python LIST,TUPLE,STRING,DICTIONAR(only KEYS) are iterable things


There is 4 step to make lambda in list comprehension,
1)First Make Lambda Function           ex.---lambda i:i.capitalize() 
2)Second Add your iterator             ex.---lambda i:i.capitalize(),l1
3)Map both function and iterator       ex.---map(lambda i:i.capitalize(),l1)
4)Save the result in the List          ex.---list(map(lambda i:i.capitalize(),l1))


so, when we do the list comprehension, The format will be change like :- lambda <argument>:<output>,<iterator> 
'''

'''
l1=['hyd','mumbai','chennai']

print(lambda i:i.capitalize(),l1)
# OUTPUT= <function <lambda> at 0x00000187FB13D3A0> ['hyd', 'mumbai', 'chennai']

# NOTE-here we use the function and list but now we need to "map" the function and list 
lx=map(lambda i:i.capitalize(),l1)
print(lx)
#OUTPUT= <map object at 0x000001F6978B6350>
#NOTE - here we generate the lambda function with the map , now we need to convert it in the list
lx=list(map(lambda i:i.capitalize(),l1))
print(lx)


# Q - Apply the square using lambda in list comprehension

list1=[1,2,3,4,5]
list2=list(map(lambda i:i*i,list1))
print(list2)

# so, we mension lot of time that list is iterable sp we can used mapped lambda function in the for loop. see,
for i in map(lambda i:i*i,list1):
    print(i)


# Q - make sum of two list using the lambda in list comprehension
lt1=[1,2,3]
lt2=[11,22,33]
lt3=list(map(lambda i,j:i+j,lt1,lt2)) # NOTE - if we give two arguments we can give two list in iterable
print(lt3)

'''


#-----------use of LAMBDA in list comprehension with if and else

'''

l1=['h#d','mum#ai','chennai']
# Q - Find the # containing letter using the lambda in list comprehension and before solve using loop and list comprehension

# ans using loop
l3=[]
for i in l1:
    if "#" in i:
        l3.append(i)
print("ans using the loop...",l3)

# ans uding list comprehension
l4=[i for i in l1 if "#" in i]
print("ans using the list comprehension...",l4)


#l2=list(map(lambda i:i if "#" in i ,l1)) # NOTE we can use single if in the for loop or list comprehension but we can not use single 'if' in the LAMBDA,else compulsary
# OUTPUT-----SyntaxError: expected 'else' after 'if' expression

# NOTE - so whenever we use sigle if in lambda so, the format will be---------lambda <argument> : <condition> in <argument>,<iterable>.......like,
l2=list(map(lambda i:"#" in i ,l1))
print(l2) 
# OUTPUT---[True, True, False]------NOTE here we didnt got the list with # because we just map the condition on list, thats why its given the boolean answer, so do filter
l2=list(filter(lambda i:"#" in i ,l1))
print(l2) 
'''















#------------------------------------------------------------------------FILE HANDLING--------------------------------------------------------------------------

'''
***TYPE OF FILES***
1).txt      ---means text file
2).csv      ---means comma separeted value
3).xlsx     ---means XL SHEET
4).json     ---Dictionary format data
5).xml      ---IOT data comes in xml format
6).parquet  ---encoded file(we cant open the file)... which is use to save the imp data........ but we read it like parki because t is silent
7).delta    ---encoded file(we cant open the file)... which is use to save the imp data
8).pdf
9).jpg
10).png



# First 3 question are-
1) What is the file location   -----ex--E:\\Data Science Study Material\\Naresh IT Study MATERIAL
2) what is the file Name       -----ex--mbox-short
3) what is extend of file (What is the type of file)    -----ex--.txt
'''



file_location="E:\\Data Science Study Material\\Naresh IT Study MATERIAL"  # the file location is an adress so save it in the "" 
file_name="mbox-short"
file_type=".txt"

#print(file_location) # we got the unicode error means, NOTE in order to read this files, we need to make adress with // so you not get unicode error
#OUTPUT SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 556-557: malformed \N character escape


# so will make // code
file_location="E:\\Data Science Study Material\\Naresh IT Study MATERIAL"  # the file location is an adress so save it in the "" 
file_name="mbox-short" 
file_type=".txt"


# NOTE-first write file location and \\ and then file name and type of file
file_path="E:\\Data Science Study Material\\Naresh IT Study MATERIAL\\mbox-short.txt"

open(file_path)
# OUTPUT:-   <_io.TextIOWrapper name='E:\\Data Science Study Material\\Naresh IT Study MATERIAL\\mbox-short.txt' mode='r' encoding='cp1252'>

# What is encoding :- if wwe cant understand the information of file. beacuse if the file contain some spesial character 
# here we have default encoding file is 'encoding='cp1252  

# NOTE there are too many encoding types like cp1252 and utf-8 like that. so we cant remember the encoding type only google can help up

# NOTE if file have some special character we cant read the file so, at that time we can use the encoding code like cp1252 or utf-8 or etc.

# now save openfile in one variable them read it,
file1=open(file_path,encoding="utf-8-sig")
#print(file1.read())



# Q - now we will read the another file
file2="E:\\Data Science Study Material\\Naresh IT Study MATERIAL\\all-data.csv"
ll1=open(file2)
#print(ll1.read())