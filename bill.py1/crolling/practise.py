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
jacket_link = []
list_link_1 = []

def main_category(url):
    r = s.get(url)
    # soup = BS(r.text,'html.parser')
    # a=str(input('enter:-'))
    # category_count = 0
    # for i in soup.find_all('div','mobile-nav__has-sublist')[0:7]:
    #     main_link = i.find('a').get('href').replace('https://www.rdklu.com','')
    #     if main_link:
    #         main_link = 'https://www.rdklu.com'+main_link
    #     else:
    #         main_link = 'not given'
    #     category_count += 1
        # print(main_link)
        # main_link_link.append(main_link)
    all_data = ['https://www.rdklu.com/collections/mens','https://www.rdklu.com/collections/womens','https://www.rdklu.com/collections/rdklu-smart-jackets','https://www.rdklu.com/collections/tie-and-dye','https://www.rdklu.com/collections/series','https://www.rdklu.com/collections/new-arrivals-2','https://www.rdklu.com/collections/the-sunshine-sale-2023']
    print(all_data)

    for i in (len(all_data)):
        list_page(all_data[i])
        # print(list_page)
    # list_page(a)

def list_page(url1):
    r = s.get(url1)
    # print('___++++++++==========_____',r.url)
    soup = BS(r.text,'html.parser')
    category_count = 0
    for i in soup.find_all('a','grid-product__link'):
        list_page_link ='https://www.rdklu.com/' +i.get('href')
        category_count += 1
        print(list_page_link)
        # print("Count__++++____+++___",category_count)
        # print("List_Page_Link:- ",list_page_link)
        # list_link_1.append(list_page_link)

    next = [_next for _next in soup.find_all('span','next')if "Next" in _next.text]
    if next:
        next_url = base_url.format(next[0].find('a').get('href'))
        # print(next_url)
        list_page(next_url)
main_category(url)
# for page in a:
    # list_page(page)