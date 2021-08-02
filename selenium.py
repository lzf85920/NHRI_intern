from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
from datetime import datetime, timedelta
import os.path
import os
import oss2

datelist2 = []
for i in [1,7,0]:
    datelist2.append((datetime.now()-timedelta(i)).strftime('%Y-%m-%d')) 
        
download_path = '/root/daily/pixalate_ivt_margin'
path = '/root/daily/pixalate_ivt_margin/'

# Basic set up for Chrome Driver
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"')
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument('ignore-certificate-errors') 
chrome_options.add_argument("--disable-extensions")
prefs = {'download.default_directory' : download_path,'profile.default_content_settings.popups': 0}
chrome_options.add_experimental_option('prefs', prefs)


browser = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)
browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}
command_result = browser.execute("send_command", params)


browser.get('')
WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,'')))
username = browser.find_element_by_xpath('')
username.send_keys('') 
