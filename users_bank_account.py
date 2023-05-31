class Bank_Account(): #created a bank account class
    all_instances =  []


    def __init__(self, int_rate, balance): #account will start from 0 but we can start with different balance just as shown on line 43, 44

      self.int_rate = int_rate
      self.balance = balance
      Bank_Account.all_instances.append(self)
    
    def deposit(self, amount): #increases the account balance by the given ammount
      self.balance += amount # will increase the balance by amount
      # print(f"You made a deposit of: {amount}") #if we want to print everytime it makes a deposit
      return self
    
    def withdraw(self, amount): #decreases the account balance by the given amount
      if (self.balance - amount) > 0: #if condition will work if the account balance is above $0
        self.balance -= amount # and will subtract amount from the balance
        # print(f"You made a withdrawal of: {amount}") #if we want to print everytime to makes a withdrawal
        return self
      # else: #added a else because code made an error message if we changed the beginning balance to -200 or above, on line 43r 44
      #   print(f'Not enough fund to make this withdraw. Balance: {self.balance}') #if account has not enough fund to make the transaction it will display above message and will show balance
      # return self
    
    def display_account_info(self):
      print(f"Your Current Balance Is: {self.balance}") #to show balance information
      return self
    
    def yield_interest(self):
      if self.balance > 0: #if balance is greather than 0 it will earn interest
        self.balance += (self.balance * self.int_rate) # first it will calculate the interest by multupling the rate with current balance and then will add that earned interest to the balance
        return self
      # else: #added else because code made an error message if we changed the beginning balance to - 200 or above, on line 43 and 44
      #   print('Not earnings any interest due to negative balance') #if balance is lower than 0 bank will show message as above
      # return self


    @classmethod #used class attribute but not sure why its not doing anything for the output
    def print_instances(cls):
      for i in cls.all_instances:
        print(i.display_account_info())


John = Bank_Account(0.3, 0) #def code is on line 5 with int_rate and balance
Mike = Bank_Account(0.3, 0) #def code is on line 5 with int_rate and balance


John.deposit(50).deposit(55).deposit(60).withdraw(40).yield_interest().display_account_info() #used i.e chaining to record all deposit and withdraw
Mike.deposit(50).deposit(55).withdraw(30).withdraw(20).withdraw(5).withdraw(5).yield_interest().display_account_info() #used i.e chaining to record all deposit and withdraw



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {"checking": Bank_Account(int_rate=0.02, balance = 0), "savings": Bank_Account(int_rate=0.02, balance=0)}

    def make_deposit(self, account_type, amount):
        self.account[account_type].deposit(amount)
        return self

    def make_withdrawal(self, account_type, amount):
        self.account[account_type].withdraw(amount)
        return self

    def display_user_balance(self):
        for actbal in self.account:
            print(f"{actbal} : {self.account[actbal].balance}")
            return self