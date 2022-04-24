import requests

from bs4 import BeautifulSoup


HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
class Crawler:
    def __init__(self,web_url):
        self.web_url = web_url
        self.soup = ""

    def getWebcontent(self):
        req = requests.get(self.web_url, headers=HEADERS)
        req.encoding = "utf-8"
        soup = BeautifulSoup(req.text, "html.parser")
        self.soup = soup

    def dataHandle(self):
        newdict = dict()
        index = 282
        sentences = self.soup.find_all("p")
        for sentence in sentences:
            if "、" in sentence.text:
                newsentence = sentence.text.strip().split("、")[1].strip()
                newdict[index] = newsentence
                index += 1
                print(newsentence, "\n")
        print(newdict)

# webUrl = "https://mingyanjiaju.org/juzi/jingdianduanju/2012/0414/288.html"
# crawler = Crawler(webUrl)
# crawler.getWebcontent()
# crawler.dataHandle()
