#4.Grade Calculator

m=int(input("Enter Maths Mark:"))
p=int(input("Enter Physics Mark:"))
c=int(input("Enter Chemistry Mark:"))
cs=int(input("Enter Computer Science Mark:"))
e=int(input("Enter English Mark:"))
avg=(m+p+c+cs+e)/5
if(100<=avg>=90):
  print("Grade A+")
elif(avg>=80 and avg<90):
  print("Grade A")
elif(avg>=70 and avg<80):
  print("Grade B+")
elif(avg>=60 and avg<70):
  print("Grade B")
elif(avg>=50 and avg<60):
  print("Grade C")
elif(avg>=40 and avg<50):
  print("Grade D")
elif(avg<40):
  print("Grade F")