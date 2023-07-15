# from requests import session
# from bs4 import BeautifulSoup as BS
# import pandas
# s = session()
# c=1
# s.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"
# url="https://www.imdb.com/title/tt10366206/?ref_=nv_sr_srsg_0_tt_5_nm_3_q_john%2520w"
# r=s.get(url)
# soup=BS(r.text,'html.parser')
# count=1

# list1=[]
# list2=[]

# def list_page(url):
#     r=s.get(url)
#     soup = BS (r.text,'html.parser')
#     movie_name = soup.find('span','sc-afe43def-1 fDTGTb').text
#     relesing_year = soup.find('ul','ipc-inline-list ipc-inline-list--show-dividers sc-afe43def-4 kdXikI baseAlt').text.strip().replace('A','')
#     rate_point = soup.find('div','sc-acdbf0f3-3 kpRihV').text[0:6]
#     all_rating = soup.find('div','sc-acdbf0f3-3 kpRihV').text[6:10]
#     Popularity = soup.find('div','sc-5f7fb5b4-0 cUcPIU').text
#     image = soup.find('a','ipc-lockup-overlay ipc-focusable').get('href')
#     image_icon = 'https://www.imdb.com'+image
#     video = soup.find('div','sc-385ac629-9 jiVoNU').find('a').get('href')
#     video_link = 'https://www.imdb.com'+video
#     photos = soup.find_all('a','ipc-btn ipc-btn--single-padding ipc-btn--center-align-content ipc-btn--default-height ipc-btn--core-baseAlt ipc-btn--theme-baseAlt ipc-btn--on-onBase ipc-secondary-button sc-ceb22a5b-3 lltPEH')[1].get('href')
#     photos_link = 'https://www.imdb.com' + photos
#     action = soup.find('a','ipc-chip ipc-chip--on-baseAlt').get('href')
#     action_link = 'https://www.imdb.com' + action
#     crime = soup.find_all('a','ipc-chip ipc-chip--on-baseAlt')[1].get('href')
#     crime_link = 'https://www.imdb.com' + crime
#     thriller = soup.find_all('a','ipc-chip ipc-chip--on-baseAlt')[2].get('href')
#     thriller_link = 'https://www.imdb.com' + thriller
#     director =  soup.find('a','ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').text
#     star = soup.find('a','ipc-metadata-list-item__label ipc-metadata-list-item__label--link').get('href')
#     star_link = 'https://www.imdb.com' + star
#     user_rating = soup.find('ul','ipc-inline-list sc-f1de8f0-0 cRtTs baseAlt').find('span').text
#     user_rating_l = soup.find('a','ipc-link ipc-link--baseAlt ipc-link--touch-target sc-f1de8f0-2 kvOHIk isReview').get('href')
#     user_rating_link = 'https://www.imdb.com' + user_rating_l
#     critic_reviews = soup.find_all('a','ipc-link ipc-link--baseAlt ipc-link--touch-target sc-f1de8f0-2 kvOHIk isReview')[1].text
#     critic_reviews_l = soup.find_all('a','ipc-link ipc-link--baseAlt ipc-link--touch-target sc-f1de8f0-2 kvOHIk isReview')[1].get('href')
#     critic_reviews_link = 'https://www.imdb.com' + critic_reviews_l
#     metascore = soup.find_all('a','ipc-link ipc-link--baseAlt ipc-link--touch-target sc-f1de8f0-2 kvOHIk isReview')[2].text
#     metascore_l = soup.find_all('a','ipc-link ipc-link--baseAlt ipc-link--touch-target sc-f1de8f0-2 kvOHIk isReview')[2].get('href')
#     metascore_link = 'https://www.imdb.com' + metascore_l
#     award = soup.find('a','ipc-metadata-list-item__icon-link').get('href')
#     award_link = 'https://www.imdb.com' + award
#     for i in soup.find_all('div','sc-bfec09a1-5 kUzsHJ'):
#         top_cast_name = 'https://www.imdb.com' + i.find('a').get('href')
#         item=dict()
#         item['top'] = top_cast_name
#         list2.append(item)
        
    
#     item = dict()
#     item ['Movie_Name'] = movie_name
#     item ['Relesing_Year'] = relesing_year
#     item ['Rate_point'] = rate_point
#     item ['All_Rating'] = all_rating
#     item ['Popularity'] = Popularity
#     item ['Image_Icon'] = image_icon
#     item ['Videos_Link'] = video_link
#     item ['Photos_Link'] = photos_link
#     item ['Action_Link'] = action_link
#     item ['Crime_Link'] = crime_link
#     item ['Thriller_Link'] = thriller_link
#     item ['Director_Name'] = director
#     item ['Star_Link'] = star_link
#     item ['User_Rating'] = user_rating
#     item ['User_Rating_Link'] = user_rating_link
#     item ['Critic_Reviews'] = critic_reviews
#     item ['Critic_Reviews_Link'] = critic_reviews_link
#     item ['Metascore'] = metascore
#     item ['Metascore_Link'] = metascore_link
#     item ['Award_Link'] = award_link
#     item ['Top_Cast_Name'] = list2
#     list1.append(item)
    
