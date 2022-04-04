# Write a program to print the names of the departments students by
# creating a Dept class. If no name is passed while creating an object of the
# Dept class, then the name should be "SCO", otherwise the name should
# be equal to the String value passed while creating the object of the Dept
# class.

class Dept:
    def __init__(self, *args):
        if len(args) == 1:
            self.dept=args[0]
 
        elif len(args) == 0:
            self.dept="SCO"
   
    def deptname(self):
        print(self.dept)
   
 
d1=Dept()
d1.deptname()
 
d2=Dept("CSE")
d2.deptname()