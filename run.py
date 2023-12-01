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
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import yaml

import random
def random_number(a:int, b:int)->int:
    return random.randint(a, b)


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
    sleep(random_number(1,3))
    password=driver.find_element(By.ID,'session_password')
    password.send_keys(PASSWORD)
    sign_in_button=driver.find_element(By.XPATH,'//*[@type="submit"]')
    sign_in_button.click()
    sleep(random_number(30,35))
except:
    SyntaxError

schratch=False
if schratch:
    search=driver.find_element(By.XPATH,'//*[@id="global-nav-typeahead"]/input')
    search.send_keys('dentist')
    search.send_keys(Keys.RETURN)
    sleep(random_number(5,10))

    people=driver.find_element(By.XPATH,'//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')
    people.click()
    sleep(random_number(5,10))



    from selenium.webdriver.support.ui import Select

    locations=driver.find_element(By.XPATH,'//*[@id="searchFilter_geoUrn"]')
    locations.click()
    sleep(random_number(3,5))

    options_search=driver.find_element(By.CSS_SELECTOR,'input[placeholder="Add a location"]')
    options_search.send_keys('Armenia')
    sleep(random_number(3,5))
    driver.find_element(By.CLASS_NAME,'basic-typeahead__selectable').click()

    sleep(random_number(5,8))
    aria_lable_show_results='Apply current filter to show results'
    driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[5]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]').click()
                        # f"//button[contains(@aria-label='{aria_lable_show_results}')]").click()

else:
    p=14
    start=f'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103030111%22%5D&keywords=dentsit&origin=FACETED_SEARCH&page={p}&searchId=6ff28bc3-5f2e-494d-89eb-df815f9a69ba&sid=pPI'
    driver.get(start)

data={}

sleep(random_number(3,5))
                                                 
li_element = driver.find_elements(By.XPATH,"//li[@class='reusable-search__result-container']")  # Update the XPath with your specific class or identifier


for page in range(p,55):
    # page=page+1
    namelist=[]
    jobtitlelist=[]
    profilelist=[]

    for i in li_element:
        link=i.find_element(By.CLASS_NAME,'app-aware-link')
        

        try:
            span_element=link.find_element(By.XPATH,'.//span')
            print('found a span')
        
            sleep(random_number(3,5))
            hyperlink=link.get_attribute('href')
            driver.execute_script("window.open(arguments[0], '_blank');", hyperlink)
                # link.click()
                
            sleep(random_number(5,6))
            driver.switch_to.window(driver.window_handles[1])
            sleep(random_number(4,5))
            name=driver.find_element(By.XPATH,"//h1[@class='text-heading-xlarge inline t-24 v-align-middle break-words']")
            position=driver.find_element(By.XPATH,"//div[@class='text-body-medium break-words']")
            namelist.append(name.text)
            jobtitlelist.append(position.text)
            profilelist.append(link)
            driver.close()
            sleep(random_number(1,3))
            driver.switch_to.window(driver.window_handles[0])
            data['Name']=namelist
            data['Jobtitle']=jobtitlelist
            data['Profile']=profilelist
            pd.DataFrame(data).to_csv(f'Linkedin{page}.csv',index=False)
        except:
            print('no span')
            continue
        
    sleep(random_number(5,8))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(random_number(10,20))
    next_page=f'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103030111%22%5D&keywords=dentsit&origin=FACETED_SEARCH&page={page}&searchId=6ff28bc3-5f2e-494d-89eb-df815f9a69ba&sid=pPI'
    driver.get(next_page)
    li_element = driver.find_elements(By.XPATH,"//li[@class='reusable-search__result-container']")
    

user_input=input('Enter "Y" to close the browser: ')
if user_input.upper() == 'Y':
    driver.quit()  # Close the browser if 'Y' is entered




