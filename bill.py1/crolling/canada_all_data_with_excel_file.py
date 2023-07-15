# from requests import session
# from bs4 import BeautifulSoup as BS
# import pandas

# s = session()
# s.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"


# def crawl_category(url):
#     r = s.get(url)
#     soup = BS(r.text,'html.parser')
#     for i in soup.find_all('div','category-list'):
#         sub = 'https://www.homethangs.com/'+i.find('a').get('href')
#         print(sub)
#         sub_category(sub)


# def sub_category(sub_url):
#     r = s.get(sub_url)
#     soup = BS(r.text,'html.parser')
#     for i in soup.find_all('div','category-title'):
#         urls = 'https://www.homethangs.com/'+i.find('a').get('href')
#         print('sub_category_urls------------------',urls)
#         third_sub_category(urls)
#         list_page(urls)
#         # except:
#             # list_page(urls)

# def third_sub_category(third):
#     r = s.get(third)
#     soup = BS(r.text,'html.parser')
#     for i in soup.find_all('div','category-list'):
#         third_urls = 'https://www.homethangs.com/'+i.find('a').get('href')
#         print('last--category----------------',third_urls)
#         list_page(third_urls)


# def list_page(man):
#     r = s.get(man) 
#     soup = BS(r.text,'html.parser')
#     product=soup.find_all('table','categoryitem')
#     for i in product:
#         name = i.find('td','pother').text.strip()
#         print(name)

# def 

# crawl_category("https://www.homethangs.com/bathroom-320.html")




from requests import session
from bs4 import BeautifulSoup as BS
import pandas
count=1

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.yellowpages.ca/',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=C0790620C7F07D990940FA0C664490F5; _gcl_au=1.1.147664750.1683980855; _ga_PSJJXDDSM6=GS1.1.1685711393895.24.1.1685712148.0.0.0; _ga=GA1.2.1236700346.1683980855; __gads=ID=831bd3cc4db1e7a0:T=1683980856:RT=1685711921:S=ALNI_MZ6ycPRAPIWtbwAai1X8zWOu2qTVA; __gpi=UID=00000c05810c3ef2:T=1683980856:RT=1685711921:S=ALNI_Mbc910K8sXIIYemp57hs_ksLYUaJA; yp.engagement=%5B%7B%22id%22%3A%22156059%22%2C%22ts%22%3A1684149303462%7D%5D; _gid=GA1.2.1157149431.1685620517; JSESSIONID=4F5C4A5A0B396A5504AB9BD7C80EBDDF; yp.prefs=%7B%22w%22%3A%22Toronto+ON%22%2C%22loc%22%3A%22Toronto+ON%22%2C%22locla%22%3A43.6485%2C%22loclo%22%3A-79.3853%2C%22po%22%3Atrue%2C%22rws%22%3A%5B%22Toronto+ON%22%5D%2C%22rwtsm%22%3A%7B%22DINE%22%3A%5B%22Restaurants%22%5D%7D%2C%22ts%22%3A1685711919389%7D; yp.ro=%7B%22h%22%3A1044781808%2C%22rr%22%3A578343948%2C%22ri%22%3A2139738918%7D; yp.theme=dine; yp.survey=%7B%22page_type%22%3A%22page_type_serp%22%2C%22traffic%22%3A%22traffic_direct%22%2C%22loggedin%22%3A%22loggedin_false%22%2C%22search_type%22%3A%22search_type_si%22%2C%22headings%22%3A%5B%22heading_01125710%22%5D%7D; yp.campaign=%7B%22serpCampaign%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1685711918776%7D%2C%22thirdAdMobile%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1685711918776%7D%2C%22fiveResults%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1685711918776%7D%2C%22folSizeRedcue%22%3A%7B%22v%22%3A%22control%22%2C%22u%22%3A1685711918776%7D%2C%22folRulesMobile%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1685711918776%7D%2C%22noneGroupingEnd%22%3A%7B%22v%22%3A%22test%22%2C%22u%22%3A1685711918776%7D%7D; yp.analytics=%7B%22id%22%3A%220147b691-8f60-40d8-baf6-297b72cbb12e%22%2C%22iwa%22%3A%22Restaurants%22%2C%22iw%22%3A%22Toronto+ON%22%2C%22sc%22%3A12230%2C%22si%22%3A%220147b691-8f60-40d8-baf6-297b72cbb12e_UmVzdGF1cmFudHM_VG9yb250byBPTg%22%7D; yp.ssa=%7B%22id%22%3A%221685711393895%22%7D; yp.ss=%7B%22e%22%3Afalse%7D; _dc_gtm_UA-126563938-4=1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}
s = session()
# s.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"
s.headers.update(headers)
base_url = "https://www.yellowpages.ca{}"




url="https://www.yellowpages.ca/{}"
r=s.get(url)
soup=BS(r.text,'html.parser')



list2=[]

list1=[]
def main_category(url):
    r=s.get(url)
    soup=BS(r.text,'html.parser')
    for i in soup.find_all('a','jsQuickLinks'):
        sub='https://www.yellowpages.ca/'+i.get('href')
        apple = sub
        list2.append(apple)
        # apple=(sub)
        # list_page(apple)
    
        
        # print(list2)
        # list_page(sub)
def list_page(url2):
    r=s.get(url2)
    print(r.url)

    # r=s.get(url2)
    
    soup=BS(r.text,'html.parser')
    for i in soup.find_all('div','listing__content__wrap--flexed jsGoToMp'):
        name = i.find('div','listing__title--wrap').text
        if i.find('span','listing__address--full'):
            address = (i.find('span','listing__address--full')).text
        else:
            address = ("")
        if  i.find('a','listing__logo--link sponsologolink').get('href'):
            image = ('https:/'+i.find('a','listing__logo--link sponsologolink').get('href').strip())
        if  i.find('a','mlr__item__cta jsMlrMenu'):
            mobile = (i.find('a','mlr__item__cta jsMlrMenu').get('data-phone').strip())
        else:
            mobile = ("")
        if  i.find('span','ypStars jsReviewsChart'):
            rating = (i.find('span','ypStars jsReviewsChart').get('title').strip())
        else:
            rating = ("")
        item = dict()
        # item ['Index'] = count
        item ['Name'] = name
        item ['Address'] = address
        item ['Image'] = image
        item ['Phone_no'] = mobile
        item ['Review'] = rating
        list1.append(item)
        # count+=1
        print(r.url)
    next_page = [_next for _next in soup.find_all("a","ypbtn btn-theme pageButton") if "Next" in str(_next)]


    # for _next in soup.find_all("a","ypbtn btn-theme pageButton"):
    #     if "Next" in str(_next):
    #         next_page = _next

    if next_page:
        next_url = base_url.format(next_page[0].get("href"))
        list_page(next_url)

    # if int(soup.find('div','view_more_section_noScroll').find('span').text.replace('\n\n\n',"").strip().split('1 /')[1])>=page:
    #     list_page(url2,page)
    
    

# list2=[]

main_category('https://www.yellowpages.ca/')
for url in list2:
    list_page(url)

df = pandas.DataFrame(list1)
df.to_excel('canada_yellowpage_all_data.xlsx',index=False)




