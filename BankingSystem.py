from Client import Client
from Bank import Bank
from random import randint

bank = Bank()
print()
print("Welcome to {}!".format(bank.name))
print()
running = True
while running:
    print()
    print("""Choose an option:

    1. Open new bank account
    2. Open existing bank account
    3. Exit
    """)
    choice = int(input("1, 2 or 3: "))

    if choice == 1:
        print()
        print("To create an account, please fill in the information below.")
        print()
        name = input("Name: ")
        amount = input("Deposit amount: ")
        print(isinstance(amount, int))
        if bank.check(amount) is True:
            client = Client(name, int(amount), randint(10000, 99999))
        else:
            continue
        #bank.update_db(client)
        print("Account created successfully! Your account number is: ", client.account['account_number'])
        bank.writedata(client)
    elif choice == 2:
        print()
        print("To access your account, please enter your credentials below.")
        print()
        name = input("Name: ")
        account_number = input("Account number: ")
        if bank.check(account_number) is True:
            account_number = int(account_number)
        else:
            continue
        current_client = bank.authentication(name, account_number)
        if current_client:
            print()
            print("Welcome {}!".format(current_client.account['name']))
            acc_open = True
            while acc_open:
                print()
                print("""Choose an option:
    1. Withdraw
    2. Deposit
    3. Balance
    4. Exit
                    """)
                acc_choice = int(input("1, 2, 3 or 4: "))
                if acc_choice == 1:
                    print()
                    amount = input("Withdraw amount: ")
                    if bank.check(amount) is True:
                        current_client.withdraw(int(amount))
                    else:
                        continue
                elif acc_choice == 2:
                    print()
                    amount = input("Deposit amount: ")
                    if bank.check(amount) is True:
                        current_client.deposit(int(amount))
                    else:
                        continue
                elif acc_choice == 3:
                    print()
                    current_client.balance()
                elif acc_choice == 4:
                    print()
                    print("Thank you for visiting!")
                    current_client = ''
                    acc_open = False
                    break
                bank.changedata(current_client)
        else:
            print()
            print("Authentication failed!")
            print("Reason: account not found.")
            continue
    elif choice == 3:
        print()
        print("Bye! have a nice day!")
        running = False