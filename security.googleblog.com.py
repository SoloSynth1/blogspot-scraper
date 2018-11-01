import requests
import json

start_url = "https://www.blogger.com/feeds/1176949257541686127/posts/default?alt=json&start-index={}&max-results=25"

if __name__ == "__main__":
    i = 0
    posts = []
    while True:
        url = start_url.format(i*25+1)
        print("fetching {}...".format(url))
        response = requests.get(url, timeout=20).json()
        if 'entry' in response['feed'].keys():
            posts += response['feed']['entry']
            i += 1
        else:
            break
    with open('entry.json', 'w') as f:
        f.write(json.dumps(posts))