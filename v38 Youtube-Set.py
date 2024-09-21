'''
*****************************************************************  SET  ********************************************************************

A Set in Python programming is an unordered collection data type that is iterable and has no duplicate elements. While sets are mutable, meaning you can add or 
remove elements after their creation, the individual elements within the set must be immutable and cannot be changed directly.

Set are represented by { } (values enclosed in curly braces)

The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.
This is based on a data structure known as a hash table. Since sets are unordered, we cannot access items using indexes as we do in lists.


Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

NOTE-A set is a collection which is unordered, unchangeable*, and unindexed.


----------There are four collection data types in the Python programming language:

1)List is a collection which is ordered and changeable. Allows duplicate members.

2)Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

3)Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

4)Dictionary is a collection which is ordered** and changeable. No duplicate members.













Method	         Shortcut	Description
  
  
add()	 	                Adds an element to the set
clear()	 	                Removes all the elements from the set
copy()	 	                Returns a copy of the set
pop()	 	                Removes an element from the set
remove()	 	            Removes the specified element
discard()	 	            Remove the specified item
update()	         |=  	Update the set with the union of this set and others


# NOTE-below topic belongs to the Probability we will learn in after some time 
difference()	     -      Returns a set containing the difference between two or more sets
intersection()	     &      Returns a set, that is the intersection of two other sets
union()                     	|   Return a set containing the union of sets
difference_update()	-=  	Removes the items in this set that are also included in another, specified set
intersection_update() &=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	        Returns whether two sets have a intersection or not
issubset()	        <=	    Returns whether another set contains this set or not
                	<	    Returns whether all items in this set is present in other, specified set(s)
issuperset()	    >=	    Returns whether this set contains another set or not
                	>	    Returns whether all items in other, specified set(s) is present in this set


symmetric_difference()	        ^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another



'''

'''
#print(dir({})) #it will give the dictionary methods not set


#---------------- it does not maintain the oreder
num={4,"Majid",4,5.32,"Shaikh"}
print(num)  # it will print the diffrent way
print(num)

#---------------- Its dont have the index method
num={1,2,3,4,5}
#print(num[0])

# ---------------Set not allowed the duplicate items
num1={65,65,62,"Majid",82,665,82,65,33,42,65,33,6565,"Majid"}
print(num1)

#---------------Set() Constructor which is use to convert the other data type to set
a=[1,"Shaikh",9,66,2,"Majid"]
b=("Majid",99865,6547825,26665.325,55425.0,"shekh")
c=set(a)  # here we converted list into tuple
d=set(b)  # here we converted the tuple into the list
print(c)
print(d)





#-----add() 
a={1,"Shaikh",9,66,2,"Majid"}
b={"Majid",99,7825,325,66,"shekh","Shaikh","majid"}

a.add(55)
a.add("Antapur")
print(a)



#------clear()
a={1,"Shaikh",9,66,2,"Majid"}
a.clear()
print(a) 


#--------copy()
a={1,"Shaikh",9,66,2,"Majid"}
b={"Majid",99,7825,325,66,"shekh","Shaikh","majid"}

a=b.copy()
print(a)


#------pop() --- it remove the any element of set randomly
a={1,"Shaikh",9,"Majid"}
a.pop()
print(a)


#-----remove() - use to remove the specifice element
a={122,"Shaikh",9,"Majid"}
a.remove(122)  # here we need to write the element not index
a.remove("Majid")
print(a)


#-------discard()
a={122,"Shaikh",9,"Majid"}
a.discard(956)  # this element is not present in the set but it will not give the error 
a.discard(122)
print(a)  




# --------update()
a={122,"Shaikh",9,"Majid"}
a.update("ABCD")  # itrs iterable menas it will as the string or list or tuple as a single element in the set
print(a)

b=['a','b','c','d','e']
a.update(b)
print(a)


c=("aa",'bb','cc','dd')
a.update(c)
print(a)



#---------diffrences()
a={1,"Shaikh",9,66,2,"Majid"}
b={"Majid",99,78,32,66,"shekh","Shaikh","majid"}

print("diffrence()",a.difference(b)) # it means which element of 'a' set, are not present in the 'b' set
print("diffrence()",b.difference(a)) # it means which element of 'b' set, are not present in the 'a' set


# -------------intersection()   -- it will print the items which are present in the both sets 
a={1,"Shaikh",9,66,2,"Majid"}
b={"Majid",99,78,32,66,"shekh","Shaikh","majid"}
print("Intersection()",a.intersection(b))



# -------------diffrence_update()
a={1,"Shaikh",9,66,2,"Majid"}
b={"Majid",99,78,32,66,"shekh","Shaikh","majid"}
b.difference_update(a)  # it removes the all item of the set which are present in the another set
print("diffrence_update()",b)  # we can see only {1,2,9} are present in 'a' because remaining item are present in the 'b' set



# -----------diffrence_intersection() 
a={1,"Shaikh",9,66,2,"Majid"}
b={"Majid",99,78,32,66,"shekh","Shaikh","majid"}
b.intersection_update(a)
print("diffrence_intersection()",b)


#-------------union()
a={4,5,6}
b={6,7,8}
c=a.union(b)
print(c)  # here we combining the two sets and it will skip the duplicates



#-------------isdisjoint()	 	        Returns whether two sets have a intersection or not
a={1,2,3}
b={4,5,6}
c={5,6,7}
print(a.isdisjoint(b))  # there is no intersection means "TRUE"
print(b.isdisjoint(c))  # yes there is intersection between the two set  "FALSE" 

# NOTE if the the two set are have intersection in eachother it will give "FALSE"
# NOTE if the the two set are does "not" have intersection in eachother it will give "TRUE"




#------------issubset()	        <=	    Returns whether another set contains this set or not
a={1,2,3,4,5}
b={4,5,6}
c={5,6}
print(a.issubset(b))  #"TRUE"
print(b.issubset(c))  #"FALSE" 
print(c.issubset(b))  # True -- because c is the subset of b



#-----------issuperset()	    >=	    Returns whether this set contains another set or not

a={1,2,3,4,5}
b={4,5,6}
c={5,6}
print(a.issuperset(b))  #"FALSE"
print(b.issuperset(c))  #"TRUE" 
print(c.issuperset(b))  # FALSE 


#symmetric_difference()	        ^	Returns a set with the symmetric differences of two sets
a={1,2,3,4,5}
b={4,5,6}
c={5,6}
aa=a.symmetric_difference(b)  # it will remove the element which are present in another set
print(aa)
bb=b.symmetric_difference(c)
print(bb)



#symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
a={1,2}
b={4}
c={5,6}
aa=a.symmetric_difference_update(b)  
print(aa)
bb=b.symmetric_difference_update(c)
print(bb)
'''
# ------tuple Comprehension
s1={i for i in range(1,11)}
print(s1)

a={1,2,3,4,5}
b={6,7,8,9,10}
c={i*j for i,j in zip(a,b)} 
print(c)