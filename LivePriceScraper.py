from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import json
import os

url = 'https://www.nepalstock.com.np/live-market'
path = '//div/table'


def openchrome():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service

    CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
    GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')
    #open browser
    options = Options()
    options.binary_location = GOOGLE_CHROME_BIN
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.headless = True
    #serv = Service("C:\webdriver\chromedriver.exe")
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
    return browser
    

def scrape(browser, link, xpath):
    from selenium.webdriver.common.by import By
    browser.get(link)
    time.sleep(5)
    html = browser.find_element(By.XPATH, xpath)
    #print(html.get_attribute('outerHTML'))
    LivePrice = pd.read_html(html.get_attribute('outerHTML'))[0]
    LivePrice = json.loads('{"items":' + LivePrice.to_json(orient='records', date_format='iso') + '}')
    LivePrice = LivePrice['items']
    return LivePrice
    # df=pd.dataframe()
    # return df
browser = openchrome()
LivePrice = scrape(browser, url, path)
#LivePricess