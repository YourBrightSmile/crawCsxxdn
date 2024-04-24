import time

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5'
}
```
fileContent:
https://blog.csdn.net/junbaozi/article/details/130180xxx 第六章xxxxx
```

def downloadFromFile(filePath):
    with open(filePath, 'r+', encoding='utf-8') as f:
        for line in f.readlines():
            url = line.split(' ')[0]
            name = line.split(' ')[1].strip()
            resp = requests.get(url, headers=headers)
            print(name)
            with open(name + ".html", 'w+', encoding='utf-8') as f1:
                f1.write(resp.text)
            time.sleep(5)


def outHtml(filePath, outDir):
    style = '''
    <style>
        body {
            width: 60%;
            margin: auto;
        }
    </style>
    '''
    name = filePath.split("/")[-1]
    soup = BeautifulSoup(open(filePath, "r", encoding='utf-8'), 'html.parser')
    with open(outDir + "/" + name, "w+", encoding="utf-8") as f:
        f.write(style)
        for c in soup.find("div", class_="blog-content-box").contents:
            f.write(str(c))
