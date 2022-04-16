from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


yt_trending_url = 'https://www.youtube.com/feed/trending'


def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_videos(driver):
  
  video_div_tag = 'ytd-video-renderer'
  driver.get(yt_trending_url)
  time.sleep(20)
  videos = driver.find_elements(By.TAG_NAME, video_div_tag)
  return videos


if __name__=="__main__":
  print('Creating Driver')
  driver = get_driver()
  
  print('Fetching trending videos')
  videos = get_videos(driver)
  
  print(f'Found {len(videos)} Videos')

  print("Parsing the First Video")
  #title, channel, views, uploaded, description, thumbnail_url, url

video = videos[0]
title_tag = video.find_element(By.ID,'video-title')
title = title_tag.text
url = title_tag.get_attribute('href')

thumbnail_tag = video.find_element(By.TAG_NAME,'img')
thumbnail_url = thumbnail_tag.get_attribute('src')

description_tag = video.find_element(By.ID, 'description-text')
desc = description_tag.text

channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
channel_name = channel_div.text

view_div = video.find_element(By. CLASS_NAME, 'ytd-video-meta-block')
views = view_div.text

print('Title:', title)
print('URL:', url)
print('Thumbnail URL:', thumbnail_url)
print('Channel Name:', channel_name)
print('Description:', desc)
print('Views:', views)