#     print(list1)

# list_page("https://www.imdb.com/title/tt10366206/?ref_=nv_sr_srsg_0_tt_5_nm_3_q_john%2520w")

# df = pandas.DataFrame(list1)
# df.to_excel('john_weak_imbd.xlsx', index=False)




# from requests import session
# from bs4 import BeautifulSoup as BS
# import pandas
# s = session()
# c=1
# s.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"
# url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
# r=s.get(url)
# soup=BS(r.text,'html.parser')
# count=1

# list1=[]
# list2=[]
# list3=[]
# list4=[]
# list5=[]


# def list_page(url):
#     r=s.get(url)
#     soup = BS(r.text,'html.parser')
#     for i in soup.find_all('img'):
#         image_link = i.get('src')
#         if image_link and  image_link.startswith('https'):
#             list2.append(image_link)
#             # print(list2)
#     for i in soup.find_all('td','titleColumn'):
#         name_year = i.text.strip().replace('.\n','').split('\n')
#         list1.append(name_year)
#     # print(list1)
#     for i in soup.find_all('td','ratingColumn imdbRating'):
#         rating = i.text.strip()
#         list3.append(rating)
#     for i in soup.find_all('a'):
#         name_l = i.get('href')
#         if name_l and name_l.startswith('/title'):
#             name_link = 'https://www.imdb.com'+ name_l
#             list5.append(name_link)
#         


#     # print(list3)
#     # item = dict()
#     # item ['Name'] = list1
#     # item ['Image_Link'] = list2
#     # item ['Rating'] = list3
#     # item ['Name_Link'] = list5
#     # list4.append(item)
#     # print(list4)


# list_page('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
# # df = pandas.DataFrame(list4)
# # df.to_excel('Top_250_movies.xlsx', index=False)



from requests import session
from bs4 import BeautifulSoup as BS
import pandas
s = session()
c=1
s.headers['user-agent']="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
r=s.get(url)
soup=BS(r.text,'html.parser')
list2=[]
list1=[]

def product_page(url):
    r=s.get(url)
    soup = BS(r.text,'html.parser')
    for i in soup.find_all('a'):
        name_l = i.get('href')
        if name_l and name_l.startswith('/title'):
            name_link = 'https://www.imdb.com'+ name_l
            if name_link not in list2:
                list2.append(name_link)
            # list_page(name_link)
            # list1.append(name_link)
# list1=[]

