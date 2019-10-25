import requests
from bs4 import BeautifulSoup
from csv import writer

print('Trae Young: ')
response = requests.get('https://www.espn.com/nba/player/_/id/4277905/trae-young')

soup = BeautifulSoup(response.text, 'html.parser')

statName = soup.find_all(class_='Table__TR Table__even')[2]
stats = soup.find_all(class_='Table__TR Table__TR--sm Table__even')[3]
statsList = []
headers = []


i = 0;
for name in statName:
	name = statName.find_all(class_='Table__TH')[i].get_text()
	headers.append(name)

	for stat in stats:
		stat = stats.find_all(class_='Table__TD')[i].get_text()
		statsList.append(float(stat))
		print(name, ":", stat)
		break;
	i+=1

with open('stats.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(headers)
    csv_writer.writerow(statsList)

print(headers)
print(statsList)



