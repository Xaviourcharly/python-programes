class Bank:
    def _init_(self,name,acc_num):
        self.name=name
        self.acc_num=acc_num
        self.bal=0
        print("ACCOUNT DETAILS")
        print("-----------------")
        print("ACCOUNT HOLDER NAME: ", self.name)
        print("ACCOUNT NUMBER: ", self.acc_num)
    def deposit(self):
        dep = int(input("\nEnter the amount: "))
        self.bal+=+dep
        print("\nAmount",dep,"Rs.Deposited Successfully!! \n")
    def withdraw(self):
        wit=int(input("\nEnter the amount: "))
        if wit<=self.bal:
            self.bal-=wit
            print("\nAmount",wit,"Rs. Withdrew Successfully!!")
        else:
            print("\nInsufficient balance!! \n")
    def view(self):
        print("\nThe balance amount is: ", self.bal)
    obj=Bank("Anjali","102030405")
    ch=1
while(ch<4):
    print("\n 1.DEPOSIT \n 2.WITHDRAW \n 3.VIEW  BALANCE  \n 4.EXIT")
    ch = int(input("\n Enter your choice :  "))
    if ch==1:
        obj.deposit()
    elif ch==2:
        obj.withdraw()
    elif ch==3:
        obj.view()
    else:
        if ch==4:
            continue
        else:
            print("\nInvalid input!!")
