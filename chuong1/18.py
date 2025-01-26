# Câu 18: Viết hàm xử lý số Fibonacci (*)

# a
arr = [1, 1]
def fibonacci(x) :
    if len(arr) >= x : return arr[x - 1]
    arr.append(arr[-1] + arr[-2])
    return fibonacci(x)

# b
print(fibonacci(1))
# c
for i in range (0, len(arr)) :
    print(arr[i], end=" ")



# d. khử đệ quy
arr2 = [1, 1]
def fibonacci2(x) :
    if len(arr2) >= x : return arr2[x - 1]  
    while len(arr2) < x :
        arr2.append(arr2[-1] + arr2[-2])
    return arr2[x - 1]

print(fibonacci2(9))
for i in range (0, len(arr2)) :
    print(arr2[i], end=" ")