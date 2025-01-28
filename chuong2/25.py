# Câu 25: Viết chương trình kiểm tra chuỗi đối xứng


def stringCheck(str) :
    i = 0
    j = len(str) - 1
    while i < j :
        if str[i] != str[j] : return False
        i += 1
        j -= 1
    return True

while True :
    str = input("Nhap vao chuoi: ")
    if stringCheck(str) : print(f"{str} la chuoi doi xung")
    else : print(f"{str} khong phai chuoi doi xung")
    option = input("Ban co muon tiep tuc? (c/k): ")
    if option == "k" : 
        print("Cam on")
        break