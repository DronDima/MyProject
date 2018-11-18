import requests
import csv
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
    return data

def write_csv(data):
    with open('posts.csv', 'a') as file:
        writer = csv.writer(file, delimiter = '#')
        for d in data:
            writer.writerow((d['title'], d['link']), )


def main():
    url = "https://habr.com/all/"
    desiredWords = ["Методы", "Rust"]
    data = getData(getHtml(url), desiredWords)
    write_csv(data)







if __name__ == '__main__':
    main()