
class BankAccount:
    bank_name = "Navy Dojo"
    bank_loc = "Los Angeles"
    def __init__(self, int_rate, balance):
        self.int_rate = 0.03
        self.balance = 0
        BankAccount.bank_name = "Wells fargo"


    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited {self.balance}")
        return self


    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < amount:
            print(f"You have insufficient funds " + str(amount))
            charge = amount + 5
            deduct = amount - 5
            print(f"You are being charged for $5 " + "Your account is $" + str(deduct))
            return self
        else:
            self.balance = amount
            print(f"You have withdrawn $ " + str(amount))
            return self

    def display_account(self):
        return self

    def yield_interest(self):
        calculatedInterest = self.int_rate * self.balance
        print(f"Your account interest is {self.int_rate} and your balance is {self.balance}")
        return self

    @classmethod
    def change_bank(cls):
            print(f"The name is: ", cls.bank_name)

    @classmethod
    def change_loc(cls):
        print(cls.bank_loc, "will be the nearest location")

BankAccount.change_bank()
BankAccount.change_loc()




rodney = BankAccount(0.03, 500)
rodney.deposit(300).deposit(400).deposit(100).withdraw(300).deposit(10000).withdraw(30000)
print(f"Your account interest for {rodney.int_rate} Rodney has a balance of {rodney.balance}")
rodney.yield_interest()

selena = BankAccount(0.03, 1000)
selena.deposit(300).deposit(500).deposit(300).deposit(200).deposit(5000).withdraw(700)
print(f"Your account interest is {selena.int_rate} and you Selena has a balance of {selena.balance}")
selena.yield_interest()

ryan = BankAccount(0.03, 1000)
ryan.deposit(400).deposit(900).deposit(700).deposit(2000).withdraw(500)
print(f"Your account interest is {ryan.int_rate} and you Selena has a balance of {ryan.balance}")
ryan.yield_interest()



