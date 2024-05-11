x=input("Enter String: ")
n=input("Enter lstrip parameter: ")
res=[]

for i in n:
    if i not in res:
        res.append(i)

count=0
for i in x:
    if i not in res:
        break
    count+=1

print(x[count:])