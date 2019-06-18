import requests
from bs4 import BeautifulSoup



main_url = "https://www.tnp.sg/news/singapore"
shortUrl = "https://www.tnp.sg"

# Getting individual cities url
def getDetails(main_url):
    data = []
    # data['main_source'] = main_url #site-url
    re = requests.get(main_url)
    soup = BeautifulSoup(re.text, "html.parser")

    views_cards = soup.find_all('section', {'class':'col-sm-12'})
    card_clear = views_cards[0].find_all('div', {'class':"card clearfix"})
    
    for card in card_clear:

        sub_title = card.find('div', {'class':'card-block'})
        sub_working = sub_title.find('a').text.strip() #sub_title
        
        
        title = card.find('div', {'class':'card-block'})
        title_second = title.find('h2',{'class':'card-title'})
        title_working = title_second.find('a').text.strip() #heading_title
        

        sub_title_link = sub_title.find('a', 'active').get('href') #sub_title_link
        title_link = title.find('a').get('href').strip() #title_link
 
        img = card.find('div',{'class':'card-media'})
        img_patch = img.find('img')

        if img_patch is not None:
            img_src = img_patch['src'].strip()  



        time = card.find('time').text.strip() #time_link

        # configure post request parameters
        data.append({
                        'sub_title':sub_working,
                        'sub_title_link':shortUrl + sub_title_link,
                        'heading_title': title_working,
                        'title_link':shortUrl +title_link,
                        'news_time':time,
                        'image':img_src
                })


    return data

details = getDetails(main_url)
for detail in details:
    print(detail)


  # pic = card.find ('div',{'class':'card-media'})
        # pic2 = pic.find ('a', {'href'})
        # pic3 = pic2.find ('img',{'class':'img-responsive'})['src']
        # print(pic3)
        # img = pic3.find('img')['src'] #img_link


# https://github.com/AdityaAshtikar/backup