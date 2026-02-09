#Creating List

list1 = [1, 2, 3, 4]
mixed = [1, "Python", 3.5, True]
empty = []

#Accessing Elements
lst = [10, 20, 30, 40]
print(lst[0])     
print(lst[-1])    

#Slicing
list1 = [1, 2, 3, 4, 5]
print(list1[1:4])
print(list1[:3])
print(list1[::2])

#Updating Elements
list = [1, 2, 3]
list[0] = 100
print(list)

#Adding Elements
list = [1, 2, 3]
list.append(4)         
list.extend([5, 6])     
list.insert(1, 99)      

#Removing Elements
list = [1, 2, 3, 4]
list.remove(2)    
list.pop()        
list.pop(1)       
list.clear()      