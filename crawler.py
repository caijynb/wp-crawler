import requests
import time
from img import Img


class demosite:
    def __init__(self):
        for articleurl in self.getArticleList():
            article=self.parserArticle(articleurl)
            self.saveToDB(article)

    def getArticleList(self):
        return []

    def parserArticle(self):
        return {}

    def saveToDB(self):
        pass
