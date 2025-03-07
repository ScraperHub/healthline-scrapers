from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup:
import pandas as pd

# Initialize Crawlbase Crawling API
crawling_api = CrawlingAPI({'token': 'YOUR_CRAWLBASE_TOKEN'})

def scrape_article_page(url):
    response = crawling_api.get(url)
    if response['headers']['pc_status'] == '200':
        html_content = response['body'].decode('utf-8')
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extracting details
        title = soup.find('h1', class_='article-title').text.strip()
        byline = soup.find('time').get('datetime', '').strip()
        content = ' '.join([p.text.strip() for p in soup.find_all('p')])

        return {
            'url': url,
            'title': title,
            'byline': byline,
            'content': content
        }
    else:
        print(f"Failed to fetch the page: {response['headers']['pc_status']}")
        return None

def save_article_data_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Example usage
article_urls = [
    "https://www.healthline.com/health-news/antacids-increase-migraine-risk",
    "https://www.healthline.com/health/migraine/what-to-ask-doctor-migraine"
]

articles_data = [scrape_article_page(url) for url in article_urls if scrape_article_page(url)]
save_article_data_to_csv(articles_data, 'healthline_articles_details.csv')