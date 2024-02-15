num=int(input("enter the number"))
s=0
n=num
while n>0:
    d=n%10
    f=1
    for i in range(1,d+1):
        f=f*i
    s=s+f
    n//=10
if num==s:
    print("strong number")
else:
    ("not a strong number")
