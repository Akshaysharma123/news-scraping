
import requests
from bs4 import BeautifulSoup

main_url = "https://www.asiaone.com/lifestyle/five-guys-burger-chain-finally-lands-singapore-and-we-cant-wait"
shortUrl = "https://www.asiaone.com"

# Getting individual cities url
def getDetails(main_url):
    details = {}
    details['main_source'] = main_url
    re = requests.get(main_url)
    soup = BeautifulSoup(re.text, "html.parser")
    for data in soup.find_all('main', {'class': 'container container montserrat js-quickedit-main-content'}):
        news_heading = data.find('h1',{ 'class':'ui header page__title'}) 
        heading = news_heading.text.strip()
        details['heading'] = heading # news_heading
        # print(news_heading)

        picture = data.find ('picture', class_='img-responsive')
        img = picture.find ('img', class_ ='img-responsive')
        imgSource = img['src'].strip()
        details['imgSource'] = shortUrl + imgSource # image-source
        
        subtittle = data.find('h6', class_= 'ui header mini normal')
        img_title = subtittle.text.strip()
        details['img-title'] = img_title # news heading

        author_img = data.find('div', class_= 'photo-byline')
        picture = author_img.find ('picture', class_='img-responsive')
        author_img = picture.find ('img', class_ ='img-responsive')
        author_img = author_img['src'].strip()
        details['author_img'] = author_img # news heading

        author_name = data.find('div', class_= 'single-field-item')
        author_names= author_name.find('a').text
        author_name = author_names.strip()
        details['author_name'] = author_name # news heading
        
        author_link = data.find('div', class_= 'single-field-item')
        link_a = author_link.find('a',)
        link = link_a.get('href').strip()
        details['link'] = shortUrl + link # image-source
        # print(link)
 
        sitename = data.find('div',class_= 'field-item')
        sub_title = sitename.find('a').text.strip()
        details['sub_title'] = sub_title
        
        sitelink = data.find('div', class_= 'field field-name-field-source field--type-entity-reference field--label-hidden field--items')
        link_site = sitelink.find('a',)
        link_side = link_site.get('href').strip()
        details['link_side'] =  shortUrl + link_side # image-source
        # print(link_side)


        pub_date = data.find('div',{ 'class':'field field-name-field-publication-date field--type-datetime field--label-hidden field-item'}) 
        time = pub_date.text.strip()
        details['time'] = time # news_heading
        
    return details        

details = getDetails(main_url)
print(details["main_source"])
print(details["heading"])
print(details["imgSource"])
print(details["img-title"])
print(details["author_img"])
print(details["author_name"])
print(details["link"])
print(details["sub_title"])
print(details["link_side"])
print(details["time"])




