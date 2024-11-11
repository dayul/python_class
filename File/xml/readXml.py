import xml.etree.ElementTree as ET
import codecs

f = codecs.open('movie.xml', encoding='utf-8')
str = f.read()

tree = ET.ElementTree(ET.fromstring(str))       # 문자열에 있는 내용을 읽고 싶은 형태로 꺼냄 -> 트리
root = tree.getroot()
print(root.tag)     # movie

for child in root:
    print("tag  : " + child.tag + " - " + child.text)

f.close()