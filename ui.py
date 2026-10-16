import actions
import os
import questionary
from actions import Account
from questionary import Choice
from functools import partial

# fix for warning cpr
os.environ["PROMPT_TOOLKIT_NO_CPR"] = "1"

# this select changes questionary select for better ui
select = partial(questionary.select, qmark="", pointer=">", instruction=" ")
text = partial(questionary.text, qmark="")

# function to clear screen


def clear():
    os.system("clear")


def start_message():
    print("-----Welcome to Open Atm-----")


def login_error():
    input("Wrong Account Number or Password\nEnter to continue..")


def no_account():
    input("Account doesn't exist\nEnter to continue..")


def initial_option():
    acc_access_option = select(
        "--Account Options--",
        choices=[Choice("Create Account", value="1"),
                 Choice("Log In", value="2"),
                 Choice("Exit", value="3")],).ask()
    return acc_access_option


def account_creation_screen():
    name = text("Please enter your name: ").ask()
    created_acc_num, created_pin = actions.create_account(name)
    print(f"Your Account Number: {created_acc_num}")
    print(f"Your PIN: {created_pin}")
    input("Enter to continue..")


def login_screen():
    input_acc_num = (
        text("Enter your Account Number: ").ask() or "").strip()
    input_acc_pin = (
        text("Enter your PIN: ").ask() or "").strip()
    log_in_state = actions.log_in(input_acc_num, input_acc_pin)
    return log_in_state


def home_screen(Active_Account: Account):
    clear()
    print(f"Welcome! {Active_Account.name}")
    user_option = select(
        "What would you like to do:",
        choices=[Choice("Withraw", value="1"),
                 Choice("Deposit", value="2"),
                 Choice("Check Balance", value="3"),
                 Choice("Exit", value="4")]).ask()
    return user_option
