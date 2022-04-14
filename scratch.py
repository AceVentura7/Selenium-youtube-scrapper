import requests
from bs4 import BeautifulSoup 

yt_trending_url = 'https://www.youtube.com/feed/trending'

#Does not execute javascript
response = requests.get(yt_trending_url)

print('Status Code', response.status_code)

with open('trending.html', 'w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text,'html.parser')
print('Page title:',doc.title.text)

# Find all the video divs
video_divs = doc.find_all('div', class_='ytd-video-renderer')

print(f'Found {len(video_divs)} videos')