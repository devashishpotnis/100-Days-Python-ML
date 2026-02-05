class base:
    def display(self): #
        print("Inside base display")

class derived(base):
    def display(self): #overrided method
        print("Inside derived display")

    
def main():
    bobj=base()
    dobj=derived()

    bobj.display()
    dobj.display()


if __name__=="__main__":
    main()