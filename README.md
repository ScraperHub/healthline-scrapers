# healthline-scrapers

## Description

This repository contains Python-based scrapers for extracting article listings and detailed content from Healthline. These scrapers leverage the [Crawlbase Crawling API](https://crawlbase.com/crawling-api-avoid-captchas-blocks) to handle JavaScript rendering, CAPTCHA challenges, and anti-bot protections. The extracted data is processed using BeautifulSoup for HTML parsing and Pandas for structured storage.

➡ Read the full blog [here](https://crawlbase.com/blog/how-to-scrape-heathline/) to learn more.

## Scrapers Overview

### Healthline Article Listing Scraper

The Healthline Article Listing Scraper (**healthline_listing_scraper.py**) extracts:

1. **Article Title**
2. **Article URL**

The scraper also supports pagination to ensure comprehensive data extraction. The extracted data is saved in a CSV file.

## Healthline Article Detail Scraper

The Healthline Article Detail Scraper (`healthline_article_scraper.py`) extracts detailed article information, including:

1. **Title**
2. **Byline**
3. **Content**

The extracted data is saved in a CSV file.

## Environment Setup

Ensure that Python is installed on your system. Check the version using:

```bash
# Use python3 if required (for Linux/macOS)
python --version
```

Next, install the required dependencies:

```bash
pip install crawlbase beautifulsoup4 pandas
```

- **Crawlbase** – Handles JavaScript rendering and bypasses bot protections.
- **BeautifulSoup** – Parses and extracts structured data from HTML.
- **Pandas** – Stores and processes extracted data efficiently.

## Running the Scrapers

### Get Your Crawlbase Access Token

1. Sign up for Crawlbase [here](https://crawlbase.com/signup) to get an API token.
2. Use the JS token for Healthline scraping, as Healthline uses JavaScript-rendered content.

### Update the Scraper with Your Token

Replace "`CRAWLBASE_JS_TOKEN`" in the script with your Crawlbase JS Token.

Run the Scraper

```bash
# For article listing scraping

python healthline_listing_scraper.py

# For article detail scraping

python healthline_article_scraper.py
```

The scraped data will be saved in `healthline_articles.csv` or `healthline_articles_details.csv`, depending on the script used.

## To-Do List

- Expand scrapers to extract additional article details such as **related topics and external links**.
- Optimize data storage and add support for **JSON and database integration**.
- Improve scraper efficiency by implementing **asynchronous requests**.
- Integrate **Crawlbase Smart Proxy** to enhance reliability and prevent blocks.
- Automate scheduled data extraction for **real-time content monitoring**.

## Why Use This Scraper?

- ✔ **Bypasses anti-bot protections** with Crawlbase.
- ✔ **Handles JavaScript-rendered content** seamlessly.
- ✔ **Extracts accurate and structured article data** efficiently.
