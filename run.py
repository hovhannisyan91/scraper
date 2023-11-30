import pandas as pd
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import yaml


import yaml

# Read data from the config.yaml file
with open('config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)

# Access the values
WEBSITE = config_data['website']
USERNAME = config_data['username']
PASSWORD = config_data['password']



opts=Options()

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                        options=opts)

# driver_path = ChromeDriverManager().install()
# print(driver_path)
def validate_fields(field):
    if field:
        pass
    else:
        field='No Results'
    return field

    
driver.get(WEBSITE)
driver.maximize_window()

try:
    username=driver.find_element(By.ID, 'session_key')
    username.send_keys(USERNAME)
    sleep(0.5)
    password=driver.find_element(By.ID,'session_password')
    password.send_keys(PASSWORD)
    sign_in_button=driver.find_element(By.XPATH,'//*[@type="submit"]')
    sign_in_button.click()
    sleep(10)
except:
    SyntaxError


search=driver.find_element(By.XPATH,'//*[@id="global-nav-typeahead"]/input')
search.send_keys('dentist')
search.send_keys(Keys.RETURN)
sleep(5)

people=driver.find_element(By.XPATH,'//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')
people.click()
sleep(3)

#ember563

from selenium.webdriver.support.ui import Select

locations=driver.find_element(By.XPATH,'//*[@id="searchFilter_geoUrn"]')
locations.click()
sleep(1)

options_search=driver.find_element(By.CSS_SELECTOR,'input[placeholder="Add a location"]')
options_search.send_keys('Armenia')
sleep(1)
driver.find_element(By.CLASS_NAME,'basic-typeahead__selectable').click()
# sleep(5)


driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[5]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]').click()


# reusable-search__entity-result-list list-style-none


  

user_input=input('Enter "Y" to close the browser: ')
if user_input.upper() == 'Y':
    driver.quit()  # Close the browser if 'Y' is entered