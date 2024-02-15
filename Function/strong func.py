def strong(n):
    s=0
    while(n>0):
        d=n%10
        f=1
        for i in range(1,d+1):
            f=f*i
        n//=10
        s+=f
    return s
a=int(input("enter the number"))
st=strong(a)
temp=a
if temp==st:
    print("strong number")
else:
    print("not a strong number")
