from requests import session
from bs4 import BeautifulSoup as BS
import pandas
list1=[]
list2=[]
count=1


S=session()
S.headers['user-agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0'
url="https://www.homethangs.com/vanities-384.html"
r=S.get(url)
soup=BS(r.text,'html.parser')
def crawl (url,page):
    r=S.get(url)
    soup=BS(r.text,'html.parser')
    product=soup.find_all('table','categoryitem')
    if product:
        for i in soup.find_all('table','categoryitem'):
            name=i.find('p','h1-link').text
            features=i.find('p','h1-link').text
            image=i.find('a').find('img').get('src')
            price=i.find('b').find('span').text.replace ('$','Sale: $')
            item=dict()
            item['index']=count
            item['Name']=name
            item['features']=features
            item['image']=image
            item['price']=price
            list1.append(item)
            print(list1)
        page+=1
        x="{}&page={}".format(url,page)
        crawl(x,page)
crawl(url,page=1)

    # count+=1
# print(list1)
# df = pandas.DataFrame(list1)
# df.to_excel('T_shirtflipkarddata.xlsx', index=False)