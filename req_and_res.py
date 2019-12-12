import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.naver.com')
print(response.text)


