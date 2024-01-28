from selenium import webdriver
from selenium.webdriver.common.by import By

# # to make sure the Chrome browser does not close
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.in/insta360-Action-Camera-Capture-Optical/dp/B0BCW1S7XR/ref=sr_1_4?crid=2PWY4E8W8F8QQ&keywords=insta+360&qid=1706284702&sprefix=insta%2Caps%2C324&sr=8-4")
#
# value = driver.find_element(By.CLASS_NAME,"a-price-whole")
# print(f"{value.text}")
#
#
#
# driver.close() #closes the active tab
# #driver.quit() #quits entire program
upcoming_events_dict = {}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

upcoming_events = driver.find_element(By.CLASS_NAME, "event-widget")
menu = upcoming_events.find_element(By.CLASS_NAME, "menu")
times = menu.find_elements(By.CSS_SELECTOR, "time")
names = menu.find_elements(By.CSS_SELECTOR, "a")

for index in range(len(times)):
    upcoming_events_dict[index] = {
        'time': times[index].text,
        'name': names[index].text
    }
print(upcoming_events_dict)
