import logging

logging.basicConfig(
    filename='bank.log',
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance
        logging.info(f"Account created for {account_holder} with initial balance: ${balance}")
    
    def deposit(self, amount):
        if amount < 0:
            logging.error(f"Invalid deposit amount: {amount}")
            raise ValueError("Cannot deposit a negative amount")
        elif amount == 0:
            logging.info(f"Zero deposit detected: ${amount}")
            return
        
        self.balance += amount
        logging.info(f"Deposit: ${amount} | New Balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount < 0:
            logging.error(f"Invalid withdrawal amount: {amount}")
            raise ValueError("Cannot withdraw a negative amount")
        
        if amount > self.balance:
            logging.warning(f"Insufficient funds for withdrawal: {amount}")
            raise ValueError("Insufficient funds")
        
        self.balance -= amount
        logging.info(f"Withdrawal: ${amount} | New Balance: ${self.balance}")
    
    def get_balance(self):
        logging.info(f"Balance check: ${self.balance}")
        return self.balance