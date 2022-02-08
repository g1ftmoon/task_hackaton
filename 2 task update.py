import requests
from bs4 import BeautifulSoup as BS
import csv
URl = 'https://www.mashina.kg/search/all/'
def get_html(url):
    response = requests.get(url)
    return response.text
    
def get_data(html):
    soup = BS(html, 'lxml')
    cars = soup.find_all('div', class_="list-item list-label")
    for car in cars:
        try:
            title = car.find('h2', class_="name").text.strip() 
        except:
            title = ''
        try:
            img = car.find('img', class_='lazy-image').get('data-src')
        except:
            img = ''
        try:
            price = car.find('p', class_="price").find('strong').text 
        except:
            price = ''
        try:
            obje = car.find('p', class_="year-miles").text.strip() 
        except:
            obje = ''
        try:
            obj = car.find('p', class_="body-type").text.strip()
        except:
            obj = ''
        try:
            pro = car.find('p', class_="volume").text.strip() 
        except:
            pro = ''
           
        data = {
            'title' : title,
            'img' : img,
            'price': price,
            'obje' : obje,
            'obj' : obj,
            'pro' : pro
        }
        write_csv(data)
def write_csv(data):
    with open ('car.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='\n')
        writer.writerow(
            (
                data['title'],
                data['img'],
                data['price'],
                data['obje'],
                data['obj'],
                data['pro']
            )
        )
def main():
    for page in range(33):
        print(f'парсинг {page} страницы...')
        url = 'https://www.mashina.kg/search/all/?page=2{page}'
        html = get_html(url)
        get_data(html)
main()