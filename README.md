# 🏛️ Subsidy-Crawl 🏛️

This is the web crawler for the [LINEBot_For_Subsidy_Search](https://github.com/Fionn88/LineBot-Subsidy) project. Currently, we are encountering anti-crawling mechanisms, and the code is still under development.

The "src" is the code that we are currently researching and developing.

## Getting Started and Documentation

### Using SeleniumBase sometimes passes the Cloudflare validation, and sometimes it doesn't

```
poetry install
```

- For detailed settings, please refer to the README.md under the src directory. The crawl_url.py script will write to Google Sheet after crawling the government website.
```
cd src/
poetry run python3 crawl_url.py
```

## Licensing

Subsidy-Crawl is under the [MIT license](https://github.com/Fionn88/Subsidy-Crawl/blob/dev/LICENSE).
