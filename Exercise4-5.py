#5.Concatenate two strings alternatively

x=input("Enter String 1 :")
y=input("Enter String 2 :")
z=""

for i in range (0,len(x)):
    z+=x[i]
    z+=y[i]

print("Resultant String = ",z)