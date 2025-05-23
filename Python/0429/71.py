class BankAccount:
    def __init__(self, acnt):
        self.acnt = acnt
        self.balance = 0
    def deposit(self, amt):
        self.balance += amt
    def withdraw(self, amt):
        if self.balance >= amt:
            self.balance -= amt
        else:
            print("잔액 부족")
a = BankAccount('123-456')
a.deposit(10000)
a.withdraw(5000)

b = BankAccount('456-789')
b.deposit(2000)