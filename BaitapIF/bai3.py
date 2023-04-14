t=int(input('Nhập tháng: '))
while not (1<= t and t <=12):
    t=int(input('Nhập từ tháng 1 đến tháng 12'))
if t in (4,6,9,11):
        print('tháng', t ,'có 30 ngày')
elif t==2:
        n=int(input('Nhập năm: '))
        if n%4==0:
         print('tháng',t,'năm',n,'có 29 ngày')
        else:
         print('tháng',t,'năm',n,'có 28 ngày')
else:
    print('tháng',t,'có 31 ngày')
