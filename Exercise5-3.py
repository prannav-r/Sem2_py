#3.Menu-driven Program

def check_armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit**3
        temp //= 10
    if sum == n:
        return True
    else:
        return False

def check_deficient(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum < n:
        return True
    else:
        return False

def check_palindrome(n):
    temp = n
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10
    if n == rev:
        return True
    else:
        return False


while True:
        print("1. Check if a given integer is an Armstrong number")
        print("2. Check if a given integer is a Deficient number")
        print("3. Check if a given integer is a Palindrome")
        print("4. Exit the program")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            n = int(input("Enter the number: "))
            if check_armstrong(n):
                print("The number is an Armstrong number")
            else:
                print("The number is not an Armstrong number")
        elif choice == 2:
            n = int(input("Enter the number: "))
            if check_deficient(n):
                print("The number is a Deficient number")
            else:
                print("The number is not a Deficient number")
        elif choice == 3:
            n = int(input("Enter the number: "))
            if check_palindrome(n):
                print("The number is a Palindrome")
            else:
                print("The number is not a Palindrome")
        elif choice == 4:
            break
        else:
            print("Invalid choice")