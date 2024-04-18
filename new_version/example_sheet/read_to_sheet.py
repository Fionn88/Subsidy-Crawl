import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1-iWW4nYbc5Kx8WvAImKNBAXpYCy4mXj4k9SMOZ0R-nU"
sheet = client.open_by_key(sheet_id)

value_list = sheet.sheet1.row_values(1)
print(value_list)