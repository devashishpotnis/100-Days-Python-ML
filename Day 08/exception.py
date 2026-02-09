
def main():
    ans=0
    try:
        print("Enter 1st no")
        no1=int(input())

        print("Enter 2nd no")
        no2=int(input())
        
        ans=no1/no2
    
    except ZeroDivisionError as zobj:
        print("Exception ocurred due to second input :",zobj)
    
    except ValueError as vobj:
        print("Invalid input od datatype :",vobj)
    
    except Exception as eobj:
        print("Exception ocurred :",eobj)

    finally:
        print("Inside Finally Block")

    print ("The Division is:",ans)

if __name__ == "__main__" :
    main()