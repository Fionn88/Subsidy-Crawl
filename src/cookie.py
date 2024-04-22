from time import sleep
from json import dumps
import browser_cookie3

while True:
    try:
        cookies = browser_cookie3.chrome(domain_name='.www.gov.tw')
        break
    except PermissionError:
        sleep(10)

new_cookies = []
for cookie in cookies:
    new_cookies.append({
        'domain': cookie.domain,
        #'httpOnly': True if cookie.name in ['__cf_bm', 'cf_clearance'] else False, # 可以不填
        'name': cookie.name,
        'path': cookie.path,
        'secure': True if cookie.secure else False, # 必須是True/False，不能是1或0
        'value': cookie.value
        })

with open('我的E政府cookie.json', 'w') as f:
    f.write(dumps(new_cookies))