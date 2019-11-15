import requests
from bs4 import BeautifulSoup
from csv import writer
import datetime

response = requests.get('https://www.espn.com/nba/player/_/id/4277905/trae-young')
soup = BeautifulSoup(response.text, 'html.parser')

headers = ['GP', 'MIN', 'FG%', '3P%', 'FT%', 'REB',	'AST', 'BLK', 'STL', 'PF', 'TO', 'PTS']

statsContainer = soup.find_all(class_='Table__ScrollerWrapper relative overflow-hidden')[1]
stats = statsContainer.find_all(class_='Table__TR Table__TR--sm Table__even')[0]
statsList = []

i = 0
for stat in stats:
	stat = stats.find_all(class_='Table__TD')[i].get_text()
	statsList.append(stat)
	i+=1

#j = 0
#for name in headers:
#	print(name, ': ', statsList[j])
#	j+=1

with open('stats.csv', 'a') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(statsList)

now = datetime.datetime.now()
curr = now.strftime("%Y-%m-%d %H:%M")
print("@", curr)

#print(headers)
#print(statsList)