import sys

def addition(a,b):
    return a+b

def main(): 
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    c=addition(a,b)
    print(c)

if __name__ == "__main__":
    main()
