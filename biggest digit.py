n=int(input("enter the number"))
b_d=0
while n>0:
    d=n%10
    if d>b_d:
        b_d=d
    n//=10
print("the biggest digit of the given numbr is",b_d)
