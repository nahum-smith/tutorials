# Scraping Wikipedia Content Pages for Links

```python
# Import your tools
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now())

def getLinks(articleUrl):
  html = urlopen("http://en.wikipedia.org"+articleUrl)
  bsObj = BeautifulSoup(html)
  return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                    href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")

while len(links) > 0:
  newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
  print(newArticle)
  links = getLinks(newArticle)
```

1. Set the random number generator seed with current system time, which ensures a random path through articles every time
2. define `getLinks` function.
  * takes in an article URL of the form: '/wiki/...' and prepends the Wikipedia domain name: 'http://en.wikipedia.org'
  * Retrieves BeautifulSoup object from that html.
  * Extracts a list of article link tags based on specific parameters.
3.
