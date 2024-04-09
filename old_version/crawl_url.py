import requests
from bs4 import BeautifulSoup
import random
import time
import re
import datetime

#設定爬蟲日期
today = datetime.date.today()
crawling_date = today.strftime('%Y%m%d')

header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
url_list = []

#設定津貼爬蟲網址清單為url_crawling_今天日期.txt
f = open(f'title_list_{crawling_date}.txt')


def organ_type(pattern, text, none_value, match_value):
    result = re.match(pattern, text)
    
    if result is None:
        return none_value
    else:
        return result.group()

#在申請專區爬蟲 (目前總共31頁) 
for page in range (1, 32):
    
    #延遲時間避免被ban
    delay_choices = [8, 5, 15, 19, 16, 11]  #延遲的秒數
    delay = random.choice(delay_choices)  #隨機選取秒數
    time.sleep(delay)  #延遲
        
    url = f'https://www.gov.tw/News3.aspx?n=2&sms=9037&page={page}&PageSize=200' # 指定網址
    r = requests.get(url, headers=header) # 送請求、並將伺服器的回應存進 r 變數
    soup = BeautifulSoup(r.text, 'html.parser') # 用BeautifulSoup解析回應的內容
    all_subjects = soup.find_all('td', class_ = 'td_title') # 查找所有標題
    all_organ = soup.find_all('td', class_= 'td_organ') # 查找所有發布機關
    for subject in all_subjects:
        name = subject.find('span', string = re.compile ('.*津貼.*|.*補助.*|.*給付.*|.*紓困.*|.*獎助學金.*|.*補貼.*')) 
        if name != None: #符合上述關鍵字的標題才進入判斷
            name_seq = all_subjects.index(subject) #先找到現在判斷的標題在所有標題的index
            organ = (all_organ[name_seq]).find('span', class_ = 'place').text #再依標題的index找到機關的index，並取出機關名稱
            #判定機關屬於中央還是地方政府
            try:
                organ_type = re.match('.*縣政府|.*市政府', organ).group()
            except AttributeError :
                organ_type = '中央政府' 

            name = name.text #把標題中的CSS去除
            link = subject.find('a')['href'] #取得標題的連結

            f.write(f'{name}$$${organ_type}$$$https://www.gov.tw/{link}\n')

        else: #如果不符合關鍵字條件就繼續下一個迴圈
            continue
f.close()