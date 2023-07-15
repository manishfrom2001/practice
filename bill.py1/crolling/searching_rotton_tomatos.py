from requests import session

from bs4 import BeautifulSoup as BS

import pandas

s=session()

s.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0"

url = 'https://www.rottentomatoes.com/m/hum-saathsaath-hain-we-stand-united'

r=s.get(url)

soup = BS(r.text,'html.parser')
list1=[]

def main_link(url):
    r=s.get(url)
    soup = BS(r.text,'html.parser')
    image = soup.find('div','movie-thumbnail-wrap').find('img').get('src')
    movie_name = soup.find('h1','title').text
    movie_info = soup.find('div','media-body').find('p').text.replace('\n                    ','')
    durection = soup.find('p','info').text
    review = soup.find('a','link').text.replace('\n            ','').strip()
    review_link = soup.find('a','link').get('href')
    review_link = 'https://www.rottentomatoes.com'+review_link
    total_rating = soup.find_all('a','link')[1].text.strip()
    total_rating_link = soup.find_all('a','link')[1].get('href')
    total_rating_link = 'https://www.rottentomatoes.com'+total_rating_link
    crew_link = soup.find('div','cast-and-crew-item').find('img').get('src')
    trending_link = soup.find('a','trending-bar__link').get('href')
    watch_fast_x = soup.find_all('a','trending-bar__link')[1].get('href')
    the_flash_review = soup.find_all('a','trending-bar__link')[2].get('href')
    june = soup.find_all('a','trending-bar__link')[3].get('href')
    list4=[]
    for i in soup.find_all('a'):
        most_popular_link = i.get('href')
        if most_popular_link and  most_popular_link.startswith('/m/'):
            most_popular_link = 'https://www.rottentomatoes.com' + most_popular_link
            # if most_popular_link not in list4:
            list4.append(most_popular_link)
    list3 = []
    for i in soup.find_all('li','info-item'):
        director_link = i.find('a')
        if director_link:
            director_link = 'https://www.rottentomatoes.com'+director_link.get('href')
            list3.append(director_link)
    item = dict()
    item ['Movie_Name'] = movie_name
    item ['Movie_Info'] = movie_info
    item ['Image'] = image
    item ['Movie_Durection'] = durection
    item ['Review'] = review
    item ['Review_Link'] = review_link
    item ['Total_Rating'] = total_rating
    item ['Total_Rating_Link'] = total_rating_link
    item ['Director_Link'] = list3
    item ['Crew_Link'] = crew_link
    item ['Trending_Link'] = trending_link
    item ['Watch_Fast_X'] = watch_fast_x
    item ['The_flash_Review'] = the_flash_review
    item ['June'] = june
    item ['Most_Popular_Link'] = most_popular_link
    list1.append(item)
    print(list1)
main_link('https://www.rottentomatoes.com/m/hum-saathsaath-hain-we-stand-united')

df = pandas.DataFrame(list1)
df.to_excel('searching_tomatos.xlsx')   