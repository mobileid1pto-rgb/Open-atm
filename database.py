import json
import os

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
