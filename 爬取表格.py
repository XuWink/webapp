from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

# 配置 edgedriver
edge_options = Options()
edge_options.add_argument("--headless") # 无头模式，不打开浏览器
service = Service(r"D:\Program Files\WebDriver\edgedriver_win64\msedgedriver.exe")

# 启动浏览器
driver = webdriver.Edge(service=service, options=edge_options)

# 打开目标网站
url = 'http://www.piaofang.biz/'
driver.get(url)

# 等待页面加载完成
time.sleep(5)  # 简单等待，实际应用中可以使用 WebDriverWait 进行更精确的等待

# 查找表格元素
table = driver.find_element(By.TAG_NAME, 'table')
rows = table.find_elements(By.TAG_NAME, 'tr')

# 这种写法已经在selenium4中被弃用
# table = driver.find_element_by_tag_name('table')
# rows = table.find_elements_by_tag_name('tr')

data = []

for row in rows:
    cols = row.find_elements(By.TAG_NAME, 'td')
    raw_data = [col.text for col in cols]
    data.append(raw_data)

# 关闭浏览器
driver.quit()

# 打印数据
for row in data:
    print(row)

