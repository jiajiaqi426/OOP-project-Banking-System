from random import randint
from csv import DictWriter
from pathlib import Path

class Client:
    # {account_number: xxxxx, name: "xxxxxx", holdings: xxxx}
    account = {}

    def __init__(self, name, deposit, act_num):
        self.account['account_number'] = act_num
        self.account['name'] = name
        self.account['holdings'] = deposit

    def withdraw(self, amount):
        if self.account['holdings'] >= amount:
            self.account['holdings'] -= amount
            print("The sum of {} has been withdrawn from your account balance.".format(amount))
            self.balance()
        else:
            print("Not enough funds!")
            self.balance()

    def deposit(self, amount):
        self.account['holdings'] += amount
        print("The sum of {} has been added to your account balance.".format(amount))
        self.balance()

    def balance(self):
        print("Your current account balance is: {} ".format(self.account['holdings']))


            # w = csv.DictWriter(f, self.account.keys())
            # w.writeheader()
            # w.writerow(self.account)
