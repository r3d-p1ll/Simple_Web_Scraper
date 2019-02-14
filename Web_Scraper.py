from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

url_1 = "https://takecareof.com/products"
uClient = uReq(url_1)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"products-type"},{"id":"vitamins"})
filename = "products.csv"
f = open(filename, "w")
headers = "product_name, price \n"
f.write(headers)
contain = containers[0]
title_container = contain.findAll("div", {"class": "products-type__product-panel-title"})
price_container = contain.findAll("div", {"class": "products-type__product-panel-price"})
for _ in range (len(contain)-1):
	product_name = title_container[_].text
	# product_price = price_container[_].findAll(text = re.compile("^\$+[0-9]$"))
	product_price = price_container[_].findAll(text = re.compile("^\$+\d"))
	f.write(product_name + "," + product_price[0] + "\n")
f.close()