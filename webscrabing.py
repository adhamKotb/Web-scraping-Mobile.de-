import requests
from bs4 import BeautifulSoup
import os

html_text = requests.get('https://www.autoscout24.de/lst/bmw?atype=C&cy=D&damaged_listing=exclude&desc=0&fregfrom=2021&ocs_listing=include&powertype=kw&search_id=odkgon18a4&sort=standard&source=detailsearch&ustate=N%2CU').text
base_url = 'https://www.autoscout24.de'
soup = BeautifulSoup(html_text, 'lxml')
articles = soup.find_all('article')

directory = 'cars'

if not os.path.exists(directory):
    os.makedirs(directory)

filename = f'{directory}/cars_list.txt'

with open(filename, 'w') as file:
    for article in articles:
        car_name_element = article.find('h2')
        car_specs = article.find('span', class_='ListItem_subtitle__VEw08')
        price = article.find('p', class_='Price_price__APlgs PriceAndSeals_current_price__ykUpx')
        Provider = article.find('span', class_="SellerInfo_name__nR9JH")
        more_info = article.find('a', class_='ListItem_title__ndA4s ListItem_title_new_design__QIU2b Link_link__Ajn7I')
        
        car_name = car_name_element.text.strip() if car_name_element else "N/A"
        car_specifications = car_specs.text.strip() if car_specs else "N/A"
        car_price = price.text.strip() if price else "N/A"
        provider_name = Provider.text.strip() if Provider else "N/A"
        more_info_link = base_url + more_info.get('href') if more_info else "N/A"
        
        
        file.write(f"Car Name: {car_name}\n")
        file.write(f"Car Specs: {car_specifications}\n")
        file.write(f"Price: {car_price}\n")
        file.write(f"Provider: {provider_name}\n")
        file.write(f"More Info Link: {more_info_link}\n")
        file.write('\n')
            

