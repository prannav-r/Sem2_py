x=input("Enter String: ")
n=input("Enter rstrip parameter: ")
res=[]

for i in n:
    if i not in res:
        res.append(i)

count=0
for i in range(len(x)-1,-1,-1):
    if x[i] not in res:
        break
    count+=1

print(x[:(len(x)-count)])