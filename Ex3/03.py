# Write a program to print the names of the departments students by
# creating a Dept class. If no name is passed while creating an object of the
# Dept class, then the name should be "SCO", otherwise the name should
# be equal to the String value passed while creating the object of the Dept
# class.

class Dept:
    def __init__(self, name=None):
        self.name = name or "SCO"
    
    def __str__(self):
        return self.name

    
if __name__ == "__main__":
    dept1 = Dept()
    dept2 = Dept("CSE")
    print(dept1.__str__())
    print(dept2.__str__())