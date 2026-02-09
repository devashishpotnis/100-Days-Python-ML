s = {1, 2, 3, 3}
print(s)   # {1, 2, 3}

#Creating a Set
s1 = {1, 2, 3}
s2 = set([3, 4, 5])
empty_set = set()   

#Add & Update Operations
s = {1, 2}
s.add(3)                 
s.update([4, 5, 6])      
print(s)

#Remove Operations
s = {1, 2, 3, 4}

s.remove(3)     
s.discard(10)   
s.pop()         
s.clear()       