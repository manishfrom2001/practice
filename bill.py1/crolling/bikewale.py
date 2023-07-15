cookies = "BWC=jSOqruVjiMEyASJspl59iXrFI; _cwv=jSOqruVjiMEyASJspl59iXrFI.uwefftnytG.1686932610.1686939105.1686939107.10; newUserSession=0; _bwtest=62; _bwutmz=utmcsr%3Dgoogle%7Cutmgclid%3D%7Cutmccn%3D%28organic%29%7Cutmcmd%3Dorganic; _CustCityMaster=Delhi; _CustAreaId=3657; _CustCityIdMaster=10; _CustAreaName=Pitampura; _CustZoneIdMaster=; _CustZoneMaster=Select%20Zone; _CustLatitude=-100; _CustLongitude=-200; BHC=jSOqruVjiMEyASJspl59iXrFI; _fbp=fb.1.1686579531113.1111083771; _ga_KQ9B4GY2C7=GS1.1.1686912810.13.1.16869…dDk2YkMxRHJ6RGplYnNzSTFqbENkNjFrUkh0WU5vWiUyRjJQejZWc2hicWN1JTJCWDJhbGd5bVVNS0klMkI1VXNFam8zTHVUdmRjWVg4cnMzWmslMkZkYg; __gads=ID=95831f7a7d360c4f:T=1686579556:RT=1686918985:S=ALNI_MYmFbEP3Xb1Zy5JW5omKcBpSH7lcQ; __gpi=UID=00000c1281012b3e:T=1686579556:RT=1686918985:S=ALNI_MZxONrqSCqEpTsY-8v0G4LEWxyG4w; _gid=GA1.2.2128639825.1686739098; DesktopDetected=1; location=10_Delhi_3657_Pitampura; _CustState=Delhi; panoramaId_expiry=1687000428782; AMP_TOKEN=%24NOT_FOUND; _gat_UA-34771801-1=1; _dc_gtm_UA-34771801-1=1"



from requests import session
from bs4 import BeautifulSoup as BS
import pandas
s=session()
s.headers['Cookie']=cookies.encode('utf-8')


url = 'https://www.bikewale.com/'

r=s.get(url)

soup = BS(r.text,'html.parser')

list1=[]

def main_model_name(url):
    r = s.get(url)
    soup = BS (r.text,'html.parser')
    main_link = ['https://www.bikewale.com'+i.find('a').get('href') for i in soup.find('div', attrs = {'id' : 'brand-type-container'}).find_all('li')]
    
    return main_link

def list_page(url2):
    r = s.get(url2)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('div','bikeDescWrapper'):
        b = 'https://www.bikewale.com'+i.find('a').get('href')
        product_page(b)

def product_page(url3):
    r = s.get(url3)
    soup = BS(r.text,'html.parser')
    on_road_price = soup.find('div','o-NBTwp o-SoIQT o-cpnuEd')
    if on_road_price:
        on_road_price = on_road_price.text
    else:
        on_road_price = 'not given'

    ex_showroom_price = soup.find('span','font22 font-bold')
    if ex_showroom_price:
        ex_showroom_price = ex_showroom_price.text
    else:
        ex_showroom_price = 'not given'

    ex_showroom_price_2 = soup.find('span','o-Hyyko o-bPYcRG o-eqqVmt')
    if ex_showroom_price_2:
        ex_showroom_price_2 = ex_showroom_price_2.text
    else:
        ex_showroom_price_2 = 'not given'
    
    
    image_link = soup.find('a','carousel-img-container redirect-url')
    if image_link:
        image_link = image_link.find('img').get('src')
    else:
        image_link = 'not given'
    
    about_bike = soup.find('div','font14 margin-top20 border-divider content-details-wrapper js-readmore-container-multiple-wrapper')
    if about_bike:
        about_bike = about_bike.text.strip().replace('\n                \n\n                               ','')
    else:
        about_bike = 'not given'

    about_bike_1 = soup.find('div','o-bfyaNx o-bNxxEB o-bqHweY')
    if about_bike_1:
        about_bike_1 = about_bike_1.text
    else:
        about_bike_1 = 'not given'

    all_varient = soup.find('div','bw-model-tabs-data content-box-shadow content-inner-block-20 card-bottom-margin')
    if all_varient:
        all_varient = all_varient.text.strip().replace('\n                       ','').replace('\n\n','').replace('\n','').replace('\xa0','')
    else:
        all_varient = 'not given'

    all_varient_2 = soup.find('div','o-bfyaNx o-bNxxEB o-bqHweY')
    if all_varient_2:
        all_varient_2 = all_varient_2.text
    else:
        all_varient_2 = 'not given'
    
    star_rating = soup.find('div','inline-block')
    if star_rating:
        star_rating = star_rating.find('span').text
    else:
        star_rating = 'not given'

    review = soup.find('a','o-fzpimR o-fzpibr o-eemiLE o-eqqVmt')
    if review:
        review = review.text
    else:
        review = 'not given'

    review_2 = soup.find('a','review-count-target left-divider')
    if review_2:
        review_2 = review_2.text
    else:
        review_2 = 'not given'

    review_link = soup.find('a','o-fzpimR o-fzpibr o-eemiLE o-eqqVmt')
    if review_link:
        review_link = 'https://www.bikewale.com'+review_link.get('href')
    else:
        review_link = 'not given'

    review_link_2 = soup.find('a','review-count-target left-divider')
    if review_link_2:
        review_link_2 = 'https://www.bikewale.com'+review_link_2.get('href')
    else:
        review_link_2 = 'not given'

    name = soup.find('div','o-dsiSgT o-gHAVo o-fzpihY o-fzpilm o-cpnuEd')
    if name:
        name = name.find('h1').text
    else:
        name = 'not given'

    name_1 = soup.find('div','margin-right15 flex-container')
    if name_1:
        name_1 = name_1.find('h1').text
    else:
        name_1 = 'not given'

    price_link = soup.find('a','o-elzeOy')
    if price_link:
        price_link  = 'https://www.bikewale.com'+price_link.get('href')
    else:
        price_link = 'not given'
    
    price_link_1 = soup.find('a', attrs = {'id':'viewBreakupText'})
    if price_link_1:
        price_link_1 = 'https://www.bikewale.com'+price_link_1.get('href')
    else:
        price_link_1 = 'not given'
    
    item=dict()

    item ['Name'] = name , name_1
    item ['Image_Link'] = image_link
    item ['About_Bike'] = about_bike , about_bike_1
    item ['All_Veriant'] = all_varient , all_varient_2
    item ['Star_Rating'] = star_rating
    item ['On_Road_Price'] = on_road_price
    item ['Ex_Showroom_Price'] = ex_showroom_price , ex_showroom_price_2
    item ['Review'] = review , review_2
    item ['Review_Link'] = review_link , review_link_2
    item ['Price_Link'] = price_link , price_link_1
    list1.append(item)
    
    print(r.url)

    



list_1 = main_model_name('https://www.bikewale.com/')
for url in list_1:
    list_page(url)

df=pandas.DataFrame(list1)
df.to_excel("Bike_wala_data.xlsx")