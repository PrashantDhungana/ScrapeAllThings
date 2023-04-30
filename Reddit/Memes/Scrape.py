import requests
import os
import uuid
import re
from concurrent.futures import ThreadPoolExecutor

# Function to fetch free proxies from https://free-proxy-list.net/
def get_free_proxies():
    response = requests.get("https://free-proxy-list.net/")
    proxies = re.findall(r'\d+\.\d+\.\d+\.\d+:\d{2,5}', response.text)
    return proxies

# Class to scrape memes from Reddit using free proxies
class RedditMemes:
    def __init__(self):
        self.proxies_list = get_free_proxies()

    # Function to get list of subreddits from user input
    def get_subreddits(self):
        return input("Enter subreddits, separated by single space: ").split()

    # Function to make directory if not exists
    def make_directory(self, directory_path):
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    # Function to scrape memes from a subreddit
    def scrape_subreddit(self, subreddit):
        url = f'https://api.reddit.com/r/{subreddit}'
        resp = self._get_response(url)
        if not resp:
            return
        data = resp.json()
        directory_path = f'./images/{subreddit}'
        self.make_directory(directory_path)
        for post in data['data']['children']:
            try:
                post_data = post['data']
                if post_data['over_18'] or "url_overridden_by_dest" not in post_data:
                    print("NSFW content detected! Skipping...")
                    continue
                self.get_meme_image(directory_path, post_data['url_overridden_by_dest'])
            except Exception as e:
                pass

    # Function to fetch meme image and save it
    def get_meme_image(self, directory_path, meme_url):
        resp = self._get_response(meme_url)
        if not resp:
            return
        try:
            filename = str(uuid.uuid4())
            regex = r"\.\w+$"
            ext = re.search(regex, meme_url).group(0)
            with open(f"{directory_path}/{filename}{ext}", 'wb+') as f:
                f.write(resp.content)
        except Exception as e:
            pass

    # Function to get response from URL using free proxies
    def _get_response(self, url):
        for proxy in self.proxies_list:
            try:
                resp = requests.get(url, proxies= {'http': f'http://proxy'})
                if resp.status_code == 200:
                    return resp
            except:
                continue
        print(f'Error accessing URL: {url} with all proxies')
        return None

    def main(self):
        subreddits = self.get_subreddits()
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(self.scrape_subreddit, subreddits)
        print('finished.....')

if __name__ == "__main__":
    RedditMemes().main()