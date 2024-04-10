from seleniumbase import SB
import time

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
            print("Click Again!")
            # 確定不可行，需再定位，或換方式 => 抓出來的 element #challenge-stage > div > label > input[type=checkbox]
            sb.switch_to_frame('input[type=checkbox]')
            sb.click("span.mark")
        try:
            verify_success(sb)
        except Exception:
            raise Exception("Detected!")
    for titles in driver.find_elements('td.td_title'):
        print(titles.text)
