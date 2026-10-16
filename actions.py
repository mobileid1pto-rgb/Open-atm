import database
import random


class Account():
    def __init__(self, acc_num, name, pin, balance):
        self.acc_num = acc_num
        self.name = name
        self.pin = pin
        self.balance = balance


def create_account(name):
    accounts = database.load_accounts()
    acc_num = str(random.randint(200000, 999999))
    # this loop is to get rid of duplicates
    while acc_num in accounts:
        acc_num = str(random.randint(200000, 999999))
    pin = str(random.randint(1000, 9999))
    balance = random.randint(5000, 25000)
    accounts[acc_num] = {"name": name, "pin": pin, "balance": balance}
    database.save_accounts(accounts)
    return acc_num, pin


def log_in(acc_num, pin):
    accounts = database.load_accounts()
    account = accounts.get(acc_num)
    if account and account["pin"] == pin:
        # class object created here
        Active_Account = Account(
            account,
            account["name"],
            account["pin"],
            account["balance"])
        return Active_Account
    elif account and account["pin"] != pin:
        return "2"
    else:
        return "1"
