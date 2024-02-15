a=0
b=1
i=0
def fib(a,b):
    s=a+b
    print(s,end="")
n=int(input("enter the limit"))
print(a,end="")
print(b,end="")
while i<n-2:
    fib(a,b)
    a,b=b,a+b
    i+=1
