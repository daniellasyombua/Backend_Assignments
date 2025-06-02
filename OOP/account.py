from datetime import datetime

class Transaction:
    def __init__(self, narration, amount, transaction_type):
        self.date = datetime.now()
        self.narration = narration
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} | {self.transaction_type.upper():<10} | {self.narration:<30} | {self.amount:.2f}"



class Account:
    def __init__(self, owner, account_number):
        self.__account_number = account_number
        self.owner = owner
        self.__transactions = []
        self.__loan = 0
        self.frozen = False
        self.__min_balance = 0

    def is_active(self):
        return not self.frozen

    def deposit(self, amount):
        if not self.is_active():
            return "Account is frozen. Cannot deposit."
        if amount < 0:
            return "You have insufficient funds"
            self.deposits.append(amount)
            self.transactions.append(f"Deposit: +{amount}")
            self.balance = self.get_balance()
            return f"Confirmed, you have received {amount}, new balance is {self.balance}"
            
    def withdraw(self, amount):
        if not self.is_active():
            return "Account is frozen. Cannot withdraw."
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if self.get_balance() - amount < self.__min_balance:
            return f"Insufficient funds. Minimum balance of {self.__min_balance:.2f} must be maintained."
        self.__transactions.append(Transaction("Withdrawal", -amount, "debit"))
        return f"Withdrew {amount:.2f}. New balance is {self.get_balance():.2f}"

    def transfer(self, amount, target_account):
        if not isinstance(target_account, Account):
            return "Target must be an Account instance."
        withdrawal_result = self.withdraw(amount)
        if "Withdrew" in withdrawal_result:
            target_account.deposit(amount)
            self.__transactions.append(Transaction(f"Transfer to {target_account.owner}", -amount, "debit"))
            target_account.__transactions.append(Transaction(f"Transfer from {self.owner}", amount, "credit"))
            return f"Transferred {amount:.2f} to {target_account.owner}."
        return withdrawal_result

    def get_balance(self):
        return sum(t.amount for t in self.__transactions)

    def request_loan(self, amount):
        if amount <= 0:
            return "Loan amount must be positive."
        self.__loan += amount
        self.__transactions.append(Transaction("Loan", amount, "credit"))
        return f"Loan of {amount:.2f} approved. New balance is {self.get_balance():.2f}"

    def repay_loan(self, amount):
        if amount <= 0:
            return "Repayment must be positive."
        repay_amount = min(amount, self.__loan)
        self.__loan -= repay_amount
        self.__transactions.append(Transaction("Loan Repayment", -repay_amount, "debit"))
        return f"Repaid {repay_amount:.2f} of loan. Remaining loan: {self.__loan:.2f}"

    def apply_interest(self):
        interest = self.get_balance() * 0.05
        self.__transactions.append(Transaction("Interest Applied", interest, "credit"))
        return f"Interest of {interest:.2f} applied. New balance: {self.get_balance():.2f}"

    def view_account_details(self):
        return f"Owner: {self.owner}, Account Number: {self.__account_number}, Balance: {self.get_balance():.2f}"

    def change_account_owner(self, new_owner):
        self.owner = new_owner
        return f"Account owner updated to {self.owner}."

    def account_statement(self):
        print(f"Statement for {self.owner}'s Account:")
        for txn in self.__transactions:
            print(txn)

    def freeze_account(self):
        self.frozen = True
        return "Account has been frozen."

    def unfreeze_account(self):
        self.frozen = False
        return "Account has been unfrozen."

    def set_minimum_balance(self, amount):
        if amount < 0:
            return "Minimum balance cannot be negative."
        self.__min_balance = amount
        return f"Minimum balance set to {self.__min_balance:.2f}"

    def close_account(self):
        self.__transactions.clear()
        self.__loan = 0
        return "Account closed. All transactions cleared and balance reset."

    def get_account_number(self):
        return self.__account_number

    def get_transactions(self):
        return list(self.__transactions)




acc1 = Account("Alice", "123456")
acc2 = Account("Bob", "654321")

print(acc1.deposit(10000))
print(acc1.withdraw(200))
print(acc1.transfer(100, acc2))
print(acc1.request_loan(500))
print(acc1.repay_loan(200))
print(acc1.apply_interest())
acc1.account_statement()
print(acc1.freeze_account())
print(acc1.withdraw(100)) # Should fail
print(acc1.unfreeze_account())
print(acc1.set_minimum_balance(300))
print(acc1.withdraw(800)) # Should fail due to minimum balance
print(acc1.change_account_owner("Alice Johnson"))
print(acc1.view_account_details())
print(acc1.close_account())

