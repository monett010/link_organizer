from selenium import webdriver

class Scraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def getTitle(self):
        self.driver.get(self.url)
        title = self.driver.title
        return title

    # def getDescription(self):
    #     description = self.driver.