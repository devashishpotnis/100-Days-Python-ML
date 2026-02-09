student = {
    "name": "Devashish",
    "age": 22,
    "course": "AIML"
}

#Access Dictionary Elements
print(student["name"])      
print(student.get("age"))  


#Add / Update Elements
student["college"] = "XYZ College"   
student["age"] = 23                  

#Remove Elements
student.pop("age")         
student.popitem()           
del student["course"]       
student.clear()           

#Dictionary Methods
student.keys()      
student.values()    
student.items()     
