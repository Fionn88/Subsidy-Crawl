from json import loads
from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
#option.add_argument('--headless') # 不可用無頭模式，資料不會讀入
driver = webdriver.Chrome(options=option)
# driver.minimize_window() # 但可以縮小
#driver.maximize_window()

# 進入我的E政府
url = 'https://www.gov.tw/'
driver.get(url)
driver.implicitly_wait(8)
time.sleep(1)

# 用cookies繞過驗證
with open('我的E政府cookie.json', 'r') as f:
    cookies = loads(f.read())

for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(0.2)
driver.refresh()
driver.implicitly_wait(15)
time.sleep(2)

driver.get('https://www.gov.tw/News3_Content.aspx?n=2&s=316389')
driver.implicitly_wait(8)
time.sleep(1)

# 試抓資料
for i in driver.find_elements('css selector', 'div[class="css-tr"] div[class="css-th"]'):
    print(i.text)

time.sleep(60)