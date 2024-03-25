#3.Maximum of three numbers

a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=int(input("Enter the 3rd number:"))
if (a>b and a>c):
    print(a,"is the largest nubmer.")
elif (b>a and b>c):
    print(b,"is the largest number.")
else:
    print(c,"is the largest number.")