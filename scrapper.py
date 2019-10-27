import requests
from bs4 import BeautifulSoup
from csv import writer

print('Trae Young: ')
response = requests.get('https://www.espn.com/nba/player/_/id/4277905/trae-young')
soup = BeautifulSoup(response.text, 'html.parser')

headers = {'GP', 'MIN', 'FG%', '3P%', 'FT%', 'REB',	'AST', 'BLK', 'STL', 'PF', 'TO', 'PTS'}

stats = soup.find_all(class_='Table__TR Table__TR--sm Table__even')[4]
statsList = []


i = 0;
for stat in stats:
	stat = stats.find_all(class_='Table__TD')[i].get_text()
	statsList.append(stat)
	i+=1

with open('stats.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(headers)
    csv_writer.writerow(statsList)

print(headers)
print(statsList)
#print(statsList)



