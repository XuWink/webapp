from time import sleep
from selenium.webdriver.common.by import By
from common.driver_config import driver

register_url = f"https://demo5.tp-shop.cn/Home/User/reg.html"
driver.get(register_url)
sleep(3)

telephone = driver.find_element(By.XPATH, "//form/div/div/div/div[1]/div/input")
telephone.send_keys("17838346011")
sleep(1)

image_input = input("请输入图像验证码：")
image_code = driver.find_element(By.XPATH, "//form/div/div/div/div[2]/div/input")
image_code.send_keys(image_input)
sleep(1)

send_button = driver.find_element(By.ID, "count_down")
send_button.click()
sleep(1)
code = input("请输入手机验证码：")
telephone_input_code = driver.find_element(By.XPATH, "//form/div/div/div/div[3]/div/input")
telephone_input_code.send_keys(code)
sleep(1)

gen_password = f"qpwo123@"
password = driver.find_element(By.XPATH, "//form/div/div/div/div[4]/div/input")
password.send_keys(gen_password)
sleep(1)

comfirm_password = driver.find_element(By.XPATH, "//form/div/div/div/div[5]/div/input")
comfirm_password.send_keys(gen_password)
sleep(1)

checkbox = driver.find_element(By.ID, "checktxt")
if not checkbox.is_selected():
    checkbox.click()

sleep(1)

register_button = driver.find_element(By.CLASS_NAME, "regbtn")
register_button.click()
sleep(3)


driver.quit()
