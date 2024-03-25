import re
"""def happy(n):
    sum=0
    while n!=0:
        rem=n%10
        sum+=(rem**2)
        n//=10
    if sum==1:
        print("Happy Number")
    else:
        happy(sum)

happy(203)

def ab(n):
    sum=0
    for i in range(n):
        if n%i==0:
            sum+=i"""

'''def pt(x,n):
    sum=0
    a=1
    for i in range(1,n*2,2):
        if a%2!=0:
            sum+=x**i
            a+=1
        elif a%2==0:
            sum-=x**i
            a+=1
    print(sum)

pt(2,4)'''

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=' ')
    for k in range(i+1):
        print("*",end=" ")
    print()


x=231.21345124
print(format(x,"0.3f"))

import re

# Define a sample text
text = "The quick brown fox jumps over the lazy dog"

# 1. Square brackets []
pattern1 = r'[aeiou]'
matches1 = re.findall(pattern1, text)
print("1. Square brackets []:", matches1)

# 2. Character set complement ^
pattern2 = r'[^aeiou]'
matches2 = re.findall(pattern2, text)
print("2. Character set complement ^:", matches2)

# 3. Caret ^
pattern3 = r'^fox'
matches3 = re.findall(pattern3, text)
print("3. Caret ^:", matches3)

# 4. Dollar $
pattern4 = r'dog$'
matches4 = re.findall(pattern4, text)
print("4. Dollar $:", matches4)

# 5. Asterisk *
pattern5 = r'of*'
matches5 = re.findall(pattern5, text)
print("5. Asterisk *:", matches5)

# 6. Plus +
pattern6 = r'fox+'
matches6 = re.findall(pattern6, text)
print("6. Plus +:", matches6)

# 7. Question mark ?
pattern7 = r'fo?x'
matches7 = re.findall(pattern7, text)
print("7. Question mark ?:", matches7)

# 8. Dot .
pattern8 = r'.'
matches8 = re.findall(pattern8, text)
print("8. Dot .:", matches8)

# 9. Curly braces {}
pattern9 = r'\b\w{3}\b'
matches9 = re.findall(pattern9, text)
print("9. Curly braces {}:", matches9)

# 10. Pipe |
pattern10 = r'fox|dog'
matches10 = re.findall(pattern10, text)
print("10. Pipe |:", matches10)

# 11. Parentheses ()
pattern11 = r'(The|quick)'
matches11 = re.findall(pattern11, text)
print("11. Parentheses ():", matches11)

# 12. Backslash \
pattern12 = r'\.'
matches12 = re.findall(pattern12, text)
print("12. Backslash \\:",matches12)

match = re.search(r'fox', text)
print(match)
print(match.group())  # Output: fox
print(match.start())  # Output: 16
print(match.end())    # Output: 19
print(match.span())   # Output: (16, 19)