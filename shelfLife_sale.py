import bs4
from urllib.request import urlopen as Ureq
from bs4 import BeautifulSoup as soup

#target web page
my_url = "https://www.shelflife.co.za/Online-store/sneakers"

#opening connection and grabbing page

uClient = Ureq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.find_all("div", {"class": "col-xs-6 col-sm-3"})
title = page_soup.find_all("div", {"class": "title"})
price = page_soup.findAll("div", {"class" : "price"})
#finds sale product
sale_products = page_soup.findAll('div', {"class" : "special_label sale"} )

#open a new csv file to write data scraped from  website
filename = "shelf_life_sneaks_sale.csv"
f = open(filename, "w")
headers = "product_name,price\n"
f.write(headers)

#writing the data to the csv file
for i in range (0, len(containers)):
    if containers[i].a.div.div.text == 'ON SALE':
        print (title[i].text)
        print (price[i].text)
        f.write(title[i].text + "," + (price[i].text).replace(",", "") + "\n")
f.close()