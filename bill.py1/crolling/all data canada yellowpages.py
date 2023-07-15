# from requests import session
# from bs4 import BeautifulSoup as BS
# import pandas
# list1=[]
# list2=[]
# list3=[]
# count=1





# S=session()
# S.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"
# url="https://www.yellowpages.ca/"
# r=S.get(url)
# soup=BS(r.text,'html.parser')
# for i in soup.find_all('a','jsQuickLinks'):
#     b=i.get('href')
#     item=dict()
#     item['all link']="https://www.yellowpages.ca/"+b
#     list1.append(item)
# # print(list1)

# # S.headers.update(new_headers)
# for j in list1:
#     # print(j)
#     c=j.get('all link')
#     r=S.get(c)
#     soup=BS(r.text,'html.parser')
#     product=soup.find_all('div','listing__content__wrap--flexed jsGoToMp')
#     for num in product:
#         if num.find('a','listing__name--link listing__link jsListingName'):
#             tit=(num.find('a','listing__name--link listing__link jsListingName').text)
#         else:
#             tit=('')
#         if num.find('span','ypStars jsReviewsChart'):
#             rating=(num.find('span','ypStars jsReviewsChart').get('title').strip)
#         else:
#             rating=(' ')
#         if num.find('span','listing__address--full'):
#             address=(num.find('span','listing__address--full').text.strip())
#         else:
#             address = (" ")
#         if num.find('a','mlr__item__cta jsMlrMenu'):
#             mobile_no=(num.find('a','mlr__item__cta jsMlrMenu').get('data-phone').strip())
#         else:
#             mobile_no=(' ')
#         if num.find('a','listing__direction'):
#             direction=(num.find('a','listing__direction').get('title').strip())
#         else:
#             direction=(' ')
#         item=dict()
#         item['Index']=count
#         item['Name']=tit
#         item['Stars']=rating
#         item['Add']=address
#         item['Number']=mobile_no
#         item['direction']=direction
#         # print(item)
#         list2.append(item)
        
#         count+=1
# print(list2)
# df=pandas.DataFrame(list2)
# df.to_excel("canadayellow.xlsx",index=False)




from requests import session
from bs4 import BeautifulSoup as BS
import pandas
s=session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.yellowpages.ca/',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=8DF185334C2B70111214405E4462E8A0; _gcl_au=1.1.147664750.1683980855; _ga_PSJJXDDSM6=GS1.1.1688469669427.30.1.1688469693.0.0.0; _ga=GA1.2.1236700346.1683980855; __gads=ID=831bd3cc4db1e7a0:T=1683980856:RT=1688469673:S=ALNI_MZ6ycPRAPIWtbwAai1X8zWOu2qTVA; __gpi=UID=00000c05810c3ef2:T=1683980856:RT=1688469673:S=ALNI_Mbc910K8sXIIYemp57hs_ksLYUaJA; yp.engagement=%5B%7B%22id%22%3A%22156059%22%2C%22ts%22%3A1684149303462%7D%5D; JSESSIONID=8DF185334C2B70111214405E4462E8A0; yp.analytics=%7B%22id%22%3A%22dfe8a69f-2c29-4ad0-b889-3832ff98853a%22%2C%22iwa%22%3A%22Restaurants%22%2C%22iw%22%3A%22Toronto+ON%22%2C%22sc%22%3A12212%2C%22si%22%3A%22dfe8a69f-2c29-4ad0-b889-3832ff98853a_UmVzdGF1cmFudHM_VG9yb250byBPTg%22%7D; yp.ssa=%7B%22id%22%3A%221688469669427%22%7D; yp.prefs=%7B%22w%22%3A%22Toronto+ON%22%2C%22loc%22%3A%22Toronto+ON%22%2C%22locla%22%3A43.6485%2C%22loclo%22%3A-79.3853%2C%22po%22%3Atrue%2C%22rws%22%3A%5B%22Toronto+ON%22%5D%2C%22rwtsm%22%3A%7B%22DINE%22%3A%5B%22Restaurants%22%5D%7D%2C%22ts%22%3A1688469693941%7D; yp.ro=%7B%22h%22%3A1938225239%2C%22rr%22%3A816159611%2C%22ri%22%3A720990142%7D; yp.theme=dine; yp.survey=%7B%22page_type%22%3A%22page_type_merchant%22%2C%22traffic%22%3A%22traffic_internal%22%2C%22loggedin%22%3A%22loggedin_false%22%2C%22headings%22%3A%5B%22heading_02000022%22%2C%22heading_02000065%22%2C%22heading_01125710%22%2C%22heading_02000062%22%5D%7D; ga_cid=999.999595062326; _gid=GA1.2.2067283510.1688469672; yp.ss=%7B%22e%22%3Afalse%7D; yp.campaign=%7B%22serpCampaign%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1688469673020%7D%2C%22fiveResults%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1688469673020%7D%2C%22folSizeRedcue%22%3A%7B%22v%22%3A%22control%22%2C%22u%22%3A1688469673020%7D%2C%22folRulesMobile%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1688469673021%7D%2C%22noneGroupingEnd%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1688469673021%7D%2C%22thirdAdMobile%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1688469673021%7D%2C%22dealerMapToAdresses%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1688469690357%7D%7D',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}
s.headers.update(headers)
base_url = "https://www.yellowpages.ca{}"
url = 'https://www.yellowpages.ca/'
# r=s.get(url)
# soup = BS(r.text,'html.parser')
list2=[]
list1=[]
def main_category(url1):
    r=s.get(url1)
    soup = BS(r.text,'html.parser')


    for i in soup.find_all('a','jsQuickLinks'):
        main_category_link = 'https://www.yellowpages.ca'+i.get('href')
        # product_page(main_category_link)
        list_page(main_category_link)
        # print(main_category_link)

