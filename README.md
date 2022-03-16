# OOP-project-Banking-System
![image](https://user-images.githubusercontent.com/92885525/158514153-d07f98e3-71eb-489c-963a-863e9ebbaf1f.png)

The Python script includes three classes to simulate a simple banking system:


#### Class Bank
define __init__ bank, Authentication, create CSV file, update CSV file
#### Class Client
Define services for each client, include withdraw, deposit, check balance
#### BankingSystem
The test file  requests for user information, first asks if user wan to register new account or log in to existing account. If create new account, save user name and account number in csv file. If log in existing file, then check name and account name authentication. Then ask user to choose servicer from class Client, modify balance in CSV file.

```
C:\Users\JiaJi\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/JiaJi/PycharmProjects/pythonProject/BankingSystem.py

Welcome to International Bank!


Choose an option:

    1. Open new bank account
    2. Open existing bank account
    3. Exit
    
1, 2 or 3: 1

To create an account, please fill in the information below.

Name: Joey
Deposit amount: 7000

Account created successfully! Your account number is:  53807

Choose an option:

    1. Open new bank account
    2. Open existing bank account
    3. Exit
    
1, 2 or 3: 2

To access your account, please enter your credentials below.

Name: Joey
Account number: 53807

Authentication successful!

Welcome Joey!

Choose an option:
    1. Withdraw
    2. Deposit
    3. Balance
    4. Exit
                    
1, 2, 3 or 4: 1

Withdraw amount: 1000
The sum of 1000 has been withdrawn from your account balance.
Your current account balance is: 6000 

Choose an option:
    1. Withdraw
    2. Deposit
    3. Balance
    4. Exit
                    
1, 2, 3 or 4: 2

Deposit amount: 3000
The sum of 3000 has been added to your account balance.
Your current account balance is: 9000 

Choose an option:
    1. Withdraw
    2. Deposit
    3. Balance
    4. Exit
                    
1, 2, 3 or 4: 4

Thank you for visiting!

Choose an option:

    1. Open new bank account
    2. Open existing bank account
    3. Exit
    
1, 2 or 3: 3

Bye! have a nice day!

Process finished with exit code 0
```
