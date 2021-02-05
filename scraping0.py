import requests
import bs4

url='https://www.crummy.com/software/BeautifulSoup/bs4/doc/'
# making a request to an website
r=requests.get(url)
# print(type(r))
# print(r.text)

soup=bs4.BeautifulSoup(r.text, 'lxml')
heading=soup.select('.section')
for h in heading:
    print(h.text)
