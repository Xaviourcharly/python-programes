def spy(n):
    s=0
    p=1
    while(n>0):
        d=n%10
        s+=d
        p*=d
        n//=10
    if s==p:
        print("spy number")
    else:
        print("not a spy number")
a=int(input("enter the number"))
spy(a)
