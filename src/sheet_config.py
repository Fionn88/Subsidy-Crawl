import gspread
from google.oauth2.service_account import Credentials
import config

global workbook
scopes = ["https://www.googleapis.com/auth/spreadsheets"]

creds = Credentials.from_service_account_file(
    config.CREDENTIAL_SERVICE_ACCOUNT, scopes=scopes)
client = gspread.authorize(creds)

sheet_id = config.SHEET_ID
workbook = client.open_by_key(sheet_id)
