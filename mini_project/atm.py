class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def verify_pin(self):
        user_pin = input("Enter PIN: ")
        if user_pin == self.pin:
            print("Login Successful!\n")
            return True
        else:
            print("Incorrect PIN!")
            return False

    def check_balance(self):
        print("Your Balance:", self.balance)

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)



atm = ATM(pin="1234", balance=1000)

print("---- ATM MACHINE ----")

if atm.verify_pin():
    while True:
        print("\n--- MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            atm.deposit()
        elif choice == "3":
            atm.withdraw()
        elif choice == "4":
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid Choice!")
