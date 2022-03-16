from csv import DictWriter
import pandas as pd
from Client import Client
from pathlib import Path

class Bank:
    name = 'International Bank'
    Users = []
    file_path = None

    def __init__(self):
        path = Path(r'C:\Users\JiaJi\PycharmProjects\pythonProject\user_file.csv')
        if not path.is_file():
            with open(r'C:\Users\JiaJi\PycharmProjects\pythonProject\user_file.csv', 'w', newline='') as f:
                headerscsv = ['account_number', 'name', 'holdings']
                dictwriter_object = DictWriter(f, fieldnames=headerscsv)
                dictwriter_object.writeheader()
        self.file_path = r'C:\Users\JiaJi\PycharmProjects\pythonProject\user_file.csv'

    # def update_db(self, client):
    #     self.Users.append(client)

    def authentication(self, name, account_number):
        file = pd.read_csv(self.file_path)
        for row in file.itertuples():
            if name == row.name and account_number == row.account_number:
                print()
                print("Authentication successful!")
                return Client(row.name, row.holdings, row.account_number)

    def writedata(self, input_client: Client):
        with open(self.file_path, 'a', newline='') as f:
            headerscsv = ['account_number', 'name', 'holdings']
            dictwriter_object = DictWriter(f, fieldnames=headerscsv)
            dictwriter_object.writerow(input_client.account)
            f.close()

    def changedata(self, input_client: Client):
        file = pd.read_csv(self.file_path)
        file.loc[file['account_number'] == input_client.account['account_number'], 'holdings'] = input_client.account['holdings']
        #print(file)
        file.to_csv(self.file_path, index=False)