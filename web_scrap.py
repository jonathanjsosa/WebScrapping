from bs4 import BeautifulSoup
import requests

from tutorial import Tutorial

URL = "https://realpython.com/"
response = requests.get(URL)
response_content = response.content
soup = BeautifulSoup(response_content, features="html.parser")
topics = soup.find_all("a", class_="badge badge-light text-muted")
topics_list = []
for anchor in topics:
    topics_list.append(anchor.text)
topics_list = list(dict.fromkeys(topics_list))
responses_html_topics = []
for item in topics_list:
    topic_url = f"{URL}tutorials/{item}/"
    response_topic = requests.get(topic_url)
    if response_topic.status_code == 200:
        responses_html_topics.append(response_topic.content)
# ------------
# print the title of each sitio
tutorials_list = []
for site in responses_html_topics:
    site_soup = BeautifulSoup(site, features="html.parser")
    tutorials = site_soup.find_all('div', class_='col-12 col-md-6 mb-5')
    for t in tutorials:
        tutorial_title = t.find('h2', class_='card-title')
        tutorial_image = t.find('img', class_='card-img-top')
        tutorial_topics = t.find_all('a', class_='badge')
        t_topics = []
        for topic in tutorial_topics:
            t_topics.append(topic)
        tutorial_obj = Tutorial(tutorial_title.text, tutorial_image['src'], t_topics)
        tutorials_list.append(tutorial_obj)