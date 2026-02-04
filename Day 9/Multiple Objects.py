class devashish:
    def __init__(self,id,password):
        self.id=id
        self.password=password
    
    def myfun(self):
        print(self.id,self.password)
      

obj1=devashish(1,101)
obj2=devashish(2,"Demo")

obj1.myfun()
obj2.myfun()