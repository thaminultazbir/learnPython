class Polygon:

    def __init__(self, NoOfSides):
        self.n = NoOfSides
        self.sides = [0 for i in range(NoOfSides)]

    def inputSides(self):
        self.sides = [float(input("Enter Side "+str(i+1)+" : ")) for i in range(self.n)]

    
    def DisplaySide(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def FindArea(self):
        a, b, c = self.sides

        s = (a+b+c) / 2
        area = (s*(s-a)*(s-b)*(s-c))**0.5

        print("Area of Triangle is: %0.2f" %area + " sqrUnit")


t = Triangle()
t.inputSides()
t.DisplaySide()

t.FindArea()