# Web Scraping and Social Media Scraping Project
*Authors:* Artur Skowroński

- wykop.pl contains articles on current news from Poland and the rest of the world, where users have the opportunity to comment freely (unfortunately these are often hate comments)
- The scope of the analysis is limited to scraping 120 pages of the wykop.pl website, where from each subpage, only the first article was taken into account, which was on the page
- The codes leave open the possibility of changing the scope of the pages analysed as well as the articles. However, please note that if you set the number of scraped pages too high, your requests will be rejected by the website at some point
- In each article, the following articles were scraped: title, nickname of the user who posted the article, number of likes/dislikes/views and all the hashtags that have been placed under the article
- The project was done in 3 different ways using libraries: Beautiful Soup 4, Selenium and Scrapy, which allowed me to check the performance and precision of all the libraries
- In addition, a brief analysis of the data was carried out using the pandas and matplotlib libraries to see which messages dominated the news zone (as at 11.05.2022, 21.30)

Sample chart from EDA     |  Sample output from BeautifulSoup
:-------------------------:|:-------------------------:
![](https://github.com/askovr0n/Portfolio/blob/main/images/Project_8/EDA.png)  |  ![](https://github.com/askovr0n/Portfolio/blob/main/images/Project_8/output.png)

## Instruction how to run the scrapers
### Beautiful Soup (on Windows)
1. Install BeautifulSoup
    * Open Terminal by pressing <kbd>Windows</kbd> + <kbd>R</kbd> and then write `cmd`.
    * Run `pip install beautifulsoup4` command.
2. Run the scraper
    * Open Terminal by pressing <kbd>Windows</kbd> + <kbd>R</kbd> and then write cmd.
    * Navigate to the directory where the script is located using the `cd` command.
    * Run `python BS_wykop.py` command.
### Selenium (on Windows)
1. Install GeckoDriver
    * Go to the geckodriver releases page. Find the latest version of the driver for your platform and download it.  
   On the GeckoDriver [Github](https://github.com/mozilla/geckodriver/releases) website, you can always find the latest release.
    * Extract it using WinRar or any application you may have.
    * Add it to Path using Command Prompt `setx path "%path%;GeckoDriver Path`.
2. Install Selenium
    * Open Terminal by pressing <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd>.
    * Run `pip install selenium` command.
3. Run the scraper
    * Open Terminal by pressing <kbd>Windows</kbd> + <kbd>R</kbd> and then write cmd.
    * Navigate to the directory where the script is located using the `cd` command.
    * Run `python selenium_wykop.py` command.
### Scrapy (on Windows)
1. Install BeautifulSoup
    * Open Terminal by pressing <kbd>Windows</kbd> + <kbd>R</kbd> and then write `cmd`.
    * Run `pip install scrapy` command.
2. Run the scraper
    * Open Terminal by pressing <kbd>Windows</kbd> + <kbd>R</kbd> and then write cmd.
    * Navigate to the directory where the script *scrapy.cfg* is located using the `cd` command.
    * * Run `scrapy crawl wykop -o wykop.csv` command.
