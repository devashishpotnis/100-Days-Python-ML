class circle:
    PI=3.14

    def __init__(self,a):
        self.radius=a

    def calculatearea(self):
        answer=0.0
        answer =circle.PI*self.radius*self.radius
        return answer
    
def main():
    obj=circle(10.5)

    ret=obj.calculatearea()
    print("Area of circle is:",ret)


if __name__ == "__main__":
    main()