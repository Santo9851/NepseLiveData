from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import json

url = 'https://www.nepalstock.com.np/live-market'
path = '//div/table'


def openchrome():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    
    #open browser
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    serv = Service("C:\webdriver\chromedriver.exe")
    browser = webdriver.Chrome(service=serv, options=opt)
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