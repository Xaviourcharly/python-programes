a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
x=((b**2)-(4*a*c))
if (x>0):
  x1=((-b)-((x)**(0.5)))/(2*a)
  x2=((-b)+((x)**(0.5)))/(2*a)
  print(x1,x2)
elif x==0:
  x3=(-b)/(2*a)
  print(x3)
else:
  print("img")
