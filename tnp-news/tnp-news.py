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
        sub_working = sub_title.find('a').text #sub_title
        
        
        title = card.find('div', {'class':'card-block'})
        title_second = title.find('h2',{'class':'card-title'})
        title_working = title_second.find('a').text #heading_title
        

        sub_title_link = sub_title.find('a', 'active').get('href') #sub_title_link
        title_link = title.find('a').get('href') #title_link

        img = card.find('img')['src'] #img_link
        time = card.find('time').text #time_link

        # configure post request parameters
        data.append({
                        'sub_title':sub_working,
                        'sub_title_link':shortUrl + sub_title_link,
                        'heading_title': title_working,
                        'title_link':shortUrl +title_link,
                        'news_time':time,
                        'image':img
                })


    return data

details = getDetails(main_url)
for detail in details:
    print(detail)


        # else:
        #     non_overlay = card.find('div', {'class':'content'})
        #     if non_overlay is not None:
        #         href_link = non_overlay.find('a').get('href')
        #         href_text = non_overlay.find('a').text

        # img_src = ''
        # for i in image:
        #     img_src = "{0}{1}".format(shortUrl, i['src'])




 # little_title = card.find('div',{'class':'card-block'})
        # sub_title = card.find('div',{'class':'card-sub-title'})
        # time = card.find('div',{'class':'card-footer'})


        
        # data.append({
        #     # 'heading':col_heading,
        #     # 'href':href_link,
        #     'text':href_text,
        #     # 'image':img_src,
        #     # 'heading':href_heading
        # })

        #   for card in card_clear:
#         card_media = card.find('div', {'class':'card-block'})

#         if card_media is not None:
#             href_sub_link = card_media.find('a').get('href')
#             href_text_heading = card_media.find('a').text

#         for heading_card in card_clear:   
#                 big_heading = heading_card.find('h2', {'class':'card-title'})

#                 if  big_heading is not None:
#                         href_link =  big_heading.find('a').get('href')
#                         href_text =  big_heading.find('a').text
#                         # print(href_link)

#         for card in card_clear:   
#                 card_media = card.find('div', {'class':'card-footer'})

#                 if card_media is not None:
#                         href_text_time = card_media.find('time').text
#                         # print(href_text_time)                          


         
#         data.append({
#                 'heading_text':href_text_heading,
#                 'sub_href':shortUrl + href_sub_link,
#                 'href': href_link,
#                 'text':href_text,
#                 'Time':href_text_time           
#         })