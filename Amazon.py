import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get('https://en.wikipedia.org/wiki/Allu_Arjun')
soup = BeautifulSoup(page.content, 'html.parser')
details = soup.find(class_='infobox biography vcard')

Birthplace =details.find(class_='birthplace').get_text()
Residence =details.find(class_="label").get_text()
Nationality =details.find(class_="category").get_text()

print(Birthplace)
print(Residence)
print(Nationality)

allu_arjun=pd.DataFrame(
    {
        'Birthplace':Birthplace,
        'Residence':Residence,
        'Nationality':Nationality
    }
)

print(allu_arjun)
allu_arjun.to_csv("allu_arjun.csv")