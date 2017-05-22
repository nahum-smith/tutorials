from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'


html = urlopen(url)
bsObj = BeautifulSoup(html, 'lxml')

# return a list of links from a wikipedia article
def raw_link_return():
    for link in bsObj.findAll("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'])

def updated_link_return():
    for link in bsObj.find('div', {'id':'bodyContent'}).findAll('a',
                            href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])

updated_link_return()
