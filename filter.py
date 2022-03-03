from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


url = "https://www.zara.com/ca/en/woman-trend-58-l4565.html?v1=2044463"
headers = {'User-Agent': 'Mozilla/5.0'}
request = Request(url, headers=headers)
html = urlopen(request).read()
soup = BeautifulSoup(html, "html.parser")

items = soup.find_all("a", {"class": "product-link _item product-grid-product-info__name link"})

links = set()
f = open('links.txt', 'w')

for item in items:
    url = item["href"]
    request = Request(url, headers=headers)
    html = urlopen(request).read()
    soup = BeautifulSoup(html, "html.parser")
    sizeLabel = soup.find_all("div", {"class": "product-detail-size-info__size"})
    for size in sizeLabel:
        size_str = size.find("span").string
        if size_str.find('M') != -1 or size_str.find('27') != -1:
            if size.find("div") == None:
                links.add(url)
                #print(url)
               # print('\n')
                f.write(url)
                f.write('\n')
f.close()
  