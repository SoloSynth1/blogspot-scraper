from crawler.crawler import BlogspotCrawler
import os

if __name__ == "__main__":
    bc = BlogspotCrawler(2940307687099594687, os.path.join('.','data', 'marcoramilli.blogspot.com','posts.json'))
    bc.crawl()