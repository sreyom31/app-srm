# Write a Python class named SRMIST with six attributes school,
# dept1, dept2, dept2 and dept3. Add a new attribute specialization and
# display the entire attribute and their values of the said class. Now remove
# the dept1 and dept2 attribute and display the entire attribute with values.

class SRMIST:
    school = "SRMIST"
    dept1 = "CSE"
    dept2 = "ECE"
    dept3 = "EEE"
    dept4 = "MECH"
    specialization = "Blockchain"

    def __init__(self, dept1, dept2, dept3, dept4, specialization):
        self.dept1 = dept1
        self.dept2 = dept2
        self.dept3 = dept3
        self.dept4 = dept4
        self.specialization = specialization

    def remove_dept(self):
        del self.dept1
        del self.dept2
        print(self.school, self.dept3, self.dept4, self.specialization)

name = input("Enter your name: ")
dept1 = input("Enter your dept1: ")
dept2 = input("Enter your dept2: ")
dept3 = input("Enter your dept3: ")
dept4 = input("Enter your dept4: ")
specialization = input("Enter your specialization: ")
sreyom = SRMIST(dept1, dept2, dept3, dept4, specialization)
sreyom.remove_dept()