# Câu 19: Tháp Hà Nội (*) 


def tower_of_hanoi(n, source, target, auxiliary):
    """
    Giải thuật tháp Hà Nội
    :param n: Số lượng đĩa
    :param source: Cột nguồn
    :param target: Cột đích
    :param auxiliary: Cột trung gian
    """
    if n == 1:
        print(f"Di chuyển đĩa 1 từ {source} sang {target}")
        return

    # Di chuyển n-1 đĩa từ cột nguồn sang cột trung gian
    tower_of_hanoi(n - 1, source, auxiliary, target)

    # Di chuyển đĩa cuối cùng từ cột nguồn sang cột đích
    print(f"Di chuyển đĩa {n} từ {source} sang {target}")

    # Di chuyển n-1 đĩa từ cột trung gian sang cột đích
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Số đĩa
num_disks = int(input("Nhập số lượng đĩa: "))

tower_of_hanoi(num_disks, 'Nguồn', 'Đích', 'Trung gian')
