from bs4 import BeautifulSoup as bs
from requests import get


url = get("https://apify.com/covid-19")

soup = bs(url.text, 'html.parser')


noti = soup.find_all('span', class_="number")[4].next_element.next_element.text

obitos = soup.find_all('span', class_="number")[6].next_element.next_element.text

print(noti)
print(obitos)
