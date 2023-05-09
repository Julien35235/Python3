import requests
from bs4 import BeautifulSoup

url = "https://www.flightradar24.com/data/flights/af123"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

flight_info = soup.find_all("div", {"class": "mb-1"})
for info in flight_info:
    m.save('flightradar24.html')
