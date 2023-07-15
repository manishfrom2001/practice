from requests import session
from bs4 import BeautifulSoup as BS
import pandas
s = session()
c=1
s.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"
url="https://www.homethangs.com/bathroom-320.html{}"
r=s.get(url)
soup=BS(r.text,'html.parser')
list1=[]



def crawl_all_category(url):
    r = s.get(url)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('div','category-list'):
        sub = 'https://www.homethangs.com/'+i.find('a').get('href')
        
        sub_category_(sub)

def sub_category_(url2):
    r = s.get(url2)
    soup = BS(r.text,'html.parser')
    product = soup.find_all('table','categoryitem')
    if product:
        listpage_all.append(url2)



    sub_category = soup.find_all('div','category-list')
    if sub_category:
        for i in sub_category:
            sub_main = 'https://www.homethangs.com/'+i.find('a').get('href')
            
            sub_category_(sub_main)

def listpage(url3,page):
    r = s.get("{}&page={}".format(url3,page))
    # print(r.url)

    soup = BS(r.text,'html.parser')
    product1 = soup.find_all('table','categoryitem')
    for j in product1:
        name = j.find('td','pother')
        if name:
            name = name.text

        else:
            name = 'not given'
        price = j.find('b').find('span')
        if price:
            price = price.text
        else:
            price = 'not given'
        details = j.find('p','h1-link').text
        image = j.find('a').find('img').get('src')
        if image:
            image = image.strip()
        else:
            image = 'not mention'
    
        item=dict()
        
        item['Name'] = name
        item['features'] = details
        item['image'] = image
        item['price'] = price
        
        list1.append(item)
        print(list1)
        
    page+=1
        
    if int(soup.find('div','hql-total-page').text.split(' 1 of ')[1])>=page:
        listpage(url3,page)

listpage_all = []           



crawl_all_category("https://www.homethangs.com/bathroom-320.html")

for ulr in listpage_all:
    listpage(ulr,page=1)
    # print(listpage)

df = pandas.DataFrame(list1)
df.to_excel('Home_thangs_bathroom_features.xlsx', index=False)





