import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.flipkart.com/search?q=shoes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
suop = BeautifulSoup(page.content, 'html.parser')
iteams = suop.find_all(class_='IIdQZO _1R0K0g _1SSAGr')


shoename=[item.find(class_='_2B_pmu').get_text() for item in iteams]
amount=[item.find(class_='_1vC4OE').get_text() for item in iteams]
sizes =[item.find_all(class_='_3xcxim').get_text() for item in iteams]

shoelist = pd.DataFrame(
    {
        'shoename':shoename,
        'amount':amount,
        'dicont':sizes
    })

print(shoelist)
shoelist.to_csv('shoes.csv')



