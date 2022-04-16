from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

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

def parse_video(video):
  title_tag = video.find_element(By.ID,'video-title')
  title = title_tag.text
  url = title_tag.get_attribute('href')
  
  thumbnail_tag = video.find_element(By.TAG_NAME,'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')
  
  description = video.find_element(By.ID, 'description-text').text
  
  channel_name = video.find_element(By.CLASS_NAME, 'ytd-channel-name').text
  
  view_div = video.find_element(By. CLASS_NAME, 'ytd-video-meta-block')
  views = view_div.text

  return{
    'title': title,
    'url': url,
    'thumbnail_url': thumbnail_url,
    'channel_name': channel_name,
    'description': description,
    'views': views
  }

if __name__=="__main__":
  print('Creating Driver')
  driver = get_driver()
  
  print('Fetching trending videos')
  videos = get_videos(driver)
  
  print(f'Found {len(videos)} Videos')

  print("Parsing Top 10 Video")
  videos_data = [parse_video(video) for video in videos[:10]]

  print('Save the data to a CSV')
  videos_df = pd.DataFrame(videos_data)
  print(videos_df)
  videos_df.to_csv('tending.csv', index=None)
  
  #title, channel, views, uploaded, description, thumbnail_url, url
