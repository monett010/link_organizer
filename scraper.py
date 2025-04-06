from bs4 import BeautifulSoup
import requests

# def scrapePage ():
#     site = str("https://www.scrapethissite.com/pages/ajax-javascript/")
#     html_doc = requests.get(site, headers={'User-Agent': 'Custom user agent'})
#     with open ('sample.html', "w", encoding='utf-8') as file:
#         file.write (html_doc.text)

def scrapePage (address):
    site = str(address)
    html_doc = requests.get(site, headers={'User-Agent': 'Custom user agent'})
    with open ('sample_2.html', "w", encoding='utf-8') as file:
        file.write (html_doc.text)


def printTitle ():
    with open ('sample.html','r', encoding='utf-8') as file2:
        s = BeautifulSoup(file2, 'html.parser')
        print (s.title.contents[0])

def getText ():
    with open ('sample_2.html', "r", encoding='utf-8') as file2:
        s = BeautifulSoup (file2, 'html.parser')
        print (s.get_text())

# printTitle()
# scrapePage("https://www.rollingstone.com/music/music-features/bootsy-collins-james-brown-george-clinton-album-of-the-year-1235297617/")
getText()