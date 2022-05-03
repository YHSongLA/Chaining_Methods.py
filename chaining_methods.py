class User:
    bank_name = "Bank of Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_bal = 0
# make deposit method
    def make_deposit(self, amount):
        self.account_bal += amount
        return self
# make withdrawal method
    def make_withdrawal(self, amount):
        self.account_bal -= amount
        return self
# display user balance method
    def display_user_balance(self):
        print(f"{self.name}, Balance: {self.account_bal}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_bal -= amount
        other_user.account_bal += amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self



# Instance Users
ana = User("Ana Banana", "ana@python.com")
moxi = User("Moxi Bossy", "moxi@python.com")
monty = User("Monty Python", "monty@python.com")

ana.make_deposit(1000).make_deposit(300).make_deposit(300).make_withdrawal(500).display_user_balance()

moxi.make_deposit(9000).make_deposit(3000).make_withdrawal(1000).make_withdrawal(2000).display_user_balance()

monty.make_deposit(2000).make_withdrawal(500).make_withdrawal(500).make_withdrawal(500).display_user_balance()

# User tranfer funds
monty.transfer_money(ana, 400)