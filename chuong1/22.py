# Câu 22: Viết hàm tính xác suất bóng đèn hư

from math import comb

def calculate_probability(N, D, M):
    # Kiểm tra nếu số lượng bóng chọn vượt quá tổng số bóng đèn
    if M > N:
        return 0.0

    # Tính xác suất
    numerator = comb(D, 1) * comb(N - D, M - 1)
    denominator = comb(N, M)

    probability = numerator / denominator
    return probability

# Thông số đầu vào
N = int(input("Nhập tổng số bóng đèn trong hộp (N): "))
D = int(input("Nhập số bóng đèn bị hư (D): "))
M = int(input("Nhập số bóng đèn được chọn (M): "))

# Tính xác suất
probability = calculate_probability(N, D, M)

print(f"Xác suất để chọn được 1 bóng đèn hư trong {M} bóng đèn là: {probability:.6f}")
