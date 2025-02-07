# Câu 34: Các thao tác trên mảng

import math


def oddNumber(arr) :
    print("odd number in array: ")
    oddNum = 0
    for i in range (0, len(arr)) :
        if arr[i] % 2 != 0 : 
            print(arr[i], end=" ")
            oddNum += 1
    print(f"Number of odd: {oddNum}")

def evenNumber(arr) :
    print("even number in array: ")
    evenNum = 0
    for i in range (0, len(arr)) :
        if arr[i] % 2 == 0 : 
            print(arr[i], end=" ")
            evenNum += 1
    print(f"Number of odd: {evenNum}")

def isPrime(x) :
    if x < 2 : return False
    for i in range (2, int(math.sqrt(x)) + 1) :
        if x % i == 0 : return False
    return True

def primeNumber(arr) :
    print("prime number in array: ")
    primeNum = 0
    for i in range (0, len(arr)) :
        if isPrime(arr[i]) : 
            print(arr[i], end=" ")
            primeNum += 1
    print(primeNum)

def notPrimeNumber(arr) :
    print("none prime number in array: ")
    notprimeNum = 0
    for i in range (0, len(arr)) :
        if not isPrime(arr[i]) : 
            print(arr[i], end=" ")
            notprimeNum += 1
    print(notprimeNum)

def deleteEvenNumber(arr) :
    print("array after delete even number: ")
    i = 0
    while i < len(arr):
        if arr[i] % 2 == 0:
            arr.pop(i)
        else:
            i += 1
    print("Array after deleting even numbers:", arr)


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

oddNumber(arr)
evenNumber(arr)
primeNumber(arr)
notPrimeNumber(arr)
deleteEvenNumber(arr)