from requests import session

from bs4 import BeautifulSoup as BS

import pandas

s=session()

s.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0"

url = 'https://www.shiksha.com/'

r=s.get(url)

soup = BS(r.text,'html.parser')
list1=[]
list3=[]

def main_category(url):
    r=s.get(url)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('a',attrs = {'ea':'Top Ranked Colleges'}):
        main_link=i.get('href')
        if "http" not in main_link:
            main_link='https://www.shiksha.com'+main_link
            list_page(main_link)

def list_page(url2):
    r=s.get(url2)
    # print('______________+++++++++++++++++++++++++',r.url)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('a','rank_clg ripple dark'):
        sub_category='https://www.shiksha.com'+i.get('href')
        list1.append(sub_category)
    # for j in range(1,5):

    #     url2 = f"https://www.shiksha.com/mba/ranking/top-mba-colleges-in-india/2-2-0-0-0?pageNo={j}"
    #     list_page
    #     print(j)

def product_page(url3):
    r=s.get(url3)
    # print('____________',r.url)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('div','b876 three_col uilp reverse_two_col'):
        college_name = i.find('h1','e70a13')
        if college_name:
            college_name = college_name.text
        else:
            college_name = 'not given'

        image_link = i.find('div','c55b78')
        if image_link:
            image_link = image_link.find('img').get('src')
        else:
            image_link = 'not given'

        rating = i.find('span','f05f57 ece774 ece774')
        if rating:
            rating = rating.text
        else:
            rating= 'not given'

        rating_link = i.find('span','ce0fdc ece774 ece774')
        if rating_link:
            rating_link = 'https://www.shiksha.com'+rating_link.find('a').get('href')
        else:
            rating_link = 'not given'

        comment_link = i.find('span','_318533')
        if comment_link:
            comment_link = comment_link.find('a').get('href')
        else:
            comment_link = 'not given'

        lunch_date = i.find('ul','e1a898')
        if lunch_date:
            lunch_date = lunch_date.text.replace('Public/GovernmentUniversity','').replace('PrivateUniversity','').replace('A+NAAC accredited','').replace('ANAAC accredited','').replace('A++NAAC accredited','')
        else:
            lunch_date = 'not given'

    list2=[]
    for i in soup.find('ul','_4b29'):
        link = i.find('a')
        if link:
            link = 'https://www.shiksha.com'+link.get('href')
            list2.append(link)
    data = {
        "college_name" : college_name,
        "image_link" : image_link,
        "rating" : rating,
        "rating_link" : rating_link,
        "comment_link" : comment_link,
        "launch_date" : lunch_date,
        "link" : list2,

    }
    list3.append(data)

    # print(r.url)

            



main_category('https://www.shiksha.com/')

for url in list1:
    product_page(url)

df = pandas.DataFrame(list3)
df.to_excel('shiska_site.xlsx',index=False)