from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


TWITTER_EMAIL = os.environ.get("TWITTER_NAME")
TWITTER_PASS = os.environ.get("TWITTER_PASS")
PROMISED_DOWN = 50
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = self.create_driver()
        self.up = 0
        self.down = 0

    def create_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)

        driver.implicitly_wait(60)
        return driver

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        cookie_accept = self.driver.find_element(By.ID, "onetrust-button-group")
        cookie_accept.click()
        start_check = self.driver.find_element(By.CSS_SELECTOR, "div.start-button a")
        start_check.click()
        time.sleep(60)
        result_container = self.driver.find_element(By.CLASS_NAME, "result-container-data")
        self.down = float(result_container.find_element(By.CLASS_NAME, "download-speed").text)
        self.up = float(result_container.find_element(By.CLASS_NAME, "upload-speed").text)

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.driver.get("https://twitter.com/i/flow/login")
            login_user_name = self.driver.find_element(By.NAME, "text")
            login_user_name.send_keys(TWITTER_EMAIL)
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
            password = self.driver.find_element(By.NAME, "password")
            password.send_keys(TWITTER_PASS)
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
            time.sleep(10)
            tweet_msg = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            time.sleep(5)
            message = f"Hey Internet Service provider! My internet speed is {self.down}down/{self.up}up. Although I pay for {PROMISED_DOWN}down/{PROMISED_UP}up\n Bot"
            tweet_msg.send_keys(message)
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]').click()


my_obj = InternetSpeedTwitterBot()
my_obj.get_internet_speed()
my_obj.tweet_at_provider()
