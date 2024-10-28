import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement

root = Element("movie")             # 전달된 문자열을 태그(요소)의 이름으로 하는 태그 객체 생성
title = SubElement(root, "title")   # 전달된 파라미터를 부모로 하고 전달된 문자열을 태그의 이름으로 하는 자식 태그 객체 생성
title.text = "트랜스포머"                 # 만들어진 객체의 텍스트 값에 접근하여 태그 내부의 텍스트 값 지정 가능
genre = SubElement(root, "genre")
genre.text = "SF"
rating = SubElement(root, "rating")
rating.text = "8"

ET.ElementTree(root).write("movie.xml", encoding='UTF-8', xml_declaration=True)