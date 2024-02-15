n=int(input("enter the number"))
s=0
p=1
while n>0:
    d=n%10
    n//=10
    s+=d
    p*=d
if s==p:
    print("spy")
else:
    print("not")
    

