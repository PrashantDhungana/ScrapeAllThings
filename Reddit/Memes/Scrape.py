import requests
import random
import urllib.request
import uuid
import re
import os

header={'User-agent':'my bot 0.1'}
subreddits = ["funny","memes"]

# Select random subreddit from the list
CurrentSub = random.choice(subreddits)

#Fetch Reddit API
r = requests.get(f'https://api.reddit.com/r/{CurrentSub}',headers=header)

data=r.json()
newData=data['data']['children']

def main(newData):
	# Check if folder exists
	dirCheck = os.path.exists("images")
	# Create folder if doesn't exist
	if not dirCheck:
		os.mkdir("images")
	# Loop for every meme
	for x in newData:
		data = x['data']
		filename = str(uuid.uuid4())
		# Filter out invalid link and NSFW content
		if data['over_18'] or "url_overridden_by_dest" not in data:
			continue
		try:
			# Get URL for the meme
			memeURL = data['url_overridden_by_dest']
			regex = r"\.\w+$"
			# Get the image extension
			imgExt = re.search(regex,memeURL)
			imgExt = imgExt.group(0)
			#Save meme to a folder 
			urllib.request.urlretrieve(memeURL, f"./images/{filename}{imgExt}")
		except:
			continue

main(newData)


