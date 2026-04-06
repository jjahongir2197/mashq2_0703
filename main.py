class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Pul qo'shildi.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Pul yechildi.")
        else:
            print("Yetarli mablag' yo'q.")

    def get_balance(self):
        return self.__balance


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, owner, balance):
        acc = Account(owner, balance)
        self.accounts.append(acc)

    def show_accounts(self):
        print("\nHisoblar:")
        for acc in self.accounts:
            print(acc.owner, "-", acc.get_balance())

    def find_account(self, owner):
        for acc in self.accounts:
            if acc.owner == owner:
                return acc
        return None


def run_bank():
    bank = Bank()

    bank.create_account("Ali", 1000)
    bank.create_account("Vali", 2000)

    acc = bank.find_account("Ali")

    if acc:
        acc.deposit(500)
        acc.withdraw(300)

    bank.show_accounts()


run_bank()
