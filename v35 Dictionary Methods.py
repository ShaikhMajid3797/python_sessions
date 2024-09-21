#-------------------------------------------*------------------------Dictionary Methods---------------------------- *---------------------------------------------------
'''
1)'clear'
2)'copy'
3)'fromkeys'
4)'get'
5)'items'
6)'keys'
7)'pop'
8)'popitem'
9)'setdefault'
10)'update'
11)'values'
'''


#-----------Items, Keys & Values ---------------------------
#_______items():- Return the list with all dictionary keys with values

#_______keys():- Returns a view object that displays a list of all the keys in the dictionary in order of insertion

#_______Values() -Returns a view object containing all dictionary values, which can be accessed and iterated through efficiently

'''


d1={'ram':35,'rahim':45,'robert':55}
a=d1.items()
b=d1.keys()
c=d1.values()

print(a)

print(b)

print(c)


# NOTE if we have to do some operation on the keys and values so first of all we need to convert it into the list ...
# NOTE list and Dictionary Methds are totally diffrent. we cant use methods to each other


#-1---IMP Question - I will give you the sictionry can you extract keys and values list?

l1=list(b) # here we converted keys into the list , now we can apply the list mehtods
l1.append(652)
print(l1)

l2=list(c)
l2.append("MAJID")
print(l2)


#-2---IMP Question - i will give you two list of key and value. can you make dictionry using this list?

# using for loop
newdic={} 
for i,j in zip(l1,l2):
    newdic[i]=j
print("Using for loop.----",newdic)

# using the list comprehension (in)
dic2={i:j for i,j in zip(l1,l2)}
print("Using in dictionary compr.----",dic2)

# using the list comprehension (range)
dic3={l1[i]:l2[i] for i in range(len(l1))}
print("Using range dictionary compr.----",dic3)


# - --------IMP QUESTION

string1="virat.kohli@bangluru.com,rohit.sharma@munmbai.com,mahendra.dhoni@chennai.com"

s1=string1[:string1.find(",")]
s2=string1[string1.find(",")+1:string1.find(",",string1.find(",")+1)]
#s3=string1[string1.find(",",string1.find(",")+1)+1:string1.find(",",string1.find(",",string1.find(",")+1)+1)]
s3=string1[string1.find(",",string1.find(",")+1)+1:len(string1)]

print(s1)

print(s2)

print(s3)

fs1=s1[:s1.find(".")]
ss1=s1[s1.find(".")+1:s1.find("@")]
cs1=s1[s1.find("@")+1:s1.find(".",s1.find(".")+1)]
print(fs1,ss1,cs1)

fs2=s2[:s2.find(".")]
ss2=s2[s2.find(".")+1:s2.find("@")]
cs2=s2[s2.find("@")+1:s2.find(".",s2.find(".")+1)]
print(fs2,ss2,cs2)


fs3=s3[:s3.find(".")]
ss3=s3[s3.find(".")+1:s3.find("@")]
cs3=s3[s3.find("@")+1:s3.find(".",s3.find(".")+1)]
print(fs3,ss3,cs3)

fnamelist=[]
fnamelist.append(fs1)
fnamelist.append(fs2)
fnamelist.append(fs3)

snamwlist=[]
snamwlist.append(ss1)
snamwlist.append(ss2)
snamwlist.append(ss3)

cnamelist=[]
cnamelist.append(cs1)
cnamelist.append(cs2)
cnamelist.append(cs2)
print(fnamelist,snamwlist,cnamelist)


dictx={}
dictx["First Name"]=fnamelist
dictx["Last Name"]=snamwlist
dictx["Compamany Name"]=cnamelist
print(dictx)

# USING LOOP

st1="virat.kohli@bangluru.com,rohit.sharma@mumbai.com,shubhman.gill@gujrat.com"
split1=st1.split(",")
fname=[]
sname=[]
cname=[]
dicx={}
for i in split1:
    fname.append(i[0:i.find(".")])
    sname.append(i[i.find(".")+1:i.find("@")])
    cname.append(i[i.find("@")+1:len(i)-4])
print(fname,sname,cname)

dicx["First Name"]=fname
dicx["Sir Name"]=sname
dicx["Company Name"]=cname
print(dicx)



# USING LIST COMPREHENSION
st1="virat.kohli@bangluru.com,rohit.sharma@mumbai.com,shubhman.gill@gujrat.com"

first_name=[i[:i.find(".")] for i in st1.split(",")]
sir_name=[i[i.find(".")+1:i.find("@")] for i in st1.split(",")]
company_name=[i[i.find("@")+1:i.find(".",i.find(".")+1)] for i in st1.split(",")]

print(first_name)
print(sir_name)
print(company_name)

'''



# ans should {'can':4,'you':2,'canner':2,'able':1,'to':1}

'''
sx="can can you canner can you able to can to canner"

cancount=sx.count("can ")
youcount=sx.count("you")
cannercount=sx.count("canner")
ablecount=sx.count("able")
tocount=sx.count("to")

print(cancount,youcount,cannercount,ablecount,tocount)

dx={}
dx["can"]=cancount
dx["you"]=youcount
dx["canner"]=cannercount
dx["able"]=ablecount
dx["to"]=tocount

print(dx)

sx="can can you canner can you able to can to canner"
dd={}
ww=sx.split(" ")

for i in ww: # after split this , here i= every word between sentence
    dd[i]=i.count(i)
    print(i)  
print(dd)
'''



#----------Q---------- out put should {'a':70,'b':130,'c':240}
'''

d1={'a':20,'b':30,'c':40}
d2={'a':50,'b':100,'c':200}

l1=list(d1.values())
l2=list(d2.values())
sumlist=[]

# using loop....done
#for i,j in zip(l1,l2):
#    sumlist.append(i+j)

# here we will add the two element of two lists
sumlist=[i+j for i,j in zip(l1,l2)]
print(sumlist)


# here we will give the answer after the additon in new dictionary
sumdic={i:j for i,j in zip(d1,sumlist)}
print(sumdic)
'''






#----------Q---------- out put should {'a':70,'b':130,'c':240,'d':500}

d1={'a':20,'b':30,'c':40,'d':500}
d2={'a':50,'b':100,'c':200}


l1=list(d1.values())
l2=list(d2.values())
sumlist=[]

# using loop....done
#for i,j in zip(l1,l2):
#    sumlist.append(i+j)

# here we will add the two element of two lists
sumlist=[i+j for i,j in zip(l1,l2)]
print(sumlist)


# here we will give the answer after the additon in new dictionary
sumdic={i:j for i,j in zip(d1,sumlist)}
print(sumdic)






d1={'a':20,'b':30,'c':40,'d':500}
d2={'a':50,'b':100,'c':200}
de={}


'''
for i in range(len(d2)):
    de[i]=d1.keys()+d2.keys()
print(de)
'''



for i in range(min(len(d1),len(d2))):
    d1[list(d1.keys())[i]]+=d2[list(d2.keys())[i]]
print(d1)





    