# Câu 31: Tách lấy tên các thành phần trong URL

import re

def splitUrl(url) :
    str = re.split(r"//?", url)
    urlElement = ["protocol", "hostname", "directory", "filename", "query parameters"]
    for i in range (0, len(str)) :
        print(f"{urlElement[i]}: {str[i]}\n")

splitUrl("https://www.mywebsite.com/apparel/skirt.php?sku=phamlucchuong")
# splitUrl("https://www.google.com/search?q=ph%E1%BA%A1m+l%E1%BB%A5c+ch%C6%B0%C6%A1ng&oq=ph%E1%BA%A1m+l%E1%BB%A5c+ch%C6%B0%C6%A1ng&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRifBTIHCAQQIRifBdIBCDMxNTZqMGo5qAIAsAIA&sourceid=chrome&ie=UTF-8")