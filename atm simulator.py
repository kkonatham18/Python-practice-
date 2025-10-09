balance = 10000.00  # Starting balance
correct_pin = "1234"
max_attempts = 3

# --- Function to check balance ---
def check_balance():
    print(f"💰 Your current balance is: ₹{balance:.2f}\n")

# --- Function to deposit money ---
def deposit(amount):
    global balance
    if amount <= 0:
        print(" Invalid amount. Please enter a positive number.\n")
    elif amount > 50000:
        print(" Deposit limit exceeded. Maximum allowed per transaction is ₹50,000.\n")
    else:
        balance += amount
        print(f"₹{amount:.2f} deposited successfully.\n")

# --- Function to withdraw money ---
def withdraw(amount):
    global balance
    if amount <= 0:
        print(" Invalid amount. Please enter a positive number.\n")
    elif amount % 100 != 0:
        print(" Amount must be in multiples of ₹100.\n")
    elif amount > 20000:
        print(" Withdraw limit exceeded. Maximum allowed per transaction is ₹20,000.\n")
    elif amount > balance:
        print(" Insufficient funds.\n")
    elif (balance - amount) < 1000:
        print(" Minimum balance of ₹1000 must be maintained. Transaction declined.\n")
    else:
        balance -= amount
        print(f" ₹{amount:.2f} withdrawn successfully.\n")

# --- Main ATM function ---
def atm():
    print("Welcome to the ATM")

    # --- PIN verification ---
    for attempt in range(1, max_attempts + 1):
        entered_pin = input(" Enter your 4-digit PIN: ")
        if entered_pin == correct_pin:
            print(" PIN is correct. Access granted.\n")
            break
        else:
            print(f" Incorrect PIN. Attempt {attempt} of {max_attempts}.\n")
    else:
        print(" Card Blocked. Please contact bank.")
        return

    # --- ATM Menu Loop ---
    while True:
        print("===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input(" Select an option (1-4): ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            try:
                amount = float(input(" Enter amount to deposit: ₹"))
                deposit(amount)
            except ValueError:
                print(" Invalid input. Please enter a number.\n")

        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                withdraw(amount)
            except ValueError:
                print(" Invalid input. Please enter a number.\n")

        elif choice == "4":
            print(" Thank you for banking with us!")
            break

        else:
            print(" Invalid option. Please choose between 1 and 4.\n")

# --- Run the ATM program ---
atm()

