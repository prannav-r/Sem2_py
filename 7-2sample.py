#2.ATM Machine

balance=10000

def pin_check(pin):
    if not(len(pin)==4 and pin.isnumeric()):
        global balance
        return True

pin=input("Enter the ATM pin: ")
if pin_check(pin):
        print("Invalid Pin")
        exit()
    
def withdraw(x,balance):
    if x>balance:
        print("Insufficient Balance")
    else:
        balance-=x
        print(balance)
        print("Withdrew Successfully")

while True:
    print("ATM Machine")
    print("1.Withdraw\n2.Check Balance\n3.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        x=int(input("Enter the amount to withdraw: "))
        withdraw(x,balance)
    elif ch==2:
        print("Balance =",balance)
    elif ch==3:
        break
    else:
        print("Enter Valid Choice")