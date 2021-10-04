from crawler.crawler import BlogspotCrawler

if __name__ == "__main__":
    bc = BlogspotCrawler('https://security.googleblog.com')
    bc.crawl()