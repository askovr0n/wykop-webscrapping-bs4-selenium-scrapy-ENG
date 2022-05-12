# Web Scraping and Social Media Scraping Project
## Instruction how to run our scrapers
### Beautiful Soup (on Windows)
1. Install BeautifulSoup
    * Open Terminal by pressing <kbd>Windows</kbd> + <kbd>R</kbd> and then write `cmd`.
    * Run `pip install beautifulsoup4` command.
2. Run the scraper
    * Open Terminal by pressing <kbd>Windows</kbd> + <kbd>R</kbd> and then write cmd.
    * Navigate to the directory where the script is located using the `cd` command.
    * Run `python bs_wykop.py` command.
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
### Scrapy
1. Install BeautifulSoup
    * Open Terminal by pressing <kbd>Windows</kbd> + <kbd>R</kbd> and then write `cmd`.
    * Run `pip install scrapy` command.
2. Run the scraper
    * Open Terminal by pressing <kbd>Windows</kbd> + <kbd>R</kbd> and then write cmd.
    * Navigate to the directory where the script *scrapy.cfg* is located using the `cd` command.
    * * Run `scrapy crawl wykop -o wykop.csv` command.
