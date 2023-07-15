from requests import session
from bs4 import BeautifulSoup as BS
import pandas


S=session()
S.headers['user-agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url="http://yellowpages.in/hyderabad/apparels-and-accessories/110497301"
r=S.get(url)
soup=BS(r.text,'html.parser')
list1=[]
count = 1
for i in soup.find_all('div','eachPopular'):
    Name=i.find('a','eachPopularTitle').text
    Shop=i.find('div','openNow').text
    Contact=i.find('a','businessContact').text
    Address=i.find('address','businessArea').text
    Rating=i.find('div','eachPopularRatingBlock').text
    item=dict()
    item['Index'] = count
    item['Title'] = Name
    item['Timing'] = Shop
    item['Phone no'] = Contact
    item['Area'] = Address
    item['Rating'] = Rating
    list1.append(item)
    count += 1
print(list1)

df = pandas.DataFrame(list1)
df.to_excel('yellow.xlsx', index=False)
