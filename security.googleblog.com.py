from crawler.crawler import BlogspotCrawler
import os

if __name__ == "__main__":
    bc = BlogspotCrawler(1176949257541686127, os.path.join('.','data', 'security.googleblog.com','posts.json'))
    bc.crawl()