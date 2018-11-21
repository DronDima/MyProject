import requests
import vk_api
import time
import csv
import re
import sql


def sendMessages(id, session, messages):
    for message in messages:
        session.method("messages.send", {"peer_id": id, "message": message})

def main():
    vk = vk_api.VkApi(token = "78ccb04e1d6f50682ffab06d51406acb407d580d7e693a9bf265367fa6540b4a2b613767a678569dd7d14")
    oldCount = 0
    id = 153050249
    while True:
        newCount = sql.countOfRows()
        if (oldCount < newCount):
            linksToPosts = sql.getLinksToPosts(oldCount, newCount)
            sendMessages(id, vk, linksToPosts)
        time.sleep(1)
        oldCount = newCount


if __name__ == '__main__':
    main()