#2.Simple and Compound Interest Calculation

P=float(input("Enter the Principal Amount:"))
R=float(input("Enter the Rate of Interest:"))
T=int(input("Enter the Term of Deposit:"))
print("Simple Interest =",round((P*T*R)/100,4)) #Simple Interest

N=int(input("Enter the number of times interest is compounded in a year:"))
compound_interest = P * (1 + R / (N * 100)) ** (N * T) - P
print("Compound Interest=",round(compound_interest,4))  #Compound Interest