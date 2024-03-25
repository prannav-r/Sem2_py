#4.Number Systems and Operations

num1=int(input("Enter the 1st decimal number:"))
num2=int(input("Enter the 2nd decimal number:"))

print("Binary representation of", num1, "is", bin(num1))
print("Binary representation of", num2, "is", bin(num2))
print("Octal representation of", num1, "is", oct(num1))
print("Octal representation of", num2, "is", oct(num2))
print("Hexadecimal representation of", num1, "is", hex(num1))
print("Hexadecimal representation of", num2, "is", hex(num2))

l_and = num1 & num2
l_or = num1 | num2
l_not1 = ~num1
l_not2 = ~num2
l_shift1 = num1 << 3
r_shift1 = num1 >> 4
l_shift2 = num2 << 3
r_shift2 = num2 >> 4

print("Bitwise AND of the numbers, in binary:", bin(l_and), "in decimal:", l_and)
print("Bitwise OR of the numbers, in binary:", bin(l_or), "in decimal:", l_or)
print("Bitwise NOT of the first number, in binary:", bin(l_not1), "in decimal:", l_not1)
print("Bitwise NOT of the second number, in binary:", bin(l_not2), "in decimal:", l_not2)
print("Left shift of first number by 3, in binary:", bin(l_shift1), "in decimal:", l_shift1)
print("Left shift of second number by 3, in binary:", bin(l_shift2), "in decimal:", l_shift2)
print("Right shift of first number by 4, in binary:", bin(r_shift1), "in decimal:", r_shift1)
print("Right shift of second number by 4, in binary:", bin(r_shift2), "in decimal:", r_shift2)