from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3809662043&distance=25&f_AL=true&f_E=4&f_PP=105214831"
           "&f_WT=3&geoId=102713980&keywords=software%20engineer%20c%2B%2B&origin=JOB_SEARCH_PAGE_JOB_FILTER&sortBy=R")
driver.implicitly_wait(60)

sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary.btn-md.btn-secondary-emphasis")

sign_in.click()

user_name = driver.find_element(By.NAME, "session_key")
user_name.send_keys("************")
password = driver.find_element(By.NAME, "session_password")
password.send_keys("********")

submit_butn = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
submit_butn.click()

job_name = driver.find_element(By.LINK_TEXT, "Sr. Software Engineer (Onboard Application) – 2.2")

time.sleep(2)
job_name.click()
# Sr. Software Engineer (Onboard Application) – 2.2

apply_job = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div')
apply_job_button = apply_job.find_element(By.TAG_NAME, "button")
apply_job_button.click()