#2.Sub-Strings with same first and last characters

a=input("Enter a String:")
res=[]

for i in range(len(a)):
    if a[i] not in res:
        res.append(a[i])
    for j in range(i+1,len(a)):
        x=a[i:j+1]
        if x[0]==x[-1]:
            res.append(x)

print("Count of Sub-Strings = ",len(res))
print("Sub-Strings are:")
for i in res:
    print(i)