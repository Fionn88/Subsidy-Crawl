from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL")
SHEET_ID = os.environ.get("SHEET_ID")
CREDENTIAL_SERVICE_ACCOUNT = os.environ.get("CREDENTIAL_SERVICE_ACCOUNT")

FORMAT = '%(asctime)s %(filename)s %(levelname)s:%(message)s'

match LOGGING_LEVEL:
    case "DEBUG":
        logging.basicConfig(level=logging.DEBUG, filename='Log.log',
                            filemode='a', format=FORMAT)

    case "INFO":
        logging.basicConfig(level=logging.INFO, filename='Log.log',
                            filemode='a', format=FORMAT)

    case "WARNING":
        logging.basicConfig(level=logging.WARNING, filename='Log.log',
                            filemode='a', format=FORMAT)

    case "ERROR":
        logging.basicConfig(level=logging.ERROR, filename='Log.log',
                            filemode='a', format=FORMAT)

    case "CRITICAL":
        logging.basicConfig(level=logging.CRITICAL, filename='Log.log',
                            filemode='a', format=FORMAT)

    case "PRINT":
        logging.basicConfig(level=logging.INFO, format=FORMAT)

    case _:
        logging.basicConfig(level=logging.NOTSET, filename='Log.log',
                            filemode='a', format=FORMAT)
