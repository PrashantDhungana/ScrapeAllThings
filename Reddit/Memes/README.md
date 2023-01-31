# RedditMemes
A python script that fetches memes from Reddit using free proxies.

### Requirements
- `requests`
- `os`
- `uuid`
- `re`
- `concurrent.futures`
- `bs4`

### Features
- Fetches free proxies from [Free Proxy List](https://free-proxy-list.net/)
- Prompts user to input subreddits separated by single space
- Makes a directory for each subreddit and saves the memes in the corresponding directory
- Uses free proxies to fetch memes from Reddit API
- Saves the memes with a unique filename

### How to run
- Clone the repository to your local machine
- Install the required packages using `pip install -r requirements.txt`
- Run the script using `python RedditMemes.py`
- Enter the list of subreddits separated by single space when prompted
- The memes will be saved in the `./images/` directory. Each subreddit will have its own directory inside `./images/`.
