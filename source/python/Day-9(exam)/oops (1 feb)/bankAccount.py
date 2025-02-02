class bankAccount:
    def __init__(self,initial_balance=0):
        self.balance=initial_balance
    
    def deposit(self,amount):
        if amount > 0 :
            self.balance+=amount
            print(f"Deposited amount is {amount}, New Balance in the account is : {self.balance}")
        else:
            print("enter a positive number")
    
    def withdraw(self,amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance-=amount
                print(f"the amount you withdrawn is {amount}, balance avaliable {self.balance}")
            else:
                print("Insfficiant balance")
        else:
            print("enter positive number")

def main():
    p=bankAccount()
    while True:
        print("1. Deposite")
        print("2. Withdraw")
        print("3. exit")
        n=int(input("enter number which operation has to perform"))
        if n == 1:
            amount=int(input("enter the amount you want to deposite:"))
            p.deposit(amount)
        if n == 2:
            amount=int(input("enter the amount you wnat to withdraw :"))
            p.withdraw(amount)
        if n == 3:
            break
main()
        



