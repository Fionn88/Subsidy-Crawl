from seleniumbase import SB
from selenium.webdriver.common.by import By
import re

def verify_success(sb):
    sb.assert_exact_text("我的E政府", "h1", timeout = 8)
    sb.sleep(4)

with SB(uc_cdp=True, guest_mode=True) as sb:
    sb.open("https://www.gov.tw/News3.aspx?n=2&sms=9037&page=1&PageSize=200")
    driver = sb.driver
    try:
        verify_success(sb)
    except Exception:
        if sb.assert_exact_text("www.gov.tw", "h1"):
            # <iframe src="https://challenges.cloudflare.com/cdn-cgi/challenge-platform/h/b/turnstile/if/ov2/av0/rcv0/0/jqouz/0x4AAAAAAADnPIDROrmt1Wwj/dark/normal" allow="cross-origin-isolated; fullscreen" sandbox="allow-same-origin allow-scripts allow-popups" id="cf-chl-widget-jqouz" tabindex="0" title="包含 Cloudflare 安全性查問的小工具" style="border: none; overflow: hidden; width: 300px; height: 65px;"></iframe>
            print("Click Again!")
            sb.switch_to_frame('iframe[title="包含 Cloudflare 安全性查問的小工具"]')
            sb.click("span.mark")
        try:
            sb.sleep(4)
            verify_success(sb)
        except Exception:
            raise Exception("Detected!")
    all_subjects =  driver.find_elements('td.td_title')
    all_organ =  driver.find_elements('td.td_organ')
    for subject in all_subjects:
        name = subject.text
        # regex = re.compile('.*津貼.*|.*補助.*|.*給付.*|.*紓困.*|.*獎助學金.*|.*補貼.*')
        match_result = re.match('.*津貼.*|.*補助.*|.*給付.*|.*紓困.*|.*獎助學金.*|.*補貼.*', name)
        if match_result != None: # 符合上述關鍵字的標題才進入判斷
            title_seq = all_subjects.index(subject)
            organ = (all_organ[title_seq])
            # 判定機關屬於中央還是地方政府
            try:
                organ_type = re.match('.*縣政府|.*市政府', organ.text).group()
            except AttributeError:
                organ_type = '中央政府'
            
            link = subject.find_element(By.TAG_NAME, 'a').get_attribute('href')

            print(f'{name}$$${organ_type}$$${link}')