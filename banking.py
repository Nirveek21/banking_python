import random
from os import path
import json


class BankAcc:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ac_no = ""

    def acc_create(self):
        self.ac_no = str(random.randint(100000, 999999))+name[0:3]
        info_file = open(f"{self.ac_no}.txt", "a")
        userinfo = {
            "Name": self.name, "Account number": self.ac_no, "Balance": self.balance}
        userinfo = json.dumps(userinfo)
        info_file.write((userinfo))
        info_file.close()
        print(f"Account for {name} created")
        print(f"Account number {self.ac_no}")


class transanctions(BankAcc):
    def __init__(self):
        super().__init__(self)

    def debit(self):
        ac_no = input("Enter account number :")
        if (path.exists(f"{ac_no}.txt")):
            with open(f"{ac_no}.txt", "r") as info_file:
                d = info_file.read()
            data = json.loads(d)
            print((data["Balance"]))
            amount = int(input("Enter amount to withdraw : "))
            if (data['Balance'] < amount):
                print("Insufficient balance")
            else:
                print(f"{amount} debited from account")
                data["Balance"] = data["Balance"] - amount
            info_file = open(f"{ac_no}.txt", "w")
            userinfo = {
                "Name": data["Name"], "Account number": data["Account number"], "Balance": data["Balance"]}
            userinfo = json.dumps(userinfo)
            info_file.write((userinfo))
            info_file.close()
            print('Rs.', amount, 'Debited successfully')
            print('Remaining balance Rs.', data["Balance"])
        else:
            print("Account does not exist")

    def credit(self):
        ac_no = input("Enter account number :")
        if (path.exists(f"{ac_no}.txt")):
            with open(f"{ac_no}.txt", "r") as info_file:
                d = info_file.read()
            data = json.loads(d)
            print((data["Balance"]))
            amount = int(input("Enter amount to deposit : "))
            data["Balance"] = data["Balance"] + amount
            # self.balance = self.balance + amount
            info_file = open(f"{ac_no}.txt", "w")
            userinfo = {
                "Name": data["Name"], "Account number": data["Account number"], "Balance": data["Balance"]}
            userinfo = json.dumps(userinfo)
            info_file.write((userinfo))
            info_file.close()
            print(f"Rs., {amount}, credited successfully")
            print(f'Current balance Rs., {data["Balance"]}')
        else:
            print("Account does not exist")


# class minbalacc(BankAcc):
#     def __init__(self):
#         super().__init__(self)
#         self.balance = 5000

#     def balan(self):
#         print(self.balance)


while True:
    choice = int(
        input("1 to create Account\n2 to withdraw\n3 to credit\n4 to exit\nEnter your choice : "))
    if (choice == 1):
        name = input("Enter name : ")
        o1 = BankAcc(name)
        o1.acc_create()
    elif (choice == 2):
        o2 = transanctions()
        o2.debit()
    elif (choice == 3):
        o2 = transanctions()
        o2.credit()
    elif (choice == 4):
        break
    else:
        print("Wrong choice")
