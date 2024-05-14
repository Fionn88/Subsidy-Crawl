# 🏛️ Subsidy-Crawl 🏛️

This is the web crawler for the [LINEBot_For_Subsidy_Search](https://github.com/Fionn88/LineBot-Subsidy) project. Currently, we are encountering anti-crawling mechanisms, and the code is still under development.

The "src" is the code that we are currently researching and developing.

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
cd integrations/Selenium/
poetry run python3 cookie.py
```

- Using the cookies, you can successfully crawl.
```
poetry run python3 crawl_test.py
```

### method 2：Using SeleniumBase sometimes passes the Cloudflare validation, and sometimes it doesn't

```
poetry install
```

- For detailed settings, please refer to the README.md under the src directory. The ceawl_url.py script will write to Google Sheet after crawling the government website.
```
cd src/
poetry run python3 ceawl_url.py
```

- Currently, the container is unable to bypass Cloudflare. For more details, please refer to the integrations/Docker/Makefile and integrations/Docker/Dockerfile.
    - If you need to run it, you'll have to pull it to the root directory.


## Licensing

Subsidy-Crawl is under the [MIT license](https://github.com/Fionn88/Subsidy-Crawl/blob/dev/LICENSE).
