n=float(input("Nhập số cần tính giai thừa:"))
def giai_thua(n):
    if n == 0:
        return 1
    return n * giai_thua(n - 1)
print ('Ta tính được số giai thừa là: ',giai_thua(n))