def list_page(url2):

    r=s.get(url2)
    soup = BS(r.text,'html.parser')
    
    movie_name = soup.find('span','sc-afe43def-1 fDTGTb')
    if movie_name:
        movie_name=movie_name.text
    else:
        movie_name = 'not given'

    rate_point = soup.find('div','sc-acdbf0f3-3 kpRihV')
    if rate_point:
        rate_point = rate_point.text[0:6]
    else:
        rate_point =' not given'

    all_rating = soup.find('div','sc-acdbf0f3-3 kpRihV')
    if all_rating:
        all_rating = all_rating.text[6:10]
    else:
        all_rating = 'not given'

    Popularity = soup.find('div','sc-5f7fb5b4-0 cUcPIU')
    if Popularity:
        Popularity = Popularity.text
    else:
        Popularity = 'not given'

    image_icon= soup.find('a','ipc-lockup-overlay ipc-focusable')
    if image_icon:
        image_icon = 'https://www.imdb.com'+image_icon.get('href')
    else:
        image_icon = 'not given'
 
    video_link = soup.find('div','sc-385ac629-9 jiVoNU')
    if video_link:
        video_link='https://www.imdb.com'+video_link.find('a').get('href')
    else:
        video_link = 'not given'

    photos_link= soup.find_all('a','ipc-btn ipc-btn--single-padding ipc-btn--center-align-content ipc-btn--default-height ipc-btn--core-baseAlt ipc-btn--theme-baseAlt ipc-btn--on-onBase ipc-secondary-button sc-ceb22a5b-3 lltPEH')
    if photos_link:
        photos_link = 'https://www.imdb.com' + photos_link[1].get('href')
    else:
        photos_link='not given'

    action_link = soup.find('a','ipc-chip ipc-chip--on-baseAlt')
    if action_link:
        action_link = 'https://www.imdb.com' + action_link.get('href')
    else:
        action_link = 'not given'

    director =  soup.find('a','ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
    if director:
        director = director.text
    else:
        director = 'not given'

    star_link = soup.find('a','ipc-metadata-list-item__label ipc-metadata-list-item__label--link')
    if star_link:
        star_link = 'https://www.imdb.com' + star_link.get('href')
    else:
        star_link = 'not given'
    
    user_rating = soup.find('ul','ipc-inline-list sc-f1de8f0-0 cRtTs baseAlt')
    if user_rating:
        user_rating = user_rating.find('span').text
    else:
        user_rating = 'not given'

    user_rating_link = soup.find('a','ipc-link ipc-link--baseAlt ipc-link--touch-target sc-f1de8f0-2 kvOHIk isReview')
    if user_rating_link:
        user_rating_link = 'https://www.imdb.com' + user_rating_link.get('href')
    else:
        user_rating_link = 'not given'

    critic_reviews = soup.find_all('a','ipc-link ipc-link--baseAlt ipc-link--touch-target sc-f1de8f0-2 kvOHIk isReview')
    if critic_reviews:
        critic_reviews = critic_reviews[1].text
    else:
        critic_reviews = 'not given'

    critic_reviews_link = soup.find_all('a','ipc-link ipc-link--baseAlt ipc-link--touch-target sc-f1de8f0-2 kvOHIk isReview')
    if critic_reviews_link:
        critic_reviews_link = 'https://www.imdb.com' + critic_reviews_link[1].get('href')
    else:
        critic_reviews_link = 'not given'
    
    award_link = soup.find('a','ipc-metadata-list-item__icon-link')
    if award_link:
        award_link = 'https://www.imdb.com' + award_link.get('href')
    else:
        award_link ='not given'
    
    item=dict()

    item ['Movie_Name'] = movie_name
    item ['Rate_Point'] = rate_point
    item ['Movie_Name'] = movie_name
    item ['All_Rating'] = all_rating
    item ['Popularity'] = Popularity
    item ['Image_Icon'] = image_icon
    item ['Videos_Link'] = video_link
    item ['Photos_Link'] = photos_link
    item ['Action_Link'] = action_link
    item ['Director_Name'] = director
    item ['Star_Link'] = star_link
    item ['User_Rating'] = user_rating
    item ['User_Rating_Link'] = user_rating_link
    item ['Critic_Reviews'] = critic_reviews
    item ['Critic_Reviews_Link'] = critic_reviews_link
    item ['Award_Link'] = award_link
    list1.append(item)
    print(r.url)

    
product_page('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

for url in list2:
    list_page(url)

df = pandas.DataFrame(list1)
df.to_excel('IMBD_Top_250_internal_data.xlsx', index=False)
















