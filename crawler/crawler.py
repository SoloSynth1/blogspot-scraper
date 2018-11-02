import requests
from crawler.utils import dump_json, extract_domain
import os

class BlogspotCrawler:
    def __init__(self, url=None):
        self.posts_window = 100
        self.meta_url = "https://www.blogger.com/feeds/{}/posts/default?alt=json&start-index={}&max-results={}"
        self.expected_posts = 0
        if url:
            self.blog_id = self.extract_id(url)
            self.output_path = os.path.join('.', 'data', extract_domain(url), 'posts.json')

    def set_blog_id(self, blog_id):
        self.blog_id = str(blog_id)

    def set_output_path(self, output_path):
        self.output_path = output_path

    def check(self):
        try:
            if self.blog_id:
                response = requests.get("https://www.blogger.com/feeds/{}/posts/default?alt=json".format(self.blog_id))
                self.expected_posts = int(response.json()['feed']['openSearch$totalResults']['$t'])
                print("JSON reponse received. blog returns total of {} posts.".format(self.expected_posts))
                return True
            return False
        except Exception as e:
            print(e)
            return False

    def crawl(self, timeout=30):
        if not self.blog_id or not self.output_path:
            print("Params missing.")
        elif not self.check():
            print("Check failed. Please check if the url points to a valid Blogspot website.")
        else:
            i = 0
            posts = []
            while True:
                try:
                    url = self.meta_url.format(self.blog_id, i * self.posts_window + 1, self.posts_window)
                    print("fetching {}...".format(url))
                    response = requests.get(url, timeout=30).json()
                    if 'entry' in response['feed'].keys():
                        posts += response['feed']['entry']
                        i += 1
                    else:
                        break
                except TimeoutError:
                    print("Timed out. Waiting {} seconds...".format(timeout))
                    time.sleep(timeout)
                    continue
            if self.validate(posts):
                dump_json(posts,self.output_path)
                print("JSON file dumped at {}".format(self.output_path))
            else:
                print("Failed to validate scraped result.")

    def validate(self, posts):
        if len(posts) == self.expected_posts:
            return True
        return False

    def extract_id(self, url):
        import re
        response = requests.get(url, timeout=30)
        pattern = "https://www.blogger.com/feeds/(\d+)/posts/default"
        ids = re.findall(pattern, response.text)
        if ids:
            print("ids found: {}".format(set(ids)))
            return ids[0]
        else:
            return None