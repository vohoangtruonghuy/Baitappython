import math
a=int(input('Nhập a= '))
b=int(input('Nhập b= '))
c=int(input('Nhập c= '))

delta=b**2-4*a*c
if delta>0:
  print('Phương trình có hai nghiệm phân biệt: ')
  print('x1= ',(-(b)+math.sqrt(delta))/(2*a))
  print('x2= ',(-(b)-math.sqrt(delta))/(2*a))
elif delta==0:
  print('Phương trình có nghiệm kép x1=x2= ',-(b/(2*a)))
else:
  print('Phương trình vô số nghiệm!')
