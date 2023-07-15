# from requests import session
# from bs4 import BeautifulSoup as BS
# import pandas
# s = session()
# c=1
# s.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"
# url = 'https://www.lenovo.com/in/en/d/deals?IPromoID=LEN598722&sort=sortBy&resultsLayoutType=grid'
# r=s.get(url)
# soup=BS(r.text,'html.parser')
# list2=[]
# list1=[]
# def main_link(url):
#     r=s.get(url)
#     soup = BS (r.text,'html.parser')
#     for i in soup.find_all('a','text-capitalize font-weight-bold product__card__learn-more v-btn v-btn--text theme--light v-size--default primary--text'):
#         lenovo_link = i.get('href')
#         list2.append(lenovo_link)

# def product_page(url1):
#     r=s.get(url1)
#     soup = BS (r.text,'html.parser')
#     # for i in soup.find_all('div',attrs={'id':'longscroll-subseries'}):
#     laptop_name = soup.find('h1','desktopHeader')
#     if laptop_name:
#         laptop_name = laptop_name.text
#     else:
#         laptop_name = 'not given'
#     laptop_image_link = soup.find('img','subSeries-Hero rollovercartItemImg')
#     if laptop_image_link:
#         laptop_image_link = 'https://www.lenovo.com' + laptop_image_link.get('src')
#     else:
#         laptop_image_link = 'not given'
#     laptop_about = soup.find('div','hero-productDescription mediaGallery-productDescription')
#     if laptop_about:
#         laptop_about = laptop_about.text.strip()
#     else:
#         laptop_about = 'not given'
#     laptop_price = soup.find('div','cta-group-price')
#     if laptop_price:
#         laptop_price = laptop_price.find('dd').text
#     else:
#         laptop_price = 'not given'
#     list3=[]
#     for i in soup.find_all('div',attrs={'id':'configurator-wrapper'}):
#         des = i.find('h4').text
#         des1 = i.find('p','configuratorItem-mtmTable-description').text.strip()
#         list3.append({des:des1})
#     item=dict()
#     item ['laptop_Nmae'] = laptop_name
#     item ['laptop_image_link'] = laptop_image_link
#     item ['laptop_about'] = laptop_about
#     item ['laptop_price'] = laptop_price
#     item ['features'] = list3
#     list1.append(item)
#     print(list1)

#         # print(details)
# main_link('https://www.lenovo.com/in/en/d/deals?IPromoID=LEN598722&sort=sortBy&resultsLayoutType=grid')
# for url in list2:
#     product_page(url)

# df = pandas.DataFrame(list1)
# df.to_excel('lenovo_laptop_data.xlsx', index=False)



# n=int(input('enter the value'))
# i=1
# while (i<=10):
#     table = '{}*{}={}'.format(n*i,n)
#     print(table)
#     i=i+1

# n = int(input('enter the number'))
# i=1
# while(i<=10):1111

#     table = '{}*{}={}'.format(n,i,n*i)
#     print(table)
#     i=i+1

# n=int(input('enter the value'))
# f=0
# i=2
# while i<=n/2:
#     if n%i==0:
#         f=1
#         break
#     i=i+1
# if f==0:
#     print('prime')
# else:
#     print('not prime')

# a=input("enter the value")
# b=0
# l=len(a)
# p=list(a)
# i=0
# while (i<l):
#     b=int(p[i])**3+b
#     # print(b)
#     i=i+1
# if int(a)==b:
#     print("yes")
# else:
#     print("no")


a=int(input("enter the value"))
b=0
l=len(a)
# p=list(a)
i=0
while (i<l):
    b=i**3
    print(b)
    i=i+1
# if int(a)==b:
#     print("yes")
# else:
#     print("no")




