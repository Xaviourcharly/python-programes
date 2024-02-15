class password:
    passwd="myclass"

    def login(self):

        p=input("enter the password")
        if self.passwd==p:
            print("login successful!!")
        else:
            print("invalid password!!")

    def reset(self):
        rst_p=input("enter the new password")
        self.passwd=rst_p
        print("password reset successfully!!")
obj=password()
ch=1
while (ch<3):
    print("\n 1.LOGIN \n 2.RESET PASSWORD \n 3.EXIT")
    ch = int(input("\n enter your choice: "))
    if ch==1:
        obj.login()
    elif ch==2:
        obj.reset()
    else:
        if ch==3:
            print("exiting the program")
            continue
        else:
            print("invalid choice")
