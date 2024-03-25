#5.Circle Point Classification

import math

x=int(input("Enter the co-ordinates of x:"))
y=int(input("Enter the co-ordinates of y:"))
r=int(input("Enter the radius of the circle:"))
a=math.sqrt(x**2+y**2)
if a==r:
    print("Point lies on the circumference.")
elif a<r:
    print("Point lies inside the circle.")
else:
    print("Point lies outside the circle.")