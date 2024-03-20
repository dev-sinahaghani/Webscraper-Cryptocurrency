from helium import *
from bs4 import BeautifulSoup
class wb_helium:
    def __init__(self,url,tag,attr,attr_name):
        self.url = url
        self.tag = tag
        self.attr = attr
        self.attr_name= attr_name
        self.price = None
    def get_tether_price(self):
        browser = start_chrome(self.url,headless=True)
        soup = BeautifulSoup(browser.page_source, 'html.parser') 
        price = soup.find_all(self.tag,{self.attr:self.attr_name})
        self.price = price[0].text.strip()

# browser = start_chrome(url,headless=True)
# soup = BeautifulSoup(browser.page_source, 'html.parser') 
# price = soup.find_all('span',{'class':'fw-bold ml-8-multi text-white fs-36'})
# print(price[0].text.strip())