def sum_fact(n):
    s=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            s+=i
    return s
a=int(input("enter the number"))
s_f=sum_fact(a)
print("sum of factors",s_f)
