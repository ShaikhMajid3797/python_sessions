#.............................................................LOOP..........................................................................
'''Loops are used to iterate the block of statement untill condition is true
there are two types of loop For and While loop
'''


#Q- ihave to print 1 to 10 
'''
so, we use for loop to print it

...............PATTERN 1...................
for i in range(10) ......i=variable

-if we have only single value in the bracket in the bracket then it consider as a stop value
-the default start from the 0
-python index always start with 0
-if direction sign(+=incriment,-=decrement) is not mention in the bracket by default it will go in forward direction
-end value is stop-1(like if its 10 so it will stop on 9)
'''



'''
for i in range(20):  #Range is built in function # 20 will be consider as a stop value and by default 0 will be start value
    #print(i)
    #if we have to print the numbers in horizontal line so we use (i,end='')
    print(i,end=' ')
'''
    

''' # Pattern 2 - here we are giving the two values start and stop

for i in range (10,20):
    print(i,end=' @ ')# if we put something between the quotes so it will print with the i 
'''


'''# Pattern 3 - we will give the 3 values in teh condition start,stop,step 
               - NOTE-Always the step sign decide the direction




#for i in range (2,20,2): #step=2 means it will skip every second value after printing one value like after 1 it will skip 2 and print 3 (n-1 value will skip whre n=2)
#    print(i)    

for i in range (-1,-10,-1):
    print(i)
'''    


# IMP NOTE-bwlow if we not given - sign so it menas positive direction but we have to go ack direction.so it will fail
'''
-----9---8---7---6---5---4---3---2---1----0+++1+++2+++3+++5+++6+++7+++8+++9   9 this is diagram    
 according to above diagram we have to print the -1 to -10 but we given step=+1 means we have given the order to go forward but we have to go backward direction,
 so we will not reach our condition
 
for i in range (-1,-10,1):
    print(i)
    
'''


'''
#in this case also we given the wrong sign means we have to go forward direction and we given the - sign
for i in range(2,20,-2):
    print(i)
'''


for i in range(-10,30,2):
    print(i)    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    