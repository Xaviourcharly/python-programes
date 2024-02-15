n=3215
sml=9
while n!=0:
  d=n%10
  if sml>d:
    sml=d
  n//=10
print(sml)
