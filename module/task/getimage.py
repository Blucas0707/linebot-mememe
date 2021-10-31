import requests
from bs4 import BeautifulSoup

def findMemeImage(keyword= ""):
    googleImageUrl = "https://www.google.co.in/search?q=" +"Meme "+ keyword +"&source=lnms&tbm=isch"
    print(googleImageUrl)
    req = requests.get(googleImageUrl)
    print(req)
    req.encoding = "utf-8"
    soup = BeautifulSoup(req.text, "html.parser")

    images = soup.find_all("img")
    firstimageUrl = images[1].get("src")
    
    if req.status_code == 200:
        return firstimageUrl
    else:
        return "http://memenow.cc/wp-content/uploads/2020/04/20200409_5e8ea59dc8fd9.jpg"

# findMemeImage("Meme")