import requests
import random

from bs4 import BeautifulSoup

from module.task.trashtalk import trashtalk
from module.task.positivetalk import positivetalk


def findMemeImage(keyword=""):
    googleImageUrl = (
        "https://www.google.co.in/search?q="
        + "Meme "
        + keyword
        + "&source=lnms&tbm=isch"
    )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    }
    req = requests.get(googleImageUrl, headers=headers)
    req.encoding = "utf-8"
    soup = BeautifulSoup(req.text, "lxml")
    images = soup.find_all("img", {"class": "Q4LuWd"})

    firstimageUrl = getFirstImageUrl(images)

    if req.status_code == 200:
        return firstimageUrl
    else:
        return "http://memenow.cc/wp-content/uploads/2020/04/20200409_5e8ea59dc8fd9.jpg"


def findTrachTalk():
    totalNumber = len(trashtalk)
    id = random.randint(1, totalNumber)
    return id, trashtalk[id]


def findPositiveTalk():
    totalNumber = len(positivetalk)
    id = random.randint(1, totalNumber)
    return id, positivetalk[id]


def getFirstImageUrl(images):
    for image in images:
        if image.get("data-src") != None:
            return image.get("data-src")


if __name__ == "__main__":
    findMemeImage("問號")
