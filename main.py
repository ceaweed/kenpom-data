import csv

from bs4 import BeautifulSoup
import requests

filename = 'outputWeb.csv'

url = 'https://kenpom.com/index.php'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
html_text = requests.get(url, headers=header).text

soup = BeautifulSoup(html_text, 'lxml')
teams = soup.findAll('td', class_ = 'next_left')

with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for team in teams:
        csvwriter.writerow([team.text])

