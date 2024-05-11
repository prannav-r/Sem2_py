#6.Caeser's Cipher

text=input("Enter the String :")
s=int(input("Enter the value of n :"))

result = ""
for char in text:
    if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
    else:
            result += chr((ord(char) + s - 97) % 26 + 97)

print("Resultant String = ",result)