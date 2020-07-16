from bs4 import BeautifulSoup
import requests

URL = 'https://realpython.com/'
response = requests.get(URL)
response_content = response.content

soup = BeautifulSoup(response_content, 'html.parser')

topics = soup.find_all('a', class_='badge badge-light text-muted')

topic_list = []

for topic in topics:
  topic_list.append(topic.get_text())

topic_list_no_duplicates = list(dict.fromkeys(topic_list))

url_topic_list = []

for item_topic in topic_list_no_duplicates:
  url_topic = f'{URL}tutorials/{item_topic}'
  url_topic_response = requests.get(url_topic)

  if url_topic_response.status_code == 200:
    url_topic_list.append(url_topic)
  #print(f'Process for {url_topic}')

img_list = []
print('\n')
for item_topic in url_topic_list:
  print(f'\nContent for: {item_topic}')
  item_url_response = requests.get(item_topic)
  item_url_response = item_url_response.content
  soup = BeautifulSoup(item_url_response, 'html.parser')
  container = soup.find_all('div', class_='col-12 col-md-6 mb-5')
  for content in container:
    print(f'{content.h2.get_text()}')
    print(f'{content.img["src"]}')





'''for item_topic in topic_list_no_duplicates:
  print(f'Content for: {URL}tutorials/{item_topic}')
  for url_topic_item in url_topic_list:
    url_topic_item_response = requests.get(url_topic_item)
    url_topic_item_response = url_topic_item_response.content
    soup = BeautifulSoup(url_topic_item_response, 'html.parser')
    images = soup.find_all('img', class_='card-img-top m-0 p-0 embed-responsive-item rounded')

    for img in images:
      img_list.append(img['src'])
      print(img['src'])
'''

