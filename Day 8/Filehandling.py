#Opening a File
file = open("data.txt", "r")

#Reading from File
file = open("data.txt", "r")
print(file.read())
file.close()


#Writing to File
file = open("data.txt", "w")
file.write("Hello Python")
file.close()

#Appending to File
file = open("data.txt", "a")
file.write("\nWelcome AIML")
file.close()

