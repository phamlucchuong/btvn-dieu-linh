# Câu 28: Thống kê số trong chuỗi

import math

def isPrime(x) :
    if x < 2 : return False
    for i in range (2, int(math.sqrt(x) + 1)) :
        if x % i == 0 : return False
    return True

str = input()
splitStr = str.split(";")
even = 0
odd = 0
sum = 0
prime = 0
for i in range (0, len(splitStr)) :
    if splitStr[i] != ";" :
        print(splitStr[i])
        num = int(splitStr[i])
        if num % 2 == 0 : even += 1
        else : odd += 1
        if isPrime(num) : prime += 1
        sum += num
print(f"even number: {even}\nodd number: {odd}\nprime number: {prime}\navg: {sum / len(splitStr)}")