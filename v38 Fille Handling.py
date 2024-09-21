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
1) What is the file location   -----ex--E:\\Data Science Study Material\\Naresh IT Study MATERIAL\\
2) what is the file Name       -----ex--mbox-short
3) what is extend of file (What is the type of file)    -----ex--.txt
'''

# -------------------------------How to Read The DATA--------------------
file_location="E:\\Data Science Study Material\\Naresh IT Study MATERIAL\\"  # the file location is an adress so save it in the "" 
file_name="mbox-short"
file_type=".txt"

#print(file_location) # we got the unicode error means, NOTE in order to read this files, we need to make adress with // so you will not get unicode error
#OUTPUT SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 556-557: malformed \N character escape


# so will make \\ code
file_location="E:\\Data Science Study Material\\Naresh IT Study MATERIAL"  # the file location is an adress so save it in the "" 
file_name="mbox-short" 
file_type=".txt"


# NOTE-first write file location and \\ and then file name and type of file
file_path="E:\\Data Science Study Material\\Naresh IT Study MATERIAL\\mbox-short.txt"

open(file_path)
# OUTPUT:-   <_io.TextIOWrapper name='E:\\Data Science Study Material\\Naresh IT Study MATERIAL\\mbox-short.txt' mode='r' encoding='cp1252'>

# What is encoding :- if wwe cant understand the information of file. beacuse if the file contain some special character 
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


#-NOTE---Whenever the data file and python file on diffrent location we need to provide th location but When the data file and python file are on the same location so 
#        at that time we dont need to whole provide location  


# and we can see that the currunt location on python file, using import os:getcwd()  ( get currunt working directory)
import os;
print(os.getcwd())   #E:\vs code files\PYthon



#-----------now we will copy our file and paste in the same python file using THIS PC.... 

# NOTE location of python file and location of the data file should be same
# so done the copy preocess in this pc....NOW we dont need to provide location of m-box file 


# no need of this whole location.....file_path="E:\\Data Science Study Material\\Naresh IT Study MATERIAL\\mbox-short.txt"

file_loc="mbox-short.txt"
file=open(file_loc,encoding="utf-8-sig")   
file.read()   # its  sucessfully worked
 

#---------------change directory-----------
# we can change our file directory using the chdir()
print(os.getcwd())      #as we can see that our currunt working file directory is 'E:\vs code files\PYthon'  now we can change it 

os.chdir("E:\\c++") # here we given new location "E:\\c++" for currunt working directory 
print(os.getcwd())   # as we can see our currunt working directory is "E:\\c++", so its sucessfully change!

# now again we cahnge the location 
os.chdir("E:\\vs code files\\PYthon")
print(os.getcwd())   #  so we got the previous location


# NOTE - Whenever we make files we should think about,
# - If hard code is there this should be reduce
# - Many lines ====== into single line
# - is our file can run at any place



#------------WITH KEYWORD---------------

# 2nd Method of reading the data

file_loc1="mbox-short.txt"
file_op=open(file_loc1,encoding="utf-8-sig")
file_op.read()
#file.read() 



# 3rd method to read the data

# # above we read the file suddenly ones agian we need to read the file so it will give EMPTY.....
# SO THIS IS BIGGEST DRAWBACK BECAUSE SESSION WILL CLOSED SUDDENLY 
# if we use the 'with' keyword we can read file any time 

# FORMAT: with open(<file_location>) as <File_Path>

jkl="mbox-short.txt"  # here we have saved file path in 'jkl' variable   

with open(jkl) as xyz:   # here we have open 'jkl' file and saved opened 'jkl' file in the 'xyz' variable 
    abc=xyz.read()       # here we read the 'xyz' file and saved in new 'abc' variable 
    #print(abc)           # here we have print the 'abc' variable




# Q-------If we want to know the length of the file. NOTE Length means how much letters are present in the file 
print(len(abc)) 





#----------------------------------enumerate------------

# Q-----if we want to know the How much lines are present in the file 
# ans---there is special keyword is available is there its called the 'enumerate'    



# NOTE 1----AFTER READING WE WILL GOT THE CHARACTER
file_loc1="mbox-short.txt"
file_op=open(file_loc1)

newfile=file_op.read()


# if we use the LOOP, we get the character as 'i' not LINES
count=0
print("IF WE USED THE AFTER READING FILE")
for i in newfile:  #NOTE here we take the newfile ehich is read() of file_op, Thats WHY we are getting character
    print(i,end="")
    count=count+1
    if count==10:
        print("THE END\n")
        break
# CONCLUSION - if you want character so work on "read() file"




# NOTE 2---BEFORE READING THE FILE WE WILL GOT THE ***LINES*** 

file_loc1="mbox-short.txt"
file_op=open(file_loc1)
    
cnt=0
print("IF WE USED THE BEFORE READING FILE")
for i in file_op:  # NOTE and here we have taken 'opened file_loc1' NOT read(), so thats why we got the LINES 
    print(i,end="")
    cnt=cnt+1
    if cnt==3:
        break   
# CONCLUSION - if you want lines so work on "open file only"



# Q --2-- Count How many lines are present in the file
line_counter=0
for i in file_op:
    line_counter=line_counter+1
    
print("\n\nThe total lines in the file is by First Way = ",line_counter+2)

 



 #NOW WE WILL LEARN------enumerate------------
'''
 Q-----if we want to know the How much lines are present in the file 
 ans---there is special keyword is available is there its called the 'enumerate'    

