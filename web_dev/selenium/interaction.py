from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()
# driver.get("https://en.wikipedia.org/wiki/Main_Page/")
#
# top_box_article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(top_box_article_count.text)
# top_box_article_count.click()
# driver.quit()


#click method to select any link.

#send_keys - type something in text box - types in the particular text box with curesor

# pass Keys class attribute to send_keys to enter, shift, tab or any othere operation. (importing Keys from common class)

#sign up page



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()
driver.implicitly_wait(60)
driver.get("https://secure-retreat-92358.herokuapp.com/")
fname_input = driver.find_element(By.NAME, "fName")
lname_input = driver.find_element(By.NAME, "lName")
email_input = driver.find_element(By.NAME, "email")
button = driver.find_element(By.CSS_SELECTOR, "button")

fname_input.send_keys("Bindu")
lname_input.send_keys("HC")
email_input.send_keys("sample@gmail.com")

button.click()


