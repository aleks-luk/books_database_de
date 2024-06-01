import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import logging

def scrape_book_details(self, link):
    book_url = self.landing_page + link.get('href')
    logging.info(f"Scraping book details: {book_url}")
    try:
        r_book_url = requests.get(book_url)
        r_book_url.raise_for_status()
        web2 = bs(r_book_url.text, 'html.parser')

        title = web2.find('h1', class_='header-size my-3')
        author = web2.find('span', class_='il-font-size il-textcolor-light-secondary')

        # Dodaj logowanie pobranych danych
        logging.info(f"Title: {title.get_text(strip=True) if title else 'N/A'}")
        logging.info(f"Author: {author.get_text(strip=True) if author else 'N/A'}")

        table = {
            'Title': title.get_text(strip=True) if title else 'N/A',
            'Author': author.get_text(strip=True) if author else 'N/A'
        }

        tbody = web2.find('tbody')
        if tbody:
            trs = tbody.find_all('tr')
            for tr in trs:
                tds = tr.find_all('td')
                if len(tds) == 2:
                    name, attribute = tds
                    table[name.get_text(strip=True)] = attribute.get_text(strip=True)

        self.results.append(table)
        logging.info(f"Added book data: {table}")
    except requests.RequestException as e:
        logging.error(f"Error scraping book details: {e}")
