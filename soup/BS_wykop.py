from urllib import request
from bs4 import BeautifulSoup as BS
import re
import time

# Mapping
'''REMEMBER TO CHANGE THE BOOLEAN VALUE BELOW !!!! '''
START_100_SCRAPE = True
SET_PAGES_TO_SCRAPE_PER_ONE_LOOP = 1  # 35 IS MAX, 1 IS MIN

# Choose number of subpages
def adjust_loop():
    last_loop = 0
    if START_100_SCRAPE:
        last_loop = 120
    else:
        last_loop = 3  # For testing
    return last_loop

# Check if number of articles per subpage is correct
def check_pages(checker):
    if checker > 35 or checker < 1:
        checker = 1
    return checker


list_of_result = []
cannot_be_scraped = 0

# Loop per each subpage
for idx in range(1, adjust_loop()+1):
    url = f'https://www.wykop.pl/strona/{idx}/'
    html = request.urlopen(url)
    bs = BS(html.read(), 'html.parser')

    tags = bs.find_all('li', {'class':re.compile('link iC')})
    links = []

    # Get links from each subpage - some links are +18, which requires to be logged in. Get rid of them
    iteration_of_article = 0
    for tag in tags:
        iteration_of_article += 1
        try:
            links.append(tag.h2.a['href'])
        except:
            cannot_be_scraped += 1
            print(f'ARTICLE {iteration_of_article} FROM PAGE {idx} CONTAINS CONTENT ONLY FOR ADULTS. CANNOT BE SCRAPED.\n'\
                  f'CURRENT 18+ WHICH CANNOT BE SCRAPED: {cannot_be_scraped}\n')
        continue

    # Loop per each article
    for idx_link, link in enumerate(links[:check_pages(SET_PAGES_TO_SCRAPE_PER_ONE_LOOP)]):
        if re.search('paylink', link):  # Omit advertisements
            print(f'ARTICLE: {idx_link+1}, SUBPAGE: {idx} - ACCESS DENIED: THIS IS ADVERTISEMENT !!!')
        else:
            html = request.urlopen(link)
            bs_new = BS(html.read(), 'html.parser')

            # Scrape variables
            try:
                title = bs_new.find('span',{'class':'data-wyr'}).img['alt']
            except:
                title = bs_new.find('span',{'class':'data-wyr'}).text  # should work, if article contains video

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
                hashtags_all = [hashtag.text for hashtag in hashtags]
            except:
                hashtags_all = ''

            # Saving part
            post_summary = {'title': title,
                            'username': username,
                            'post_likes': likes,
                            'post_dislikes': dislikes,
                            'views': views,
                            'hashtags': hashtags_all}
            list_of_result.append(post_summary)
            print(f'Article: {idx_link+1} from subpage: {idx} has been successfully scraped !')  # Initialize log
    print('The subpage will be changed in 2 seconds.\n')
    time.sleep(2)

print('Below, you can find your final output, number of scraped articles is equal to {}'.format(len(list_of_result)))
print(list_of_result)




