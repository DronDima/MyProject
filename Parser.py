import requests
import csv
import re
import time
import sql
from bs4 import BeautifulSoup


def getHtml(url):
    response = requests.get(url)
    return response.text

def getData(html, desiredWords):
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find('ul', class_ = 'content-list_posts').find_all('li', {'class' : 'content-list__item', 'id' : True})
    data = []
    for post in posts:
        title = post.find('a', class_ = 'post__title_link').text.strip()
        words = title.split()
        for desiredWord in desiredWords:
            if desiredWord in words:
                link = post.find('a', class_='post__title_link').get('href')
                data.append({'link': link,'title' : title})
                break
    return data


def main():
    url = "https://habr.com/all/"
    desiredWords = ["на", "и", "но", "в", "c", "На", "И", "Но", "В", "С", "о", "О"]
    while True:
        data = getData(getHtml(url), desiredWords)
        sql.writeData(data)
        time.sleep(300)







if __name__ == '__main__':
    main()