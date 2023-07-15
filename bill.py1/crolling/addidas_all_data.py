from requests import Session
from bs4 import BeautifulSoup as BS
import pandas
s=Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Connection': 'keep-alive',
    # 'Cookie': 'geo_ip=103.212.156.70; geo_country=IN; onesite_country=CO.IN; akacd_generic_prod_grayling_adidas=3866093655~rv=99~id=71a102bda8e4f4fbfd901c1d7fe9842c; _abck=B67BC551063BDDF90FEA55BCFB329481~-1~YAAQdRwgF/lh4AOJAQAANsLeKgrLAk8kjzrZqXlQDdVoODc0QikA659YZ/2lg+p95kAqLCjlEdWi+JJicTcIH6T+WPXVMIi/2sn3qHMf47FXGfhaoHTpxTOV4I92DgWWU1desf0NoYpYtwoWkeDHAbH3AXRvrsRnoa0gzUk4nsJZBi9jJ4jXdy5VYKoi4qfTMGRbICjEEpiEbHyiL6LsRc0Re8fBNybugKskre7mFvUn5iyut6UTCjSlBOWdGxC52qLDcNLy750u2nwEIoqq0hJFqh2ekYhTpmilE569Nnck2vMJLsk/Yw7cha5y4L53Y+1CQ9GvnTfmMgC65RZwwqRQl9rr5whtNSz+3zgh3h1GTOJOAmJ+vyXwUSKu4BpRKtff1j4elQx9iq2y7wQ+IvPdrP9tP/wm8AoacGMmbZPBn8ncsUCb6ZSdR0KCHSgLvAU1EIQQZ2tsvADnnQ==~-1~-1~1688644956; ak_bmsc=1A9D6BC5F2BE06D58DCF2A700D48D95D~000000000000000000000000000000~YAAQdRwgF/VF4AOJAQAAcv7YKhSxNvdp5VNuph5WlTWJ+JSmzqjghnLBiL4tPwXUAtZzcaycChaOGsFBCmm3GV7rvk81pQHsp6+J56JGrOeM2IczL+mP3jVB+dAHbk4EUAOb2DxpX+yvTX2zZkd0+J5NJpMsbzyRblUmY1d8a8RaHrh8YEcRBRMQxq0wE0G54GE+HY2hjy6hzMerafx7YZF80YyGhzBz6WBRXcaQNin8Ycwz57UoYjZMmmjxWLJXGbdgZKonp2kSW0CunLLt1LMRXSOzki+oyaPuqoI3pn44VcZgnO/0y2tGsi76OMF6M9vXJegNufpOX8jwyM1mE15fLM3ymwL6FsIYtF/637I0RM8s+EsKsucBOVlCJptQ7ItEwVvCprhxkQEDMQ==; bm_sz=56769CC3B7C1661991B2057609A7FD87~YAAQdRwgF8Y74AOJAQAAXaPWKhT1NTF9Th8BeF5mrrFcaSNQ10ixrfDrEeF1sP4jsc7NWjt9ydqGXST4wY2PqO/jX7z2JcsuLJb5zE9Q5wgWbHlupUJ7u87obKS2QoTQoQI93Ue0ELb6GmLwF5oghl69YeSfV3+OwPX7Yu4mi02NgpcnoMGnzlVqtOfvZyYc/kT1b1Gv78JTrN4brIhGsD/0+9KW/fDEya8y3wXA+TBczemm2AAkRmCJtCk6o40gDZD7WpOoKpY5v9DSUo+T2IzNKZRz5PkATN2dNX3fyusaM12FDH+uPFaiD0fyB47AZhC3LRlbsoV0kxmPK2Ac+u/kln4xnzmyuSPQvJ4Al0wrSKRBkbhyulyVnFVv4GAYpg5o8RjbphRu6ecPKROuN8JClWBqDI7nrA==~3355440~4470851; akacd_plp_prod_adidas_grayling=3866093656~rv=95~id=eed185ebee54541b01ca04bb2f3bd0b6; mt.v=2.741908643.1688640859923; dwsid=pi7LAlTSDD1d59TfCnP_ojopDYYCKIYG6nCoDDQnk8Wl228zsljWjTa_U4Bfqfu33fNTTWYhOADxkG3mXo-Q3Q==; fallback_dwsid=pi7LAlTSDD1d59TfCnP_ojopDYYCKIYG6nCoDDQnk8Wl228zsljWjTa_U4Bfqfu33fNTTWYhOADxkG3mXo-Q3Q==; UserSignUpAndSave=7; persistentBasketCount=0; userBasketCount=0; newsletterShownOnVisit=true; pagecontext_cookies=; pagecontext_secure_cookies=; utag_main=v_id:01892ad6d0580016b9505450cea605054002a00f0083e$_sn:1$_se:9$_ss:0$_st:1688642813507$ses_id:1688640868441%3Bexp-session$_pn:1%3Bexp-session$ab_dc:TEST%3Bexp-1693824868449$_vpn:7%3Bexp-session$_prevpage:HOME%3Bexp-1688644613518$dcsyncran:1%3Bexp-session$dc_visit:1$dc_event:6%3Bexp-session; ab_qm=b; RT="z=1&dm=www.adidas.co.in&si=028eb2bf-af7d-47a0-8512-1da500a51f71&ss=ljr15zpc&sl=6&tt=x0v&bcn=%2F%2F684d0d41.akstat.io%2F"; AMCV_7ADA401053CCF9130A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19545%7CMCMID%7C37821451587605900764398853764725009875%7CMCAAMLH-1689245670%7C12%7CMCAAMB-1689245670%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1688648071s%7CNONE%7CMCAID%7CNONE; ab_inp=b; AMCVS_7ADA401053CCF9130A490D4C%40AdobeOrg=1; s_pers=%20s_vnum%3D1690828200487%2526vn%253D1%7C1690828200487%3B%20s_invisit%3Dtrue%7C1688642813559%3B%20pn%3D1%7C1691233013563%3B; s_cc=true; _scid=e9cb982e-6d62-4f8e-a8e2-d2a32ef6b87f; _scid_r=e9cb982e-6d62-4f8e-a8e2-d2a32ef6b87f; mt.sc=%7B%22i%22%3A1688640871616%2C%22d%22%3A%5B%5D%7D; _ga=GA1.1.562882962.1688640872; _gid=GA1.3.804693592.1688640872; _gcl_au=1.1.1138102231.1688640872; _fbp=fb.2.1688640872807.883765422; _ga_4DGGV4HV95=GS1.1.1688640873.1.1.1688641016.0.0.0; _sctr=1%7C1688581800000; QSI_HistorySession=https%3A%2F%2Fwww.adidas.co.in%2Fmen-running-shoes~1688640874579; tfpsi=902adb1e-c21a-4cb5-9823-6129c1de84b2; QSI_SI_29N2pXneAOM1p8G_intercept=true; QuantumMetricSessionID=a72354d4a19a5cf78c347a06f65be12a; QuantumMetricUserID=2564b6e69dfd874435d24fd64ed55208; s_sess=%5B%5BB%5D%5D; _uetsid=7cc848001beb11eea17c476aa581e445; _uetvid=7cc871201beb11eea8beb50faff3cda6',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
