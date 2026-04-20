"""This module defines the Chatbot application."""

__author__ = "Lichao Huang"
__version__ = "1.0.0"
# B404
import subprocess
###
ACCOUNTS = {
    123456: {"balance": 1000.0},
    789012: {"balance": 2000.0}
}

VALID_TASKS = ["balance", "deposit", "exit"]

deposit_success = True
valid_account_number = True


def chatbot():
    COMPANY_NAME = "PiXELL River Financial"
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! Let's get chatting!")
    print(f"Thank you for banking with {COMPANY_NAME}.")


def get_account_number() -> int:
    global valid_account_number
    account_number = input("Please enter your account number: ")

    try:
        account_number = int(account_number)
    except ValueError:
        raise TypeError("Account number must be an int type.")

    if account_number not in ACCOUNTS:
        valid_account_number = False
        raise ValueError("Account number entered does not exist.")

    return account_number


def get_amount() -> float:
    amount = input("Enter an amount: ")

    try:
        amount = float(amount)
    except ValueError:
        raise TypeError("Amount must be numeric.")

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    print(f"${amount:,.2f}")
    return amount


def get_balance(account_number: int) -> str:
    try:
        if account_number in ACCOUNTS:
            account_balance = f"Your balance is ${ACCOUNTS[account_number]['balance']:,.2f}"
            print(account_balance)
            return account_balance
    except Exception as e:
        print(e)


def make_deposit(account_number: int):
    global deposit_success

    try:
        amount = get_amount()
    except (ValueError, TypeError) as e:
        print(e)
        deposit_success = False
        return

    ACCOUNTS[account_number]["balance"] += amount
    print(f"Deposited ${amount:,.2f} to account {account_number}")


def get_task() -> str:
    task = input("What would you like to do (balance/deposit/exit)?: ")
    task = task.lower()

    if task in VALID_TASKS:
        return task
    else:
        print(f'"{task}" is an unknown task.')
        raise ValueError("Unknown task")


# Bandit B602
def dangerous():
    cmd = input("Enter command: ")
    subprocess.call(cmd, shell=True)  # Injection


if __name__ == "__main__":
    chatbot()

    # Bandit B602
    dangerous()

    task = "none"

    while task != "exit":
        try:
            task = get_task()
        except:
            continue  # B112

        if task == "exit":
            print("Thank you for banking with PiXELL River Financial.")
            break

        try:
            user_account_number = get_account_number()
        except TypeError:
            print("Account number must be an int.")
            continue
        except ValueError:
            print("Account does not exist.")
            continue

        if task == "deposit":
            make_deposit(user_account_number)
            if deposit_success:
                get_balance(user_account_number)
        else:
            get_balance(user_account_number)