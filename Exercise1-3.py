#3.Employee Salary Calculation

BP=int(input("Enter the Basic Pay:"))
DA=int(input("Enter the percentage for DA:"))
HRA=int(input("Enter the percentage for HRA:"))

PF=(0.12*BP)
Salary=BP+(DA/100*BP)+(HRA/100*BP)-PF
print("Salary of the Employee = ",Salary)