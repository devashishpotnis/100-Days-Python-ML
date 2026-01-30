#Default Arguments
def demo(name="User"):
    print("Hello", name)

demo()
demo("Devashish")

#Keyword Arguments
def student(name, age):
    print(name, age)

student(age=22, name="Devashish")