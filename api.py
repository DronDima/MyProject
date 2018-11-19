import requests
import vk_api
import time
import csv
import re


def countOfStrings(path):
    with open(path, "r") as file:
        fileObject = csv.reader(file)
        result = sum(1 for row in fileObject)
    file.close()
    return result

def getLinksToPosts(path, oldCount, newCount):
    result = []
    with open(path, "r") as file:
        data = file.readlines()
        for i in range (oldCount, newCount):
            result.append(re.search("(?P<url>https?://[^\s]+)", data[i]).group("url"))
    return result

def sendMessages(id, session, messages):
    for message in messages:
        session.method("messages.send", {"peer_id": id, "message": message})

def main():
    vk = vk_api.VkApi(token = "78ccb04e1d6f50682ffab06d51406acb407d580d7e693a9bf265367fa6540b4a2b613767a678569dd7d14")
    oldCount = 0
    pathToFile = "posts.csv"
    id = 153050249
    while True:
        newCount = countOfStrings(pathToFile)
        if (oldCount < newCount):
            linksToPosts = getLinksToPosts(pathToFile, oldCount, newCount)
            sendMessages(id, vk, linksToPosts)
        time.sleep(1)
        oldCount = newCount


if __name__ == '__main__':
    main()