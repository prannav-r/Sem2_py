#3.Split String into multiple lines with n-characters each

a=input("Enter the String:")
n=int(input("Enter the value of N:"))
res=[]

for i in range(0,len(a),n):
    res.append(a[i:i+n])

print("Sub-Strings:")
for i in res:
    print(i)