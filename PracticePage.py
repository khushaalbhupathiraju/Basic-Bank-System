class BankingSystem:

    def __init__(self, balance, account):
        self.account = account
        self.balance = balance
    
    def CreditAmount(self, amount):
        self.balance += amount
        print("Amount = ", amount, " Has Been Credited T= Your Account")
        print("Your current Balance is = ", self.currentBalance())

    def DebitAmount(self, amount):
        self.balance -= amount
        print("Amount = ", amount, " Has Been Debited From Your Account")
        print("Your current balance is = ", self.currentBalance())

    def currentBalance(self):
        return self.balance

amount = int(input("Enter the amount your want to debit/credit: "))
account_no = int(input("Enter your account Number: "))
bank = BankingSystem(10000, account_no)
bank.CreditAmount(amount)
bank.DebitAmount(amount)

