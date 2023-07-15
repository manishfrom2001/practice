from requests import Session
from bs4 import BeautifulSoup as BS
import pandas

s = Session()
s.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0"
url = 'https://www.rdklu.com/'
base_url = 'https://www.rdklu.com{}'
r = s.get(url)
soup = BS(r.text,'html.parser')
main_link_link =[]
sub_catogery=[]
whole_data = []

def main_category(url):
    r = s.get(url)
    soup = BS(r.text,'html.parser')
    category_count = 0
    for i in soup.find_all('div','grid__item small--one-half medium-up--one-quarter'):
        main_link = 'https://www.rdklu.com/'+i.find('a').get('href')
        category_count += 1
        # print("Count___________________",category_count)
        # print("Main_Link:- ",main_link)
        main_link_link.append(main_link)

def list_page(url1):
    r = s.get(url1)
    print(r.url)
    soup = BS(r.text,'html.parser')
    category_count = 0
    for i in soup.find_all('a','grid-product__link'):
        list_page_link ='https://www.rdklu.com/' +i.get('href')
        category_count += 1
        # print("Count__++++____+++___",category_count)
        # print("List_Page_Link:- ",list_page_link)
        sub_catogery.append(list_page_link)

    next = [_next for _next in soup.find_all('span','next')if "Next" in _next.text]
    if next:
        next_url = base_url.format(next[0].find('a').get('href'))
        # print(next_url)
        list_page(next_url)

def product_page(url2):
    r = s.get(url2)
    soup = BS(r.text,'html.parser')
    category_count = 0
    name = soup.find('h1','h2 product-single__title')
    if name:
        name = name.text.strip()
    else:
        name = "nor given"

    price = soup.find('span','product__price on-sale')
    if price:
        price = price.text.strip()
    else:
        price = "not given"
    
    size = soup.find('div','variant-wrapper variant-wrapper--dropdown js')
    if size:
        size = size.text.strip().replace('\n        \n        ','').replace('\n  \n\n\n         ','')
    else:
        size = 'not given'

    product_discription = soup.find('div','rte')
    if product_discription:
        product_discription = product_discription.text.strip().replace('\n\n','').replace('\xa0','').replace('\n','')
    else:
        product_discription = "not given"
    image_all_link = []
    for i in soup.find_all('div','product__thumb-item'):
        all_image_link = 'https://www.rdklu.com/' + i.find('a').get('href')
        image_all_link.append(all_image_link)

    item = dict()
    item['Name'] = name
    item["Price"] = price
    item["All_Size"] = size
    item["Product_Discription"] = product_discription
    item["All_Image_Link"] = image_all_link
    category_count += 1
    print("Product_Page_Link:- ",category_count)
    whole_data.append(item)
    print("Product_Page_link::-  ",r.url)


    # print(size)
    


main_category(url)
for main in main_link_link:
    list_page(main)

for page in sub_catogery:
    product_page(page)

df = pandas.DataFrame(whole_data)
df.to_excel("All_Radklu.xlsx",index=False)