# Selenuim Solution

## Getting Started and Documentation

### We're facing blocking from CloudFlare, with a 30-minute verification interval. However, the driver is unable to pass through.

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
cd integrations/Selenium/
poetry run python3 cookie.py
```

- Using the cookies, you can successfully crawl.
```
poetry run python3 crawl_test.py
```