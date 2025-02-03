# Câu 30: Tách tên bài hát và loại tập tin

import re

def splitFileName(s) :
    fileName = re.split(r"[\\/]", s)[-1]
    songName = re.split(r"\.", fileName)
    print(f"File name: {fileName}")
    print(f"Song name: {songName[0]}")

splitFileName("d:\music\muabui.mp3")