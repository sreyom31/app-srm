# Write a program to print the area and perimeter of a triangle having
# sides of 3, 4 and 5 units by creating a class named 'Triangle' with a
# function to print the area and perimeter.

class Triangle:
    def findPerimeter(self, s1, s2, s3):
        return (s1 + s2 + s3)
 
    def findArea(self, s1, s2, s3):
        p = (s1 + s2 + s3)
        s = p/2
        return (s * (s-s1) * (s-s2)*(s-s3))**0.5
 
 
s1 = float(input("Enter the first side of the triangle : "))
s2 = float(input("Enter the second side of the triangle : "))
s3 = float(input("Enter the third side of the triangle : "))
 
u = Triangle()
 
print("The perimeter of the triangle is : {0:.2f}".format(
    u.findPerimeter(s1, s2, s3)))
print("The area of the triangle is : {0:.2f}".format(u.findArea(s1, s2, s3)))