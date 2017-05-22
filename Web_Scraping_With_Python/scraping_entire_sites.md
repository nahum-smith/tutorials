# Scraping Entire Sites

## The Exhaustive Site Crawl

1. Start with the top-level-page (like the homepage)
  1. Search for a list of all internal links on the page
  2. For every one of those links, repeat steps 1 + 2

**BUT**
In order to do this effectively, we cannot scour the pages blindly following every links without keeping a record of the links we have previously found.  So we must create a system that tracks our progress.  

**For example:**

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
  global pages
  html = urlopen("http://en.wikipedia.org"+pageUrl)
  bsObj = BeautifulSoup(html)
  for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
    if 'href' in link.attrs:
      if link.attrs['href'] not in pages:
        #We have encountered a new page
        newPage = link.attrs['href']
        print(newPage)
        pages.add(newPage)
        getLinks(newPage)
getLinks("")

```
