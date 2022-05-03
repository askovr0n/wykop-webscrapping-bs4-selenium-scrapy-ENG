from urllib import request
from bs4 import BeautifulSoup as BS
import re
import time

# Mapping
'''REMEMBER TO CHANGE THE BOOLEAN VALUE BELOW !!!! '''
START_100_SCRAPE = False
SET_PAGES_TO_SCRAPE_PER_ONE_LOOP = 1  # 35 IS MAX, 2 IS MIN

def adjust_loop():
    last_loop = 0
    if START_100_SCRAPE:
        last_loop = 101
    else:
        last_loop = 3 # For testing
    return last_loop


def check_pages(checker):
    if checker > 35 or checker <= 1:
        checker = 2
    return checker


list_of_result = []

for idx in range(1, adjust_loop()):
    url = f'https://www.wykop.pl/aktywne/strona/{idx}/'
    html = request.urlopen(url)
    bs = BS(html.read(), 'html.parser')

    tags = bs.find_all('li', {'class':'link iC'})
    try:
        links = [tag.h2.a['href'] for tag in tags if 'link' in tag.h2.a['href']] # we are deleting advertisements
    except:
        links = ''

    for link in links[:check_pages(SET_PAGES_TO_SCRAPE_PER_ONE_LOOP)-1]:
        html = request.urlopen(link)
        bs_new = BS(html.read(), 'html.parser')

        try:
            title = bs_new.find('span',{'class':'data-wyr'}).img['alt']
            # bs_new.find('span',{'class':'data-wyr'}).img['alt']
        except:
            title = bs_new.find('span',{'class':'data-wyr'}).text

        try:
            username = bs_new.find('span',{'class':re.compile('color-[0-9]')}).text
        except:
            username = ''
        try:
            likes = bs_new.find('a', {'href':'#voters'}).text
            likes = int(re.findall('[0-9]{1,5}', likes)[0])
        except:
            likes = ''

        try:
            dislikes = bs_new.find('a', {'href':'#votersBury'}).text
            dislikes = int(re.findall('[0-9]{1,5}', dislikes)[0])
        except:
            dislikes = ''

        try:
            views = bs_new.find('a', {'class':'donttouch','href':'#'}).text.replace("\t", "").replace("\r","").replace("\n","").lstrip()
        except:
            views = ''

        try:
            hashtags = bs_new.find_all('a', {'class':'tag affect create'})
            hashtags_all = [hash.text for hash in hashtags]
        except:
            hashtags_all=''

        post_summary = {'title': title,
                        'username': username,
                        'post_likes': likes,
                        'post_dislikes': dislikes,
                        'views': views,
                        'hashtags': hashtags_all}
        list_of_result.append(post_summary)
    time.sleep(10)
print(list_of_result)




