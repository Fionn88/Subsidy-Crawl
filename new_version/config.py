from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL")
SHEET_ID = os.environ.get("SHEET_ID")
CREDENTIAL_SERVICE_ACCOUNT = os.environ.get("CREDENTIAL_SERVICE_ACCOUNT")