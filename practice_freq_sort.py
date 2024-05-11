x=input()
res={}
final=[]

for i in x:
    if i not in res:
        res[i]=1
    else:
        res[i]+=1

for i in res:
    final.append(i)

for i in range(len(final)):
    for j in range(i+1):
        if res[final[i]]>res[final[j]]:
            final[i],final[j]=final[j],final[i]
for i in final:
    print(i*res[i],end=' ')