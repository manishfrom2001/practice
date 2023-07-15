from requests import session
from bs4 import BeautifulSoup as BS
import pandas
list1=[]
list2=[]
count=1


S=session()
S.headers['user-agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0 FKUA/website/42/website/Desktop'
url="https://www.flipkart.com/search?q=iphone+14+pro&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&as-pos=1&as-type=RECENT&suggestionId=iphone+14+pro%7CMobiles&requestId=b91e7a25-ec71-4b47-b6ac-aa5e489826b9&as-searchtext=i"
r=S.get(url)
soup=BS(r.text,'html.parser')
for i in soup.find_all('div','_2kHMtA'):
    Modal_no=i.find('div','_4rR01T').text
    Price=i.find('div','_30jeq3 _1_WHN1').text
    Bank_offer=i.find('div','col col-5-12 nlI3QM').text
    Specific=i.find('div','col col-7-12').text
    Image_link=i.find('img','_396cs4').get('src').strip()
    Rating=i.find('span','_1lRcqv').text
    Review=i.find('span','_2_R_DZ').text
    item=dict()
    item['Index'] = count
    item['Mobile'] = Modal_no
    item['Cost'] = Price
    item['Offer'] = Bank_offer
    item['Internal'] = Specific
    item['Image'] = Image_link
    item['Stars'] = Rating
    item['Review'] = Review
    list1.append(item)
    count += 1

print(list1)
df = pandas.DataFrame(list1)
df.to_excel('flipkardiphonedata.xlsx', index=False)