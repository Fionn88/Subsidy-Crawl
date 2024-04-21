# Install

## Run locally
- This project requires permissions to access Google Sheets. You can refer to this [link](https://www.youtube.com/watch?v=zCEJurLGFRk&ab_channel=TechWithTim) for instructions on how to add credentials to your local machine and name the file as you like, then add it to the current directory to change the environment variable name.
- You can observe the execution status based on the `Log.log` file generated in the same folder.

---

- Create a file named '.env' within the project directory with the following contents:
- Replace the contents of sheet_id to the ID of the worksheet where you want to write the data.
- If LOGGING_LEVEL is not specified, it will neither write to FILE nor print anything. You have five options available. Usually, INFO is sufficient. The PRINT option also has the `INFO` logging level.
    - "DEBUG"
    - "INFO"
    - "WARNING"
    - "ERROR"
    - "CRITICAL"
    - "PRINT"
```
LOGGING_LEVEL = "INFO"
sheet_id = "{replace_me}"
CREDENTIAL_SERVICE_ACCOUNT = "{YOUR CREDENTIAL FILE NAME}"
```

## Use Host Run

```
poetry install
```

```
poetry run python3 crawl_url.py
```

### A simple tool

- I've written a simple zsh script to execute your test.sh in a for loop. Since using SeleniumBase sometimes passes the Cloudflare validation, and sometimes it doesn't, this can serve as a validation for your web scraper.

- For example, if you want to execute it 10 times.
> test.sh 10
