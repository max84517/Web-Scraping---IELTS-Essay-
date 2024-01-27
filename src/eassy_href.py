import pandas as pd
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.ielts-blog.com/ielts-writing-samples/ielts-essay-samples-of-band-8/#topic-celebrities')
bsobj = BeautifulSoup(html)

article_href = bsobj.find_all('a', {'href': re.compile('https:\/\/www.ielts-blog.com\/ielts-writing-samples\/ielts-essays-band-8\/ielts-essay-topic-.+')})

href_list = [link.get('href') for link in article_href]

with open('essay_href.txt', 'w') as file:   # Set your own file path
    for href in href_list:
        file.write(href + '\n')

