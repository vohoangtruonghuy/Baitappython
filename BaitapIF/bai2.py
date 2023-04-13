def so_sanh(a,b,c):
    max=a
    if max>b:max=b
    if max>c:max=c
    return max

a=int(input('Nhập số thứ nhất: '))
b=int(input('Nhập số thứ hai: '))
c=int(input('Nhập số thứ ba: '))
print('Số lớn nhất là:',max(a,b,c))
