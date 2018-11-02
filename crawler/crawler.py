import requests
from crawler.utils import dump_json

class BlogspotCrawler:
    def __init__(self, blog_id=None, output_path=None):
        self.blog_id = str(blog_id)
        self.output_path = output_path

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
                response = requests.get(url, timeout=20).json()
                if 'entry' in response['feed'].keys():
                    posts += response['feed']['entry']
                    i += 1
                else:
                    break
            dump_json(posts,self.output_path)
        else:
            print("No blog id entered. Exiting...")