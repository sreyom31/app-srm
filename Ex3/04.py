
# Create a class named 'Rectangle' with two data members- length and breadth and a function to calculate the area which is 'length*breadth'. The class has three constructors which are :
# 1 - having no parameter - values of both length and breadth are assigned zero.
# 2 - having two numbers as parameters - the two numbers are assigned as length and breadth respectively.
# 3 - having one number as parameter - both length and breadth are assigned that number.
# Now, create objects of the 'Rectangle' class having none, one and two parameters and print their areas.

class rectangle:
    length=0  
    breadth=0
    def __init__(self, *args):
        if len(args) == 2:
            self.length=args[0];
            self.breadth=args[1]
        elif len(args) == 1:
            self.length=args[0]
            self.breadth=args[0]
        else:
            self.length=0
            self.breadth=0
    def area(self):
        return self.length*self.breadth;

r1=rectangle(5,10)
print(r1.area())

r2=rectangle(10)
print(r2.area())
 
r3=rectangle()
print(r3.area())