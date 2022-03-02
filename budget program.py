class Budget:

    current_balance = 0.0
    def __init__(self):

        ''' constructor '''
        
        amount = float(input('Enter the budget:' ))
        self.current_balance = amount
    
    def switcher(self):
        argument = int(input('Enter the option: 0 to deposit,\n 1 to withdraw,\n 2 to display current balance\n>'))
        if argument == 0:
            self.deposit()
        elif argument == 1:
            self.withdraw()
        elif argument == 2:
            self.display_current_bal()
        else:
            print('Wrong Input')
    def deposit(self): 

        ''' will add deposited amount to current balance '''

        deposit_amount = float(input('Enter the deposit amount:'))
        self.current_balance = self.current_balance + deposit_amount
        self.display_current_bal()

    def withdraw(self):

        ''' will deduct withdrawn amount from current balance and update the value'''

        withdraw_amount = float(input('Enter the withdrawal amount:'))
        self.current_balance = self.current_balance - withdraw_amount
        self.display_current_bal()

    def display_current_bal(self):
        ''' will display the current balance '''

        print("Current balance:", self.current_balance)
        

'''creating categories of expenses with instances of bugdet object''' 

print('Food')
food = Budget()
print('Clothing')
clothing = Budget()
print('Entertainment')
entertainment = Budget()
print('Household')
household = Budget()


'''switch case using if else, to choose a category to which we can deposit or withdraw money'''

ans = 'y'

while ans == 'y':
    argument = int(input('Enter the option: 0 for food,\n 1 for clothing,\n 2 for entertainment,\n 3 for household\n>'))    
    if argument == 0:
        food.switcher()
    elif argument == 1:
        clothing.switcher()
    elif argument == 2:
        entertainment.switcher()
    elif argument == 3:
        household.switcher()
    else:
        print('Wrong Input')
    ans = input('Do you want to continue?(y/n)')