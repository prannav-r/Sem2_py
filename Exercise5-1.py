#1.Pythagorean Triplets

def pt(N):
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            for k in range(j+1,N+1):
                if (i**2+j**2==k**2):
                    print (i ,j, k)
                

N=int(input("Enter the value of N :"))
print("Pythagorean Triplets are :")
pt(N)


res=[(i,j,k) for i in range (1,N+1) for j in range (i+1,N+1) for k in range(i+1,N+1) if i**2+j**2==k**2]
print("using comprehension:")
print(res)