#https://www.avito.ru/moskva/muzykalnye_instrumenty/gitary_i_drugie_strunnye?p=1&q=ibanez
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.avito.ru/moskva/muzykalnye_instrumenty/gitary_i_drugie_strunnye?s_trg=3&q=ibanez'

def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    
    return int(total_pages)

def write_csv(data):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f)
        
        writer.writerow((data['title'],
            data['url'],
            data['price'],
            data['metro']
            ))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
    for ad in ads:
        name = ad.find('div', class_='description').find('h3').text.strip().lower()
        
        if 'ibanez' in mane:
            try:
                title = ad.find('div', class_='description').find('h3').text.strip()
            except:
                title = ''
            try:
                url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
            except:
                url = ''
            try:
                price = ad.find('div', class_='about').text.strip()
            except:
                price = ''
            try:
                metro = ad.find('div', class_='data').find_all('p')[-1].text
            except:
                metro = ''

            data - {'title': title,
                'url': url,
                'price': price,
                'metro': metro
                }
            
            write_csv(data)
        else:
            continue

def main():
    avito_url = 'https://www.avito.ru/moskva/muzykalnye_instrumenty/gitary_i_drugie_strunnye?'
    page_count = 'p='
    query_p = '&q=ibanez'
    
    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages):
        url_gen = avito_url + page_count + str(i) + query_p
        print(url_gen)

    #pass
if __name__ == '__main__':
    main()