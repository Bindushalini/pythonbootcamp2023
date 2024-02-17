import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")

soup = BeautifulSoup(response.text, 'html.parser')
listings = soup.select(selector=".List-c11n-8-84-3-photo-cards address")
price = soup.select(selector=".List-c11n-8-84-3-photo-cards .PropertyCardWrapper__StyledPriceLine")
links = soup.select(selector='.List-c11n-8-84-3-photo-cards a')
listings_list = [x.get_text().strip("\n").strip().strip("|") for x in listings]
price_list = [x.get_text().strip("+/mo") for x in price]
links_list = [x.get('href') for x in links]
print(listings_list)
print(price_list)
print(links_list)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfzTsf0v1-egcdZyAsg22EvmgPAoRt00VrjaNPBZ3oVajTjSg/viewform?usp=sf_link")
data_list = [listings_list, price_list, links_list]
for index in range(len(listings_list)):
    count = 0
    time.sleep(2)
    inputs = driver.find_elements(By.CSS_SELECTOR, "input.whsOnd.zHQkBf")
    for boxes in inputs:
        data = data_list[count][index]
        boxes.send_keys(data)
        count = count + 1
    submit_button = driver.find_element(By.CLASS_NAME, "NPEfkd.RveJvd.snByac")
    submit_button.click()
    time.sleep(2)
    anothr_response = driver.find_element(By.LINK_TEXT, "Submit another response")
    anothr_response.click()
