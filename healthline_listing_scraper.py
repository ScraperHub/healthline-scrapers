from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import pandas as pd

# Initialize Crawlbase Crawling API
crawling_api = CrawlingAPI({'token': 'YOUR_CRAWLBASE_TOKEN'})

options = {
    'ajax_wait': 'true',
    'page_wait': '5000'
}

def scrape_article_listings(url):
    response = crawling_api.get(url, options)
    if response['headers']['pc_status'] == '200':
        html_content = response['body'].decode('utf-8')
        soup = BeautifulSoup(html_content, 'html.parser')
        articles = []
        for item in soup.find_all('a', class_='article-link'):
            article_title = item.text.strip()
            article_url = "https://www.healthline.com" + item['href']
            articles.append({'title': article_title, 'url': article_url})
        return articles
    else:
        print(f"Failed to fetch the page: {response['headers']['pc_status']}")
        return []

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Example usage
url = "https://www.healthline.com/search?q1=migraine"
articles = scrape_article_listings(start_url)
save_to_csv(articles, 'healthline_articles.csv')