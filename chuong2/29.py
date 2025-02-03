# Câu 29: Trích lọc số âm trong chuỗi

import re

def NegativeNumberInStrings(s) :
    str = re.findall(r'-\d+', s)
    for i in range (0, len(str)) :
        print(str[i])

NegativeNumberInStrings("abc-5xyz-12k9l--p")