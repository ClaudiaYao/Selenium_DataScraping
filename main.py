import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://global.jd.com/")
time.sleep(5)

div = driver.find_element(By.XPATH, "//div[@class='recommend_list']")

elements = div.find_elements(By.XPATH, "./div/div[@class='item']")

items = []
prices = []
for ele in elements:
    items.append(ele.find_element(By.XPATH, "./div[@class='item_title']").text)
    prices.append(ele.find_element(By.XPATH, "./div[@class='price']").text)

df = pd.DataFrame({"Item": items, "Price": prices})
print(df)

df.to_excel('result.xlsx')
driver.close()