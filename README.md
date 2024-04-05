# Subsidy-Crawl

## Run locally

### Use Host Run

```
poetry install
```

- First, open the URL using Chrome to enable cookie storage.
```
https://www.gov.tw/
```

- To close all Chrome tabs/windows.
- Save the cookies to JSON.
```
poetry run python3 cookie.py
```

- Using the cookies, you can successfully crawl.
```
poetry run python3 crawl.py
```