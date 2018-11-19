import requests
import csv
import re
import time
from api import countOfStrings
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

def isPostInPosts(link):
    pattern = re.compile('.*' + link + '.*')
    with open('posts.csv', 'r') as file:
        data = file.readlines()
        for d in data:
            if (pattern.match(d)):
                return (True)
    file.close()
    return (False)


def write_csv(data):
    for d in data:
        if (isPostInPosts(d["link"]) == False):
            with open('posts.csv', 'a') as file:
                writer = csv.writer(file, delimiter='#')
                writer.writerow((d['title'], d['link']))
            file.close()


def main():
    url = "https://habr.com/all/"
    desiredWords = ["Методы", "Rust", "Windows", "на", "и", "но", "в", "c", "На", "И", "Но", "В", "С", "о", "О"]
    path = "posts.csv"
    while True:
        data = getData(getHtml(url), desiredWords)
        write_csv(data)
        clearFile(path)
        time.sleep(300)







if __name__ == '__main__':
    main()