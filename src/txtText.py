# example.py
import ddddocr
import os

ocr = ddddocr.DdddOcr()
def a(x):
    try:
        c = os.listdir(x)
        return len(c)
    except Exception as e:
        print(f"Error: {e}")
        return 0


fileName = "../images"

fileNum = a(fileName)

print(f"在目录'{fileName}'下有{fileNum}个文件")

for i in range(fileNum):
    image = open(f"../images/img{i}.jpg", "rb").read()
    result = ocr.classification(image)
    print(f"第{i + 1}个字为{result}")
