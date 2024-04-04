#1.Program to find the minimal number of coins or notes to be given to his kid for fee payment

def countRupees(fee):
  if fee < 0:
    return -1

  count = 0
  denominations = [500, 100, 50, 10, 5, 1]
  for i in denominations:
    while fee >= i:
      count += 1
      fee -= i
  return count

fee=int(input("Enter the fee :"))
count=countRupees(fee)

if count == -1:
  print("Invalid fee amount (negative).")
else:
  print("Minimum number of coins/notes needed:",count)