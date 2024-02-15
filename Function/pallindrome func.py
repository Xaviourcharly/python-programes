def pallindrome(n):
    rev=0
    while(n>0):
        rev=(rev*10)+n%10
        n//=10
    if temp==rev:
        print("the number is pallindrome")
    else:
        print("the number is not pallindrome")
n=int(input("enter the number"))
temp=n
pallindrome(n)
