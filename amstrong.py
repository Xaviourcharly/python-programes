n=int(input("enter the number"))
temp=n
ns=str(n)
nd=len(ns)
sum=0
while n>0:
  d=n%10
  sum=sum+(d**nd)
  n//=10
if temp==sum:
  print("amstrong number")
else:
  print("not amstrong number")
