# câu 17 : Viết hàm đệ quy chuyển cơ số 10 sang cơ số thập lục phân

arr = []
lett = ['A', 'B', 'C', 'D', 'E', 'F']

def decToHex(x) :
    if x <= 0 : return
    arr.append(x % 16 if x % 16 < 10 else lett[x % 16 % 10])
    x //= 16
    decToHex(x)


decToHex(317547)
arr.reverse()
print(arr)          