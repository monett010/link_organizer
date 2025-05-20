from selenium import webdriver
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, url):
        self.url = url
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self.url)

    def getTitle(self):
        # self.driver.get(self.url)
        return self.driver.title

    def getTitleSoup(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        return soup.title.get_text()
    
    def getDescription(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        return soup.find("meta", attrs={'name':'description'})['content']
