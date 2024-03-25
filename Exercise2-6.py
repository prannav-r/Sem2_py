#6.Quadrilateral Classification

side1=float(input('Enter the side 1:'))
side2=float(input('Enter the side 2:'))
side3=float(input('Enter the side 3:'))
side4=float(input('Enter the side 4:'))
angle1=float(input('Enter the angle 1 in degrees:'))
angle2=float(input('Enter the angle 2 in degrees:'))
angle3=float(input('Enter the angle 3 in degrees:'))
angle4=float(input('Enter the angle 4 in degrees:'))
if(angle1+angle2+angle3+angle4==360):
    print("Valid Quadrilateral.")
    if(side1==side2==side3==side4 and angle1==angle2==angle3==angle4==90):
      print("It is a Square.")
    elif(angle1==angle2==angle3==angle4==90 and ((side1==side3 and side2==side4) or (side2==side3 and side1==side4))):
      print("It is a Rectangle.")
    else:
       print("Neither Square or Rectangle.")