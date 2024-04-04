#2.ATM Machine

def is_valid_pin(pin):
    """Checks if the entered PIN is valid (4 numeric characters)."""
    return pin.isdigit() and len(pin) == 4

def get_pin():
    """Prompts the user for a PIN and validates it."""
    while True:
        pin = input("Enter your 4-digit PIN: ")
        if is_valid_pin(pin):
            return pin
        else:
            print("Invalid PIN. Please enter a 4-digit number.")

def display_menu():
    """Displays the menu of options."""
    print("\nATM Menu:")
    print("1. Withdraw Cash")
    print("2. Check Account Balance")
    print("3. Exit")

def select_option():
    """Gets user input for selecting an option."""
    while True:
        try:
            option = int(input("Enter your choice (1-3): "))
            if 1 <= option <= 3:
                return option
            else:
                print("Invalid option. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_balance(balance):
    """Displays the current account balance."""
    print(f"\nYour current balance is: ₹{balance:.2f}")

def withdraw_cash(balance):
    """Allows the user to withdraw cash, updating the balance."""
    while True:
        try:
            amount = float(input("\nEnter amount to withdraw (in multiples of ₹100): "))
            if amount % 100 != 0:
                print("Withdrawal amount must be in multiples of ₹100.")
            elif amount > balance:
                print("Insufficient funds. Your balance is lower than the requested amount.")
            else:
                balance -= amount
                print(f"Withdrawal successful. Please collect your cash (₹{amount:.2f}).")
                print(f"Your remaining balance is: ₹{balance:.2f}")
                return balance
        except ValueError:
            print("Invalid input. Please enter a numerical amount.")

def main():
    """Simulates the ATM functionality."""
    balance = 10000.00  # Replace with actual balance retrieval logic
    valid_pin = "1234"  # Replace with actual PIN verification logic

    while True:
        entered_pin = get_pin()
        if entered_pin == valid_pin:
            display_menu()
            choice = select_option()
            if choice == 1:
                balance = withdraw_cash(balance)
            elif choice == 2:
                check_balance(balance)
            elif choice == 3:
                print("\nThank you for using the ATM. Have a nice day!")
                break
        else:
            print("\nInvalid PIN. Please try again.")

if __name__ == "__main__":
    main()