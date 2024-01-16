from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3
import time
from selenium.webdriver.support.ui import Select
import pandas as pd
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import re

# ブラウザをheadlessモード実行
options = webdriver.ChromeOptions()
#ヘッドレスモード（バックグラウンドで起動）で実行。コラボの場合、必須。
options.add_argument('--headless')
#サンドボックスモードの解除。これも必須。
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
wait = WebDriverWait(options,10)

driver = webdriver.Chrome()
#指定したドライバーが見つかるまで待機
driver.implicitly_wait(10)

#urlの指定
url="https://www.google.co.jp/"
driver.get(url)
time.sleep(3)
print("サイトのタイトル：", driver.title)

driver = webdriver.Chrome()
#指定したドライバーが見つかるまで待機
driver.implicitly_wait(10)

#urlの指定
url="https://www.data.jma.go.jp/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2023&month=12&day=&view="

driver.get(url)
time.sleep(3)

day = []
kiatu_list = []
kionn_list = []
situdo_list = []

for date in range(5,36):
    a = driver.find_element(By.XPATH, f'//*[@id="tablefix1"]/tbody/tr[{date}]/td[1]/div/a').text
    day.append(a)

    kiatu = driver.find_element(By.XPATH, f'//*[@id="tablefix1"]/tbody/tr[{date}]/td[2]').text
    kiatu_list.append(kiatu)

    kionn = driver.find_element(By.XPATH, f'//*[@id="tablefix1"]/tbody/tr[{date}]/td[7]').text
    kionn_list.append(kionn)
    
    situdo = driver.find_element(By.XPATH, f'//*[@id="tablefix1"]/tbody/tr[{date}]/td[10]').text
    situdo_list.append(situdo)
print(day)
print(kiatu_list)
print(kionn_list)
print(situdo_list)


# データベースに接続または作成
conn = sqlite3.connect('tenki.sqlite')
cursor = conn.cursor()

# スクレイピング用テーブルの作成
cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY,
        date TEXT,
        pressure TEXT,
        temperature TEXT,
        humidity TEXT
    )
''')

# データベースに挿入
for i in range(len(day)):
    cursor.execute('''
        INSERT INTO weather_data (date, pressure, temperature, humidity) VALUES (?, ?, ?, ?)
    ''', (day[i], kiatu_list[i], kionn_list[i], situdo_list[i]))

# コミットとクローズ
conn.commit()
conn.close()