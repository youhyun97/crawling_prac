## parser.py
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawling.settings")
import django
django.setup()
from myapp.models import Data

def parse_blog():
    req = requests.get('https://mchamp.hackers.com/?r=champstudy&c=lecture/lec_toeic')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        'section > div.recomm_list2.cont_toggle3 > ul > li > a[href]'
        )
    data = []
    for link in my_titles:
        data.append(link['href'])
        print(data)
    return data

if __name__=='__main__':
    blog_data_dict = parse_blog()
    for t in blog_data_dict:
        t = blog_data_dict.pop()
        Data(title=t).save()