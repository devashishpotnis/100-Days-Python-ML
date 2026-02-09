import sys

def main():
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(3000)
    print(sys.getrecursionlimit())

if __name__=="__main__":
    main()

