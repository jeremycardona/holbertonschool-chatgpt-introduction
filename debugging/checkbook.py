#!/usr/bin/python3
class Checkbook:
    def __init__(self):
        # Initialize balance to 0.0 when the Checkbook object is created.
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit funds into the checkbook.

        Parameters:
        - amount (float): The amount to be deposited.
        """
        try:
            # Try to convert input to float
            amount = float(amount)
            if amount <= 0:
                print("Please enter a positive amount.")
            else:
                # Update balance and print deposit confirmation
                self.balance += amount
                print("Deposited ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def withdraw(self, amount):
        """
        Withdraw funds from the checkbook.

        Parameters:
        - amount (float): The amount to be withdrawn.
        """
        try:
            # Try to convert input to float
            amount = float(amount)
            if amount <= 0:
                print("Please enter a positive amount.")
            elif amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                # Update balance and print withdrawal confirmation
                self.balance -= amount
                print("Withdrew ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def get_balance(self):
        """Print the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    # Create a Checkbook object
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            amount = input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

