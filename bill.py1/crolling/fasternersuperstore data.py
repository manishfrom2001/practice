from requests import session
from bs4 import BeautifulSoup as BS
import pandas
list1=[]
list2=[]
list3=[]

count=1


S=session()
S.headers['user-agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0'
url="https://www.fastenersuperstore.com/"
r=S.get(url)
soup=BS(r.text,'html.parser')
for i in soup.find_all('a'):
    b= i.get('href')
    if b not in list3:
        list3.append(b)

        if b and b.startswith('/category'):
            item=dict()
            item['all_link']='https://www.fastenersuperstore.com'+b
            list1.append(item)
for j in list1:
    c=j.get('all_link')
    r=S.get(c)
    soup=BS(r.text,'html.parser')
    product=soup.find_all('li')
    for num in product:
        if num.find('h2'):
            name=(num.find('h2').text)
        if num.find('span'):
            img=(num.find('img').get('src'))
        if num.find('p'):
            features=(num.find('p').text)
            item=dict()
            item['index']=count
            item['Name']=name
            item['image']=img
            item['features']=features
            list2.append(item)
            count+=1
            print(list2)
df=pandas.DataFrame(list2)
df.to_excel("fasternersuperstore.xlsx",index=False)

            