def list_page(url2):
    r=s.get(url2)
    print(r.url)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('a','listing__name--link listing__link jsListingName'):
        sub_category_link='https://www.yellowpages.ca'+i.get('href')
        if sub_category_link:
            sub_category_link = sub_category_link
        else:
            sub_category_link = 'not given'
        product_page(sub_category_link) 
    next_page = soup.find('div','view_more_section_noScroll')
    next_page = [_next for _next in soup.find_all("a","ypbtn btn-theme pageButton") if "Next" in _next.text.strip()]

    if next_page:
        next_url = base_url.format(next_page[0].get("href"))
        # list1.append(next_url)
        # print(next_url)
        list_page(next_url)
        # list1.append(sub_category_link)
        product_page(sub_category_link)

def product_page(url3):
    r=s.get(url3)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('div','merchant__header--root'):
        name = i.find('span','merchantNamejsShowCTA')
        if name:
            name = name.text
        else:
            name = 'not given'
        phone_no = i.find('span','mlr__sub-text')
        if phone_no:
            phone_no = phone_no.text
        else:
            phone_no = 'not given'

        address = i.find('div','merchant__item merchant__address merchant__address__mobile')
        if address:
            address = address.text.strip()
        else:
            address = 'not given'
        
        opning_timing = i.find('table','openHours-table')
        if opning_timing:
            opning_timing = opning_timing.text.strip().replace('\n\n\n\n','').replace('\n\n','')
        else:
            opning_timing = 'not given'
        rating = i.find('div','merchant__overall_rating')
        if rating:
            rating = rating.text
        else:
            rating = 'not given'

        image_link = i.find('li','media__item media__item--image media__item--nojs jsMediaNoJs')
        if image_link:
            image_link = image_link.find('a').get('href')
        else:
            image_link = 'not   given'
        
        web_site_link = i.find('li','mlr__item mlr__item--website')
        if web_site_link:
            web_site_link = 'https://www.yellowpages.ca'+web_site_link.find('a').get('href')
        else:
            web_site_link = 'not given'
        
        articale = i.find('article','merchant__item merchant__teaser')
        if articale:
            articale = articale.text.strip()
        else:
            articale = 'not given'
        deta = {"Name" : name,
                "Phone_No" : phone_no,
                "Address" : address,
                "Opning_Time" : opning_timing,
                "Rating" : rating,
                "Image_Link" : image_link,
                "Web_Site_Link" : web_site_link,
                "Article_details" : articale
        }
        list1.append(deta)
        print(r.url)




main_category(url)
# for url in list1:
    # list_page(url)
df = pandas.DataFrame(list1)
df.to_excel('all_data_of_canada.xlsx', index=False)

