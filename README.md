# 🏛️ Subsidy-Crawl 🏛️

This is the web crawler for the (LINEBot_For_Subsidy_Search)[https://github.com/Fionn88/LineBot-Subsidy] project. Currently, we are encountering anti-crawling mechanisms, and the code is still under development.

The "old_version" represents the previously successful version of the crawler, serving as a record and backup.

The "new_version" is the code that we are currently researching and developing.

## Getting Started and Documentation

### method 1：We're facing blocking from CloudFlare, with a 30-minute verification interval. However, the driver is unable to pass through.

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
cd new_version/
poetry run python3 cookie.py
```

- Using the cookies, you can successfully crawl.
```
poetry run python3 crawl.py
```

### method 2：Using SeleniumBase may bypass CloudFlare, as the package is different. Further research is needed to determine if crawling can be successfully done.

- The code still needs adjustment.
```
cd new_version/
poetry run python3 cloudflare_bypass.py
```