we use the zip if file in the combination of two list & used in the Dictionary.we combine list and use i,j to print ........here we will do same thing,
we will take j,k and 'j' Belongs to Index of line and 'k' Belings to line

FORMAT---------for <index>,<line> in enumerate(file_name):
                    print(i,j)
NOTE- the file should be opended and should not be read() (readed)
''' 
file_loc1="mbox-short.txt"
file_op=open(file_loc1)

#for i,j in enumerate(file_op):
#    print(i,j)   #  Total lines are printed Sucssesfully  
 
 



#------3------Q---put the all index in list and find the length of list


# answer by first way
file_loc1="mbox-short.txt"
file_op=open(file_loc1)


for i,j in enumerate(file_op):
    pass
total_lines=i
print("The total lines in the file using first method = ",total_lines+1)



# answer by second way

file_loc1="mbox-short.txt"
file_op=open(file_loc1)

list1=[]
for i,j in enumerate(file_op):
    list1.append(i)
print("The Total lines in the file using the second way is = ",len(list1))



# ans by third way using list comprehension
file_loc1="mbox-short.txt"
file_op=open(file_loc1)

list2=[i for i,j in enumerate(file_op)] 
print("The Total lines in the file using the Third way(LIST COMPREHENSION) is = ",len(list2))
#print(list2)

'''
- here line are not required 
- whenever you dont need or you dont use any specific variable
- keep that variiable name as underscore "_" 
- its increase the quality of code
'''
file_loc1="mbox-short.txt"
file_op=open(file_loc1)

list2=[i for i,_ in enumerate(file_op)] 
print("The Total lines in the file using the Third way(LIST COMPREHENSION) is = ",len(list2))
#print(list2)





# Q---4-----print the first 10 lines of the file
file_loc1="mbox-short.txt"
file_op=open(file_loc1)

# first way of ans,
print("FIRST WAY OF ANSWER USING THE COUNER METHOD")
count=0
for i in file_op:
    print(i,end="")
    count+=1
    if count==10:
        break

#second way of ans
file_loc1="mbox-short.txt"  #NOTE  here we taken and open file again because, we printed the 10 lines in above code, and if dont take and open file agian it will print
file_op=open(file_loc1)      #     from the 11th line of the code. IF YOU WANT FROM LINE ONE, TAKE AND OPEN ONES AGAIN 

print("SECOND WAY OF ANSWER USING THE ENUMERATE METHOD")
for i,j in enumerate(file_op):
    print(j,end='')  # j means line only. it will not print the index 
    if i==20: # it will break when the index will reach the 9
        break




# Q --5- remove the first spaces from the lines

# we can solve it using the strip method
file_loc1="mbox-short.txt" 
file_op=open(file_loc1)   

for i,j in enumerate(file_op):
    print(j.strip(),end='')  
    if i==10: # it will break when the index will reach the 9
        break


# Q -6-- Extract the line which starting 'From' in the file and add it in the list and count the elements if the list

# answer 1st method using loop,list,list methods
file_loc1="mbox-short.txt" 
file_op=open(file_loc1)   

emt_list=[]
for i,j in enumerate(file_op):
    if j.startswith("From"):
        #print(j,end="")
        emt_list.append(j)
print("\n\nThe total lines in the file e=which start with the 'From' is = ",len(emt_list))


# answer by 2nd method using the list comprehension
file_loc1="mbox-short.txt" 
file_op=open(file_loc1)   
    
emt2=[j for i,j in enumerate(file_op) if j.startswith("From")]
print("Answer by List Comprehension Method",len(emt2))






# Q-7--- remove '\n' from the lines

# First way of Answer
file_loc1="mbox-short.txt" 
file_op=open(file_loc1)   

emt_list=[]
for i,j in enumerate(file_op):
    if j.startswith("From"):
        #emt_list.append(j)  # if we use this we will get the lines which start by "From" word but it will contain '\n' 
        
        
        emt_list.append(j.removesuffix("\n"))  # here we remeove the suffix means '\n' which present at the last of the line
        
#print(emt_list) # Sucssesfully Printed without '\n'



# Second Way of Answer using the rstrip (Right Side Strip)
file_loc1="mbox-short.txt" 
file_op=open(file_loc1)   


emt_list=[]
for i,j in enumerate(file_op):
    if j.startswith("From"):
        #emt_list.append(j)  # if we use this we will get the lines which start by "From" word but it will contain '\n' 
        
        
        emt_list.append(j.rstrip("\n"))  # here we remeove the suffix means '\n' which present at the last of the line
        
#print(emt_list)  # Sucssesfully Printed without '\n'


# we can do same thing in using List Comprehension, 
file_loc1="mbox-short.txt" 
file_op=open(file_loc1)   

emtlistxx=[j.rstrip("\n") for i,j in enumerate(file_op) if j.startswith("From")]
#print(emtlistxx)





#___Q__8------Extract all the emails from the file


#em="From gopal.ramasammycook@gmail.com "
#ab=em[em.find(" "):em.find(" ",em.find(" ")+1)]
#print(ab)

# First Way of Answer using find ethod
file_loc1="mbox-short.txt" 
file_op=open(file_loc1)   

asd=[]
for i,j in enumerate(file_op):
    if j.startswith("From"):
        asd.append(j[j.find(' '):j.find(' ',j.find(' ')+1)])
        #asd.append(j.split(" ")[1]) # this is split method
#print(asd)  # sucssesfully completed



# 2nd way of answer by using the split in listcomprehension
file_loc1="mbox-short.txt" 
file_op=open(file_loc1)   

abc=[j.split(" ")[1] for i,j in enumerate(file_op) if j.startswith("From")]
#print(abc)  # sucssesfully completed




# Q----9--- In above email list there are some reated emails id so extract the list which contain non repeated email id 

# first way of answer using the loop (in & continue)
unique_email=[]
for i in abc:
    if i in unique_email:
        #pass
        continue # here we can use pass or continue. But continue means we skip the iteration and move to next iteration. and Pass means there is no code executed
    else:
        unique_email.append(i)
        

print('first way of answer using the loop (in & continue)----',len(unique_email))

mail_x=[]
for i in abc:
    if i not in mail_x:
        mail_x.append(i)
print('first way of answer using the loop (not in)----',len(mail_x))





# second way of answer using the List Comprehension
un_email=[]
un_email=[un_email.append(i) for i in abc if i not in un_email]
print('second way of answer using the List Comprehension',len(un_email))