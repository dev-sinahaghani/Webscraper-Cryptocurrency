import requests
from bs4 import BeautifulSoup
class wb_beautifulsoup:
# initialize objects of a class
    def __init__(self,url,tag,index):
        self.url = url
        self.tag = tag
        self.index = index
        self.price = None
# Function for extract data from websites:
    def get_tether_price(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        tether= soup.find_all(self.tag)[self.index]
        self.price =tether.text

    