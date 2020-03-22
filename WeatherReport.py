import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=33.824460000000045&lon=-118.22867999999994#.Xdp5_egzbIU')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
#print(week)

#print(week.find_all('li'))
items= week.find_all(class_='tombstone-container')

#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp temp-high').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]

#print(period_names)
#print(short_desc)
#print(temp)

weather_stuff = pd.DataFrame(
    {
        'period':period_names,
        'short_desc':short_desc,
        'temp':temp
    })

print(weather_stuff)
weather_stuff.to_csv('Weather.csv')