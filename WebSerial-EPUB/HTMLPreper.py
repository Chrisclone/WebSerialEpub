import requests as r
from bs4 import BeautifulSoup

class preper:

    def __init__(self, tUrl, pgCnt):
        self.urls = self.tableOContents(tUrl, pgCnt)

    def tableOContents(self, tUrl, pgCnt):
        urls = []

        tSite = r.get(tUrl).text
        tSoup = BeautifulSoup(tSite, features="lxml").find("div",{"id":"content"})
        rawLinks = tSoup.find_all("a")

        if pgCnt == 0 or pgCnt == "":
            pgCnt = len(rawLinks)


        for link in range(pgCnt):
            urls.append(rawLinks[link].get("href"))

        return urls

class pages:
    def __init__(self, site):
        self.html = r.get(site).text
        self.soup = BeautifulSoup(self.html)

    def title(self):
        return self.soup.find("h1",{"class":"entry-title"}).text

    def mainText(self):
        return "<html><body>" + f"<h1>{self.title()}</h1><br>" + str(self.soup.find("div",{"class":"entry-content"})) + "</body></html>"
