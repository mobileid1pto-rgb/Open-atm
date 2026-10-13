from functools import partial
import json
import questionary
from questionary import Choice
import random
import os

# fix for warning cpr
os.environ["PROMPT_TOOLKIT_NO_CPR"] = "1"

# this select changes questionary select for better ui
select = partial(questionary.select, qmark="", pointer=">", instruction=" ")
text = partial(questionary.text, qmark="")


# filepath
FILE = "accounts.json"


def load_accounts():
    if not os.path.exists(FILE):
        return {}
    with open(FILE) as f:
        return json.load(f)


def save_accounts(accounts):
    with open(FILE, "w") as f:
        json.dump(accounts, f, indent=4)

# function to clear screen


def clear():
    os.system("clear")


class Account_Action():
    @staticmethod
    def create_account(name):
        accounts = load_accounts()
        acc_num = str(random.randint(200000, 999999))
        # this loop is to get rid of duplicates
        while acc_num in accounts:
            acc_num = str(random.randint(200000, 999999))
        pin = str(random.randint(1000, 9999))
        accounts[acc_num] = {"name": name, "pin": pin, "balance": 0}
        save_accounts(accounts)
        print(f"Your Account Number: {acc_num}")
        print(f"Your PIN: {pin}")
        input("Enter to continue..")

    @staticmethod
    def log_in(acc_num, pin):
        accounts = load_accounts()
        account = accounts.get(acc_num)
        if account and account["pin"] == pin:
            return account
        return None


class Messages():
    @staticmethod
    def start_message():
        print("-----Welcome to Open Atm-----")

    @staticmethod
    def initial_option():
        acc_access_option = select(
            "--Account Options--",
            choices=[Choice("Create Account", value="1"),
                     Choice("Log In", value="2"),
                     Choice("Exit", value="3")],).ask()
        return acc_access_option

    @staticmethod
    def login_screen():
        try:
            input_acc_num = (
                text("Enter your Account Number: ").ask() or "").strip()
            input_acc_pin = (
                text("Enter your PIN: ").ask() or "").strip()
            return input_acc_num, input_acc_pin
        except ValueError:
            print("Please Enter Valid Input")
            input("Enter to continue..")


while True:
    clear()
    Messages.start_message()
    acc_user_option = Messages.initial_option()
    if acc_user_option == "3":
        exit()
    elif acc_user_option == "1":
        clear()
        Messages.start_message()
        name = (text("Enter your name: ").ask() or "").strip()
        Account_Action.create_account(name)
    elif acc_user_option == "2":
        clear()
        Messages.start_message()
        acc, pin = Messages.login_screen()
        account = Account_Action.log_in(acc, pin)
        if account is None:
            input("Invalid Account\nEnter to continue..")
    else:
        input("Invalid Input\nEnter to continue..")
