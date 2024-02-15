n=4586
lrg=0
while n!=0:
  d=n%10
  if lrg<d:
    lrg=d
  n//=10

print(lrg)

n=int(input("enter a number"))
rev=''
while n!=0:
  d=n%10
  rev=rev+str(d)
  n//=10
print(rev)



