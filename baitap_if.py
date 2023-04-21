def bai_1():
 print('Bài 1:\nChương trình kiểm tra số chẵn hay lẻ trong Python:')
 n=int(input('Nhập một số: '))
 if n%2==0:
    print('là số chẵn')
 else:
    print('la số lẻ')

def bai_2():
 print('Bài 2:\nChương trình tìm số lớn nhất trong 3 số bằng Python:')
 a=int(input('Nhập số thứ nhất: '))
 b=int(input('Nhập số thứ hai: '))
 c=int(input('Nhập số thứ ba: '))
 max=a
 if max<b:max=b
 if max<c:max=c
 print('Số lớn nhất là:',max)

def bai_3():
  print('Bài 3:\nChương trình in ra các ngày trong tháng bằng Python:')
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

def bai_4():
   print('Bài 4:\nViết chương trình cho người dùng nhập vào một số nguyên n. Nếu n lẻ thì in ra màn hình dòng chữ “Số lẻ”. Nếu số n chẵn và lớn hơn hoặc bằng 100 thì in ra màn hình dòng chữ “Số chẵn và lớn hơn hoặc bằng 100”, ngược lại thì in ra dòng chữ “Số chẵn và bé hơn 100”.')
   n=int(input('Nhập một số nguyên: '))
   if n%2!=0:
    print('Số lẻ')
   elif n>=100:
    print('Số chẵn và lớn hơn hoặc bằng 100')
   else:
    print('Số chẵn và bé hơn hoặc bằng 100')

def bai_5():
  print('Bài 5:\nBiện luận phương trình bậc nhất ax+b=0.')
  a=int(input('Nhập a= '))
  b=int(input('Nhập b= '))

  if(a!=0):
    x=(-b/a)
    print('Phương trình nghiệm x= ',x)
  elif a==0 and b==0:
    print('phương trình vô số nghiệm!')
  else:
    print('Phương trình vô nghiệm!')

def bai_6():
   print('Bài 6:\nBiện luận phương trình bậc hai ax2+bx+c=0.')
   import math

   a=int(input('Nhập a= '))
   b=int(input('Nhập b= '))
   c=int(input('Nhập c= '))

   delta=b**2-4*a*c
   if delta>0:
    print('Phương trình có hai nghiệm phân biệt:')
    print('x1=',(-(b)+math.sqrt(delta))/(2*a))
    print('x2=',(-(b)-math.sqrt(delta))/(2*a))
   elif delta<0:
    print('Phương trình có nghiệm kép x1=x2=',-(b/(2*a)))
   else:
    print('Phương trình vô số nghiệm!')

def bai_7():
  print('Bài 7:\nNgười dùng nhập vào một năm là một số nguyên dương bất kì. Cho biết năm đó có là năm nhuận hay không?')
  n = int(input("Nhập số năm: "))
  if(n % 4 == 0):
    print("Năm nhuận")
  else:
    print("Năm không nhuận")

def bai_8():
  print('Bai 8:\nHãy nhập vào tuổi của một người và đưa ra kết luận và lứa tuổi của người đó theo quy tắc sau:\n-Tuổi >0 và <=2 là trẻ sơ sinh\n-Tuổi >2 và <=10 là mhi đồng\n-Tuổi >10 và <=17 là thành niên\n-Tuổi >17 và <=39 là thanh niên\n-Tuổi >39 và <=50 là trung niên\nTừ tuổi >50 là cao niên.')
  tuoi=int(input('Nhập số tuổi: '))

  if tuoi>0 and tuoi<=2:
    print('Trẻ sơ sinh')
  elif tuoi>2 and tuoi<=10:
    print('Nhi đồng')
  elif tuoi>10 and tuoi<=17:
    print('Thành niên')
  elif tuoi>17 and tuoi <=39:
    print('Thanh niên')
  elif tuoi>39 and tuoi<=50:
    print('Trung niên')
  else:
    print('Cao niên')

def bai_9():
  print('Bai 9:\nHãy nhập vào năm sản xuất của một máy vi tính sau đó đưa ra đề xuát đối với máy tính đó theo quy tắc sau:\n-Nếu năm sản xuất >=15 thì đưa ra đề xuất là thay thế\n-Nếu năm sản xuất >=10 và <15 thì đưa ra đề xuất là Bảo trì\n-Những trường hợp khác đưa ra đề xuất là Không có đề xuất.')
  nam=int(input('Nhập năm sản xuất: '))

  if nam>=10 and nam<15:
    print('Bảo trì')
  elif nam>=15:
    print('Thay thế')
  else:
    print('Không có đề xuất')

def bai_10():
  print('Bai 10:\nHãy nhập vào 1 điểm trung binhg và xét học bổng đối với điểm trung bình đó theo quy tắc sau:\n-Nếu điểm trung bình >=9 thì học bổng là 5000000\n-Nếu điểm trung bình >=8 và <9 thì học bổng là 3000000\n-Nếu điểm trung bình >=7 và <8 thì học bổng là 1000000\n-Những trường hợp còn lại học bổng =0')
  diem=int(input('Nhập số điểm: '))
  if diem>=9:
   print('Học bổng là 5000000')
  elif diem>=8 and diem<9:
   print('Học bổng là 3000000')
  elif diem>=7 and diem<8:
   print('Học bổng là 1000000')
  else:
   print('Học bổng 0')

def bai_11():
 print('Bài 11:\n1.Nhập một số N bất kỳ từ bàn phím.\n2.N có phải số nguyên không ?.\n3.Kiểm tra tính chẵn lẻ của N.\n4.N có phải là cố chẵn dương không.\n5.N có phải là số lẻ âm không?.\n6.N có phải chính dương không?')
 import math
 n=float(input('Nhập số N= '))
 if n%1==0:
    print(n,'là số nguyên')
 else:
    print(n,'không phải số nguyên')

 if n%2==0 and n%1==0:
    print(n,'là số chẵn')
 elif n%2==1 and n%1==0:
    print(n,('là số lẻ'))
 if n%2==0 and n>=0:
        print(n,'Là số chẵn dương')
 elif n%2!=0 and n%1<=0:
        print(n,'là số lẻ âm')
 if n<0:
            print(n,'không phải là số chính dương')
 elif n==0:
            print(n,'là số chính dương')
 else:
            sqrt_n= int(math.sqrt(n))
            if sqrt_n**2==n:
                print(n,'là số chính dương')
            else:
                print(n,'không phải số chính dương')

while True:
    bai_tap=int(input('->Ta có các bài từ 1-->11\n->Vui lòng nhập bài cần tìm: '))
    if bai_tap==0:
      break
    elif bai_tap==1:
        bai_1()
    elif bai_tap==2:
        bai_2()
    elif bai_tap==3:
        bai_3()
    elif bai_tap==4:
        bai_4()
    elif bai_tap==5:
       bai_5()
    elif bai_tap==6:
       bai_6()
    elif bai_tap==7:
       bai_7()
    elif bai_tap==8:
       bai_8()
    elif bai_tap==9:
       bai_9()
    elif bai_tap==10:
       bai_10()
    elif bai_tap==11:
       bai_11()
