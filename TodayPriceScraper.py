#For Scraping Today's Price
import pandas as pd
import time
import json

url = 'https://www.nepalstock.com.np/today-price'
path = '//table[@class="table table__lg table-striped table__border table__border--bottom"]'



def openchrome():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.common.exceptions import NoSuchElementException, WebDriverException

    CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
    GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')
    #open browser
    options = Options()
    options.binary_location = GOOGLE_CHROME_BIN
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    #options.headless = True
    #serv = Service("C:\webdriver\chromedriver.exe")
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
    return browser
    

def scrape(browser, link, xpath):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.chrome.options import Options
    browser.get(link)
    time.sleep(3)
    items_per_page = browser.find_element(By.XPATH, "//select")
    dropdown = Select(items_per_page)
    dropdown.select_by_visible_text('500')
    filter_now = browser.find_element(By.XPATH, "//div[@class='box__filter--btns mt-md-3 mt-xl-0']/button[1]")
    filter_now.click()
    html = browser.find_element(By.XPATH, xpath)
    print(html.get_attribute('outerHTML'))
    todayprice = pd.read_html(html.get_attribute('outerHTML'))[0]
    todayprice = json.loads('{"items":' + todayprice.to_json(orient='records', date_format='iso') + '}')
    todayprice = todayprice['items']
    return todayprice


browser = openchrome()
todayprice = scrape(browser, url, path)
#todayprice.to_json('todayprice.json')