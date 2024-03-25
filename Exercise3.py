#3.Programs using Loops and Nested Loops

def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)

def pn(a):
    if a==1:
       print("It is not a Prime Number.")  
    elif a>1:
        for i in range(2,a):
            if a%i==0:
                print("It is not a Prime Number.")
                break
        else:
            print("It is a Prime Number.")


def div():
    a=int(input("Enter Dividend:"))
    b=int(input("Enter Divisor:"))
    count=0
    if(b>a):
        count=0
    elif(a>b):
        while(a>=b):
         a-=b
         count+=1
    elif(a==b):
        count=1 
    print("Quotient = ",count) 

def sd(a):
    sum=0
    while a!=0:
        sum=sum+a%10
        a=a//10
    return sum

def mult(a):
    for i in range(1,11):
        print(i,"x",a,"=",a*i)

def ss(num):
    res = 0
    fact = 1
     
    for i in range(1, num+1):
        fact *= i
        res = res + (i/ fact)
         
    return res

def pattern(rows):
    for i in range(rows):
      for j in range(i+1):
        print("* ", end="")
      print()

def square_root(number):
    epsilon = 0.01
    k = number
    guess = k / 2.0
    while abs(guess * guess - k) >= epsilon:
        guess = guess - (guess ** 2 - k) / (2 * guess)
    return guess

#Main Code

while True:
    print("Main Menu\n1.GCD\n2.Prime Number\n3.Division\n4.Sum of Digits\n5.Multiplication Table\n6.Sum of a Series\n7.Pattern Printing\n8.Square Root(Newton's Method)")
    ch=int(input("Enter your choice:"))
    if ch==1:
       a=int(input("Enter 1st Number:"))
       b=int(input("Enter 2nd Number:"))
       print("GCD of",a,"and",b,"is",gcd(a,b))
    elif ch==2:
        a=int(input("Enter the Number:"))
        pn(a)
    elif ch==3:
        div()
    elif ch==4:
        a=int(input("Enter the Number:"))
        print("Sum of Digits = ",sd(a))
    elif ch==5:
        a=int(input("Enter the Number:"))
        mult(a)
    elif ch==6:
        num=int(input("Enter the Number:"))
        print("Sum of Series = ",ss(num))
    elif ch==7:
        rows=int(input("Enter the Number of Rows:"))
        pattern(rows)
    elif ch==8:
        number=int(input("Enter the Number:"))
        print("Square Root = ",square_root(number))
    else:
        print("Enter Valid Choice!")
    x=input("Do you want to continue?(y/n):")
    if x.lower()=='n':
        break