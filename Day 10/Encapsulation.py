#It is concept of acccess specifier
class student:
    def __init__(self,a,b,c):
        self.name=a              #public
        self._age=b              #protected
        self.__marks=c           #private

    def display(self):
        print(self.name)
        print(self._age)
        print(self.__marks)
    

obj=student('Rahul',24,89)
obj.display()


print(obj.name)
print(obj._age)
#print(obj.__marks)


