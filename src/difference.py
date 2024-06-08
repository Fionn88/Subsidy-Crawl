import datetime
import logging
import time
import sheet_config

worksheet_list = map(lambda x: x.title, sheet_config.workbook.worksheets())
dateList = []

for sheet in worksheet_list:
    sheetNameSplit = sheet.rsplit("-", 2)
    if sheet == "current-subsidy-url" or sheetNameSplit[-1] != 'url':
        continue
    date_part = sheetNameSplit[0]
    dateList.append(date_part)

maxDate = max(dateList,
              key=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d'))
sheet1 = sheet_config.workbook.worksheet("current-subsidy-url")
sheet2 = sheet_config.workbook.worksheet(f'{maxDate}-subsidy-url')

data1 = sheet1.get_all_values()
data2 = sheet2.get_all_values()

data1_first_values = [sublist[0] for sublist in data1]
data2_first_values = [sublist[0] for sublist in data2]

new_data = []
for index, row in enumerate(data2_first_values):
    if row not in data1_first_values:
        new_data.append(data2[index])

deleted_data = []
for index, row in enumerate(data1_first_values):
    if row not in data2_first_values:
        deleted_data.append(data1[index])

dataNewLength = len(new_data)
dataDeletedLength = len(deleted_data)
logging.info(f"""There are a total of {dataNewLength} records to be added and
             a total of {dataDeletedLength} records to be deleted.""")

today = datetime.date.today()
workSheetName = f"{today}-insert-data"
worksheet_list = map(lambda x: x.title, sheet_config.workbook.worksheets())
if workSheetName in worksheet_list:
    sheet = sheet_config.workbook.worksheet(workSheetName)
else:
    sheet = sheet_config.workbook.add_worksheet(title=workSheetName,
                                   rows=dataNewLength, cols=4)

logging.info(f"""Prepare to write {dataNewLength} entries
             to the {workSheetName} Google Sheet.""")
num_retries = 4
for i, row in enumerate(new_data):
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
                logging.info(f"""The {i + 1} row {j + 1} col has been
                             successfully written to the {workSheetName}.""")
                break

logging.info(f"""{dataNewLength} entries have been successfully written to
             the {workSheetName} Google Sheet.""")

workSheetName = f"{today}-deleted-data"
worksheet_list = map(lambda x: x.title, sheet_config.workbook.worksheets())
if workSheetName in worksheet_list:
    sheet = sheet_config.workbook.worksheet(workSheetName)
else:
    sheet = sheet_config.workbook.add_worksheet(title=workSheetName,
                                   rows=dataDeletedLength, cols=4)

logging.info(f"""Prepare to write {dataDeletedLength} entries to
             the {workSheetName} Google Sheet.""")

for i, row in enumerate(deleted_data):
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
                logging.info(f"""The {i + 1} row {j + 1} col has been
                             successfully written to the {workSheetName}.""")
                break

logging.info(f"""{dataDeletedLength} entries have been successfully written to
             the {workSheetName} Google Sheet.""")
