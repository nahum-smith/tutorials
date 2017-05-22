import urllib, re
from

def download(url, user_agent='wswp', num_retries=2):
    print('Downloading: ', url)
    headers = {'User-agent': user_agent}
    request = urllib.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib.URLError as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries-1)
    return html

def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>|<a/shref=".*?">(.*?)</a>', sitemap)
    print(links)
    # download each link
    for link in links:
        html = download(link)
        # scrape html here
        # ...
        print(link)

def link_crawler(seed_url, link_regex):
    """Crawl from the given seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        # filter for links matching the regular expression
        for link in get_links(html):
            if re.match(link_regex, link):
                crawl_queue.append(link)

def get_links(html):
    """Return a list of links from html
    """
    # a regular expresssion to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',
                               re.I)
    # list of all links from the webpage
    return webpage_regex.findall(html)
