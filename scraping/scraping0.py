# to scrape imdb for top 100 movies


import requests
import bs4

# url you want to scrape
url='https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'

# making a request to an website and getting a response
r=requests.get(url) 

# converting request variable to bs's
soup=bs4.BeautifulSoup(r.text, 'lxml')


# after a little reserch on the website
names=soup.find_all(class_='titleColumn')
for mname in names:
    print(mname.find('a').contents[0])