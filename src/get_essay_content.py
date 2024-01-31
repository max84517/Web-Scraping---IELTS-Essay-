import pandas as pd
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_essay_content(href_list):
    num = 1
    for href in href_list:
        html = urlopen(href)
        bsobj = BeautifulSoup(html)

        contents = bsobj.find_all('p')  
        for content in contents:
            if not re.search(r'Click here to see more IELTS essays of Band 8', content.text):
                 with open('sample_essay_' + str(num) + '.txt', 'a') as file:
                    file.write(content.text + '\n')
            else:
                break
        num+=1
    return True