from requests import session
from bs4 import BeautifulSoup as BS
import pandas
s = session()
c=1
s.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"
url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/'
r=s.get(url)
soup = BS(r.text,'html.parser')
list1=[]
list2=[]
# list3=[]

def movie_main_link(url):
    r=s.get(url)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('a'):
        movie_link = i.get('href')
        if movie_link and  movie_link.startswith('/m/'):
            movie_link = 'https://www.rottentomatoes.com' + movie_link
            list2.append(movie_link)
            # print(movie_link)

def product_page(url1):
    r=s.get(url1)
    # print(r.url)
    soup = BS (r.text,'html.parser')
    image = soup.find('div','movie-thumbnail-wrap').find('img').get('src')
    # print(image)
    # for i in soup.find_all('img'):
    #     image_link = i.get('src')
    #     if image_link and image_link.startswith('https://resizing'):
    #         if image_link not in list1:
    #             list1.append(image_link)
    movie_info = soup.find('div','media-body').find('p').text.replace('\n                    ','')
    movie_name = soup.find('h1','title').text
    durection = soup.find('p','info').text
    review = soup.find('a','link').text.replace('\n            ','').strip()
    review_link = soup.find('a','link').get('href')
    review_link = 'https://www.rottentomatoes.com'+review_link
    total_rating = soup.find_all('a','link')[1].text.strip()
    total_rating_link = soup.find_all('a','link')[1].get('href')
    total_rating_link = 'https://www.rottentomatoes.com'+total_rating_link
    # director_link = soup.find_all('span','info-item-value')
    # if director_link:
    #     director_link = 'https://www.rottentomatoes.com'+director_link[4].find('a').get('href')
    # else:
    #     director_link = 'not given'
    #     print(director_link)
    list3 = []
    for i in soup.find_all('li','info-item'):
        director_link = i.find('a')
        if director_link:
            director_link = 'https://www.rottentomatoes.com'+director_link.get('href')
            list3.append(director_link)
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
    print(r.url)

movie_main_link('https://www.rottentomatoes.com/browse/movies_in_theaters/')
for url in list2:
    product_page(url)

df = pandas.DataFrame(list1)
df.to_excel('rotten_tomatoes.xlsx', index=False)