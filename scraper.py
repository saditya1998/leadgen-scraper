import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = input("Enter URL to scrape leads: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

emails = set(re.findall(r'[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', soup.text))
phones = set(re.findall(r'\+?\d[\d\s()-]{7,}\d', soup.text))

data = {'Email': list(emails), 'Phone': list(phones)}

df = pd.DataFrame(data).drop_duplicates()
df.to_csv('leads.csv', index=False)
df.head()
