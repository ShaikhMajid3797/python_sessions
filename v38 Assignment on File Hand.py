'''
Q-------------------------------------------------------Assignment on File Handling-----------------------------------------------------------------------------

-get, open and read the file the file which contain details of employees and file name is 'emails'

    ***Task***
-extract names list
-extract surname list 
-etract company name list
-extract email id list    

'''

# first step we will copy the 'emails' file and copy in the currunt working directory which is 'E:\vs code files\PYthon'
import os
print(os.getcwd()) 

file_loc="E:\\vs code files\\Python\\emails.txt"
op_file=open(file_loc)

# step 1 we will find that the how much employees are in the file
all_details=[i.split(";") for i in op_file]
print(len(all_details))  # here we got we have total 14 employees


# step 2 now will sort out the total first name list
file_loc="E:\\vs code files\\Python\\emails.txt"
op_file=open(file_loc)

f_name=[i[i.find(",")+1:i.find("<")] for i in op_file]
firstname=[i.strip() for i in f_name]
print(firstname)


# step 3 now will sort out the total Surname name list
file_loc="E:\\vs code files\\Python\\emails.txt"
op_file=open(file_loc)

surname=[i[:i.find(",")] for i in op_file]
print(surname)

# step 4 now will sort out the total Company name list
file_loc="E:\\vs code files\\Python\\emails.txt"
op_file=open(file_loc)

company=[i[i.find("@")+1:i.find(".com")] for i in op_file]
print(company)


# step 5 now will sort out the total EMAIL list
file_loc="E:\\vs code files\\Python\\emails.txt"
op_file=open(file_loc)

email=[i[i.find("<")+1:i.find(">")] for i in op_file]
print(email)

#WWWWOOOOOWW!!!!!!    Now we got special lists of the First Name, Sur Name, Company Name  and Email ID
firstname
surname
company
email

ind=0
for i,j,k,l in zip(firstname,surname,company,email):
    ind=ind+1
    print(ind,i,j,k,l)

# using list comp,
finallist=[i+j+k+l for i,j,k,l in zip(firstname,surname,company,email)]

print(finallist)

for i in finallist:
    print(i)
#--------------------------------------------------ABOVE PROGRAM IS MADE BY MAJID-------------------------------------------------------------------------







#--------------------------------------------------Below Program Solved by PROFESSOR--------------------------------------------------------------------

