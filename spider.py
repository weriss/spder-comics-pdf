import os.path

import requests
from lxml import etree
import re

url = "https://boylove.co/chapter/8496"
res = requests.get(url)
print(res.encoding)
content = res.content
print(content)
html = etree.HTML(content)
imgs=html.xpath('//img[@class="lazy"]/@data-original')

# newurl = 'https://boylove.co/chapter/7742'
cnt = 'https://boylove.co/chapter/8592'

comic_name = "BJ_Alex"
begin = 8496
end = 8592
dirpath = "G:/123/漫画整理/21年12月/" + comic_name +"/"

y=end - begin
x=1
if (os.path.exists(dirpath) == 0):
    os.mkdir(dirpath)
while(x<=y):
    url = "https://boylove.co/chapter/" + str(x+begin)
    res = requests.get(url)
    print(res.encoding)
    content = res.content
    print(content)
    html = etree.HTML(content)
    imgs = html.xpath('//img[@class="lazy"]/@data-original')
    path = dirpath + str(x)
    if (os.path.exists(path) == 0):
        os.mkdir(path)
    print(path)
    cnt=1
    for img in imgs:
        new_path = path + "/"  + str(cnt) + ".jpg"
        print(new_path)
        with open(new_path, "wb") as f:
            Img = requests.get(img)
            f.write(Img.content)
            cnt= cnt+1
    x += 1


