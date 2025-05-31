from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

login_options = Options()
# login_options.add_argument("--headless") # 无头模式，不打开浏览器
service = Service(r"D:\Program Files\WebDriver\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=login_options)