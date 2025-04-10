import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def scrape_leads(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    emails = set(re.findall(r'[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', soup.text))
    phones = set(re.findall(r'\+?\d[\d\s()-]{7,}\d', soup.text))

    data = {'Email': list(emails), 'Phone': list(phones)}

    df = pd.DataFrame(data).drop_duplicates()
    df.to_csv('data/leads.csv', index=False)
    print(df.head())

if __name__ == '__main__':
    url = input("Enter the website URL to scrape leads from: ")
    scrape_leads(url)
