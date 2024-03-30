
"""
Web Scraper for Persian Crypto Currency Purpose
Start : Mar 18, 2024
Version : V0.1
"""
# 
# Import essential modules:
import requests
from bs4 import BeautifulSoup
from wb_beautifulsoup import wb_beautifulsoup  #import this library for prices that load by HTML
from wb_helium import wb_helium #import this library for prices that load by JavaScript
# Websites:
# {
#     1-https://bitbarg.com/coin/tether
#     2-https://tabdeal.org/buy-usdt
#     3-https://wallex.ir/markets/usdt
#     4-https://nobitex.ir/usdt/
# }

price_1 = wb_beautifulsoup('https://bitbarg.com/coin/tether','span',7)
price_1.get_tether_price()

price_2 = wb_beautifulsoup('https://tabdeal.org/buy-usdt','p',702)
price_2.get_tether_price()

price_3 = wb_beautifulsoup('https://wallex.ir/markets/usdt','span',42)
price_3.get_tether_price()

price_4 = wb_helium('https://nobitex.ir/usdt/','span','class','fw-bold ml-8-multi text-white fs-36')
price_4.get_tether_price()

print("The tether price on "+price_1.url+" is "+price_1.price+"")
print("The tether price on "+price_2.url+" is "+price_2.price.strip()[14:]+"")
print("The tether price on "+price_2.url+" is "+price_3.price+"")
print("The tether price on "+price_4.url+" is "+price_4.price+"")














