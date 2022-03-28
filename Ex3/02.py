# Write a Python program to crate four empty classes, CTECH,
# CINTEL, NWC and DSBS. Now create some instances and check
# whether they are instances of the said classes or not. Also, check whether
# the said classes are subclasses of the built-in object class or not.

class CTECH:
    pass

class CINTEL:
    pass

class NWC:
    pass

class DSBS:
    pass

ins1 = CTECH()
ins2 = CINTEL()
ins3 = NWC()
ins4 = DSBS()

print("ins1 is an instance of CTECH:", isinstance(ins1, CTECH))
print("ins2 is an instance of CINTEL:", isinstance(ins2, CINTEL))
print("ins3 is an instance of NWC:", isinstance(ins3, NWC))
print("ins4 is an instance of DSBS:", isinstance(ins4, DSBS))

print("ins1 is a subclass of object:", issubclass(CTECH, object))
print("ins2 is a subclass of object:", issubclass(CINTEL, object))
print("ins3 is a subclass of object:", issubclass(NWC, object))
print("ins4 is a subclass of object:", issubclass(DSBS, object))