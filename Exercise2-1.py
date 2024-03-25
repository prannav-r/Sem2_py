#1.Simple Calculator

a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
op=input("Enter the operation:")
if op=='+':
    print("Result = ",a+b)
elif op=='-':
    print("Result = ",a-b)
elif op=="*":
    print("Result = ",a*b)
elif op=="/":
    print("Result = ",a/b)
else:
    print("Enter valid operator.")