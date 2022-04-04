# Write a Python program to crate four empty classes, CTECH, CINTEL, NWC and DSBS. Now create some instances and check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not.

class CTECH:
    pass
class CINTEL:
    pass
class NWC:
    pass
class DSBS:
    pass
 
student1 = CTECH()
marks1 = CINTEL()
stu=NWC()
ma=DSBS()
 
print(isinstance(student1, CTECH))
print(isinstance(marks1, CTECH))
print(isinstance(stu, CTECH))
print(isinstance(ma, CTECH))
 
print(isinstance(marks1, CINTEL))
print(isinstance(student1, CINTEL))
print(isinstance(stu, CINTEL))
print(isinstance(ma, CINTEL))
 
 
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(CTECH, object))
print(issubclass(CINTEL, object))
print(issubclass(NWC, object))
print(issubclass(DSBS, object))