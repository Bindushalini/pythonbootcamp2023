from selenium import webdriver
from selenium.webdriver.common.by import By
import time


five_min_timeout = time.time() + 60*5


def create_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stormyskitten.github.io/CookieClickerUnblocked/")
    driver.implicitly_wait(60)
    return driver


def check_upgrades(drive):
    upgrades_dict = {}
    enabled_products = drive.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    for products in enabled_products:
        prod_price = products.find_element(By.CSS_SELECTOR, ".content .price").text
        prod_price = prod_price.replace(",", '')
        upgrades_dict.update({products: int(prod_price)})
    max_product = max(upgrades_dict, key=upgrades_dict.get)
    max_product.click()


def set_language(drive):
    lang = drive.find_element(By.ID, "langSelect-EN")
    lang.click()


def create_cookie(drive):
    five_sec_timeout = time.time() + 5
    while time.time() <= five_sec_timeout:

        button = drive.find_element(By.ID, "bigCookie")
        button.click()
    check_upgrades(drive)


driver_obj = create_driver()
set_language(driver_obj)

while time.time() <= five_min_timeout:
    time.sleep(1)
    create_cookie(driver_obj)
cookies_per_second = driver_obj.find_element(By.ID, "cookiesPerSecond")

print(f"My game created {cookies_per_second.text} per second")

driver_obj.quit()
