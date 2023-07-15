from requests import session
from bs4 import BeautifulSoup as BS
import pandas
list1=[]
count=1
list2=[]



S=session()
S.headers['user-agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url="https://www.yellowpages.ca/search/si/1/Restaurants/Toronto+ON"
r=S.get(url)
soup=BS(r.text,'html.parser')
for i in soup.find_all('div','listing__content__wrap--flexed jsGoToMp'):
    name=i.find('a','listing__name--link listing__link jsListingName').text.strip()
    # rating=i.find('span','ypStars jsReviewsChart').get('title')
    # address=i.find('span','listing__address--full').text.strip()
    mobile_no=i.find('a','mlr__item__cta jsMlrMenu').get('data-phone').strip()
    direction=i.find('a','listing__direction').get('title').strip()
    item=dict()
    item['Index']=count
    item['Name']=name
    # item['Stars']=rating
    # item['Add']=address
    item['Number']=mobile_no
    item['direction']=direction
    list1.append(item)
    count+=1
print(list1)
df=pandas.DataFrame(list1)
df.to_excel("allcanadayellow.xlsx",index=False)

