class Account:
    def __init__(self,name,account_number):
        self.name = name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.transfers =[]
        self.frozen = True
        self.accounts = [{"account_number":12345, "username":"Alice", "balance": 1000}, {"account_number": 54321, "username": "Bob", "balance": 500}]
        self.account_number = account_number
        self.transactions =[]
        self.close = True

    def deposit(self,amount):
        if amount>0:
            self.deposits.append(amount)
            self.transactions.append(f"Deposit: +{amount}")
            self.balance = self.balance + amount
            return f"Confirmed, you have received {amount}, new balance is {self.balance}"

    def withdrawal(self,amount):

        if amount <= sum(self.balance):
            self.withdrawals.append(amount)
            self.transactions.append(f"Withdrawal: -{amount}")
            self.balance =sum(self.deposits) - amount
            return f"Confirmed, you have withdrawn {amount}, new balance is {self.balance}"
        else:
            return f"You have insufficient funds"

    def get_balance(self):
        deposits = sum(self.deposits)
        withdrawals = sum(self.withdrawals)
        transfers = sum(self.transfers)
        self.balance = deposits - ( withdrawals + transfers)
        return self.balance

    def transfer_funds(self,recipient,amount):
        # if self.account_number == self.recipient:
        #     print("You cannot transfer funds to your own account")
        if amount <= self.get_balance():
            self.withdrawal(amount)
            recipient.deposit(amount)
            return f"You have transferred {amount} from your account to {recipient.name}"
        else:
            return "Insufficient funds"

    def request_loan(self, amount):
        if amount >= 0:
            self.loan += amount
            self.deposits.append(amount)
            return f"Loan of {amount} was successful.Your new balance is {self.get_balance()}"
        else:
            return "You are not elligible for a loan"

    def repay_loan(self,amount):
        if amount > 0:
            self.loan -= amount
            self.balance -= amount
            return f"You've repaid  {amount}, your remaining debt is {self.loan}"

    def view_account_details(self):
        balance = sum(self.deposits) - ( sum(self.withdrawals) + sum(self.transfers))
        print("Name:",self.name)
        print("Account Number:", self.account_number)
        print(f"Balance: ${self.balance}\n")   

    def account_statement(self):
        statement = f"This is an account Statement for Account #{self.account_number}"+ " "
        statement += f"Initial Balance: {self.balance}" + " "
        statement += "Transactions" + " "
        for transaction in self.transactions:
            statement += f"- {transaction}" + " "
        statement += f"Final Balance: {self.balance}"
        return statement


    def set_min_balance(self):
        # if self.balance<=0:
    if check_withdrawal(balance, withdrawal_amount):
        balance -= withdrawal_amount
        print(f"Withdrawal successful. New balance: {balance}")
    else:
        print("Withdrawal failed.") 


    def change_account_owner(self):
        if account_number in accounts:
            self.accounts[account_number]['owner'] = new_owner
            print(f"Account {self.account_number} owner updated to {new_owner}")
            return True
        else:
            print(f"Account {self.account_number} not found.")
            return False


    def interest_calculation(self,rate,time):
        interest = self.balance * rate * time
        return interest

    def close_account(self,username):
        for account in self.accounts:
            if account.username == self.accounts["username"]:
                accounts.remove(account)
                self.balance = 0
                self.deposits.clear()
                self.withdrawals.clear()
                self.loan = 0
                self.closed = True
                print(f"Account for {username} closed.")
                return
            else:
                print("Account not found.")

    def freeze_account(self):
        self.frozen = True
        return "Account has been frozen."

    def unfreeze_account(self):
        self.frozen = False
        return "Account has been unfrozen."

    
    




