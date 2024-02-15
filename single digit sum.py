n=int(input("enter the number"))
while n>9:
    s=0
    while n>0:
        s=s+n%10
        n//=10
    n=s
else:
    s=n
    print("single digit sum",s)
