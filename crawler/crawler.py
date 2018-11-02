import requests
from crawler.utils import dump_json, extract_domain
import os

class BlogspotCrawler:
    def __init__(self, url=None):
        if url:
            self.blog_id = self.extract_id(url)
            self.output_path = os.path.join('.', 'data', extract_domain(url), 'posts.json')

    def set_blog_id(self, blog_id):
        self.blog_id = str(blog_id)

    def set_output_path(self, output_path):
        self.output_path = output_path

    def crawl(self):
        if self.blog_id and self.output_path:
            meta_url = "https://www.blogger.com/feeds/{}/posts/default?alt=json&start-index={}&max-results=25"
            i = 0
            posts = []
            while True:
                url = meta_url.format(self.blog_id, i * 25 + 1)
                print("fetching {}...".format(url))
                response = requests.get(url, timeout=30).json()
                if 'entry' in response['feed'].keys():
                    posts += response['feed']['entry']
                    i += 1
                else:
                    break
            dump_json(posts,self.output_path)
        else:
            print("Params (likely id) missing. Please check if the url points to a valid Blogspot website.")

    def extract_id(self, url):
        import re
        response = requests.get(url, timeout=30)
        pattern = "https://www.blogger.com/feeds/(\d+)/posts/default"
        ids = re.findall(pattern, response.text)
        if ids:
            return ids[0]
        else:
            return None