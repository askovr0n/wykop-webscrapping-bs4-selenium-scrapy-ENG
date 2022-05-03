from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass
import datetime

# Mapping
'''REMEMBER TO CHANGE THE BOOLEAN VALUE BELOW !!!! '''
START_100_SCRAPE = False
SET_PAGES_TO_SCRAPE_PER_ONE_LOOP = 2 # 35 IS MAX

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

# Init:
gecko_path = '/usr/local/bin/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options=options, service=ser)

url = 'https://www.wykop.pl/'

# Actual program:
driver.get(url)
time.sleep(5)

# Accept cookies
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='cmp-iframe']"))
driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained ZeroLayer__button___1zzzuM MuiButton-containedPrimary MuiButton-containedSizeLarge MuiButton-sizeLarge MuiButton-fullWidth']").click()
driver.switch_to.default_content()  # Back to main site
driver.find_element(By.XPATH, "/html/body/div[4]/div/a").click()  # Accept privacy politics

websites = []
list_of_result = []

for j in range(1, adjust_loop()):

    for i in range(1, check_pages(SET_PAGES_TO_SCRAPE_PER_ONE_LOOP)):

        check_adv = f'/html/body/div[2]/div/div[3]/div/ul[2]/li[{i}]/div/div[1]/a/span[1]'.format(i)
        check_adv_txt = driver.find_element(By.XPATH, check_adv).text

        if check_adv_txt != 'S':
            site_xpath = f'/html/body/div[2]/div/div[3]/div/ul[2]/li[{i}]/div/div[3]/h2/a'.format(i)
            elem = driver.find_element(By.XPATH, site_xpath)
            elem.click()

            try:
                title = driver.find_element(By.XPATH, "//div[@class='lcontrast m-reset-float m-reset-margin']/h2/span[@class = 'data-wyr']").text
            except:
                title = '' # NIE MAM JESZCZE TYTULU< CZYLI TO JEST TO DO:

            try:
                username = driver.find_element(By.XPATH, "//div[@class='usercard']//span/b").text
            except:
                username = ''

            try:
                likes = driver.find_element(By.XPATH, "//a[@href='#voters']/b").text
            except:
                likes = ''

            try:
                dislikes = driver.find_element(By.XPATH, "//a[@href='#votersBury']/b").text
                # /html/body/div[3]/div/div[3]/div[1]/table/tbody/tr/td[2]/a/b
            except:
                dislikes = ''

            try:
                views = driver.find_element(By.XPATH, "//a[@class='donttouch']//b").text
            except:
                views = ''

            try:
                get_hashtags = driver.find_elements(By.XPATH, "//div[@class='lcontrast m-reset-float m-reset-margin']/div[@class='fix-tagline']/a[position()>1]")
                hashtags = []
                for ghash in get_hashtags:
                    hashtags.append(ghash.text)
            except:
                hashtags = ''

            post_summary = {'title': title, 'username': username, 'post_likes': likes, 'post_dislikes': dislikes,
                            'views': views, 'hashtags': hashtags}
            list_of_result.append(post_summary)
            time.sleep(2)
            driver.back()

    time.sleep(5)
    driver.find_element(By.XPATH, '//a[contains(text(),"następna")]').click() # change site

print(list_of_result)
