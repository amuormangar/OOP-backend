class Account:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.transactions = []
        self.loan_amount = 0
        self.is_frozen = False
        self.minimum_balance = 0
    def deposit(self,amount):
        if self.is_frozen:
            return "Account is frozen,you cannot deposit"
        if amount <= 0:
            return "Only positive amount can be deposited"
        self.balance += amount 
        self.transactions.append(amount)
        return f"Deposited:{amount}:New balance {self.balance}"
    
    def withdraw(self,amount):
        if self.is_frozen:
            return "Account is frozen,you can't withdraw money"
        if amount <= 0:
            return "You don't have enough amount in your account"
            
        if self.balance-amount < self.minimum_balance:
            return 'Can not withdraw,amount is less than minimun balance'
        self.balance -= amount
        self.transactions.append(amount)
        return f'You have withdraw {amount}:New balance:{self.balance}'

    
    def transfer_funds(self,amount,other_account):
        if amount < 0 :
            return 'amount can be positive numbers only'
        
        self.withdraw(amount)
        other_account.deposit(amount)
        return f'transferred {amount} to {other_account.name}'


    def get_balance(self):
        return f'{self.balance}'

    def request_loan(self,amount):
        if amount <= 0:
            return "You don't have enough amount in your account"
        self.loan_amount+=amount
        self.balance += amount
        self.transactions.append(amount)
        return f'Loan requested:{amount}.New balance:{self.balance}'

    def repay_loan(self,amount):
        if amount <= 0:
            return "You don't have enough amount in your account"
        if amount > self.loan_amount:
            return 'Can not pay more than the loan amount'
        self.balance -= amount
        self.loan_amount -= amount
        return f'repay_loan:{amount}.Remaining amount:{self.loan_amount}'
        

    def account_details(self):
        return f'Account owner:{self.name}.current balance:{self.balance}.Loan amount:{self.loan_amount}'

    def change_account_owner(self, new_owner):
        self.owner = new_owner
        return f"Account owner changed to: {self.owner}"

    def account_statement(self):
        statement = 'account_statement'
        for transaction in self.transactions:
            statement+= f'{transaction}'
        return statement


    def interest_calculation (self):
        interest = self.balance * 0.05 
        self.balance += interest 
        self.transactions.append(interest)
        return f'interest {interest}.New balance:{self.balance}'

    def freeze_account(self):
        self.is_frozen = True 
        return 'Account is locked'

    def unfreeze_account (self):
        self.is_frozen = False
        return 'Account has been unfrozen'

    def set_minimun_balance (self):
        if amount <= 0:
            return 'minimum value must be positive numbers'
        self.minimum_balance = amount
        return f'minimum balance set to:{self.minimun_balance}'

    def close_account(self):
        self.balance = 0
        self.transactions.clear()
        return 'Account closed .All balances set to zero and transactions cleared'   
