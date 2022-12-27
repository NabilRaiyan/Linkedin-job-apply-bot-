from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

chrome_driver_path = "F:\Software\chromedriver_win32.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=option)

driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3403355181&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

# Log in to linkedin
sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

# Email enter
email = driver.find_element(By.XPATH, '//*[@id="username"]')
email.send_keys("your email address")

# Password enter
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("your password")

# Cliking log in button
log_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
log_in.click()

# apply = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
# apply.click()

# phone = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3403355181-77366355-phoneNumber-nationalNumber"]')
# phone.send_keys("039390303003")
#
# next = driver.find_element(By.XPATH, '//*[@id="ember361"]/span')
# next.click()

time.sleep(3)

# Job1 save notification
job1_save = driver.find_element(By.XPATH,
                                '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button/span[1]')
job1_save.click()
time.sleep(3)

# Job 2 find  website
job2 = driver.find_element(By.XPATH, '//*[@id="ember187"]')
job2.click()

time.sleep(3)

# Job 2 save notification
job2_save = driver.find_element(By.XPATH,
                                '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button/span[1]')
job2_save.click()

# Quit the browser
driver.quit()
