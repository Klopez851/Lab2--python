# Author: Keidy lopez
# Inputs:
# Outputs:
import math


A = float(input("Please enter height of triangle: "))
B = float(input("Please enter base of triangle: "))
C = (math.sqrt((A**2) + (B**2)))

area = ((A * B) / 2)
per = (A + ((math.sqrt((C**2)-(A**2)) + (math.sqrt(C**2)))))

print("The area of your triangle is: ", area)
print("The perimeter of your triangle is: ", per)
