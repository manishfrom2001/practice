from requests import session
from bs4 import BeautifulSoup as BS
import pandas
list1=[]
list2=[]
count=1


S=session()
S.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"
url="https://www.homethangs.com/"
r=S.get(url)
soup=BS(r.text,'html.parser')
def crawl (url,page):
    r=S.get(url)
    soup=BS(r.text,'html.parser')
    for i in soup.find_all('a'):
        b=i.get("href")
        item=dict()
        item ['all link'] = "https://www.homethangs.com/"+b
        list1.append(item)

        # print(item)
    for j in list1:
        if j.get('all link'):
            # print("*****____________*******{}".format(j))
            c=j.get('all link')

            r=S.get(c)
            soup=BS(r.text,'html.parser')
            product=soup.find_all('table','categoryitem')
            if product:
                for num in product:
                        name=num.find('td','pother').text.strip()
                        if num.find('b').find('span'):
                            price=(num.find('b').find('span').text.strip())
                        details=num.find('p','h1-link').text
                        image=num.find('a').find('img').get('src')
                        # sale=num.find('div').find('img').get('src')
                        item=dict()
                        item['index']=count
                        item['Name']=name
                        item['features']=details
                        item['image']=image
                        item['price']=price
                        # item['sales']=sale
                        list1.append(item)
                        # count+=1
                        print(list1)
                page+=1
                x="{}&page={}".format(url,page)
                crawl(x,page)
crawl(url,page=1)


# df = pandas.DataFrame(list1)
# df.to_excel('all_homethangs_new.xlsx', index=False) 

# import math



# from requests import session
# from bs4 import BeautifulSoup as BS
# s=session()
# s.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"
# import pandas
# list1=[]

# def crawl_all_category (url):
#     r=s.get(url)
#     soup=BS(r.text,'html.parser')
#     for i in soup.find_all('div','category-list'):
#         sub='https://www.homethangs.com/'+i.find('a').get('href')
#         print('main_sub',sub)
#         sub_category1(sub)

# def sub_category1(url):
#     r=s.get(url)
#     soup=BS(r.text,'html.parser')
#     for i in soup.find_all('div','category-list'):      
#         sub_all = 'https://www.homethangs.com/'+i.find('a').get('href')
#         print('2nd_sub',sub_all)
#         sub_category2(sub_all)


# def sub_category2(url):
#     r=s.get(url)
#     soup=BS(r.text,'html.parser')
#     for i in soup.find_all('div','category-list'):
#         sub_category3='https://www.homethangs.com/'+i.find('a').get('href')
#         print('3rd_sub',sub_category3)
#         list_page(sub_category3)

# def list_page(sub_category3):
#     r=s.get(sub_category3)
#     soup=BS(r.text,'html.parser')
#     for i in soup.find_all('table','categoryitem'):
#         name=i.find('td','pother').text.strip()
#         # if i.find('b').find('span'):
#             # rate=(i.find('b').find('span').text.strip())
#         # else:
#             # rate = ''
#         # details=i.find('p','h1-link').text
#         # image=i.find('a').find('img').get('src')
#         item=dict()
#         item['title'] = name
#         # item['price'] = rate
#         # item['Details'] = details
#         # item['Image_link'] = image
#         list1.append(item)
#         print(list1)
#     # page+=1
#     # x="{}&page={}".format(,page)
#     # list_page(x,page=1)
# # list_page(sub_category3,page=1)


# crawl_all_category("https://www.homethangs.com/bathroom-320.html")




# from r÷
# def sub_category1(url):
#     r=s.get(url)
#     soup=BS(r.text,'html.parser')
#     for i in soup.find_all('div','category-list'):      
#         sub_all = 'https://www.homethangs.com/'+i.find('a').get('href')
#         print('2nd_sub',sub_all)
#         sub_category2(sub_all)


# def sub_category2(url):
#     r=s.get(url)
#     soup=BS(r.text,'html.parser')
#     for i in soup.find_all('div','category-list'):
#         sub_category3='https://www.homethangs.com/'+i.find('a').get('href')
#         print('3rd_sub',sub_category3)
#         list_page(sub_category3)


# def list_page(sub):
#     r=s.get(sub)
#     soup=BS(r.text,'html.parser')
#     for i in soup.find_all('table','categoryitem'):
#         name=i.find('td','pother').text.strip()
#         # if i.find('b').find('span'):
            # rate=(i.find('b').find('span').text.strip())
        # else:
            # rate = ''
        # details=i.find('p','h1-link').text
        # image=i.find('a').find('img').get('src')
        # item=dict()
        # item['title'] = name
        # item['price'] = rate
        # item['Details'] = details
        # item['Image_link'] = image
        # list1.append(item)
        # print(list1)
    # page+=1
    # x="{}&page={}".format(,page)
    # list_page(x,page=1)
# list_page(sub_category3,page=1)


# crawl_all_category(""https://www.homethangs.com/bathroom-320.html)














