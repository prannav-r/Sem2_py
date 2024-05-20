import random

wlist=["dick","lick","naughty"]
x=wlist[random.randint(0,len(wlist)-1)]
mat=[]
for i in range(len(x)):
        mat+=["-"]

attempt=8
while True:
    c=list(mat)
    guess=input("\nEnter your guess:")
    for i in range(len(x)):
        if x[i]==guess:
            mat[i]=guess
            for j in mat:
                print(j,end='')    
    if mat==c:
        attempt-=1
        print("You Have ",attempt,"attempts left!")
    if attempt==0:
        print("\nGame Over, you lost!")
        break
    if "-" not in mat:
        print("\nCongratulations you have won!")