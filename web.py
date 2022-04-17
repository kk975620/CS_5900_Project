import os
from selenium import webdriver
import time
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

#Search URL for Cleveland-Hopkins International airport (CLE)

driver.get("https://prd-tnm.s3.amazonaws.com/index.html?prefix=StagedProducts/Elevation/13/TIFF/current/n42w082/")
soup = BeautifulSoup(driver.page_source,'html.parser')
listing = soup.find('div',id='listing').pre
links = []
for link in listing.findAll('a'):
  href = link.get('href')
  links.append(href)
tiff_url= links[3]

r = requests.get(tiff_url, allow_redirects=True)
open('USGS_13_n42w082.tif', 'wb').write(r.content)

driver.quit()