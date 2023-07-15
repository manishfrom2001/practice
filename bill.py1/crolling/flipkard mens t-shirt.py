from requests import session
from bs4 import BeautifulSoup as BS
import pandas
list1=[]
list2=[]
count=1


S=session()
S.headers['user-agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0 FKUA/website/42/website/Desktop'
url=("https://www.flipkart.com/clothing-and-accessories/topwear/tshirt/men-tshirt/pr?sid=clo,ash,ank,edy&otracker=categorytree&otracker=nmenu_sub_Men_0_T-Shirts")
r=S.get(url)
soup=BS(r.text,'html.parser')
for i in soup.find_all('div','_1xHGtK _373qXS'):
    image=i.find('img').get('src')
    name=i.find('div','_2WkVRV').text
    T=i.find('a','IRpwTa').text
    price=i.find('div','_30jeq3').text.strip()
    off=i.find('div','_3Ay6Sb').text
    item=dict()
    item['index']=count
    item['Name']=name
    item['T-shirt_name']=T
    item['Price']=price
    item['OFF']=off
    list1.append(item)
    count+=1
print(list1)
df = pandas.DataFrame(list1)
df.to_excel('T_shirtflipkarddata.xlsx', index=False)