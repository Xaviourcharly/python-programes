class Bank:
    def _init_(self):
        self.balance=0
    def login(self,name,num):
        print("ACCOUNT DETAILS")
        print("-----------------")
        print("Account Holder:",name)
        print("Account Number:",num)
    def deposite(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,w_amount):
        if w_amount>self.balance:
            print("Not Enough balance!!!!!")
        else:
            self.balance=self.balance-w_amount
    def view(self):
        print("Balance Amount=",self.balance)
obj=Bank()
name=input("Enter the Account Holder name:")
num=int(input("Enter the Account Number:"))
obj.login(name,num)
check=0
while(check!=4):
    print("1:Deposite Money")
    print("2:Withdraw Money")
    print("3:View Balanace")
    print("4:Exit")
    check=int(input())
    if check==1:
        amount=int(input("Enter the amount:"))
        obj.deposite(amount)
    elif check==2:
        w_amount=int(input("Enter the amount:"))
        obj.withdraw(w_amount)
    elif check==3:
        obj.view()
    elif check==4:
        pass
    else:
        print("Invalid selection!!!!!")
