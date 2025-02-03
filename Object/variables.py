class Bank:
    bank_name = "SBI"
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.user_balance = balance

    def display_info(self):
        print(f'Name: {self.name}, Account Number: {self.acc_no}, Balance: {self.user_balance}')

          
