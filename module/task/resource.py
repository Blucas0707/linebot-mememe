import requests
from bs4 import BeautifulSoup
import random
from module.task.trashtalk import trashtalk
from module.task.positivetalk import positivetalk

def findMemeImage(keyword= ""):
    googleImageUrl = "https://www.google.co.in/search?q=" +"Meme "+ keyword +"&source=lnms&tbm=isch"
    print(googleImageUrl)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
    req = requests.get(googleImageUrl, headers=headers)
    # print(req)
    req.encoding = "utf-8"
    soup = BeautifulSoup(req.text, "html.parser")
    # print(soup.prettify())
    images = soup.find_all("img")
    # showimages(images)
    firstimageUrl = images[1].get("src")
    
    if req.status_code == 200:
        return firstimageUrl
    else:
        return "http://memenow.cc/wp-content/uploads/2020/04/20200409_5e8ea59dc8fd9.jpg"
        
def findTrachTalk():
    totalNumber = len(trashtalk)
    id = random.randint(1,totalNumber)
    return id, trashtalk[id]

def findPositiveTalk():
    totalNumber = len(positivetalk)
    id = random.randint(1,totalNumber)
    return id, positivetalk[id]

def showimages(images):
    for image in images:
        print(image,"\n")

def showtalk():
    print(trashtalk)

showtalk()

# findMemeImage("問號")

if __name__ == "__main__":
    findMemeImage("問號")