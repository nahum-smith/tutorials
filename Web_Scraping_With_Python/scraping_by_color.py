from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.pythonscraping.com/pages/warandpeace.html'

# Grab the entire page and create a beautisoup object
html = urlopen(url)
bsObj = BeautifulSoup(html, 'lxml')

# use the findall function to extract a Python list of proper
# nouns found by selecting only the text within the <span class='green'><tags</span>
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    # bsObj.get_test() strips all tags from the document and returns a string with text-only
    print(name.get_text())
