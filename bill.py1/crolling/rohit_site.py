# from requests import session
# from bs4 import BeautifulSoup as BS
# import pandas
# s=session()
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Language': 'en-US,en;q=0.5',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Authorization': 'Basic cDFob3NwaXRhbGl0eTpzZWNyZXQ=',
#     'Connection': 'keep-alive',
#     # 'Cookie': 'XSRF-TOKEN=eyJpdiI6IlA3S3RNNTdINTdPMHFMMjB3NHMyQ1E9PSIsInZhbHVlIjoiUFlKNVlxbHpSU2JuNlk5aThBTGI3b0tobnpWL0NqVS95NjJ4SW5BODNMRndDRDdXZmRBTjA0cXRkamlwVThLTG5Pejh2eVhWQ2VPcWRZNzI0OVpyLzdYa2I4cnBFM3Y3OFJWR0xjcGI4b3dTRUlCVzZRQ1ZuVFgyZXpoWmJKc2MiLCJtYWMiOiI4MWVhNGExNzRmOTdhZWQ5Mjg2OWY1MjU2OTVjYTdjZmI3ZTRjYWUwOTZjM2I5MjllMzI2ZjAxZTgxNWRkOTFkIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IkkxSm4yWHFEYXNWdUZkWE5mU2JZQVE9PSIsInZhbHVlIjoiZ2NOUzE4ZEhibk4wNGtnY3F5cUV4TUtPR0JTZ2NTaDR2d3Nra1Qyd1ZvUlh0U1JBcGlPbUg5b1NjT05LbFFGNmdLbEFKRmd2bExWTFgxT3pib0ptOTd6MDlzQzR3VlpvQk1lTnd0ZVRIQWsyRGJoUmRjVzlMMXp3RTJteDB0a2MiLCJtYWMiOiIwOTI5MzIwNjRlMGExY2VkMjgwN2EzZWJkYzE5YTcwYzdlZTU4MTE4NDZmYjUxMmUyOTAyYWM2NjIwZmYwMGZmIiwidGFnIjoiIn0%3D',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'cross-site',
# }
# s.headers.update(headers)
# url = 'https://b2b.travelflow.com/p1-corporate-hospitality'
# r=s.get(url)
# soup = BS (r.text,'html.parser')
# list1 = []
# def producat_page(url):
#     r=s.get(url)
#     soup = BS (r.text,'html.parser')
#     club_name = []
#     club_year = []
#     club_match_date = []
#     organiger = []
#     organiger_data = []
#     organiger_venue = []
#     for i in soup.find_all('div','p-2 events-title-container'):
#         club_name_ = i.find('span').text.strip().split(",")[0]
#         club_name.append(club_name_)
#         club_year1 = i.find('span').text.split(",")[1]
#         club_year.append(club_year1)
#         club_match_date1 = i.find('span').text.strip().replace('        ','').replace('\n','').split(",")[2]
#         club_match_date.append(club_match_date1)
#         organiger1 = i.find('small').text.split("-")[0]
#         organiger.append(organiger1)
#         organiger_data1 = i.find('small').text.split("-")[1]
#         organiger_data.append(organiger_data1)
#         organiger_venue1 = i.find('small').text.split("-")[2]
#         organiger_venue.append(organiger_venue1)
        
#     title = []
#     for j in soup.find_all('td','pl-4'):
#         title1 = j.find('h5').text
#         title.append(title1)
    
#     prize = []
#     for i in soup.find_all('tr')[1:]:
#         tds = i.find_all('td')
#         if len(tds) == 1:
#             prize.append({"Price": ''})
#         else:
#             prize.append({"Price": tds[1].text.strip()})
    

#     prize_with_pool = []
#     for i in soup.find_all('tr')[1:]:
#         tds = i.find_all('td')
#         if len(tds) == 1:
#             prize_with_pool.append({"Price_with_pool": ''})
#         else:
#             prize_with_pool.append({"Price_with_pool": tds[2].text.strip()})

#     stock = []
#     for i in soup.find_all('tr')[1:]:
#         tds = i.find_all('td')
#         if len(tds) == 1:
#             stock.append({"stock": ''})
#         else:
#             stock.append({"stock": tds[3].text.strip()})
    
#     details = []
#     for i in soup.find_all('div','checkout-button'):
#         details_link = i.find('a').get('href')
#         details.append(details_link)

#     item = dict()

#     item ['Club_Name'] = club_name
#     item ['Club_Year'] = club_year
#     item ['Club_Match_Date'] = club_match_date
#     item ['Organiger'] = organiger
#     item ['Organiger_Date'] = organiger_data
#     item ['Organiger_Venue'] = organiger_venue
#     item ['Title'] = title
#     item ['Prize'] = prize
#     item ['Prize_With_Pool'] = prize_with_pool
#     item ['Stocks'] = stock
#     item ['Deatails_Link'] = details
#     list1.append(item)
#     print(list1)



# producat_page('https://b2b.travelflow.com/p1-corporate-hospitality')

# df = pandas.DataFrame(list1)
# df.to_excel('P_Travel.xlsx',index=False)



# a=int(input("enter the number"))
# b=a
# reversed = 0
# while(b>0):
#     remainder = b%10
#     b=b//10
#     reversed = reversed *  10 +remainder
# if (a==reversed):
#     print("yes")
# else:
#     print("no")


# a=int(input("enter the number"))
# b=a
# reversed = 0
# while(b>0):
#     remainder = b%10
#     b=b//10
#     reversed = reversed * 10 +remainder
# print(reversed)


# a=int(input("enter the value"))
# b=int(input('enter the value'))
# c=13
# while (a,b):
#     if a%c:




a=100
b=500
# i = a 
while (a<=b):
    # i=i+1
    if a%13==0 and a%3!=0:

        print(a)
    a=a+1
    



