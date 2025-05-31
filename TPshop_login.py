import time

from selenium.webdriver.common.by import By

from common.driver_config import driver

login_url = f"https://demo5.tp-shop.cn/Home/user/login.html"
driver.get(login_url)

time.sleep(3)

username = driver.find_element(By.ID, "username")
username.send_keys("17838346011")
time.sleep(1)

password = driver.find_element(By.ID, "password")
password.send_keys("qpwo123@")
time.sleep(1)

verify_code = input("请手动输入验证码：")

verifyCode = driver.find_element(By.ID, "verify_code")
verifyCode.send_keys(verify_code)
time.sleep(1)

# submit_button = driver.find_element(By.NAME, "sbtbutton")
submit_button = driver.find_element(By.XPATH, "//*[@id='loginform']/div/div[6]/a")
submit_button.click()

time.sleep(3)

driver.quit()