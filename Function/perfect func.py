def perfect(n):
    temp=n
    sum=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            sum+=i
    if sum==temp:
        print("perfect")
    else:
        print("not a perfect number")
n=int(input("enter the number"))
temp=n
sum=0
perfect(n)
