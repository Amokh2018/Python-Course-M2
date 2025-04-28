import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Alice", 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)
    
    def test_zero_deposit(self):
        initial_balance = self.account.get_balance()
        self.account.deposit(0)
        self.assertEqual(self.account.get_balance(), initial_balance)

    def test_valid_withdrawal(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 800)

    def test_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)
    
    def test_exact_balance_withdrawal(self):
        account = BankAccount("Bob", 500)
        account.withdraw(500)
        self.assertEqual(account.get_balance(), 0)
    
    def test_negative_withdrawal(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-50)

if __name__ == "__main__":
    unittest.main()