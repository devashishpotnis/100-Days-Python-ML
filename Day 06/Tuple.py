#Creating Tuple
t1 = ()                 
t2 = (10,)             
t3 = (1, 2, 3)
t4 = tuple([4, 5, 6])   

t = (10, 20, 30, 40)
print(t[0])
print(t[-1])

#Slicing
t = (10, 20, 30, 40, 50)
print(t[1:4])
print(t[:3])
print(t[::2])

#Looping Through Tuple
t = (1, 2, 3)
for i in t:
    print(i)

#Tuple is Immutable (Not Allowed)
t = (1, 2, 3)
