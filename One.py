from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/search?q=fastrack%20watches%20men%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"IIdQZO _1R0K0g _1SSAGr"})
print(len(containers))

#price=containers.findAll("div",{"class":"_1uv9Cb"})
#print(price[0].text)

