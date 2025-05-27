class Account:
    def __init__(self,name,account_number):
        self.name = name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.transfers =[]
        self.accounts = [{"account_number":12345, "owner":"Alice", "balance": 1000}, {"account_number": 54321, "owner": "Bob", "balance": 500}]
        self.account_number = account_number
        self.recipient = {"name": "Yordanos", "account_number": 123456789}
        self.transactions =[]

    def deposit(self,amount):
        if amount>0:
            self.deposits.append(amount)
            self.transactions.append(f"Deposit: +{amount}")
            self.balance = self.balance + sum(self.deposits)
            return f"Confirmed, you have received {amount}, new balance is {self.balance}"

    def withdrawal(self,amount):
       if amount <= sum(self.deposits):
            self.withdrawals.append(amount)
            self.transactions.append(f"Withdrawal: -{amount}")
            self.balance =sum(self.deposits) - sum(self.withdrawals)
            return f"Confirmed, you have withdrawn {amount}, new balance is {self.balance}"

    def get_balance(self):
        deposits = sum(self.deposits)
        withdrawals = sum(self.withdrawals)
        transfers = sum(self.transfers)
        self.balance = deposits - ( withdrawals + transfers)
        return balance

    def transfer_funds(self,amount):
        if self.account_number == self.recipient.account_number:
            print("You cannot transfer funds to your own account")
        elif amount <= self.balance:
            self.balance = self.balance - amount
            recipient.balance = recipient.balance + amount 
            print(f"You have transferred {amount} from your account to {recipient.account_number}")
        else:
            print("Insufficient funds")

    # def request_loan(self,loan):
    #     if self.balance ==0:

    # def repay_loan(self):

    def view_account_details(self):
        balance = sum(self.deposits) - ( sum(self.withdrawals) + sum(self.transfers))
        print("Name:",self.name)
        print("Account Number:", self.account_number)
        print(f"Balance: ${self.balance}\n")   

    def account_statement(self):
        statement = f"Account Statement for Account #{self.account_number}"
        statement += f"Initial Balance: {self.balance}"
        statement += "Transactions"
        for transaction in self.transactions:
            statement += f"- {transaction}"
        statement += f"Final Balance: {self.balance}"
        return statement


    # def set_min_balance(self):




    def change_account_owner(self):
        if account_number in accounts:
            accounts[account_number]['owner'] = new_owner
            print(f"Account {account_number} owner updated to {new_owner}")
            return True
        else:
            print(f"Account {account_number} not found.")
            return False


    def interest_calculation(self,principal,rate,time):
        interest = principal * rate * time
        return interest

    def close_account(self,username):
        for account in accounts:
            if account.username == username:
                accounts.remove(account)
                print(f"Account for {username} closed.")
                return
            else:
                print("Account not found.")
