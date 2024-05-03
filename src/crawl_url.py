# crawl
from seleniumbase import SB
from selenium.webdriver.common.by import By
# Google Sheet API
import gspread
from google.oauth2.service_account import Credentials
# system & regular expression
import re
import sys
import datetime
import time
import logging
import config

FORMAT = '%(asctime)s %(levelname)s:%(message)s'

if config.LOGGING_LEVEL == "DEBUG":
    logging.basicConfig(level=logging.DEBUG, filename='Log.log',
                        filemode='a', format=FORMAT)
elif config.LOGGING_LEVEL == "INFO":
    logging.basicConfig(level=logging.INFO, filename='Log.log',
                        filemode='a', format=FORMAT)
elif config.LOGGING_LEVEL == "WARNING":
    logging.basicConfig(level=logging.WARNING, filename='Log.log',
                        filemode='a', format=FORMAT)
elif config.LOGGING_LEVEL == "ERROR":
    logging.basicConfig(level=logging.ERROR, filename='Log.log',
                        filemode='a', format=FORMAT)
elif config.LOGGING_LEVEL == "CRITICAL":
    logging.basicConfig(level=logging.CRITICAL, filename='Log.log',
                        filemode='a', format=FORMAT)
elif config.LOGGING_LEVEL == "PRINT":
    logging.basicConfig(level=logging.INFO, format=FORMAT)
else:
    logging.basicConfig(level=logging.NOTSET, filename='Log.log',
                        filemode='a', format=FORMAT)

url_data = [
    ["津貼名稱", "發布單位", "link"]
]


def verify_success(sb):
    sb.assert_exact_text("我的E政府", "h1", timeout=8)
    sb.sleep(4)


with SB(uc_cdp=True, guest_mode=True, headless=True) as sb:
    sb.open("https://www.gov.tw/News3.aspx?n=2&sms=9037&page=1&PageSize=200")
    driver = sb.driver

    try:
        verify_success(sb)
    except Exception:
        """
        When the code reaches this point, an exception occurs,
        preventing successful execution.
        We need an automated detection mechanism
        to keep the code running until success.
        """
        if sb.assert_exact_text("www.gov.tw", "h1"):
            """
            <iframe src=
            "https://challenges.cloudflare.com/cdn-cgi/challenge-platform/h/b/turnstile/if/ov2/av0/rcv0/0/jqouz/0x4AAAAAAADnPIDROrmt1Wwj/dark/normal"
            allow="cross-origin-isolated; fullscreen"
            sandbox="allow-same-origin allow-scripts allow-popups"
            id="cf-chl-widget-jqouz" tabindex="0"
            title="包含 Cloudflare 安全性查問的小工具"
            style="border: none; overflow: hidden;
            width: 300px; height: 65px;"></iframe>
            """
            # sb.switch_to_frame('iframe[title="包含 Cloudflare 安全性查問的小工具"]')
            # sb.click("span.mark")
            logging.error("Can Not Enter The WebSite")
            sys.exit(1)
            # raise Exception("Detected!")

    logging.info("Passing through Cloudflare.")

    all_subjects = driver.find_elements('td.td_title')
    all_organ = driver.find_elements('td.td_organ')
    if not all_subjects or not all_organ:
        logging.error("Page 1 Not found the title or organ")
        sys.exit(1)

    logging.info("The web scraping process is about to begin.")
    for subject in all_subjects:
        name = subject.text
        match_result = re.match('.*津貼.*|.*補助.*|.*給付.* \
                                |.*紓困.*|.*獎助學金.*|.*補貼.*', name)
        # Only titles that match the aforementioned keywords
        # are considered for evaluation.
        if match_result is not None:
            title_seq = all_subjects.index(subject)
            organ = (all_organ[title_seq])
            # The determination of whether an organization
            # belongs to the central or local government.
            try:
                organ_type = re.match('.*縣政府|.*市政府', organ.text).group()
            except AttributeError:
                organ_type = '中央政府'

            link = subject.find_element(By.TAG_NAME, 'a').get_attribute('href')

            url_data.append([name, organ_type, link])

    logging.info("Page 1 Completed")
    pages = driver.find_elements('ul.page')
    if not pages:
        logging.error("Not found the page")
        sys.exit(1)
    # 1 2 3 4 ... 34 => ['1\n2\n3\n4\n', '\n34'] => '34' => 34
    page = int(str(pages[-1].text).split('...')[-1].replace('\n', ''))
    for index in range(2, page + 1):
        sb.open(f"https://www.gov.tw/News3.aspx? \
                n=2&sms=9037&page={index}&PageSize=200")

        all_subjects = driver.find_elements('td.td_title')
        all_organ = driver.find_elements('td.td_organ')
        if not all_subjects or not all_organ:
            logging.error(f"Page {index} Not found the title or organ")
            continue

        for subject in all_subjects:
            name = subject.text
            match_result = re.match('.*津貼.*|.*補助.*|.*給付.* \
                                    |.*紓困.*|.*獎助學金.*|.*補貼.*', name)
            if match_result is not None:
                title_seq = all_subjects.index(subject)
                organ = (all_organ[title_seq])
                try:
                    organ_type = re.match('.*縣政府|.*市政府', organ.text).group()
                except AttributeError:
                    organ_type = '中央政府'

                link = subject.find_element
                (By.TAG_NAME, 'a').get_attribute('href')
                url_data.append([name, organ_type, link])
        logging.info(f"Page {index} Completed")


scopes = ["https://www.googleapis.com/auth/spreadsheets"]

creds = Credentials.from_service_account_file(
    config.CREDENTIAL_SERVICE_ACCOUNT, scopes=scopes)
client = gspread.authorize(creds)

sheet_id = config.SHEET_ID
workbook = client.open_by_key(sheet_id)

today = datetime.date.today()
workSheetName = f"{today}-subsidy-url"

worksheet_list = map(lambda x: x.title, workbook.worksheets())

dataLength = len(url_data)
if workSheetName in worksheet_list:
    sheet = workbook.worksheet(f"{today}-subsidy-url")
else:
    sheet = workbook.add_worksheet(title=f"{today}-subsidy-url",
                                   rows=dataLength, cols=4)

logging.info(f"The {dataLength} data entries are ready to be written.")
num_retries = 4
for i, row in enumerate(url_data):
    for j, value in enumerate(row):
        sleep_time = 60
        for _ in range(0, num_retries):
            try:
                sheet.update_cell(i + 1, j + 1, value)
            except Exception:
                logging.info(f"Wait me for {sleep_time} seconds...")
                time.sleep(sleep_time)
                sleep_time *= 1.5
            else:
                logging.info(f"""The {i + 1} row {j + 1} col
                             has been successfully written.""")
                break

logging.info(f"The {dataLength} data entries have been successfully written.")
