#1.Palindromic Strings

a=input("Enter a String:")
res=[]
for i in range(0,len(a)):
    if a[i] not in res:
        res.append(a[i])
    for j in range(i+1,len(a)):
        x=a[i:j+1]
        if x==x[::-1]:
            res.append(x)

print("Palindromic Sub-Strings:")
for i in res:
    print(i)