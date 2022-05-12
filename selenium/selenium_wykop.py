from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Mapping
'''REMEMBER TO CHANGE THE BOOLEAN VALUE BELOW !!!! '''
START_100_SCRAPE = False
SET_PAGES_TO_SCRAPE_PER_ONE_LOOP = 1 # 35 IS MAX

# Choose number of subpages
def adjust_loop():
    if START_100_SCRAPE:
        last_loop = 120
    else:
        last_loop = 3 # For testing
    return last_loop

# Check if number of articles per subpage is correct
def check_pages(checker):
    if checker > 35 or checker < 1:
        checker = 1
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

# Loop per each subpage
for idx_subpage in range(1, adjust_loop()+1):

    # Loop per each article
    for idx_article in range(1, check_pages(SET_PAGES_TO_SCRAPE_PER_ONE_LOOP)+1):

        # OMIT THINGS WHICH ARE NOT ARTICLES
        time.sleep(2)
        try:
            check_adv = f'/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/ul[2]/li[{idx_article}]/div[1]/div[1]/a[1]/span|/span[1]'
            check_adv_txt = driver.find_element(By.XPATH, check_adv).text
        except:
            print(f'ARTICLE: {idx_article}, SUBPAGE {idx_subpage} IS NOT AN ARTICLE !')
            continue

        # Check advertisements, we don't want it
        if check_adv_txt != 'S':
            site_xpath = f'/html/body/div[2]/div[2]/div[2]/div/ul[2]/li[{idx_article}]/div/div[3]/h2/a'
            elem = driver.find_element(By.XPATH, site_xpath)
            elem.click()

            # Scrape variables
            try:
                title = driver.find_element(By.XPATH, "//div[@class='lcontrast m-reset-float m-reset-margin']/h2/span[@class = 'data-wyr']").text
            except:
                title = ''

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

    time.sleep(2)
    driver.find_element(By.XPATH, '//a[contains(text(),"następna")]').click()  # change subpage

driver.quit()
print("Below you can find your final output, number of scraped articles is equal to {}".format(len(list_of_result)))
print(list_of_result)
