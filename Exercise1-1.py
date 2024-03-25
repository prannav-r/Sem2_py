#1.Area Calculation

import math

print("Triangle")
tbase=float(input("Enter the side of the triangle:"))
theight=float(input("Enter the height of the triangle:"))
tarea=0.5*tbase*theight

print("Parallelogram")
pbase=float(input("Enter the base of the parallelogram:"))
pheight=float(input("Enter the height of the parallelogram:"))
parea=pbase*pheight

print("Cylinder")
cyradius=float(input("Enter the radius of the Cylinder:"))
cyheight=float(input("Enter the height of the Cylinder:"))
cyarea=2*math.pi*cyradius**2+2*math.pi*cyradius*cyheight

print("Cone")
coradius=float(input("Enter the radius of the Cone:"))
colength=float(input("Enter the length of the Cone:"))
coarea=math.pi*coradius**2+math.pi*coradius*colength

print("Sphere")
sradius=float(input("Enter the radius of the Sphere:"))
sarea=4*math.pi*sradius**2

print("Rectangular Prism")
l=float(input("Enter the length of the Rectangular Prism:"))
w=float(input("Enter the width of the Rectangular Prism:"))
h=float(input("Enter the heigth of the Rectangular Prism:"))
rarea=2*(w*l+h*l+h*w)

print("Results:")
print("Area of Triangle=",round(tarea,2))
print("Area of Parallelogram=",round(parea,2))
print("Area of Cylinder=",round(cyarea,2))
print("Area of Cone=",round(coarea,2))
print("Area of Sphere=",round(sarea,2))
print("Area of Rectangular Prism =",round(rarea,2))