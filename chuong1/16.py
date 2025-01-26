# Câu 16: Viết hàm đệ quy chuyển cơ số 10 sang cơ số 2

# khai báo mảng toàn cục để lưu giá trị chuỗi số nhị phân
arr = []
def decToBin(x) :
    # thoát hàm đệ quy khi tham số <= 0
    if x <= 0: return
    
    arr.append(x % 2)       # thêm kết quả phép chia dư của x cho 2
    x //= 2                 # cập nhật lại giá trị cho x = x // 2
    
    # gọi hàm đệ quy với tham số là giá trị x vừa cập nhật
    decToBin(x)


decToBin(17)        # gọi hàm, truyền tham số 
arr.reverse()       # đảo mảng để ra kết quả đúng
print(arr)          