s.headers.update(headers)
base_url = 'https://www.adidas.co.in{}'
url = 'https://www.adidas.co.in/'
r=s.get(url)
soup = BS(r.text,'html.parser')
whole_data=[]
all_list_page_link = []
main_category_link = []

def main_category(url):
    r=s.get(url)
    soup = BS(r.text,'html.parser')
    category_count = 0
    for i in soup.find_all('a','_link_fgjdp_1 _column_link_5dar6_23'):
        main_link = i.get('href')
        if 'blog' not in main_link and 'sports_bras_guide' not in main_link and 'adiclub' not in main_link and 'collaborations' not in main_link:
            main_link = 'https://www.adidas.co.in'+main_link

            category_count += 1
            print('category_count-----',category_count)      
            print('main_link-------->',main_link)
            main_category_link.append(main_link)
            

def list_page(url1):
    r=s.get(url1)
    print('______________',r.url)
    # print('category_link_count_________',count)
    soup = BS(r.text,'html.parser')
    count = 0
    for i in soup.find_all('a','product-card-content-badges-wrapper___2RWqS'):
        sub_category_link = 'https://www.adidas.co.in'+i.get('href')
        count += 1
        print('category___________',count)
        print('+++++++++++++++++++=====',sub_category_link)
        all_list_page_link.append(sub_category_link)
        
    next = [_next for _next in soup.find_all('a','active gl-cta gl-cta--tertiary') if "Next" in _next.text]
    if next:
        next_url = base_url.format(next[0].get('href'))
        count += 1
        list_page(next_url)

def product_page(url2):
    r=s.get(url2)
    soup = BS(r.text,'html.parser')
    category_count = 0
    
    try:
        name = soup.find('h1','name___120FN')
        if name:
            name = name.text
        else:
            name = 'not given'
    except:
        name = ""
    color_item = soup.find('div','single-color-label___29kFh')
    if color_item:
        color_item = color_item.text
    else:
        color_item = 'not given'
    
    prize_of_item = soup.find('div','gl-price-item notranslate')
    if prize_of_item:
        prize_of_item = prize_of_item.text
    else:
        prize_of_item = 'not given'
       
    all_image_link = []
    for j in soup.find_all('div','content___3m-ue'):
        image_link = j.find('img').get('src')
        if image_link and image_link.startswith('https:'):
            
            all_image_link.append(image_link)

    
    item = dict()
    item['Name'] = name
    item["Colour_Item"] = color_item
    item["Prize_Item"] = prize_of_item
    item["Image_Link"] = all_image_link
    whole_data.append(item)
    category_count += 1
    print('product_category_______________link',category_count)
    print("Product Page:- ", r.url)
   


main_category(url)
for page in main_category_link[100:200]:
    list_page(page)

for link_list in all_list_page_link:
    product_page(link_list)

df = pandas.DataFrame(whole_data)
df.to_excel('addidas_all_part_3_data.xlsx',index=False)
