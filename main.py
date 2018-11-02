import argparse
from crawler.crawler import BlogspotCrawler

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('url')
    args = ap.parse_args()
    bc = BlogspotCrawler(args.url)
    bc.crawl()